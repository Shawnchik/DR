def flow_balance_ch2():
    import numpy as np
    import Branch0
    import Branch11
    import Branch10

    # 冷水二次系統の流量バランス
    # 入力値は各ポンプINVとバルブ開度Vlvである。
    # Nomenclature
    # GCh2CHEX      :熱交換器流量[m3/min]
    # GChAHU~2       :AHU流量
    # GCP2          :ポンプ一台当たり流量
    # NmCP2         :ポンプ台数
    # INVCP2        :ポンプINV
    # VlvCP2        :ポンプバイパス弁開度(1:全開,0:全閉)
    # VlvChAHU~2     :AHU二方弁開度(1:全開,0:全閉)

    global GCh2CHEX,GChAHU,VlvChAHU,GCP2,GVlvCP2,NmCP2,INVCP2,VlvCP2,PCP2
    global c0CP2,c1CP2,c2CP2,c3CP2,c4CP2
    global GCP1,INVCP1,PCP1,c0CP1,c1CP1,c2CP1,c3CP1,c4CP1,FlgError1
    global MvGCh2CHEX,dMvGCh2CHEX,Tv1GCh2CHEX,dTv1GCh2CHEX,MvGChAHU,dMvGChAHU,Tv1GChAHU,dTv1GChAHU
    global MvGCP1,dMvGCP1,Tv1GCP1,dTv1GCP1,MvGCP2,dMvGCP2,Tv1GCP2,dTv1GCP2,MvPCP1,dMvPCP1,MvPCP2,dMvPCP2
    global Tv1PCP2,dTv1PCP2
    global KrPpChAHU,KrChAHU,KrPpCh2CHEX,KrCh2CHEX,KrPpChTR4,KrChTR4
    global PChHdr,MvPChHdr,dMvPChHdr,Tv1PChHdr,dTv1PChHdr
    global CalStep
    # global MvGCh2Ld

    # if MvGCh2Ld >  8
    #     nAHU = 3
    # else
    #     nAHU = 2
    # end

    # INVが0の時は流量0とする
    if INVCP1 == 0 and INVCP2 == 0:
        GChAHU = 0
        GCP1 = 0
        GCP2 = 0
        PCP1 = 0
        PCP2 = 0
        GCh2CHEX = 0
        GVlvCP2 = 0
        dPChAHU = 0
    else:
        # whileに入るための初期値,二分法初期値
        GChAHU = 0
        GCh2CHEX = 10
        GCP1 = 0
        GChAHUmax = 20
        GChAHUmin = 0
        GChAHU200 = np.zeros(10)
        cnt = 0
        while GCh2CHEX * 2 + GCP1 - GChAHU > 0.01 or GCh2CHEX * 2 + GCP1 - GChAHU < - 0.01 :
            # 何らかの原因で収束しない場合に抜けるための保険
            cnt = cnt + 1

            # GChAHUを仮定する
            GChAHU = (GChAHUmax + GChAHUmin) / 2

            # dPChAHUを求める % 流量を出すためにここはGChAHUを2で割る。実システムはもっと多く分岐している。

            [dPChAHU] = Branch0.branch0(GChAHU/2,KrPpChAHU,0,KrChAHU,VlvChAHU,800)

            # GCh2CHEX,GCP2を求める
            [GCh2CHEX,GCP2,GVlvCP2,PCP2] = Branch11.branch11(dPChAHU,NmCP2,INVCP2,VlvCP2,100,c0CP2,c1CP2,c2CP2,c3CP2,c4CP2,KrPpCh2CHEX,KrCh2CHEX)

            # GCP1,GCP1を求める
            [_,GCP1,_,PCP1] = Branch10.branch10(dPChAHU,INVCP1,1,1900,0,121,c0CP1,c1CP1,c2CP1,c3CP1,c4CP1,KrPpChTR4,KrChTR4)

    #         if INVCP1 > 0
    #             dPChAHU
    #             PCP1
    #             PCP1 + dPChAHU - (KrPpChTR4 + KrChTR4) * GCP1^2
    #             pause
    #         end

            #  各枝の流量が釣り合うまで二分法
            if GCh2CHEX * 2 + GCP1 - GChAHU > 0:
                GChAHUmin = GChAHU
            elif GCh2CHEX * 2 + GCP1 - GChAHU < 0:
                GChAHUmax = GChAHU

            FlgError1 = 0
            # 0.1で収束しない場合
            for i in range(10,2,-1):
                GChAHU200[i] = GChAHU200[i-1]
            GChAHU200[1] = GCh2CHEX * 2 + GCP1 - GChAHU
            if GChAHU200 == GChAHU200[1]:
                FlgError1 = 1
                break
            if cnt > 30:
                FlgError1 = 1
                break

    # ヘッダ間差圧
    PChHdr = abs(dPChAHU)

    # センサ誤差
    MvGCh2CHEX = GCh2CHEX * (1 + dMvGCh2CHEX)
    MvGChAHU = GChAHU * (1 + dMvGChAHU)
    MvGCP1 = GCP1 * (1 + dMvGCP1)
    MvGCP2 = GCP2 * (1 + dMvGCP2)
    MvPCP1 = PCP1 + dMvPCP1
    MvPCP2 = PCP2 + dMvPCP2
    Tv1GCh2CHEX = MvGCh2CHEX + dTv1GCh2CHEX
    Tv1GChAHU = MvGChAHU + dTv1GChAHU
    Tv1GCP1 = MvGCP1 + dTv1GCP1
    Tv1GCP2 = MvGCP2 + dTv1GCP2
    Tv1PCP2 = MvPCP2 + dTv1PCP2

    MvPChHdr = PChHdr + dMvPChHdr
    Tv1PChHdr = MvPChHdr + dTv1PChHdr
