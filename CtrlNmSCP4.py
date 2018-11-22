def ctrl_nm_scp4():

    # 冷水一次放熱ポンプSCP4台数制御（流量による制御）
    # Nomenclature
    # WTNmSCP4      :効果待ち時間（Waiting Time）
    # MvGCh2Ld      :二次負荷流量[m3/min]
    # FlgNmSCP4     :台数制御のためのフラグ
    # NmSCP4        :SCP4運転台数
    # SpLFTR4         :TR4運転信号
    global NmSCP4,FlgUpNmSCP4,FlgDwNmSCP4,MvGCh2Ld,Tv1SpLFTR4

    # 効果待ち時間15分
    WTNmSCP4 = 15
    # 流量設定値
    SpGNmSCP4 = MvGCh2Ld - 4.98 * Tv1SpLFTR4

    # 増台時
    if SpGNmSCP4 > 17.622:
        for i in range(WTNmSCP4,2,-1):
            FlgUpNmSCP4[i] = FlgUpNmSCP4[i-1]
        FlgUpNmSCP4[1] = 5

    elif SpGNmSCP4 > 11.748:
        for i in range(WTNmSCP4,2,-1):
            FlgUpNmSCP4[i] = FlgUpNmSCP4[i-1]
        FlgUpNmSCP4[1] = 4

    elif SpGNmSCP4 > 5.874:
        for i in range(WTNmSCP4,2,-1):
            FlgUpNmSCP4[i] = FlgUpNmSCP4[i-1]
        FlgUpNmSCP4[1] = 3

    elif SpGNmSCP4 > 2.937:
        for i in range(WTNmSCP4,2,-1):
            FlgUpNmSCP4[i] = FlgUpNmSCP4[i-1]
        FlgUpNmSCP4[1] = 2

    else:
        for i in range(WTNmSCP4,2,-1):
            FlgUpNmSCP4[i] = FlgUpNmSCP4[i-1]
        FlgUpNmSCP4[1] = 1


    # 減台時（効果待ち時間15分）
    if SpGNmSCP4 < 2.67:
        for i in range(WTNmSCP4,2,-1):
            FlgDwNmSCP4[i] = FlgDwNmSCP4[i - 1]
        FlgDwNmSCP4[1] = 1

    elif SpGNmSCP4 < 5.34:
        for i in range(WTNmSCP4,2,-1):
            FlgDwNmSCP4[i] = FlgDwNmSCP4[i - 1]
        FlgDwNmSCP4[1] = 2

    elif SpGNmSCP4 < 10.68:
        for i in range(WTNmSCP4,2,-1):
            FlgDwNmSCP4[i] = FlgDwNmSCP4[i - 1]
        FlgDwNmSCP4[1] = 3

    elif SpGNmSCP4 < 16.02:
        for i in range(WTNmSCP4,2,-1):
            FlgDwNmSCP4[i] = FlgDwNmSCP4[i - 1]
        FlgDwNmSCP4[1] = 4

    else:
        for i in range(WTNmSCP4,2,-1):
            FlgDwNmSCP4[i] = FlgDwNmSCP4[i - 1]
        FlgDwNmSCP4[1] = 5

    # 運転台数の決定
    # 1台になる
    if NmSCP4 >= 2:
        if FlgDwNmSCP4 == 1:
            NmSCP4 = 1

    # 2台になる
    if NmSCP4 >= 3:
        if FlgDwNmSCP4 == 2:
            NmSCP4 = 2

    elif NmSCP4 == 1:
        if FlgUpNmSCP4 == 2:
            NmSCP4 = 2

    # 3台になる
    if NmSCP4 >= 4:
        if FlgDwNmSCP4 == 3:
            NmSCP4 = 3

    elif NmSCP4 <= 2:
        if FlgUpNmSCP4 == 3:
            NmSCP4 = 3

    # 4台になる
    if NmSCP4 == 5:
        if FlgDwNmSCP4 == 4:
            NmSCP4 = 4

    elif NmSCP4 <= 3:
        if FlgUpNmSCP4 == 4:
            NmSCP4 = 4

    # 5台になる
    if NmSCP4 <= 4:
        if FlgUpNmSCP4 == 5:
            NmSCP4 = 5


    # global CalStep
    # if CalStep > 24 * 60 * 4
    # #    if SpGNmSCP4 < 2.67
    #     MvGCh2Ld
    #     SpGNmSCP4
    #       NmSCP4
    #       FlgDwNmSCP4
    #       FlgUpNmSCP4
    #       pause
    #
    #
    # end

    # if NmSCP4 == 1
    #     if FlgUpNmSCP4 == 2
    #         NmSCP4 = 2
    #     end
    # elseif (NmSCP4 == 1)||(NmSCP4 == 2)
    #     if FlgUpNmSCP4 == 3
    #         NmSCP4 = 3
    #     end
    #     if FlgDwNmSCP4 == 1
    #         NmSCP4 = 1
    #     end
    # elseif (NmSCP4 == 1)||(NmSCP4 == 2)||(NmSCP4 == 3)
    #     if FlgUpNmSCP4 == 4
    #         NmSCP4 = 4
    #     end
    #     if FlgDwNmSCP4 == 2
    #         NmSCP4 = 2
    #     end
    # else
    #     if FlgDwNmSCP4 == 3
    #         NmSCP4 = 3
    #     end
    # end
