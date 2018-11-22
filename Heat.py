def heat():
    import HeatAHU
    import HeatTR
    import HeatST
    import HeatCHEX
    import HeatHHEX
    import HeatNHEX
    import HeatCT
    import Temperature
    # 熱の計算。機器の流量と入口温度から出口温度や熱量について計算する。
    # Nomenclature
    #
    global SgNHEXCT

    # AHU
    # ToutCh2CHEX,ToutChTR4からTinAHU,ToutAHU
    HeatAHU.heat_ahu()

    # 冷凍機
    # ToutCh1CHEX,ToutSTからTinChTR1~3
    # ToutChTR1~3からTinCh1CHEX
    # ToutAHUからTinChTR4,ToutChTR4
    HeatTR.heat_tr()

    # 蓄熱槽
    # ToutChTR3,ToutCh1CHEXからTinST
    HeatST.heat_st()

    # 熱交換器
    # ToutAHUからTinCh2CHEX
    # ToutChTR3,ToutSTからTinCh1CHEX
    # TinCh1CHEX,TinCh2CHEXからToutCh1CHEX,ToutCh2CHEX
    # 冷水
    HeatCHEX.heat_chex()
    # 温水
    HeatHHEX.heat_hhex()

    # 下水熱利用のみ時
    if SgNHEXCT == 1:

        # 下水熱利用熱交換器
        HeatNHEX.heat_nhex()


    # 冷却塔利用時
    else:
        # 冷却塔
        HeatCT.heat_ct()


    # 温度の時刻調整
    Temperature.tenperature()

