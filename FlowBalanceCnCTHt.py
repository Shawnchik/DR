def flow_balance_cn_ct_ht():
    import numpy as np
    import Branch0
    import Branch01
    import Branch10
    # 冷却水系統の流量バランス(冷却塔利用時、冷暖房運転時)
    # 入力値は各ポンプINVとバルブ開度Vlvである。各流量、圧力を出力とする。
    # Nomenclature
    # GCn1NHEX       :熱交換器一台あたり流量[m3/min]
    # GCDP1~4        :CDP1~4流量[m3/min]
    # INVCDP1~4      :CDP1~4のINV(0~1)
    # GCDP1~4       :TR1~4冷却水流量[m3/min]
    global INVCDP2,INVCDP3,INVCDP4
    global c0CDP2,c1CDP2,c2CDP2,c3CDP2,c4CDP2
    global c0CDP3,c1CDP3,c2CDP3,c3CDP3,c4CDP3
    global c0CDP4,c1CDP4,c2CDP4,c3CDP4,c4CDP4
    global GCDP2,GCDP3,GCDP4,PCDP2,PCDP3,PCDP4
    global FlgError5
    global MvGCDP2,dMvGCDP2,Tv1GCDP2,dTv1GCDP2
    global MvGCDP3,dMvGCDP3,Tv1GCDP3,dTv1GCDP3,MvGCDP4,dMvGCDP4,Tv1GCDP4,dTv1GCDP4
    global KrPpCnTR2,KrCnTR2,KrPpCnTR3,KrCnTR3,KrPpCnTR4,KrCnTR4
    global GCnCT1,GCnCT2,GCnCT3,NmCT,KrPpCT1,KrCnCT1,KrPpCT2,KrCnCT2,KrPpCT3,KrCnCT3
    global GVlvCT,VlvCT
    global MvGVlvCT,dMvGVlvCT,Tv1GVlvCT,dTv1GVlvCT
    global KrPpVlvCT
    # INV入力がすべて0の場合は流量0とする
    if INVCDP2 == 0 and INVCDP3 == 0 and INVCDP4 == 0:
        GCnCT1 = 0
        GCnCT2 = 0
        GCnCT3 = 0
        GVlvCT = 0
        GCDP2 = 0
        GCDP3 = 0
        GCDP4 = 0
        PCDP2 = 0
        PCDP3 = 0
        PCDP4 = 0
    else:
        # whileに入るための初期値,二分法初期値
        GCnCT1 = 10
        GCnCT2 = 0
        GCnCT3 = 0
        GVlvCT = 0
        GCDP2 = 0
        GCDP3 = 0
        GCDP4 = 0
        GCnCT1max = 40
        GCnCT1min = 0
        GCnCT100 = np.zeros(10)
        cnt = 0
        while GCnCT1 + GCnCT2 + GCnCT3 + GVlvCT - GCDP2 - GCDP3 - GCDP4 > 0.1 or \
                GCnCT1 + GCnCT2 + GCnCT3 + GVlvCT - GCDP2 - GCDP3 - GCDP4 < - 0.1:

            # 収束しないときに抜けるために繰返計算回数をカウントする
            cnt = cnt + 1

            # GCnCT1を仮定する
            GCnCT1 = (GCnCT1max + GCnCT1min) / 2
            # dPCn1NHEXを求める
            [dPCnCT1] = Branch0.branch0(GCnCT1,KrPpCT1,0,KrCnCT1,1,2846)

            # GCnCT2~3を求める
            if NmCT == 1:
                GCnCT2 = 0
                GCnCT3 = 0
            elif NmCT == 2:
                [GCnCT2,_] = Branch01.branch01(dPCnCT1,KrPpCT2,0,KrCnCT2,1,2846,20)
                GCnCT3 = 0
            elif NmCT == 3:
                [GCnCT2,_] = Branch01.branch01(dPCnCT1,KrPpCT2,0,KrCnCT2,1,2846,20)
                [GCnCT3,_] = Branch01.barnch01(dPCnCT1,KrPpCT3,0,KrCnCT3,1,2846,20)

            #  GVlvCTを求める
            [GVlvCT,_] = Branch01.branch01(dPCnCT1,KrPpVlvCT,0,0,VlvCT,25000,100)

            # GCDP2~4,GCDP2~4を求める
            [_,GCDP2,_,PCDP2] = Branch10.branch10(dPCnCT1,INVCDP2,1,2846,0,121,c0CDP2,c1CDP2,c2CDP2,c3CDP2,c4CDP2,KrPpCnTR2,KrCnTR2)

            [_,GCDP3,_,PCDP3] = Branch10.branch10(dPCnCT1,INVCDP3,1,2846,0,121,c0CDP3,c1CDP3,c2CDP3,c3CDP3,c4CDP3,KrPpCnTR3,KrCnTR3)

            [_,GCDP4,_,PCDP4] = Branch10.branch10(dPCnCT1,INVCDP4,1,2846,0,121,c0CDP4,c1CDP4,c2CDP4,c3CDP4,c4CDP4,KrPpCnTR4,KrCnTR4)

            # 各枝の流量が釣り合うまで二分法
            if GCnCT1 + GCnCT2 + GCnCT3 + GVlvCT - GCDP2 - GCDP3 - GCDP4 > 0:
                GCnCT1max = GCnCT1
            elif GCnCT1 + GCnCT2 + GCnCT3 + GVlvCT - GCDP2 - GCDP3 - GCDP4 < 0:
                GCnCT1min = GCnCT1

            FlgError5 = 0
            # 0.1で収束しない場合
            for i in range(10,2,-1):
                GCnCT100[i] = GCnCT100(i-1)
            GCnCT100[1] = GCnCT1

            if GCnCT100 == GCnCT100[1]:
                FlgError5 = GCnCT1 + GCnCT2 + GCnCT3 + GVlvCT - GCDP2 - GCDP3 - GCDP4
                break

            if cnt > 30:
                FlgError5 = 1
                break


    # センサ誤差
    MvGCDP2 = GCDP2 * (1 + dMvGCDP2)
    MvGCDP3 = GCDP3 * (1 + dMvGCDP3)
    MvGCDP4 = GCDP4 * (1 + dMvGCDP4)
    MvGVlvCT = GVlvCT * (1 + dMvGVlvCT)
    Tv1GCDP2 = MvGCDP2 + dTv1GCDP2
    Tv1GCDP3 = MvGCDP3 + dTv1GCDP3
    Tv1GCDP4 = MvGCDP4 + dTv1GCDP4
    Tv1GVlvCT = MvGVlvCT + dTv1GVlvCT

