def condenser_system():
    import CtrlCDP
    import SewageSystem
    import FlowBalanceCnNHEX
    import FlowBalanceCnCTHt
    import FlowBalanceCnCTCl
    import FlowBalanceCnNHEX1
    import CTSystem
    # 冷却水システム
    # Nomenclature
    # SgNHEXCT  :下水/冷却塔切換信号(1:下水,0:冷却塔)
    # ModeClHt      :運転モード（1:冷房モード、0:冷暖房モード）
    global SgNHEXCT,NmFCT1,NmFCT2,NmFCT3,NmPmpCT,GFCT1,GFCT2,GFCT3,NmPmpCT1,NmPmpCT2,NmPmpCT3
    global GCnCT1,GCnCT2,GCnCT3,GVlvCT,FlgFlgVlvCT
    global ModeClHt
    global NmNP,INVNP,INVNP0,CvINVNP,CvINVNP0,Tv1INVNP,GCn2NHEX,GSw,GNP,PNP
    global MvGCn2NHEX,dMvGCn2NHEX,MvGNP,dMvGNP
    global Tv1GCn2NHEX,dTv1GCn2NHEX,Tv1GNP,dTv1GNP
    # 冷却水ポンプ、弁制御
    CtrlCDP.ctrl_cdp()

    # 下水熱利用時
    if SgNHEXCT == 1:
        # 下水熱ポンプシステム
        SewageSystem.swage_system()

        # 流量バランス計算
        FlowBalanceCnNHEX.flow_balance_cn_nhex()

        NmPmpCT = 0
        NmFCT1 = 0
        NmFCT2 = 0
        NmFCT3 = 0
        NmPmpCT1 = 0
        NmPmpCT2 = 0
        NmPmpCT3 = 0
        GCnCT1 = 0
        GCnCT2 = 0
        GCnCT3 = 0
        GVlvCT = 0
        FlgFlgVlvCT = 0
        # 非運転時は自然対流が10m3/minあるとする
        GFCT1 = 10
        GFCT2 = 10
        GFCT3 = 10


    # 冷却塔利用時
    else:


        # 冷暖房時
        if ModeClHt == 0:
            # 下水熱ポンプシステム
            SewageSystem.swage_system()
            # 流量計算
            FlowBalanceCnCTHt.flow_balance_cn_ct_ht()

        # 冷房時
        else:
            NmNP = 1
            INVNP = 0
            INVNP0 = 0
            CvINVNP = 0
            CvINVNP0 = 0
            Tv1INVNP = 0
            GCn2NHEX = 0
            GSw = 0
            GNP = 0
            PNP = 0
            MvGCn2NHEX = GCn2NHEX * (1 + dMvGCn2NHEX)
            MvGNP = GNP * (1 + dMvGNP)
            Tv1GCn2NHEX = MvGCn2NHEX + dTv1GCn2NHEX
            Tv1GNP = MvGNP + dTv1GNP

            FlowBalanceCnCTCl.flow_balance_cn_ct_cl()

        # GCn1NHEXまわり
        FlowBalanceCnNHEX1.flow_balance_cn_nhex1()

        # 冷却塔システム
        CTSystem.ct_system()




