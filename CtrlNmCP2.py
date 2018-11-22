def ctrl_nm_cp2():
    # 冷水2次放熱ポンプ台数制御（流量による制御）
    # Nomenclature
    # WTNmCP2       :効果待ち時間[min]
    global NmCP2, FlgUpNmCP2, FlgDwNmCP2, MvGCh2Ld, Tv1SpLFTR4

    # 効果待ち時間15分
    WTNmCP2 = 15
    # 流量設定値
    SpGNmCP2 = MvGCh2Ld - 4.98 * Tv1SpLFTR4

    # 増台時
    if SpGNmCP2 > 17.622:
        for i in range(WTNmCP2,2,-1):
            FlgUpNmCP2[i] = FlgUpNmCP2[i-1]

        FlgUpNmCP2[1] = 5

    elif SpGNmCP2 > 11.748:
        for i in range(WTNmCP2,2,-1):
            FlgUpNmCP2[i] = FlgUpNmCP2[i-1]

        FlgUpNmCP2[1] = 4

    elif SpGNmCP2 > 5.874:
        for i in range(WTNmCP2,2,-1):
            FlgUpNmCP2[i] = FlgUpNmCP2[i-1]

        FlgUpNmCP2[1] = 3

    elif SpGNmCP2 > 2.937:
        for i in range(WTNmCP2,2,-1):
            FlgUpNmCP2[i] = FlgUpNmCP2[i-1]

        FlgUpNmCP2[1] = 2

    else:
        for i in range(WTNmCP2,2,-1):
            FlgUpNmCP2[i] = FlgUpNmCP2[i-1]

        FlgUpNmCP2[1] = 1


    # 減台時
    if SpGNmCP2 < 2.67:
        for i in range(WTNmCP2,2,-1):
            FlgDwNmCP2[i] = FlgDwNmCP2[i-1]

        FlgDwNmCP2[1] = 1

    elif SpGNmCP2 < 5.34:
        for i in range(WTNmCP2,2,-1):
            FlgDwNmCP2[i] = FlgDwNmCP2[i-1]

        FlgDwNmCP2[1] = 2

    elif SpGNmCP2 < 10.68:
        for i in range(WTNmCP2,2,-1):
            FlgDwNmCP2[i] = FlgDwNmCP2[i-1]

        FlgDwNmCP2[1] = 3

    elif SpGNmCP2 < 16.02:
        for i in range(WTNmCP2,2,-1):
            FlgDwNmCP2[i] = FlgDwNmCP2[i-1]

        FlgDwNmCP2[1] = 4

    else:
        for i in range(WTNmCP2,2,-1):
            FlgDwNmCP2[i] = FlgDwNmCP2[i-1]

        FlgDwNmCP2[1] = 5

    # 運転台数の決定
    # 1台になる
    if NmCP2 >= 2:
        if FlgDwNmCP2 == 1:
            NmCP2 = 1

    # 2台になる
    if NmCP2 >= 3:
        if FlgDwNmCP2 == 2:
            NmCP2 = 2

    elif NmCP2 == 1:
        if FlgUpNmCP2 == 2:
            NmCP2 = 2

    # 3台になる
    if NmCP2 >= 4:
        if FlgDwNmCP2 == 3:
            NmCP2 = 3

    elif NmCP2 <= 2:
        if FlgUpNmCP2 == 3:
            NmCP2 = 3

    # 4台になる
    if NmCP2 == 5:
        if FlgDwNmCP2 == 4:
            NmCP2 = 4

    elif NmCP2 <= 3:
        if FlgUpNmCP2 == 4:
            NmCP2 = 4

    # 5台になる
    if NmCP2 <= 4:
        if FlgUpNmCP2 == 5:
            NmCP2 = 5

