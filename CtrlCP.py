def ctrl_cp():
    import CtrlNmCP2
    import PID
    # 二次冷水ポンプCP2、直送系冷凍機TR4冷水ポンプCP1の制御に関するサブルーチン
    # Nomenclature
    # NmCP2: ポンプ台数
    # SpPCP2: ポンプ吐出圧設定値[kPa]
    # GCh2Ld: 負荷流量[m3 / min]
    # SgTR4: TR4運転信号(1:on, 0: off))
    # 4.98: TR4定格流量[m3 / min]
    # SpGNmCP2:台数制御用の設定流量[m3 / min]
    # TV1GNmCP2: 台数制御用の入力流量[m3 / min]
    global NmCP2,VlvCP2,PCP2,INVCP2
    global FlgNmCP2
    global FlgVlvCP2,FlgFlgVlvCP2
    global SgTR4,SpGCP1,Tv1SpLFTR4
    global INVCP1,SigGCP1
    global VlvCP20,INVCP20,INVCP10,SpGCP10
    global KpVlvCP2,TiVlvCP2,KpINVCP2,TiINVCP2,KpINVCP1,TiINVCP1

    global MvGCh2Ld,MvGCP1,MvGCP10
    global CvINVCP2,CvINVCP20,dCvINVCP2,Tv1INVCP2,dTv1INVCP2
    global CvINVCP1,CvINVCP10,dCvINVCP1,Tv1INVCP1,dTv1INVCP1
    global CvVlvCP2,CvVlvCP20,dCvVlvCP2,Tv1VlvCP2,dTv1VlvCP2
    global SpPChHdr,SpPChHdr0,SigPChHdr,PChHdr,MvPChHdr,MvPChHdr0,dMvPChHdr,Tv1PChHdr,dTv1PChHdr
    global KrCh2CHEX,GCh2CHEX

    global SpGChAHU,SpGChAHU0,MvGChAHU,MvGChAHU0,SigGChAHU

    global FlgPIDVlvCP2,FlgPIDINVCP2,FlgPIDINVCP1

    global PFVlvCP2,PFINVCP2,PFINVCP1

    global PrPChHdr

    # ポンプ台数制御（流量による制御）
    CtrlNmCP2.ctrl_nm_cp2()

    # 負荷流量がない場合、ポンプINV=0,バルブ全閉
    if MvGCh2Ld == 0:
        CvINVCP2 = 0
        CvVlvCP2 = 0
        INVCP2 = 0
        VlvCP2 = 0
        Tv1INVCP2 = 0
        Tv1VlvCP2 = 0
        CvINVCP1 = 0
        INVCP1 = 0
        Tv1INVCP1 = 0
    # 負荷流量がある場合
    else:
        FlgFlgVlvCP2 = 0   # ひとまずバイパス弁は動かさない!!!!!!!!!!!!!!!!!!!!!!

        # ポンプINV制御
        # 目標吐出圧の設定
        # 末端圧推定制御(二次)
        # バイパス弁はINV0.1が閾値。
        if FlgFlgVlvCP2 == 1:
            # INVCP2は固定値(0.1、制御計DDCからの出力のみ)とするが、制御誤差を含む
            CvINVCP2 = 0.35
            Tv1INVCP2 = CvINVCP2 + dTv1INVCP2
            INVCP2 = CvINVCP2 + dCvINVCP2
            if INVCP2 > 1:
                INVCP2 = 1
            elif INVCP2 < 0:
                INVCP2 = 0

            INVCP20 = INVCP2
            CvINVCP20 = CvINVCP2
            # 圧力をみてバイパス弁を制御する
            # ここの係数が議論の余地あり!!!
            # SpPCP2 = 1 * GCh2Ld^2
            # SpPCP2 = 0.149 * GCh2Ld^2 + 50
            # ヘッダー間差圧制御!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #         SpPChHdr = 50
            SpPChHdr = 50 + 0.149 * MvGCh2Ld^2
    #         SpPChHdr = 50 + PrPChHdr
        #     PChHdr = PCP2 - KrCh2CHEX * GCh2CHEX^2
        #     MvPChHdr = PChHdr + dMvPChHdr
        #     Tv1PChHdr = MvPChHdr + dTv1PChHdr
        #     SpPCP2 = 50
            # または、
            # SpPCP2 = 10 * (GCh2Ld / NmCP2)^2 + 50
        #     [CvVlvCP2,SpPCP20,MvPCP20,SigPCP2] = PID(1.0,0.01,1,KpVlvCP2,TiVlvCP2,0,SpPCP2,SpPCP20,MvPCP2,MvPCP20,SigPCP2,CvVlvCP20,-1)
            [CvVlvCP2,SpPChHdr0,MvPChHdr0,SigPChHdr,FlgPIDVlvCP2] = \
                PID.pid(1.0,0.001,1,KpVlvCP2,TiVlvCP2,0,SpGChAHU,SpGChAHU0,MvGChAHU,MvGChAHU0,SigGChAHU,CvVlvCP2,-1,FlgPIDVlvCP2)
            Tv1VlvCP2 = CvVlvCP2 + dTv1VlvCP2
            VlvCP2 = CvVlvCP2 + dCvVlvCP2

            if MvGCh2Ld > 0.5 and SpPChHdr > 0:
                PFVlvCP2 = PFVlvCP2 + abs((MvPChHdr - SpPChHdr) / SpPChHdr)


        # バイパス弁が閉じている場合
        else:
            VlvCP2 = 0
            CvVlvCP2 = 0
            Tv1VlvCP2 = 0
            # ヘッダー間差圧制御
    #         SpPChHdr = 50
    #         SpPChHdr = 50 + PrPChHdr
            SpPChHdr = 50 + 0.149 * MvGCh2Ld^2
        #     PChHdr = PCP2 - KrCh2CHEX * GCh2CHEX^2
        #     MvPChHdr = PChHdr + dMvPChHdr
        #     Tv1PChHdr = MvPChHdr + dTv1PChHdr
        #     SpPCP2 = 50
            # 目標吐出圧になるようにポンプINVをPI制御
            [CvINVCP2,SpPChHdr0,MvPChHdr0,SigPChHdr,FlgPIDINVCP2] = PID(1.0,0.01,1,KpINVCP2,TiINVCP2,0,SpPChHdr,SpPChHdr0,MvPChHdr,MvPChHdr0,SigPChHdr,CvINVCP2,1,FlgPIDINVCP2)
        #     [CvINVCP2,SpPCP20,MvPCP20,SigPCP2] = PID(1.0,0.001,1,KpINVCP2,TiINVCP2,0,SpPCP2,SpPCP20,MvPCP2,MvPCP20,SigPCP2,CvINVCP20,1)
            Tv1INVCP2 = CvINVCP2 + dTv1INVCP2
            INVCP2 = CvINVCP2 + dCvINVCP2

            if MvGCh2Ld > 0.5 and SpPChHdr > 0:
                PFINVCP2 = PFINVCP2 + abs((MvPChHdr - SpPChHdr) / SpPChHdr)


        # バイパス弁用フラグ（効果待ち時間5分）流量をみて制御！！！
        # if (NmCP2 == 1)&&(SigGChAHU < -3)
        #     for i = 5:-1:2
        #         FlgVlvCP2(i) = FlgVlvCP2(i-1)
        #     end
        #     FlgVlvCP2(1) = 1
        # elseif (FlgFlgVlvCP2 == 1)&&(SigGChAHU > 3)
        #     for i = 5:-1:2
        #         FlgVlvCP2(i) = FlgVlvCP2(i-1)
        #     end
        #     FlgVlvCP2(1) = 0
        # end
        # if FlgVlvCP2 == 1
        #     FlgFlgVlvCP2 = 1   # バイパス弁制御
        # elseif FlgVlvCP2 == 0
        #     FlgFlgVlvCP2 = 0
        # end


        # CP1のINV制御は流量による
        if Tv1SpLFTR4 == 0:
            SpGCP1 = 0
            INVCP1 = 0
            CvINVCP1 = 0
            Tv1INVCP1 = 0
        else:
            SpGCP1 = Tv1SpLFTR4 * 4.98
            [CvINVCP1,SpGCP10,MvGCP10,SigGCP1,FlgPIDINVCP1] = PID.pid(1.0,0.001,1,KpINVCP1,TiINVCP1,0,SpGCP1,SpGCP10,MvGCP1,MvGCP10,SigGCP1,CvINVCP1,1,FlgPIDINVCP1)
            Tv1INVCP1 = CvINVCP1 + dTv1INVCP1
            INVCP1 = CvINVCP1 + dCvINVCP1

            if SpGCP1 > 0.5:
                PFINVCP1 = PFINVCP1 + abs((MvGCP1 - SpGCP1) / SpGCP1)
