def flow_balance_fct():
    # 冷却塔ファン風量の計算
    # 冷却塔ファンは定速ファンであるため、固定値を出力する
    # Nomenclature
    # GFCT      :冷却塔ファン風量[m3/min]
    global GFCT1,GFCT2,GFCT3,NmFCT1,NmFCT2,NmFCT3

    if NmFCT1 == 0:
        GFCT1 = 10
    elif NmFCT1 == 3:
        GFCT1 = 1138 * 3

    if NmFCT2 == 0:
        GFCT2 = 10
    elif NmFCT2 == 3:
        GFCT2 = 1138 * 3
    elif NmFCT2 == 6:
        GFCT2 = 1138 * 6

    if NmFCT3 == 0:
        GFCT3 = 10
    elif NmFCT3 == 3:
        GFCT3 = 1138 * 3
    elif NmFCT3 == 6:
        GFCT3 = 1138 * 6
