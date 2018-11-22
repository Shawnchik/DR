def ctrl_nm_hp():
    # 温水2次ポンプ台数制御（流量による制御）
    # Nomenclature
    # WTNmHP1       :効果待ち時間[min]
    global NmHP1,FlgUpNmHP1,FlgDwNmHP1,MvGHt2Ld

    # 増台時（効果待ち時間15分）
    WTNmHP1 = 15
    if MvGHt2Ld > 11.748:
        for i in range(WTNmHP1,2,-1):
            FlgUpNmHP1[i] = FlgUpNmHP1[i-1]
        FlgUpNmHP1[1] = 4

    elif MvGHt2Ld > 5.874:
        for i in range(WTNmHP1,2,-1):
            FlgUpNmHP1[i] = FlgUpNmHP1[i-1]
        FlgUpNmHP1[1] = 3

    elif MvGHt2Ld > 2.937:
        for i in range(WTNmHP1,2,-1):
            FlgUpNmHP1[i] = FlgUpNmHP1[i-1]
        FlgUpNmHP1[1] = 2

    else:
        for i in range(WTNmHP1,2,-1):
            FlgUpNmHP1[i] = FlgUpNmHP1[i-1]
        FlgUpNmHP1[1] = 1

    # 減台時（効果待ち時間15分）
    if MvGHt2Ld < 2.67:
        for i in range(WTNmHP1,2,-1):
            FlgUpNmHP1[i] = FlgUpNmHP1[i-1]
        FlgDwNmHP1[1] = 1

    elif MvGHt2Ld < 5.34:
        for i in range(WTNmHP1,2,-1):
            FlgUpNmHP1[i] = FlgUpNmHP1[i-1]
        FlgDwNmHP1[1] = 2

    elif MvGHt2Ld < 10.68:
        for i in range(WTNmHP1,2,-1):
            FlgUpNmHP1[i] = FlgUpNmHP1[i-1]
        FlgDwNmHP1[1] = 3

    else:
        for i in range(WTNmHP1,2,-1):
            FlgUpNmHP1[i] = FlgUpNmHP1[i-1]
        FlgDwNmHP1[1] = 4

    # 運転台数の決定
    # 1台になる
    if NmHP1 >= 2:
        if FlgDwNmHP1 == 1:
            NmHP1 = 1

    # 2台になる
    if NmHP1 == 1:
        if FlgUpNmHP1 == 2:
            NmHP1 = 2

    elif NmHP1 >= 3:
        if FlgDwNmHP1 == 2:
            NmHP1 = 2

    # 3台になる
    if NmHP1 <= 2:
        if FlgUpNmHP1 == 3:
            NmHP1 = 3

    elif NmHP1 == 4:
        if FlgDwNmHP1 == 3:
            NmHP1 = 3

    # 4台になる
    if NmHP1 <= 3:
        if FlgUpNmHP1 == 4:
            NmHP1 = 4

    # if NmHP1 == 1
    #     if FlgUpNmHP1 == 2
    #         NmHP1 = 2
    #     end
    # elseif NmHP1 == 2
    #     if FlgUpNmHP1 == 3
    #         NmHP1 = 3
    #     end
    #     if FlgDwNmHP1 == 1
    #         NmHP1 = 1
    #     end
    # elseif NmHP1 == 3
    #     if FlgUpNmHP1 == 4
    #         NmHP1 = 4
    #     end
    #     if FlgDwNmHP1 == 2
    #         NmHP1 = 2
    #     end
    # else
    #     if FlgDwNmHP1 == 3
    #         NmHP1 = 3
    #     end
    # end
