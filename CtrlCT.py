def ctrl_ct():
    import CtrlNmCT
    import CtrlNmPmpCT
    import CtrlNmFCT
    import CtrlVlvCT
    # 冷却塔制御
    # Nomenclature
    # NmCT      :冷却塔運転台数(最大6大)
    global MvGCDP2,MvGCDP3,MvGCDP4
    global NmCT,NmPmpCT1,NmPmpCT2,NmPmpCT3,NmFCT1,NmFCT2,NmFCT3,VlvCT
    global CvVlvCT,VlvCT0,CvVlvCT0,Tv1VlvCT,FlgFlgVlvCT

    MvGCn = MvGCDP2 + MvGCDP3 + MvGCDP4

    if MvGCn > 0:
        # 冷却塔台数制御
        CtrlNmCT.ctrl_nm_ct()

        # 散水ポンプ台数制御
        CtrlNmPmpCT.ctrl_nm_pmp_ct()

        # ファン台数制御
        CtrlNmFCT.ctrl_nm_fct()

        # バイパス弁制御
        CtrlVlvCT.ctrl_vlv_ct()

    else:
        NmCT = 0
        NmPmpCT1 = 0
        NmPmpCT2 = 0
        NmPmpCT3 = 0
        NmFCT1 = 0
        NmFCT2 = 0
        NmFCT3 = 0
        VlvCT = 0
        CvVlvCT = 0
        VlvCT0 = 0
        CvVlvCT0 = 0
        Tv1VlvCT = 0
        FlgFlgVlvCT = 0

