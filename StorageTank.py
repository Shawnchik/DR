def storage_tank(Mode1,Mode2,Gin,Tin,Tf,A,SpToutChTR):
    import math
    import nunmpy as np
    #ST(Storage Tank)に関するサブルーチン
    # Nomenclature
    # Input
    # Mode1         :冷水槽 / 温水槽 = 1 / - 1
    # Mode2         :蓄熱 / 放熱 = 1 / - 1
    # so            :槽番号
    # Tin           :流入温度
    # Tout          :流出温度
    # Gin           :流量[m3/h]
    # Q0            :残蓄熱量[GJ]
    # D             :槽分割数
    # A             :槽の底面積
    # aL            :槽の深さ
    # Lp            :完全混合域の深さ
    # dtt           :計算時間間隔(h)
    # dz            :1次元拡散域の深さ方向分割幅(m)
    # Tf(1:1000)    :前時刻の対象槽の1〜1000(上限)層の温度
    # b             :流入方向(1=上→下、-1=下→上)
    # Mode          :蓄熱槽の冷暖モード
    # Output
    # T(1:1000)     :現時刻の対象槽の1〜1000(上限)層の温度
    # Q()           :有効区分水槽の残蓄熱量[GJ]
    # Q0            :残蓄熱量[GJ]
    # NmAvl         :有効区分槽の数
    # U             :流入水量／床面積(m/h)(深さ方向を正)
    # k             :拡散係数(5.08×0.0001(m2/h))

    T=np.zeros(60)
    Tf=np.zeros(60)
    D = 60
    # A = 479.2
    # A = 2000
    Lp = 0.1
    dz = 0.1
    dtt = 1 / 600
    # m3/minからm3/hに変換
    Gin = Gin * 60
    U = Gin / A
    k = 5.08 * 0.0001

    # 流入方向bの設定
    if Mode1 * Mode2 == 1:
        b = - 1
    elif Mode1 * Mode2 == - 1:
        b = 1

    # 流速が計算幅よりも大きい場合は上手く計算できないことが予想されるので注意する!!!
    for m in range(1,10,1):        # ←6秒間隔の計算であるため、1分間隔のメインに移すために10回回す
        # 流入方向が上→下の時
        if b == 1:
            # 流入側完全混合域の計算←完全混合域は、分割した最端部分のみとしている。
            T[D] = Tin - (Tin - Tf[D]) * math.exp(-1.0 * Gin / A * dtt / Lp)
            # (TTin-Tf(D))の項は、前時刻との差とexp(-1*Gin/A*dtt/Lp)のdttによって計算しているため
            # 1次元拡散域の計算
            for i in range(D-1,2,-1):
                T[i] = Tf[i] + dtt * (k * (Tf[i + 1] + Tf[i - 1] - 2.0 * Tf[i]) / ((dz)^2)-U * (Tf[i] - Tf[i + 1]) / dz)

            # 流出側完全混合域の計算←流出側には指向性はないため、完全混合域にする必要はないのでは？
            # 流出側一次元拡散域の計算
            T[1] = Tf[1] + dtt * (k * (Tf[2] + Tf[1] - 2.0 * Tf[1]) / (dz^2) - U * (Tf[1] - Tf[2]) / dz)
            Tf = T
            Tout = T[1]
        # 流入方向が下→上の時
        else:
            # 流入側完全混合域の計算
            T[1] = Tin - (Tin - Tf[1]) * math.exp(-1.0 * Gin / A * dtt / Lp)
            # 1次元拡散域の計算
            for i in range(2,D-1,1):
                T[i] = Tf[i]+dtt*(k*(Tf[i+1]+Tf[i-1]-2.0*Tf[i])/((dz)^2.0)-U*(Tf[i]-Tf[i-1])/dz)

            # 流出側完全混合域の計算
            T[D] = Tf[D]+dtt*(k*(Tf[D]+Tf[D-1]-2.0*Tf[D])/((dz)^2.0)-U*(Tf[D]-Tf[D-1])/dz)
            Tf = T
            Tout = T[D]

    # 残蓄熱量を求める

    # 厳密な求め方
    Q0 = 0
    if Mode1 == 1:
        for i in range(1,60,1):
            Q0 = Q0 + (SpToutChTR + 10 - T[i]) * A * 0.1 * 4.186 / pow(10,3)

    else:
        for i in range(1,60,1):
            Q0 = Q0 + (T[i]- (SpToutChTR - 10)) * A * 0.1 * 4.186 / pow(10,3)


    return [Tout,Q0,T,Tf]
