def primary_system():
    import CtrlSgSt_design
    import CtrlSpLFTR_design
    import CtrlSCP
    import CtrlSCP234
    import CtrlSHP
    import FlowBalanceCh1
    import FlowBalanceCh1Ht1
    # 一次システム
    # Nomenclature
    # ModeClHt      :冷暖房モード（1:冷房、0,冷暖房）Mode Cooling Heating
    global ModeClHt
    global CvINVSHP1,SpGSHP10,MvGSHP10,SpGSHP1,CvINVSHP10
    global Tv1INVSHP1,INVSHP1,INVSHP10
    global INVSHP2,Tv1INVSHP2,CvINVSHP2
    global INVSHP20,CvINVSHP20,Tv1VlvSHP2,VlvSHP2,VlvSHP20,CvVlvSHP2,CvVlvSHP20
    global CvVlvHt1HHEX,Tv1VlvHt1HHEX,VlvHt1HHEX
    global VlvHt1HHEX0,CvVlvHt1HHEX0,NmSHP2,MvGHt2Ld
    global GHt1HHEX,MvGHt1HHEX,GSHP1,MvGSHP1,GSHP2,MvGSHP2
    global Tv1GHt1HHEX,Tv1GSHP1,Tv1GSHP2

    # 蓄放熱制御（1:蓄熱、0:蓄熱終了、2:追掛）
    CtrlSgSt_design.ctrl_sg_st_design()

    # 冷凍機設定値（負荷率、ON/OFF設定）制御
    CtrlSpLFTR_design.ctrl_sp_lf_tr_design()

    # TR4をできる限り動かす
    # CtrlSpLFTR4_TR7

    # # 定格条件でとにかくTR4を動かす
    # CtrlSpLFTR4_design

    # 最適制御を試みる
    # CtrlSpLFTR_Optimal0

    # 一次ポンプ、弁制御
    # 冷房運転時
    if ModeClHt == 1:
        CtrlSCP.ctrl_scp()

        # CtrlSHP
        CvINVSHP1 = 0
        SpGSHP10 = 0
        MvGSHP10 = 0
        SpGSHP1 = 0
        CvINVSHP10 = 0
        Tv1INVSHP1 = 0
        INVSHP1 = 0
        INVSHP10 = 0
        INVSHP2 = 0
        Tv1INVSHP2 = 0
        CvINVSHP2 = 0
        INVSHP20 = 0
        CvINVSHP20 = 0
        Tv1VlvSHP2 = 0
        VlvSHP2 = 0
        VlvSHP20 = 0
        CvVlvSHP2 = 0
        CvVlvSHP20 = 0
        CvVlvHt1HHEX = 0
        Tv1VlvHt1HHEX = 0
        VlvHt1HHEX = 0
        VlvHt1HHEX0 = 0
        CvVlvHt1HHEX0 = 0
        NmSHP2 = 1
        MvGHt2Ld = 0

    # 暖房運転時
    else:
        CtrlSCP234.ctrl_scp234()
        CtrlSHP.ctrl_shp()


    # 流量バランス計算
    if ModeClHt == 1:
        FlowBalanceCh1.flow_balance_ch1()

        # Ht1
        GHt1HHEX = 0
        MvGHt1HHEX = 0
        GSHP1 = 0
        MvGSHP1 = 0
        GSHP2 = 0
        MvGSHP2 = 0
        Tv1GHt1HHEX = 0
        Tv1GSHP1 = 0
        Tv1GSHP2 = 0

    else:
        FlowBalanceCh1Ht1.flow_balance_ch1_ht1()