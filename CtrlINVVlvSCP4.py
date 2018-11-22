def ctrl_inv_vlv_scp4():
    import PID
    # SCP4のINVと、バイパス弁制御
    global FlgFlgVlvSCP4,INVSCP4,dCvINVSCP4,Tv1INVSCP4,dTv1INVSCP4,CvINVSCP4
    global INVSCP40,CvINVSCP40,CvVlvSCP4,SpToutCh2CHEX0,MvToutCh2CHEX0,SigToutCh2CHEX
    global FlgPIDVlvSCP4,KpVlvSCP4,TiVlvSCP4,SpToutCh2CHEX,MvToutCh2CHEX,CvVlvSCP40
    global Tv1VlvSCP4,dTv1VlvSCP4,VlvSCP4,dCvVlvSCP4,VlvSCP40,FlgPIDINVSCP4,KpINVSCP4,TiINVSCP4
    global NmSCP4,FlgVlvSCP4
    global GCh2CHEX,PFVlvSCP4,PFINVSCP4
    # ポンプINV制御
    # バイパス弁制御ON時
    # バイパス弁はINV0.1が閾値
    if FlgFlgVlvSCP4 == 1:
        CvINVSCP4 = 0.1
        INVSCP4 = CvINVSCP4 + dCvINVSCP4
        Tv1INVSCP4 = CvINVSCP4 + dTv1INVSCP4
        if INVSCP4 > 1:
            INVSCP4 = 1
        elif INVSCP4 < 0:
            INVSCP4 = 0

        INVSCP40 = INVSCP4
        CvINVSCP40 = CvINVSCP4
        # 温度をみてバイパス弁を制御する
        [CvVlvSCP4,SpToutCh2CHEX0,MvToutCh2CHEX0,SigToutCh2CHEX,FlgPIDVlvSCP4] = \
            PID.pid(1.0,0.001,1,KpVlvSCP4,TiVlvSCP4,0,SpToutCh2CHEX,SpToutCh2CHEX0,MvToutCh2CHEX,MvToutCh2CHEX0,SigToutCh2CHEX,CvVlvSCP4,1,FlgPIDVlvSCP4)
        Tv1VlvSCP4 = CvVlvSCP4 + dTv1VlvSCP4
        VlvSCP4 = CvVlvSCP4 + dCvVlvSCP4

        if GCh2CHEX > 0.25 and SpToutCh2CHEX > 0:
            PFVlvSCP4 = PFVlvSCP4 + abs(MvToutCh2CHEX - SpToutCh2CHEX) / SpToutCh2CHEX


    # バイパス弁制御OFF時
    else:
        VlvSCP4 = 0
        CvVlvSCP4 = 0
        Tv1VlvSCP4 = 0
        # 目標温度になるようにポンプINVをPI制御
        [CvINVSCP4,SpToutCh2CHEX0,MvToutCh2CHEX0,SigToutCh2CHEX,FlgPIDINVSCP4] = \
            PID.pid(1.0,0.1,1,KpINVSCP4,TiINVSCP4,0,SpToutCh2CHEX,SpToutCh2CHEX0,MvToutCh2CHEX,MvToutCh2CHEX0,SigToutCh2CHEX,CvINVSCP4,-1,FlgPIDINVSCP4)
        Tv1INVSCP4 = CvINVSCP4 + dTv1INVSCP4
        INVSCP4 = CvINVSCP4 + dCvINVSCP4

        if GCh2CHEX > 0.25 and SpToutCh2CHEX > 0:
            PFINVSCP4 = PFINVSCP4 + abs(MvToutCh2CHEX - SpToutCh2CHEX) / SpToutCh2CHEX


    # バイパス弁用フラグ（効果待ち時間10分）
    if MvToutCh2CHEX < SpToutCh2CHEX - 1 and CvINVSCP4 < 0.35:
    #     if (NmSCP4 == 1)&&(SigToutCh2CHEX > 10)
        for i in range(15,2,-1):
            FlgVlvSCP4[i] = FlgVlvSCP4[i-1]
        FlgVlvSCP4[1] = 1

    # #     if MvToutCh2CHEX > 7.5
    elif MvToutCh2CHEX > SpToutCh2CHEX + 1 and CvVlvSCP4 < 0.05:
        for i in range(15,2,-1):
            FlgVlvSCP4[i] = FlgVlvSCP4[i-1]
        FlgVlvSCP4[1] = -1

    else:
        for i in range(15,2,-1):
            FlgVlvSCP4[i] = FlgVlvSCP4[i-1]
        FlgVlvSCP4[1] = 0

    if FlgVlvSCP4 == 1:
        FlgFlgVlvSCP4 = 1
    #     NmSCP4 = 1
    elif FlgVlvSCP4 == -1:
        FlgFlgVlvSCP4 = 0

    # if NmSCP4 > 1
    #     FlgFlgVlvSCP4 = 0
    # end
