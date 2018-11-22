def ctrl_nm_shp2():
    # 温水一次放熱ポンプSHP2台数制御（流量による制御）
    # WTNmSHP2      :効果待ち時間（Waiting Time）
    # MvGHt2Ld      :二次負荷流量[m3/min]
    # FlgNmSHP2     :台数制御のためのフラグ
    # NmSHP2        :SHP2運転台数
    global NmSHP2,FlgUpNmSHP2,FlgDwNmSHP2,MvGHt2Ld

    # 増台時（効果待ち時間15分）
    WTNmSHP2 = 15
    if MvGHt2Ld > 17.622:
        for i in range(WTNmSHP2,2,-1):
            FlgUpNmSHP2[i] = FlgUpNmSHP2[i-1]
        FlgUpNmSHP2[1] = 5

    elif MvGHt2Ld > 11.748:
        for i in range(WTNmSHP2,2,-1):
            FlgUpNmSHP2[i] = FlgUpNmSHP2[i-1]
        FlgUpNmSHP2[1] = 4

    elif MvGHt2Ld > 5.874:
        for i in range(WTNmSHP2,2,-1):
            FlgUpNmSHP2[i] = FlgUpNmSHP2[i-1]
        FlgUpNmSHP2[1] = 3

    elif MvGHt2Ld > 2.937:
        for i in range(WTNmSHP2,2,-1):
            FlgUpNmSHP2[i] = FlgUpNmSHP2[i-1]
        FlgUpNmSHP2[1] = 2

    else:
        for i in range(WTNmSHP2,2,-1):
            FlgUpNmSHP2[i] = FlgUpNmSHP2[i-1]
        FlgUpNmSHP2[1] = 1

    # 減台時（効果待ち時間300秒）
    if MvGHt2Ld < 2.67:
        for i in range(WTNmSHP2,2,-1):
            FlgDwNmSHP2[i] = FlgDwNmSHP2[i-1]
        FlgDwNmSHP2[1] = 1

    elif MvGHt2Ld < 5.34:
        for i in range(WTNmSHP2,2,-1):
            FlgDwNmSHP2[i] = FlgDwNmSHP2[i-1]
        FlgDwNmSHP2[1] = 2

    elif MvGHt2Ld < 10.68:
        for i in range(WTNmSHP2,2,-1):
            FlgDwNmSHP2[i] = FlgDwNmSHP2[i-1]
        FlgDwNmSHP2[1] = 3

    elif MvGHt2Ld < 16.02:
        for i in range(WTNmSHP2,2,-1):
            FlgDwNmSHP2[i] = FlgDwNmSHP2[i-1]
        FlgDwNmSHP2[1] = 4
    else:
        for i in range(WTNmSHP2,2,-1):
            FlgDwNmSHP2[i] = FlgDwNmSHP2[i-1]
        FlgDwNmSHP2[1] = 5

    # 運転台数の決定
    # 1台になる
    if NmSHP2 >= 2:
        if FlgDwNmSHP2 == 1:
            NmSHP2 = 1

    # 2台になる
    if NmSHP2 >= 3:
        if FlgDwNmSHP2 == 2:
            NmSHP2 = 2

    elif NmSHP2 == 1:
        if FlgUpNmSHP2 == 2:
            NmSHP2 = 2

    # 3台になる
    if NmSHP2 >= 4:
        if FlgDwNmSHP2 == 3:
            NmSHP2 = 3

    elif NmSHP2 <= 2:
        if FlgUpNmSHP2 == 3:
            NmSHP2 = 3

    # 4台になる
    if NmSHP2 == 5:
        if FlgDwNmSHP2 == 4:
            NmSHP2 = 4

    elif NmSHP2 <= 3:
        if FlgUpNmSHP2 == 4:
            NmSHP2 = 4

    # 5台になる
    if NmSHP2 <= 4:
        if FlgUpNmSHP2 == 5:
            NmSHP2 = 5

    #
    # if NmSHP2 == 1
    #     if FlgUpNmSHP2 == 2
    #         NmSHP2 = 2
    #     end
    # elseif NmSHP2 == 2
    #     if FlgUpNmSHP2 == 3
    #         NmSHP2 = 3
    #     end
    #     if FlgDwNmSHP2 == 1
    #         NmSHP2 = 1
    #     end
    # elseif NmSHP2 == 3
    #     if FlgUpNmSHP2 == 4
    #         NmSHP2 = 4
    #     end
    #     if FlgDwNmSHP2 == 2
    #         NmSHP2 = 2
    #     end
    # else
    #     if FlgDwNmSHP2 == 3
    #         NmSHP2 = 3
    #     end
    # end
