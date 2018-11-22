def ctrl_nm_fct():
    # 冷却塔ファン台数制御
    # Nomenclature
    # NmFCT     :冷却塔ファン運転順序
    # NmTCT1~3  :冷却塔CT1~3ファン運転台数
    # NmCT      :冷却塔運転台数
    # Tair      :外気温度['C]
    # RH        :相対湿度[#]
    # SpToutChTR1   :冷凍機冷水出口設定温度['C]
    global NmFCT,Tair,RH,MvToutCnCT,FlgUpNmFCT,FlgDwNmFCT,NmFCT1,NmFCT2,NmFCT3,NmCT
    global SpToutChTR1,Twb

    # 運転開始時
    if NmFCT == 0:
        NmFCT = 1

    # 冷却塔冷却水出口温度設定値
    SpToutCT = Twb + 5
    if SpToutCT < SpToutChTR1 + 6:
        SpToutCT = SpToutChTR1 + 6

    # 効果待ち時間15分
    WTNmFCT = 15

    # 増台時
    if NmFCT == 1:
        if MvToutCnCT - SpToutCT > 2:
            for i in range(WTNmFCT,2,-1):
                FlgUpNmFCT[i] = FlgUpNmFCT[i-1]
            FlgUpNmFCT[1] = 2

        else:
            for i in range(WTNmFCT, 2, -1):
                FlgUpNmFCT[i] = FlgUpNmFCT[i - 1]
            FlgUpNmFCT[1] = 1

    elif NmFCT == 2:
        if MvToutCnCT - SpToutCT > 2:
            for i in range(WTNmFCT, 2, -1):
                FlgUpNmFCT[i] = FlgUpNmFCT[i - 1]
            FlgUpNmFCT[1] = 3

        else:
            for i in range(WTNmFCT, 2, -1):
                FlgUpNmFCT[i] = FlgUpNmFCT[i - 1]
            FlgUpNmFCT[1] = 2

    # 減台時（効果待ち時間15分）
    if NmFCT == 3:
        if MvToutCnCT - SpToutCT < - 2:
            for i in range(WTNmFCT,2,-1):
                FlgDwNmFCT[i] = FlgDwNmFCT[i-1]
            FlgDwNmFCT[1] = 2

        else:
            for i in range(WTNmFCT,2,-1):
                FlgDwNmFCT[i] = FlgDwNmFCT[i-1]
            FlgDwNmFCT[1] = 3

    elif NmFCT == 2:
        if MvToutCnCT - SpToutCT < - 2:
            for i in range(WTNmFCT,2,-1):
                FlgDwNmFCT[i] = FlgDwNmFCT[i-1]
            FlgDwNmFCT[1] = 1
        else:
            for i in range(WTNmFCT,2,-1):
                FlgDwNmFCT[i] = FlgDwNmFCT[i-1]
            FlgDwNmFCT[1] = 2

    # 運転台数の決定
    # 1台になる
    if NmFCT >= 2:
        if FlgDwNmFCT == 1:
            NmFCT = 1

    # 2台になる
    if NmFCT == 1:
        if FlgUpNmFCT == 2:
            NmFCT = 2

    elif NmFCT == 3:
        if FlgDwNmFCT == 2:
            NmFCT = 2

    # 3台になる
    if NmFCT <= 2:
        if FlgUpNmFCT == 3:
            NmFCT = 3


    # if NmFCT == 1
    #     if FlgUpNmFCT == 2
    #         NmFCT = 2
    #     end
    # elseif NmFCT == 2
    #     if FlgUpNmFCT == 3
    #         NmFCT = 3
    #     end
    #     if FlgDwNmFCT == 1
    #         NmFCT = 1
    #     end
    # else
    #     if FlgDwNmFCT == 2
    #         NmFCT = 2
    #     end
    # end

    # まずはファン停止(風量10 m3/min)
    if NmFCT == 1:
        NmFCT1 = 0
        NmFCT2 = 0
        NmFCT3 = 0

    # 次にファン3台
    elif NmFCT == 2:
        NmFCT1 = 3
        NmFCT2 = 3
        NmFCT3 = 3

    # 次にファン6台
    else:
        NmFCT1 = 3
        NmFCT2 = 6
        NmFCT3 = 6

    if NmCT == 1:
        NmFCT2 = 0
        NmFCT3 = 0
    elif NmCT == 2:
        NmFCT3 = 0


