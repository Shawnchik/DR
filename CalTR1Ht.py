def cal_tr1_ht(TinHt,GHt,TinCn,GCn):
    global FlgError15,fault1
    # 冷凍機TR1の温水モード時の計算
    # Nomenclature
    # COP           :冷凍機COP[-]
    # Pw            :冷凍機消費電力[kW]
    # TinCn         :温水入口温度['C]
    # ToutCn        :温水出口温度['C]
    # GCb           :温水流量[m3/min]
    # TinCh         :冷水入口温度['C]
    # ToutCh        :冷水出口温度['C]
    # GCh           :冷水流量[m3/min]
    # LF            :冷凍機負荷率[#](0~100)

    # 冷水側の入口温度定格値は15度か？
    # 性能曲線が一本しかない!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # 負荷率の計算
    # 温水出口温度
    ToutHt = 45.0
    LF = (ToutHt - TinHt) * GHt / (10 * 3.07) * 100
    #性能曲線が一本しかないためこの式のみ
    if LF < 100:
        COP = - 0.120275415 + 0.135689130 * LF - 0.000278601 * pow(LF,2) - 0.000007930 * pow(LF,3) + 0.000000039 * pow(LF,4)
    else:
        COP = - 0.120275415 + 0.135689130 * 100 - 0.000278601 * pow(100,2) - 0.000007930 * pow(100,3) + 0.000000039 * pow(100,4)


    #     if fault1 == 1
    #         COP = COP * 0.9
    #     end

        # 冷却水出口温度の計算
    if GCn > 0:
        ToutCn = TinCn - ((ToutHt - TinHt) * GHt - (ToutHt - TinHt) * GHt / COP) / GCn
        FlgError15 = 0
        if ToutCn < 5:
            ToutCn = 5
            FlgError15 = 1

    else:
            ToutCn = TinCn

        # 消費電力の計算
    Pw = (ToutHt - TinHt) * GHt / 60 * 1.0 * pow(10,3) * 4.186 / COP

    return [ToutHt,ToutCn,COP,Pw]