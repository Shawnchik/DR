def ct_system():
    import CtrlCT
    import FlowBalanceFCT
    # 冷却塔システム

    # 冷却塔制御
    CtrlCT.ctrl_ct()

    # 風量計算
    FlowBalanceFCT.flow_balance_fct()