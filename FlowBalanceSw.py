def flow_balance_s():
    import numpy as np
    import Branch0
    import Branch11
    # 下水系統の流量バランス
    # 入力値は各ポンプINVである。
    # Nomenclature
    # GCn2NHEX      :熱交換器一台あたり流量[m3/min]
    # GSw           :下水流量[m3/min]
    # GNP           :ポンプ一台当たり流量
    # NmNP          :ポンプ台数
    # INVNP         :ポンプINV
    global GCn2NHEX,GSw,GNP,NmNP,INVNP,PNP
    global c0NP,c1NP,c2NP,c3NP,c4NP
    global FlgError6
    global MvGCn2NHEX,dMvGCn2NHEX,Tv1GCn2NHEX,dTv1GCn2NHEX
    global MvGNP,dMvGNP,Tv1GNP,dTv1GNP
    global KrPpSw,KrPpCn2NHEX,KrCn2NHEX
    # INV入力がすべて0の場合は流量0とする
    if INVNP == 0:
        GCn2NHEX = 0
        GSw = 0
        GNP = 0
        PNP = 0
    else:
        # whileに入るための初期値,二分法初期値
        GSw = 0
        GCn2NHEX = 40
        GSwmax = 80
        GSwmin = 0
        GSw00 = np.zeros(10)
        cnt = 0
        while GCn2NHEX * 2 - GSw > 0.01 or GCn2NHEX * 2 - GSw < - 0.01:

            cnt = cnt + 1

            # GSwを仮定する
            GSw = (GSwmax + GSwmin) / 2

            # dPSwを求める
            [dPSw] = Branch0.branch0(GSw,KrPpSw,0,0,1,1900)
            # GCn2NHEX,GNPを求める
            [GCn2NHEX,GNP,_,PNP] = \
                Branch11.branch11(dPSw,NmNP,INVNP,0,121,c0NP,c1NP,c2NP,c3NP,c4NP,KrPpCn2NHEX,KrCn2NHEX)

            #  各枝の流量が釣り合うまで二分法
            if GCn2NHEX * 2 - GSw > 0:
                GSwmin = GSw
            elif GCn2NHEX * 2 - GSw < 0:
                GSwmax = GSw

            FlgError6 = 0
            # 0.1で収束しない場合
            for i in range(10,2,-1):
                GSw00[i] = GSw00[i-1]
            GSw00[1] = GSw

            if GSw00  == GSw00[1]:
                FlgError6 = GCn2NHEX * 2 - GSw
                break

            if cnt > 30:
                FlgError6 = 1
                break


    #  センサ誤差、DDC誤差
    MvGCn2NHEX = GCn2NHEX * (1 + dMvGCn2NHEX)
    MvGNP = GNP * (1 + dMvGNP)
    Tv1GCn2NHEX = MvGCn2NHEX + dTv1GCn2NHEX
    Tv1GNP = MvGNP + dTv1GNP

