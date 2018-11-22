def ctrl_hp():
    import CtrlNmHP1
    import PID
    # 二次冷水ポンプHP1の制御に関するサブルーチン
    # Nomenclature
    # NmHP1         :ポンプ台数
    # SpPHP1        :ポンプ吐出圧設定値[kPa]
    # GHt2Ld        :負荷流量[m3/min]
    global NmHP1,CvVlvHP1,SpPHtHdr,MvPHtHdr,SpPHtHdr0,MvPHtHdr0,SigPHtHdr,CvVlvHP10,INVHP1,VlvHP1
    global FlgVlvHP1,FlgFlgVlvHP1
    global VlvHP10,INVHP10
    global KpVlvHP1,TiVlvHP1,KpINVHP1,TiINVHP1
    global FlgPIDVlvHP1,FlgPIDINVHP1
    global MvGHt2Ld
    global CvINVHP1,Tv1INVHP1,Tv1VlvHP1,CvINVHP10,dCvINVHP1,dTv1INVHP1,dTv1VlvHP1,dCvVlvHP1
    global PFVlvHP1,PFINVHP1

    # ポンプ台数制御（流量による制御）
    CtrlNmHP1.ctrl_nm_hp1()

    # ポンプINV制御
    # ヘッダー間差圧一定制御
    # バイパス弁はポンプINV0.1が閾値。
    # 負荷流量がない場合、ポンプINV=0,バルブ全閉
    if MvGHt2Ld == 0:
        CvINVHP1 = 0
        CvVlvHP1 = 0
        CvINVHP10 = 0
        CvVlvHP10 = 0
        INVHP1 = 0
        VlvHP1 = 0
        INVHP10 = 0
        VlvHP10 = 0
        Tv1INVHP1 = 0
        Tv1VlvHP1 = 0
        SpPHtHdr = 0
    # ���ח��負荷流量がある場合
    else:
        FlgFlgVlvHP1 = 0           # ひとまずバイパス弁は動かさない!!!!!!!!!!!

        # 流量が少なく、バイパス弁制御を行う場合
        if FlgFlgVlvHP1 == 1:
            CvINVHP1= 0.1
            Tv1INVHP1 = CvINVHP1 + dTv1INVHP1
            INVHP1 = CvINVHP1 + dCvINVHP1
            if INVHP1 > 1:
                INVHP1 = 1
            elif INVHP1 < 0:
                INVHP1 = 0
            INVHP10 = INVHP1
            CvINVHP10 = CvINVHP1

            # ヘッダー間差圧制御!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            SpPHtHdr = 50
    #         SpPHtHdr = 50 + 0.1488 * MvGHt2Ld^2
    #         PHtHdr = PHP1 - KrHt2HHEX * GHt2HHEX^2
            [CvVlvHP1,SpPHtHdr0,MvPHtHdr0,SigPHtHdr,FlgPIDVlvHP1] = PID.pid(1.0,0.001,1,KpVlvHP1,TiVlvHP1,0,SpPHtHdr,SpPHtHdr0,MvPHtHdr,MvPHtHdr0,SigPHtHdr,CvVlvHP1,-1,FlgPIDVlvHP1)
            Tv1VlvHP1 = CvVlvHP1 + dTv1VlvHP1
            VlvHP1 = CvVlvHP1 + dCvVlvHP1

            if (MvGHt2Ld > 0.5)&&(SpPHtHdr > 0)
                PFVlvHP1 = PFVlvHP1 + abs((MvPHtHdr - SpPHtHdr) / SpPHtHdr)

        # 流量が多く、ポンプINV制御を行う場合
        else:
            CvVlvHP1 = 0
            VlvHP1 = 0
            Tv1VlvHP1 = 0
            # ヘッダー間差圧制御!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            SpPHtHdr = 50
    #         SpPHtHdr = 50 + 0.1488 * MvGHt2Ld^2
    #         PHtHdr = PHP1 - KrHt2HHEX * GHt2HHEX^2
            [CvINVHP1,SpPHtHdr0,MvPHtHdr0,SigPHtHdr,FlgPIDINVHP1] = PID.pid(1.0,0.001,1,KpINVHP1,TiINVHP1,0,SpPHtHdr,SpPHtHdr0,MvPHtHdr,MvPHtHdr0,SigPHtHdr,CvINVHP1,1,FlgPIDINVHP1)
            Tv1INVHP1 = CvINVHP1 + dTv1INVHP1
            INVHP1 = CvINVHP1 + dCvINVHP1

            if MvGHt2Ld > 0.5 and SpPHtHdr > 0:
                PFINVHP1 = PFINVHP1 + abs((MvPHtHdr - SpPHtHdr) / SpPHtHdr)

    # バイパス弁用フラグ（効果待ち時間5分）
    # if INVHP1 < 0.1
    #     for i = 5:-1:2
    #         FlgVlvHP1(i) = FlgVlvHP1(i-1)
    #     end
    #     FlgVlvHP1(1) = 1
    # end
    # if (FlgFlgVlvHP1 == 1)&&(VlvHP1 < 0.05)
    #     for i = 5:-1:2
    #         FlgVlvHP1(i) = FlgVlvHP1(i-1)
    #     end
    #     FlgVlvHP1(1) = 0
    # end
    # if FlgVlvHP1 == 1
    #     FlgFlgVlvHP1 = 1
    # elseif FlgVlvHP1 == 0
    #     FlgFlgVlvHP1 = 0


