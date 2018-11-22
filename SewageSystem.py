def sewage_system():
    import CtrlNP
    import FlowBalanceSw
    # 下水熱利用システム。下水ポンプと下水流量の計算

    # 下水ポンプ制御
    CtrlNP.ctrl_np()

    # 流量バランス計算
    FlowBalanceSw.flow_balacne_sw()