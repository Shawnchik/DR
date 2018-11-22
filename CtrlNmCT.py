def ctrl_nm_ct():
    # 冷却塔台数制御
    # 冷却水流量に応じて台数制御
    # Nomenclature
    # WTNmCT        :効果待ち時間（Waiting Time）
    # GCn           :冷却水流量[m3/min]
    # FlgNmCT       :台数制御のためのフラグ
    # NmCT          :CT運転台数
    global NmCT,FlgUpNmCT,FlgDwNmCT,MvGCDP2,MvGCDP3,MvGCDP4,Tv1VlvCT,MvGVlvCT

    # 運転開始時
    if NmCT == 0:
        NmCT = 1

    MvGCT = MvGCDP2 + MvGCDP3 + MvGCDP4 - MvGVlvCT
    # 効果待ち時間15分
    WTNmCT = 5

    # 増台時
    if MvGCT > 4.522 * 0.6 + 9.044 * 0.6:
        for i in range(WTNmCT,2,-1):
            FlgUpNmCT[i] = FlgUpNmCT[i-1]
        FlgUpNmCT[1] = 3

    elif MvGCT > 4.522 * 0.6:
        for i in range(WTNmCT,2,-1):
            FlgUpNmCT[i] = FlgUpNmCT[i-1]
        FlgUpNmCT[1] = 2

    else:
        for i in range(WTNmCT,2,-1):
            FlgUpNmCT[i] = FlgUpNmCT[i-1]
        FlgUpNmCT[1] = 1

    # 減台時（効果待ち時間15分）
    if MvGCT < 4.522 * 0.5:
        for i in range(WTNmCT,2,-1):
            FlgDwNmCT[i] = FlgDwNmCT[i-1]
        FlgDwNmCT[1] = 1

    elif MvGCT < 4.522 * 0.5 + 9.044 * 0.5:
        for i in range(WTNmCT,2,-1):
            FlgDwNmCT[i] = FlgDwNmCT[i-1]
        FlgDwNmCT[1] = 2

    else:
        for i in range(WTNmCT,2,-1):
            FlgDwNmCT[i] = FlgDwNmCT[i-1]
        FlgDwNmCT[1] = 3

    # 運転台数の決定
    # 1台になる
    if NmCT >= 2:
        if FlgDwNmCT == 1:
            NmCT = 1

    # 2台になる
    if NmCT == 1:
        if FlgUpNmCT == 2:
            NmCT = 2

    elif NmCT == 3:
        if FlgDwNmCT == 2:
            NmCT = 2

    # 3台になる
    if NmCT <= 2:
        if FlgUpNmCT == 3:
            NmCT = 3

    #
    #
    # if NmCT == 1
    #     if FlgUpNmCT == 2
    #         NmCT = 2
    #     elseif FlgUpNmCT == 3
    #         NmCT = 3
    #     end
    # elseif NmCT == 2
    #     if FlgUpNmCT == 3
    #         NmCT = 3
    #     end
    #     if FlgDwNmCT == 1
    #         NmCT = 1
    #     end
    # else
    #     if FlgDwNmCT == 2
    #         NmCT = 2
    #     end
    #     if FlgDwNmCT == 1
    #         NmCT = 1
    #     end
    # end

    # if Tv1VlvCT > 0
    #     NmCT = 1
    # end



