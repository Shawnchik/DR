def ctrl_nm_np():
    # 下水ポンプ台数制御（INVによる制御）
    # Nomenclature
    # NmNP      :下水ポンプ運転台数
    global NmNP,FlgUpNmNP,FlgDwNmNP,CvINVNP


    # 効果待ち時間15分
    WTNmNP = 15

    # 増台時
    if NmNP == 1:
        if CvINVNP > 0.9:
            for i in range(WTNmNP,2,-1):
                FlgUpNmNP[i] = FlgUpNmNP[i-1]
            FlgUpNmNP[1] = 2

        else:
            for i in range(WTNmNP,2,-1):
                FlgUpNmNP[i] = FlgUpNmNP[i-1]
            FlgUpNmNP[1] = 1

    elif NmNP == 2:
        if CvINVNP > 0.9:
            for i in range(WTNmNP,2,-1):
                FlgUpNmNP[i] = FlgUpNmNP[i-1]
            FlgUpNmNP[1] = 3
        else:
            for i in range(WTNmNP,2,-1):
                FlgUpNmNP[i] = FlgUpNmNP[i-1]
            FlgUpNmNP[1] = 1

    elif NmNP == 3:
        if CvINVNP > 0.9:
            for i in range(WTNmNP,2,-1):
                FlgUpNmNP[i] = FlgUpNmNP[i-1]
            FlgUpNmNP[1] = 4

        else:
            for i in range(WTNmNP,2,-1):
                FlgUpNmNP[i] = FlgUpNmNP[i-1]
            FlgUpNmNP[1] = 2

    else:
        if CvINVNP > 0.9:
            for i in range(WTNmNP,2,-1):
                FlgUpNmNP[i] = FlgUpNmNP[i-1]
            FlgUpNmNP[1] = 4
        else:
            for i in range(WTNmNP,2,-1):
                FlgUpNmNP[i] = FlgUpNmNP[i-1]
            FlgUpNmNP[1] = 3

    # 減台時（効果待ち時間5分）
    if NmNP == 4:
        if CvINVNP < 0.7:
            for i in range(WTNmNP, 2, -1):
                FlgDwNmNP[i] = FlgDwNmNP[i-1]
            FlgDwNmNP[1] = 3

        else:
            for i in range(WTNmNP, 2, -1):
                FlgDwNmNP[i] = FlgDwNmNP[i-1]
            FlgDwNmNP[1] = 4

    elif NmNP == 3:
        if CvINVNP < 0.7:
            for i in range(WTNmNP, 2, -1):
                FlgDwNmNP[i] = FlgDwNmNP[i-1]
            FlgDwNmNP[1] = 2
        else:
            for i in range(WTNmNP, 2, -1):
                FlgDwNmNP[i] = FlgDwNmNP[i-1]
            FlgDwNmNP[1] = 4

    elif NmNP == 2:
        if CvINVNP < 0.5:
            for i in range(WTNmNP, 2, -1):
                FlgDwNmNP[i] = FlgDwNmNP[i-1]
            FlgDwNmNP[1] = 1
        else:
            for i in range(WTNmNP, 2, -1):
                FlgDwNmNP[i] = FlgDwNmNP[i-1]
            FlgDwNmNP[1] = 3

    else:
        if CvINVNP < 0.5:
            for i in range(WTNmNP, 2, -1):
                FlgDwNmNP[i] = FlgDwNmNP[i-1]
            FlgDwNmNP[1] = 1

        else:
            for i in range(WTNmNP, 2, -1):
                FlgDwNmNP[i] = FlgDwNmNP[i-1]
            FlgDwNmNP[1] = 2

    # 運転台数の決定
    # 1台になる
    if NmNP >= 2:
        if FlgDwNmNP == 1:
            NmNP = 1

    # 2台になる
    if NmNP <= 1:
        if FlgUpNmNP == 2:
            NmNP = 2

    elif NmNP >= 3:
        if FlgDwNmNP == 2:
            NmNP = 2

    # 3台になる
    if NmNP <= 2:
        if FlgUpNmNP == 3:
            NmNP = 3

    elif NmNP == 4:
        if FlgDwNmNP == 3:
            NmNP = 3

    # 4台になる
    if NmNP <= 3:
        if FlgUpNmNP == 4:
            NmNP = 4


    if CvINVNP == 0:
        NmNP = 0

    if NmNP == 0 and CvINVNP > 0:
        NmNP = 1



    # if NmNP == 1
    #     if FlgUpNmNP == 2
    #         NmNP = 2
    #     end
    # elseif NmNP == 2
    #     if FlgUpNmNP == 3
    #         NmNP = 3
    #     end
    #     if FlgDwNmNP == 1
    #         NmNP = 1
    #     end
    # elseif NmNP == 3
    #     if FlgUpNmNP == 4
    #         NmNP = 4
    #     end
    #     if FlgDwNmNP == 2
    #         NmNP = 2
    #     end
    # else
    #     if FlgDwNmNP == 3
    #         NmNP = 3
    #     end
    # end
