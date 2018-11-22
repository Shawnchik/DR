def flow_balance_cn_nhex():
    import numpy as np
    import Branch0
    import Branch10
    # 冷却水系統の流量バランス(下水熱利用時)
    # 入力値は各ポンプINVとバルブ開度Vlvである。各流量、圧力を出力とする。
    # Nomenclature
    # GCn1NHEX       :熱交換器一台あたり流量[m3/min]
    # GCDP1~4        :CDP1~4流量[m3/min]
    # INVCDP1~4      :CDP1~4のINV(0~1)
    # GCDP1~4       :TR1~4冷却水流量[m3/min]
    global GCn1NHEX
    global INVCDP1,INVCDP2,INVCDP3,INVCDP4
    global c0CDP1,c1CDP1,c2CDP1,c3CDP1,c4CDP1
    global c0CDP2,c1CDP2,c2CDP2,c3CDP2,c4CDP2
    global c0CDP3,c1CDP3,c2CDP3,c3CDP3,c4CDP3
    global c0CDP4,c1CDP4,c2CDP4,c3CDP4,c4CDP4
    global GCDP1,GCDP2,GCDP3,GCDP4,PCDP1,PCDP2,PCDP3,PCDP4
    global FlgError5
    global MvGCn1NHEX,dMvGCn1NHEX,Tv1GCn1NHEX,dTv1GCn1NHEX
    global MvGCDP1,dMvGCDP1,Tv1GCDP1,dTv1GCDP1,MvGCDP2,dMvGCDP2,Tv1GCDP2,dTv1GCDP2
    global MvGCDP3,dMvGCDP3,Tv1GCDP3,dTv1GCDP3,MvGCDP4,dMvGCDP4,Tv1GCDP4,dTv1GCDP4
    global KrPpCn1NHEX,KrCn1NHEX,KrPpCnTR1,KrCnTR1,KrPpCnTR2,KrCnTR2,KrPpCnTR3,KrCnTR3,KrPpCnTR4,KrCnTR4

    # INV入力がすべて0の場合は流量0とする
    if INVCDP1 == 0 and INVCDP2 == 0 and INVCDP3 == 0 and INVCDP4 == 0:
        GCn1NHEX = 0
        GCDP1 = 0
        GCDP2 = 0
        GCDP3 = 0
        GCDP4 = 0
        PCDP1 = 0
        PCDP2 = 0
        PCDP3 = 0
        PCDP4 = 0
    else:
        # whileに入るための初期値,二分法初期値
        GCn1NHEX = 10
        GCDP1 = 0
        GCDP2 = 0
        GCDP3 = 0
        GCDP4 = 0
        GCn1NHEXmax = 40
        GCn1NHEXmin = 0
        GCn1NHEX100 = np.zeros(10)
        cnt = 0
        while GCn1NHEX * 2 - GCDP1 - GCDP2 - GCDP3 - GCDP4 > 0.1 or \
                GCn1NHEX * 2 - GCDP1 - GCDP2 - GCDP3 - GCDP4 < - 0.1:

            cnt = cnt + 1

            # GCn1NHEXを仮定する
            GCn1NHEX = (GCn1NHEXmax + GCn1NHEXmin) / 2
            # dPCn1NHEXを求める
            [dPCn1NHEX] = Branch0.branch0(GCn1NHEX,KrPpCn1NHEX,KrCn1NHEX,0,1,2846)

            # GCDP1~4,GCDP1~4を求める
            [_,GCDP1,_,PCDP1] = Branch10.branch10(dPCn1NHEX,INVCDP1,1,2846,0,121,c0CDP1,c1CDP1,c2CDP1,c3CDP1,c4CDP1,KrPpCnTR1,KrCnTR1)

            [_,GCDP2,_,PCDP2] = Branch10.branch10(dPCn1NHEX,INVCDP2,1,2846,0,121,c0CDP2,c1CDP2,c2CDP2,c3CDP2,c4CDP2,KrPpCnTR2,KrCnTR2)

            [_,GCDP3,_,PCDP3] = Branch10.branch10(dPCn1NHEX,INVCDP3,1,2846,0,121,c0CDP3,c1CDP3,c2CDP3,c3CDP3,c4CDP3,KrPpCnTR3,KrCnTR3)

            [_,GCDP4,_,PCDP4] = Branch10.branch10(dPCn1NHEX,INVCDP4,1,2846,0,121,c0CDP4,c1CDP4,c2CDP4,c3CDP4,c4CDP4,KrPpCnTR4,KrCnTR4)


            # 各枝の流量が釣り合うまで二分法
            if GCn1NHEX * 2 - GCDP1 - GCDP2 - GCDP3 - GCDP4 > 0:
                GCn1NHEXmax = GCn1NHEX
            elif GCn1NHEX * 2 - GCDP1 - GCDP2 - GCDP3 - GCDP4 < 0:
                GCn1NHEXmin = GCn1NHEX

            FlgError5 = 0
            # 0.1で収束しない場合
            for i in range(10,2,-1):
                GCn1NHEX100[i] = GCn1NHEX100[i-1]
            GCn1NHEX100[1] = GCn1NHEX

            if GCn1NHEX100 == GCn1NHEX100[1]:
                FlgError5 = GCn1NHEX * 2 - GCDP1 - GCDP2 - GCDP3 - GCDP4
                break

            if cnt > 30:
                FlgError5 = 1
                break


    # センサ誤差
    MvGCn1NHEX = GCn1NHEX * (1 + dMvGCn1NHEX)
    MvGCDP1 = GCDP1 * (1 + dMvGCDP1)
    MvGCDP2 = GCDP2 * (1 + dMvGCDP2)
    MvGCDP3 = GCDP3 * (1 + dMvGCDP3)
    MvGCDP4 = GCDP4 * (1 + dMvGCDP4)
    Tv1GCn1NHEX = MvGCn1NHEX + dTv1GCn1NHEX
    Tv1GCDP1 = MvGCDP1 + dTv1GCDP1
    Tv1GCDP2 = MvGCDP2 + dTv1GCDP2
    Tv1GCDP3 = MvGCDP3 + dTv1GCDP3
    Tv1GCDP4 = MvGCDP4 + dTv1GCDP4

