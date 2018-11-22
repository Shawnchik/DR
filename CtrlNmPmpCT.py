def ctrl_nm_pmp_ct():
    # 散水ポンプ台数制御
    global NmCT,NmPmpCT1,NmPmpCT2,NmPmpCT3

    # 散水ポンプ台数は冷却塔台数によるものとする
    if NmCT == 1:
        NmPmpCT1 = 2
        NmPmpCT2 = 0
        NmPmpCT3 = 0
    elif NmCT == 2:
        NmPmpCT1 = 2
        NmPmpCT2 = 4
        NmPmpCT3 = 0
    else:
        NmPmpCT1 = 2
        NmPmpCT2 = 4
        NmPmpCT3 = 4