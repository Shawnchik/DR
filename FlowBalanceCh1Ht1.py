def flow_balance_ch1_ht1():
    import numpy as np
    import Branch0
    import Branch01
    import Branch11
    import Branch10
    # 暖房時冷水1次温水1次系統の流量バランス
    # 入力値は各ポンプINVとバルブ開度Vlvである。各流量、圧力を出力とする。
    # Nomenclature
    # GCh1CHEX      :熱交換器一台あたり流量[m3/min]
    # GSCP4         :SCP4一台当たり流量[m3/min]
    # NmSCP4        :SCP4運転台数
    # INVSCP4       :SCP4のINV(0~1)
    # VlvSCP4       :SCP4バイパス弁開度(1:全開,0:全閉)
    # INVSCP1~3     :SCP1~3のINV(0~1)
    # GSCP1~3       :SCP1~3流量[m3/min]
    # GST           :蓄熱槽流量[m3/min]

    global GCh1CHEX
    global KrPpST,KrPpCh1CHEX,KrCh1CHEX,KrPpChTR2,KrChTR2,KrPpChTR3,KrChTR3
    global KrPpHt1HHEX,KrHt1HHEX,KrPpHtTR1,KrHtTR1
    global INVSCP2,INVSCP3,INVSCP4,NmSCP4,VlvSCP4,VlvCh1CHEX
    global c0SCP2,c1SCP2,c2SCP2,c3SCP2,c4SCP2
    global c0SCP3,c1SCP3,c2SCP3,c3SCP3,c4SCP3
    global c0SCP4,c1SCP4,c2SCP4,c3SCP4,c4SCP4
    global GSCP1,GSCP2,GSCP3,GSCP4,GVlvSCP4,PSCP1,PSCP2,PSCP3,PSCP4
    global FlgError3,FlgError12
    global ModeClHt,GST1,GST2,GST3,GST12
    global GHt1HHEX,GHtTR1,VlvHt1HHEX
    global NmSHP2,INVSHP2,VlvSHP2,c0SHP2,c1SHP2,c2SHP2,c3SHP2,c4SHP2
    global INVSHP1,c0SHP1,c1SHP1,c2SHP1,c3SHP1,c4SHP1
    global GSHP1,PSHP1,GSHP2,GVlvSHP2,PSHP2

    # 冷水系統
    # INV入力値がすべて0の場合は流量0とする
    if INVSCP2 == 0 and INVSCP3 == 0 and INVSCP4 == 0:
        GSCP2 = 0
        GSCP3 = 0
        GSCP4 = 0
        PSCP2 = 0
        PSCP3 = 0
        PSCP4 = 0
        GCh1CHEX = 0
        GVlvSCP4 = 0
        GST12 = 0
    else:
        # whileに入るための初期値,二分法初期値
        GCh1CHEX = 0
        GST12 = 20
        GSCP2 = 0
        GSCP3 = 0
        GST12max = 40
        GST12min = -40
        GST1200 = np.ones(10) * 100
        cnt = 0
        while GCh1CHEX * 2 - GST12 - GSCP2 - GSCP3 > 0.01 \
                or GCh1CHEX * 2 - GST12 - GSCP2 - GSCP3 < - 0.01:

            cnt = cnt + 1

            # GST12を仮定する
            GST12 = (GST12max + GST12min) / 2

            # dPSTを求める
            [dPST] = Branch0.branch0(GST12,KrPpST,0,0.1,1,1900)

            # GCh1CHEX,GSCP4,GVlvSCP4を求める
            if INVSCP4 == 0:
                [_,GCh1CHEX] = Branch01.branch01(dPST,KrPpCh1CHEX,KrCh1CHEX,0,VlvCh1CHEX,500,20)
                GSCP4 = 0
                PSCP4 = 0
                GVlvSCP4 = GCh1CHEX * 2
            else:
                [GCh1CHEX,GSCP4,GVlvSCP4,PSCP4] = \
                    Branch11.branch11(dPST,NmSCP4,INVSCP4,VlvSCP4,15000,c0SCP4,c1SCP4,c2SCP4,c3SCP4,c4SCP4,KrPpCh1CHEX,KrCh1CHEX)

            # GChTR2~3,GSCP2~3を求める
            [_,GSCP2,_,PSCP2] = Branch10.branch10(dPST,INVSCP2,1,1900,0,121,c0SCP2,c1SCP2,c2SCP2,c3SCP2,c4SCP2,KrPpChTR2,KrChTR2)

            [_,GSCP3,_,PSCP3] = Branch10.branch10(dPST,INVSCP3,1,1900,0,121,c0SCP3,c1SCP3,c2SCP3,c3SCP3,c4SCP3,KrPpChTR3,KrChTR3)

            # 各枝の流量が釣り合うまで二分法
            if GCh1CHEX * 2 - GST12 - GSCP2 - GSCP3 > 0:
                GST12min = GST12
            elif GCh1CHEX * 2 - GST12 - GSCP2 - GSCP3 < 0:
                GST12max = GST12

            FlgError3 = 0
            # 0.01で収束しない場合
            for i in range(10,2,-1):
                GST1200[i] = GST1200[i-1]
            GST1200[1] = GST12

            if GST1200 == GST1200[1]:
                FlgError3 = GCh1CHEX * 2 - GST12 - GSCP2 - GSCP3
                break

            if cnt > 30:
                FlgError3 = GCh1CHEX * 2 - GST12 - GSCP2 - GSCP3
                break

    # 蓄熱槽への流量の割り振り
    GST1 = GST12 * 2396 / (2396 + 1920)
    GST2 = GST12 * 1920 / (2396 + 1920)

    # 温水系統
    # INV入力値がすべて0の場合は流量0とする
    if INVSHP1 == 0 and INVSHP2 == 0:
        GSHP1 = 0
        GSHP2 = 0
        PSHP1 = 0
        PSHP2 = 0
        GHt1HHEX = 0
        GVlvSHP2 = 0
        GST3 = 0
    else:
        # whileに入るための初期値,二分法初期値
        GHt1HHEX = 0
        GST3 = 20
        GSHP1 = 0
        GST3max = 40
        GST3min = -40
        GST300 = np.ones(10) * 100
        cnt = 0
        while GHt1HHEX * 2 - GST3 - GSHP1 > 0.01 or GHt1HHEX * 2 - GST3 - GSHP1 < - 0.01:
            cnt = cnt + 1
            # GST3を仮定する
            GST3 = (GST3max + GST3min) / 2

            # dPSTを求める
            [dPST] = Branch0.branch0(GST3,KrPpST,0,0.1,1,1900)

            # GHt1HHEX,GSHP2,GVlvSHP2を求める
            if INVSHP2 == 0:
                [_,GHt1HHEX] = Branch01.branch01(dPST,KrPpHt1HHEX,KrHt1HHEX,0,VlvHt1HHEX,500,20)
                GSHP2 = 0
                PSHP2 = 0
                GVlvSHP2 = GHt1HHEX * 2
            else:
                [GHt1HHEX,GSHP2,GVlvSHP2,PSHP2] = Branch11.branch11(dPST,NmSHP2,INVSHP2,VlvSHP2,15000,c0SHP2,c1SHP2,c2SHP2,c3SHP2,c4SHP2,KrPpHt1HHEX,KrHt1HHEX)

            # GHtTR1,GSHP1を求める
            [_,GSHP1,_,PSHP1] = Branch10.branch10(dPST,INVSHP1,1,2846,0,121,c0SHP1,c1SHP1,c2SHP1,c3SHP1,c4SHP1,KrPpHtTR1,KrHtTR1)

            #  各枝の流量が釣り合うまで二分法
            if GHt1HHEX * 2 - GST3 - GSHP1 > 0:
                GST3min = GST3
            elif GHt1HHEX * 2 - GST3 - GSHP1 < 0:
                GST3max = GST3

            FlgError12 = 0
            # 0.01で収束しない場合
            for i in range(10,2,-1):
                GST300[i] = GST300[i-1]
            GST300[1] = GST3
            if GST300 == GST300[1]:
                FlgError12 = GHt1HHEX * 2 - GST3 - GSHP1
                break

            if cnt > 30:
                FlgError12 = GHt1HHEX * 2 - GST3 - GSHP1
                break


    #  SCP1(配管経路が閉ざされているため流量や圧力は0)
    GSCP1 = 0
    PSCP1 = 0

    # センサ誤差
    global MvGCh1CHEX,dMvGCh1CHEX,MvGSCP1,dMvGSCP1,MvGSCP2,dMvGSCP2,MvGSCP3,dMvGSCP3
    global Tv1GCh1CHEX,dTv1GCh1CHEX,Tv1GSCP1,dTv1GSCP1,Tv1GSCP2,dTv1GSCP2,Tv1GSCP3,dTv1GSCP3
    MvGCh1CHEX = GCh1CHEX * (1 + dMvGCh1CHEX)
    MvGSCP1 = GSCP1 * (1 + dMvGSCP1)
    MvGSCP2 = GSCP2 * (1 + dMvGSCP2)
    MvGSCP3 = GSCP3 * (1 + dMvGSCP3)
    Tv1GCh1CHEX = MvGCh1CHEX + dTv1GCh1CHEX
    Tv1GSCP1 = MvGSCP1 + dTv1GSCP1
    Tv1GSCP2 = MvGSCP2 + dTv1GSCP2
    Tv1GSCP3 = MvGSCP3 + dTv1GSCP3

    # センサ誤差
    global MvGHt1HHEX,dMvGHt1HHEX,MvGSHP1,dMvGSHP1,MvGSHP2,dMvGSHP2
    global Tv1GHt1HHEX,dTv1GHt1HHEX,Tv1GSHP1,dTv1GSHP1,Tv1GSHP2,dTv1GSHP2
    MvGHt1HHEX = GCh1CHEX * (1 + dMvGHt1HHEX)
    MvGSHP1 = GSHP1 * (1 + dMvGSHP1)
    MvGSHP2 = GSHP2 * (1 + dMvGSHP2)
    Tv1GHt1HHEX = MvGHt1HHEX + dTv1GHt1HHEX
    Tv1GSHP1 = MvGSHP1 + dTv1GSHP1
    Tv1GSHP2 = MvGSHP2 + dTv1GSHP2


    