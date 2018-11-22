def flow_balance_ch1():
    import numpy as np
    import Branch0
    import Branch01
    import Branch11
    import Branch10
    # 冷房時冷水一次系統の流量バランス
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
    global INVSCP1,INVSCP2,INVSCP3,INVSCP4,NmSCP4,VlvSCP4,VlvCh1CHEX
    global c0SCP1,c1SCP1,c2SCP1,c3SCP1,c4SCP1
    global c0SCP2,c1SCP2,c2SCP2,c3SCP2,c4SCP2
    global c0SCP3,c1SCP3,c2SCP3,c3SCP3,c4SCP3
    global c0SCP4,c1SCP4,c2SCP4,c3SCP4,c4SCP4
    global GSCP1,GSCP2,GSCP3,GSCP4,GVlvSCP4,PSCP1,PSCP2,PSCP3,PSCP4
    global FlgError3
    global GST123,GST1,GST2,GST3
    global MvGCh1CHEX,dMvGCh1CHEX,Tv1GCh1CHEX,dTv1GCh1CHEX
    global MvGSCP1,dMvGSCP1,Tv1GSCP1,dTv1GSCP1
    global MvGSCP2,dMvGSCP2,Tv1GSCP2,dTv1GSCP2
    global MvGSCP3,dMvGSCP3,Tv1GSCP3,dTv1GSCP3
    global MvGSCP4,dMvGSCP4,Tv1GSCP4,dTv1GSCP4
    global KrPpST,KrPpCh1CHEX,KrCh1CHEX,KrPpChTR1,KrChTR1,KrPpChTR2,KrChTR2,KrPpChTR3,KrChTR3

    # INV入力値がすべて0の場合は流量0とする
    if INVSCP1 == 0 and INVSCP2 == 0 and INVSCP3 == 0 and INVSCP4 == 0:
        GSCP1 = 0
        GSCP2 = 0
        GSCP3 = 0
        GSCP4 = 0
        PSCP1 = 0
        PSCP2 = 0
        PSCP3 = 0
        PSCP4 = 0
        GCh1CHEX = 0
        GVlvSCP4 = 0
        GST123 = 0
    else:
        # whileに入るための初期値,二分法初期値
        GCh1CHEX = 0
        GST123 = 20
        GSCP1 = 0
        GSCP2 = 0
        GSCP3 = 0
        GST123max = 40
        GST123min = -40
        GST12300 = np.ones(10) * 100
        cnt = 0
        while GCh1CHEX * 2 - GST123 - GSCP1 - GSCP2 - GSCP3 > 0.01 or \
                GCh1CHEX * 2 - GST123 - GSCP1 - GSCP2 - GSCP3 < - 0.01:

            cnt = cnt + 1

            # GSTを仮定する
            GST123 = (GST123max + GST123min) / 2

            # dPSTを求める
            [dPST] = Branch0.branch0(GST123,KrPpST,0,0.1,1,1900)

            # GCh1CHEX,GSCP4,GVlvSCP4を求める
            if INVSCP4 == 0:
                [_,GCh1CHEX] = Branch01.branch01(dPST,KrPpCh1CHEX,KrCh1CHEX,0,VlvCh1CHEX,500,20)
                GSCP4 = 0
                PSCP4 = 0
                GVlvSCP4 = GCh1CHEX * 2
            else:
                [GCh1CHEX,GSCP4,GVlvSCP4,PSCP4] = Branch11.branch11(dPST,NmSCP4,INVSCP4,VlvSCP4,15000,c0SCP4,c1SCP4,c2SCP4,c3SCP4,c4SCP4,KrPpCh1CHEX,KrCh1CHEX)

            # GSCP1~3,GSCP1~3を求める
            [_,GSCP1,_,PSCP1] = Branch10.branch10(dPST,INVSCP1,1,1900,0,121,c0SCP1,c1SCP1,c2SCP1,c3SCP1,c4SCP1,KrPpChTR1,KrChTR1)

            [_,GSCP2,_,PSCP2] = Branch10.branch10(dPST,INVSCP2,1,1900,0,121,c0SCP2,c1SCP2,c2SCP2,c3SCP2,c4SCP2,KrPpChTR2,KrChTR2)

            [_,GSCP3,_,PSCP3] = Branch10.branch10(dPST,INVSCP3,1,1900,0,121,c0SCP3,c1SCP3,c2SCP3,c3SCP3,c4SCP3,KrPpChTR3,KrChTR3)


            # 各枝の流量が釣り合うまで二分法
            if GCh1CHEX * 2 - GST123 - GSCP1 - GSCP2 - GSCP3 > 0:
                GST123min = GST123
            elif GCh1CHEX * 2 - GST123 - GSCP1 - GSCP2 - GSCP3 < 0:
                GST123max = GST123

            FlgError3 = 0
            # 0.01で収束しない場合
            for i in range(10,2,-1):
                GST12300[i]= GST12300[i-1]
            GST12300[1]= GST123

            if GST12300 == GST12300[1]:
                # FlgError3 = 1
                FlgError3 = GCh1CHEX * 2 - GST123 - GSCP1 - GSCP2 - GSCP3
                break

            if cnt > 30:
                FlgError3 = GCh1CHEX * 2 - GST123 - GSCP1 - GSCP2 - GSCP3


    # 蓄熱槽への流量の割り振り
    GST1 = GST123 * 2396 / (2396 + 1920 + 2154)
    GST2 = GST123 * 1920 / (2396 + 1920 + 2154)
    GST3 = GST123 * 2154 / (2396 + 1920 + 2154)

    # センサ誤差
    MvGCh1CHEX = GCh1CHEX * (1 + dMvGCh1CHEX)
    MvGSCP1 = GSCP1 * (1 + dMvGSCP1)
    MvGSCP2 = GSCP2 * (1 + dMvGSCP2)
    MvGSCP3 = GSCP3 * (1 + dMvGSCP3)
    MvGSCP4 = GSCP4 * (1 + dMvGSCP4)
    Tv1GCh1CHEX = MvGCh1CHEX + dTv1GCh1CHEX
    Tv1GSCP1 = MvGSCP1 + dTv1GSCP1
    Tv1GSCP2 = MvGSCP2 + dTv1GSCP2
    Tv1GSCP3 = MvGSCP3 + dTv1GSCP3
    Tv1GSCP4 = MvGSCP4 + dTv1GSCP4

