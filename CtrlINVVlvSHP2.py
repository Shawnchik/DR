def ctrl_inv_vlv_shp():
    import PID
    # SHP2のINVと、バイパス弁制御
    global FlgFlgVlvSHP2,INVSHP2,dCvINVSHP2,Tv1INVSHP2,dTv1INVSHP2,CvINVSHP2
    global INVSHP20,CvINVSHP20,SpToutHt2HHEX,CvVlvSHP2,SpToutHt2HHEX0,MvToutHt2HHEX0
    global SigToutHt2HHEX,FlgPIDVlvSHP2,KpVlvSHP2,TiVlvSHP2,MvToutHt2HHEX,CvVlvSHP20
    global Tv1VlvSHP2,dTv1VlvSHP2,VlvSHP2,dCvVlvSHP2,VlvSHP20
    global FlgPIDINVSHP2,KpINVSHP2,TiINVSHP2,NmSHP2,FlgVlvSHP2
    global GHt2HHEX,PFVlvSHP2,PFINVSHP2
    # バイパス弁制御時
    if FlgFlgVlvSHP2 == 1:
        CvINVSHP2 = 0.3
        Tv1INVSHP2 = CvINVSHP2 + dTv1INVSHP2
        INVSHP2 = CvINVSHP2 + dCvINVSHP2
        if INVSHP2 > 1:
            INVSHP2 = 1
        elif INVSHP2 < 0:
            INVSHP2 = 0
        INVSHP20 = INVSHP2
        CvINVSHP20 = CvINVSHP2
        # 温度をみてバイパス弁を制御する
        [CvVlvSHP2,SpToutHt2HHEX0,MvToutHt2HHEX0,SigToutHt2HHEX,FlgPIDVlvSHP2] = \
            PID.pid(1.0,0.001,1,KpVlvSHP2,TiVlvSHP2,0,SpToutHt2HHEX,SpToutHt2HHEX0,MvToutHt2HHEX,MvToutHt2HHEX0,SigToutHt2HHEX,CvVlvSHP2,-1,FlgPIDVlvSHP2)
        Tv1VlvSHP2 = CvVlvSHP2 + dTv1VlvSHP2
        VlvSHP2 = CvVlvSHP2 + dCvVlvSHP2

        if GHt2HHEX > 0.25 and SpToutHt2HHEX > 0:
            PFVlvSHP2 = PFVlvSHP2 + abs(MvToutHt2HHEX - SpToutHt2HHEX) / SpToutHt2HHEX

    # 流量が十分で、ポンプSHP2のINV制御を行う場合
    else:
        VlvSHP2 = 0
        CvVlvSHP2 = 0
        VlvSHP20 = 0
        CvVlvSHP20 = 0
        Tv1VlvSHP2 = 0
        # 目標温度になるようにポンプINVをPI制御
        [CvINVSHP2,SpToutHt2HHEX0,MvToutHt2HHEX0,SigToutHt2HHEX,FlgPIDINVSHP2] = \
            PID.pid(1.0,0.3,1,KpINVSHP2,TiINVSHP2,0,SpToutHt2HHEX,SpToutHt2HHEX0,MvToutHt2HHEX,MvToutHt2HHEX0,SigToutHt2HHEX,CvINVSHP2,1,FlgPIDINVSHP2)
        Tv1INVSHP2 = CvINVSHP2 + dTv1INVSHP2
        INVSHP2 = CvINVSHP2 + dCvINVSHP2

        if GHt2HHEX > 0.25 and SpToutHt2HHEX > 0:
            PFINVSHP2 = PFINVSHP2 + abs(MvToutHt2HHEX - SpToutHt2HHEX) / SpToutHt2HHEX


    # バイパス弁用フラグ（効果待ち時間5分）
    if MvToutHt2HHEX > SpToutHt2HHEX + 1 and CvINVSHP2 < 0.35:
    #         if (NmSHP2 == 1)&&(SigToutHt2HHEX < - 10)
        for i in range(15,2,-1):
            FlgVlvSHP2[i] = FlgVlvSHP2[i-1]
        FlgVlvSHP2[1] = 1

    elif MvToutHt2HHEX < SpToutHt2HHEX - 1 and CvVlvSHP2 < 0.05:
    # if (NmSHP2 == 1)&&(SigToutHt2HHEX > 10)
        for i in range(15, 2, -1):
            FlgVlvSHP2[i] = FlgVlvSHP2[i - 1]
        FlgVlvSHP2[1] = -1
    else:
        for i in range(15, 2, -1):
            FlgVlvSHP2[i] = FlgVlvSHP2[i - 1]
        FlgVlvSHP2[1] = 0

    if FlgVlvSHP2 == 1:
        FlgFlgVlvSHP2 = 1
    elif FlgVlvSHP2 == -1:
        FlgFlgVlvSHP2 = 0

    # if NmSHP2 > 1
    #     FlgFlgVlvSHP2 = 0
    # end
