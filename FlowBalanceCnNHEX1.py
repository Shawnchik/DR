def flow_balance_cn_nhex1():
    import numpy as np
    import Branch0
    import Branch10
    # 冷却水系統の流量バランス(冷却塔利用時のTR1)
    # 入力値は各ポンプINVとバルブ開度Vlvである。各流量、圧力を出力とする。
    # Nomenclature
    # GCn1NHEX       :熱交換器一台あたり流量[m3/min]
    # GCDP1~4        :CDP1~4流量[m3/min]
    # INVCDP1~4      :CDP1~4のINV(0~1)
    # GCDP1~4       :TR1~4冷却水流量[m3/min]
    global ModeClHt
    global GCn1NHEX
    global INVCDP1
    global c0CDP1,c1CDP1,c2CDP1,c3CDP1,c4CDP1
    global GCDP1,PCDP1
    global FlgError5
    global MvGCn1NHEX,dMvGCn1NHEX,Tv1GCn1NHEX,dTv1GCn1NHEX
    global MvGCDP1,dMvGCDP1,Tv1GCDP1,dTv1GCDP1
    global KrPpCn1NHEX,KrCn1NHEX,KrPpCnTR1,KrCnTR1

    # 暖房運転時
    if ModeClHt == 0:
        # INV入力がすべて0の場合は流量0とする
        if INVCDP1 == 0:
            GCn1NHEX = 0
            GCDP1 = 0
            PCDP1 = 0
        else:
            # whileに入るための初期値,二分法初期値
            GCn1NHEX = 10
            GCDP1 = 0
            GCn1NHEXmax = 40
            GCn1NHEXmin = 0
            GCn1NHEX100 = np.zeros(10)
            cnt = 0
            while GCn1NHEX * 2 - GCDP1 > 0.1 or GCn1NHEX * 2 - GCDP1 < - 0.1:

                cnt = cnt + 1

                # GSTを仮定する
                GCn1NHEX = (GCn1NHEXmax + GCn1NHEXmin) / 2
                # dPCn1NHEXを求める
                [dPCn1NHEX] = Branch0.branch0(GCn1NHEX,KrPpCn1NHEX,KrCn1NHEX,0,1,2846)

                # GCDP1,PCDP1を求める
                [_,GCDP1,_,PCDP1] = Branch10.branch10(dPCn1NHEX,INVCDP1,1,2846,0,121,c0CDP1,c1CDP1,c2CDP1,c3CDP1,c4CDP1,KrPpCnTR1,KrCnTR1)

                # 各枝の流量が釣り合うまで二分法
                if GCn1NHEX * 2 - GCDP1 > 0:
                    GCn1NHEXmax = GCn1NHEX
                elif GCn1NHEX * 2 - GCDP1 < 0:
                    GCn1NHEXmin = GCn1NHEX

                FlgError5 = 0
                # 0.1で収束しない場合
                for i in range(10,2,-1):
                    GCn1NHEX100[i] = GCn1NHEX100[i-1]
                GCn1NHEX100[1] = GCn1NHEX

                if GCn1NHEX100 == GCn1NHEX100[1]:
                    FlgError5 = GCn1NHEX * 2 - GCDP1
                    break

                if cnt > 30:
                    FlgError5 = 1
                    break

        # センサ誤差
        MvGCn1NHEX = GCn1NHEX * (1 + dMvGCn1NHEX)
        MvGCDP1 = GCDP1 * (1 + dMvGCDP1)
        Tv1GCn1NHEX = MvGCn1NHEX + dTv1GCn1NHEX
        Tv1GCDP1 = MvGCDP1 + dTv1GCDP1

    # 冷房運転時(冷却水はすべて冷却塔に行くため流量0)
    else:
        GCn1NHEX = 0
        MvGCn1NHEX = GCn1NHEX * (1 + dMvGCn1NHEX)
        Tv1GCn1NHEX = MvGCn1NHEX + dTv1GCn1NHEX



