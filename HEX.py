def hex(vh,vc,th1,tc1,A,th2,tc2):
    import math
    # プレート型熱交換器の伝熱モデル
    # 向流型前提の計算
    #
    # 記号
    # vh     高温側の流量(m3/min)
    # vc    :低温側の流量(m3/min)
    # wh    :高温側の流量(kg/s)×比熱(kJ/kgK)
    # wc    :低温側の流量(kg/s)×比熱(kJ/kgK)
    # th1   :高温側の入口温度(℃)
    # tc1   :低温側の入口温度(℃)
    # A     :伝熱面積(m2)
    # Q     :交換熱量(kW)
    # k     :熱貫流率(kW/m2K)
    # kA    :熱貫流率(kW/m2K)×熱交換面積(m2)
    # th2   :高温側の出口温度(℃)
    # tc2   :低温側の出口温度(℃)
    # MTD   :対数平均温度差

    # 上記は温度による熱交換の場合。エンタルピーで考える場合は，状態量が
    # 温度から比エンタルピーへ，熱貫流率がエンタルピー基準の比エンタルピ
    # ーへ，wh,wcが流量へと置き換えられる。


    # kの計算
    # Nomenclature
    # ah,ac:高温側、低温側の熱伝導率[kcal/m2h`C]
    # Cp:流体比熱[kcal/kg`C]
    # gamma:比重量[kg/m3]
    # L:流量[kg/h]
    # S:通過断面積[m2]
    # eta:粘性係数[kgs/m2]
    # mu:粘度[kg/mh]=3600*9.80*eta
    # lambda0:流体の熱伝導率[kcal/mh`C]
    # De=2cd/(c+d) (c:通路長[m], d:通路幅[m])
    # T:流体の温度

    # 流量が少なくとも片方ない場合
    if vh < 0.01 or vc < 0.01:
        th2 = th1
        tc2 = tc1
    elif vh < 0.01 and vc >= 0.01:
        th2 = tc1
        tc2 = tc1
    elif vh >= 0.01 and vc < 0.01:
        th2 = th1
        tc2 = th1
    # 流量が両方ある場合
    else:

        # 高温側が低温側より低温の場合はデータを入れ替えて計算
        flag = 0
        if th1 < tc1:
            flag = 1
            tt=th1
            th1=tc1
            tc1=tt
            vv = vh
            vh = vc
            vc = vv



        # 温度により変化しない変数
        Cp = 1.0

        # 温度により変化する変数
        # gamma=1.735*10^(-5)*T^3-6.133*10^(-3)*T^2+2.704*10^(-2)*T+1000
        # eta = 4.359*10^(-8)*T^4-1.109*10^(-5)*T^3+1.107*10^(-3)*T^2-5.824*10^(-2)*T+1.826
        # mu = 3600 * 9.80 * eta
        # lambda0 = -5.672*10^(-6)*T^2+1.556*10^(-3)*T+0.4894

        # 機器により決まる変数
        S = 0.01
        c = 40.0
        d = 1.0
        De = 2.0 * c * d / ( c + d )

        # 変数計算ah 高温側、低温側の温度は、出入口温度の平均値とする
        T = (th1+th2) / 2
        gamma = 1.735 * pow(10,-5) * pow(T,3) - 6.133 * pow(10,-3) * pow(T,2) + 2.704 * pow(10,-2) * T + 1000.0
        L = vh * 60.0 * gamma
        eta = 4.359 * pow(10,-8) * pow(T,4) - 1.109 * pow(10,-5) * pow(T,3) + 1.107 * pow(10,-3) * pow(T,2) - 5.824 * pow(10,-2) * T + 1.826
        eta = eta * pow(10,-4)
        mu = 3600.0 * 9.80 * eta
        lambda0 = -5.672 * pow(10,-6) * pow(T,2) + 1.556 * pow(10,-3) * T + 0.4894
        ah = 0.023 * pow(Cp,(1/3)) * pow(L,0.8) * pow(lambda0,(2/3)) * pow(S,-0.8) * pow(mu,(-7/15)) * pow(De,-0.2)
        # whの計算
        wh = vh / 60.0 * gamma * 4.186
        # 変数計算ac
        T = (tc1+tc2)/2.0
        gamma = 1.735 * pow(10,-5) *pow(T,3) - 6.133 * pow(10,-3) * pow(T,2) + 2.704 * pow(10,-2) * T + 1000.0
        L = vc * 60.0 * gamma
        eta = 4.359 * pow(10,-8) * pow(T,4) - 1.109 * pow(10,-5) * pow(T,3) + 1.107 * pow(10,-3) * pow(T,2) - 5.824 * pow(10,-2) * T + 1.826
        eta = eta * pow(10,-4)
        mu = 3600.0 * 9.80 * eta
        lambda0 = -5.672 * pow(10,-6) * pow(T,2) + 1.556 * pow(10,-3) * T + 0.4894
        ac = 0.023 * pow(Cp,(1/3)) * pow(L,0.8) * pow(lambda0,(2/3)) * pow(S,-0.8) * pow(mu,(-7/15)) * pow(De,-0.2)
        # wcの計算
        wc = vc / 60.0 * gamma * 4.186
        # kの算出 kcal/m2h`C からkW/m2`Cへ変換
        k = ah * ac / ( ah + ac )
        k = k * 1.162 * pow(10,-3)

        # kAの計算
        kA = k * A

        # Qの計算
        # td1 = th2 - tc1
        # td2 = th1 - tc2
        # MTD = (td1 - td2) / LOG(td1 / td2)  !th2、tc2に関しては前時刻を参照

        # wh,wcの関係にしたがって，高温側，低温側の出口温度を求める
        wcwh = wc / wh

        # kA,wc,whの値によってexpの項が発散する危険があるため，その場合は緊急に
        # 計算をストップさせる。→一応計算させる
        z = kA * ( 1.0 - wcwh ) / wc

        if wcwh != 1.0:
            x = math.exp( z )
            y = th1 - tc1
            th2 = th1 - y * ( 1.0 - x ) / ( 1.0 - x / wcwh )
            tc2 = tc1 + y * ( 1.0 - x ) / ( wcwh - x )

            if z > 200.0:
                # 向流型の場合流量が少ない方は十分に熱交換され、
                # そうでない方は流量に応じた温度変化になる。
                if wc > wh:
                    th2=tc1
                    tc2=(th1-tc1)*wh/wc+tc1
                else:
                    tc2=th1
                    th2=(tc1-th1)*wc/wh+th1

        else:
            y = th1 - tc1
            th2 = th1 - y * kA / ( wc + kA )
            tc2 = tc1 + y * kA / ( wc + kA )


        # 2次側出口温度は1次側出口温度を、1次側出口温度は2次側入口温度を超えない。
        if th2 < tc1 or tc2 > th1:

        # 向流型の場合流量が少ない方は十分に熱交換され、
        # そうでない方は流量に応じた温度変化になる。
              if vc > vh:
                  th2 = tc1
                  tc2 = (th2 - th1) * vh / vc + tc1
              else:
                  tc2 = th1
                  th2 = (tc2 - tc1) * vc / vh + th1


    #     ! 高温側が低温側より低温の場合はデータを元に戻して返す  rifined by sumiyoshi
        if flag == 1:
    #         tt=th1
    #         th1=tc1
    #         tc1=tt
    #         tw=wh
    #         wh=wc
    #         wc=tw
            tt=th2
            th2=tc2
            tc2=tt
            vv = vh
            vh = vc
            vc = vv
    return [th2,tc2]
