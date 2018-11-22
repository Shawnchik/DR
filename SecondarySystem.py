def secondary_system():
    import CtrlCP
    import CtrlVlvChAHU
    import FlowBalanceCh2
    import CtrlHP
    import CtrlVlvHtAHU
    import FlowBalanceHt2
    # 二次ポンプシステム
    # Nomenclature
    # ModeClHt      :運転モード（1:冷房モード、0:冷暖房モード）
    global ModeClHt
    global NmHP1,INVHP1,VlvHP1
    global SpGHtAHU,GHt2Ld,VlvHtAHU,SpGHtAHU0,GHtAHU0,SigGHtAHU
    global GHtAHU,MvGHtAHU,Tv1GHtAHU,GHt2HHEX,MvGHt2HHEX,Tv1GHt2HHEX
    global GHP1,MvGHP1,Tv1GHP1,GVlvHP1,MvGVlvHP1,Tv1GVlvHP1,PHP1

    # 冷水系統
    # ポンプ台数・INV制御
    CtrlCP.ctrl_cp()

    # 冷水AHU二方弁制御
    CtrlVlvChAHU.ctrl_vlv_ch_ahu()

    # 流量バランス計算。制御されたポンプ台数・INV、ポンプバイパス弁開度、AHU二方弁開度から流量を求める
    FlowBalanceCh2.flow_balance_ch2()

    # 温水系統
    # 冷房モード時
    if ModeClHt == 1:
        # 温水系統は計算時間短縮のため計算しない。
        # ここはもっと詰める必要がある!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # CtrlHP
        NmHP1 = 1
        INVHP1 = 0
        VlvHP1 = 0
        # CtrlVlvHtAHU
        SpGHtAHU = 0
        GHt2Ld = 0
        VlvHtAHU = 0
        SpGHtAHU0 = 0
        GHtAHU0 = 0
        SigGHtAHU = 0
        # FlowBalanceHt2
        GHtAHU = 0
        MvGHtAHU = 0
        Tv1GHtAHU = 0
        GHt2HHEX = 0
        MvGHt2HHEX = 0
        Tv1GHt2HHEX = 0
        GHP1 = 0
        MvGHP1 = 0
        Tv1GHP1 = 0
        GVlvHP1 = 0
        MvGVlvHP1 = 0
        Tv1GVlvHP1 = 0
        PHP1 = 0

    # 冷暖房モード時
    else:
        # ポンプ台数・INV制御
        CtrlHP.ctrl_hp()

        # 温水AHU二方弁制御
        CtrlVlvHtAHU.ctrl_vlv_ht_ahu()

        # 流量バランス計算。制御されたポンプ台数・INV、ポンプバイパス弁開度、AHU二方弁開度から流量を求める
        FlowBalanceHt2.flow_balance_ht2()
