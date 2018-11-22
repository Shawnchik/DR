def cal_tr2(TinCh,SpToutCh,GCh,TinCn,GCn):
    import numpy as np
    global fault1
    # 冷凍機TR2の計算
    # Nomenclature
    # ToutCn        :冷却水出口温度['C]
    # COP           :冷凍機COP[-]
    # Pw            :冷凍機消費電力[kW]
    # TinCh         :冷水入口温度['C]
    # ToutCh        :冷水出口温度['C]
    # GCh           :冷水流量[kg/s]
    # TinCn         :冷却水入口温度['C]
    # GCn           :冷却水流量[m3/min]
    # LF            :冷凍機負荷率[#](0~100)

    # 冷水冷却水ともに流量がある場合、冷水入口温度が5度より大きい場合
    if GCh > 0 and GCn > 0 and TinCh > 5:
        # 負荷率、冷水出口温度の計算。負荷率100#を超えたら出口温度が上昇する。
        # →これをすると出口温度が7度以上になり、一気に制御が不安定になる
        # →そのため出口温度5度で固定。負荷率は100#としてCOPを計算する
        ToutCh = SpToutCh
        LF = (TinCh - ToutCh) * GCh / (10 * 4.98) * 100
        if LF > 100:
            LF = 100
    #         ToutCh = TinCh - 10 * 4.98 / GCh
        if LF < 20:
            LF = 20

        # 冷却水出口温度に関する収束計算
        ToutCnmax = 50
        ToutCnmin = TinCn
        ToutCn0 = 50
        ToutCn = 0
        ToutCn00 = np.zeros(10)
        while ToutCn0 - ToutCn > 0.0001 or ToutCn0 - ToutCn < - 0.0001:
            ToutCn0 = (ToutCnmax + ToutCnmin) / 2
            # 冷却水出口温度ベースのCOP算出式。
            if ToutCn0 < 22:      # 18度以下は18度として計算
                COP = 3.3395 * pow(10,-6) * pow(LF,3) - 1.1768 * pow(10,-3) * pow(LF,2) + 1.5448 * pow(10,-1) * LF + 2.6875 * pow(10,-1)
            elif ToutCn0 < 25:
                a = 3.3395 * pow(10,-6) * pow(LF,3) - 1.1768 * pow(10,-3) * pow(LF,2) + 1.5448 * pow(10,-1) * LF + 2.6875 * pow(10,-1)
                b = 3.1780 * pow(10,-6) * pow(LF,3) - 1.0950 * pow(10,-3) * pow(LF,2) + 1.4557 * pow(10,-1) * LF + 3.3369 * pow(10,-1)
                COP = b + (a - b) * (22 - ToutCn0) / 4
            elif ToutCn0 < 28:
                a = 3.1780 * pow(10,-6) * pow(LF,3) - 1.0950 * pow(10,-3) * pow(LF,2) + 1.4557 * pow(10,-1) * LF + 3.3369 * pow(10,-1)
                b = 2.8155 * pow(10,-6) * pow(LF,3) - 9.9088 * pow(10,-4) * pow(LF,2) + 1.3776 * pow(10,-1) * LF + 2.6600 * pow(10,-1)
                COP = b + (a - b) * (25 - ToutCn0) / 3
            elif ToutCn0 < 31:
                a = 2.8155 * pow(10,-6) * pow(LF,3) - 9.9088 * pow(10,-4) * pow(LF,2) + 1.3776 * pow(10,-1) * LF + 2.6600 * pow(10,-1)
                b = 3.6237 * pow(10,-6) * pow(LF,3) - 1.1231 * pow(10,-3) * pow(LF,2) + 1.4416 * pow(10,-1) * LF - 1.1266 * pow(10,-1)
                COP = b + (a - b) * (29 - ToutCn0) / 4
            elif ToutCn0 < 34:
                a = 3.6237 * pow(10,-6) * pow(LF,3) - 1.1231 * pow(10,-3) * pow(LF,2) + 1.4416 * pow(10,-1) * LF - 1.1266 * pow(10,-1)
                b = 3.5806 * pow(10,-6) * pow(LF,3) - 1.1936 * pow(10,-3) * pow(LF,2) + 1.5323 * pow(10,-1) * LF - 6.4749 * pow(10,-1)
                COP = b + (a - b) * (33 - ToutCn0) / 4
            elif ToutCn0 < 37:
                a = 3.5806 * pow(10,-6) * pow(LF,3) - 1.1936 * pow(10,-3) * pow(LF,2) + 1.5323 * pow(10,-1) * LF - 6.4749 * pow(10,-1)
                b = 2.3035 * pow(10,-6) * pow(LF,3) - 1.0792 * pow(10,-3) * pow(LF,2) + 1.5397 * pow(10,-1) * LF - 1.0714
                COP = b + (a - b) * (37 - ToutCn0) / 4
            else:                # 37度以上は37度として計算
                COP = 2.3035 * pow(10,-6) * pow(LF,3) - 1.0792 * pow(10,-3) * pow(LF,2) + 1.5397 * pow(10,-1) * LF - 1.0714

            # 出口温度が7度の時は性能が1.073倍とする
            if SpToutCh == 7:
                COP = COP * 1.073

    #         if fault1 == 1
    #             COP = COP * 0.9
    #         end

            ToutCn = TinCn + ((TinCh - ToutCh) * GCh + (TinCh - ToutCh) * GCh / COP) / GCn

            # 冷却水出口温度は50度を上限とする
            if ToutCn > 40:
                ToutCn = 40

            if ToutCn0 - ToutCn > 0.0001:
                ToutCnmax = ToutCn0
            elif ToutCn0 - ToutCn < - 0.0001:
                ToutCnmin = ToutCn0

            FlgError16 = 0
            # 0.01で収束しない場合
            for i in range(10,2,-1):
                ToutCn00[i] = ToutCn00[i-1]
            ToutCn00[1] = ToutCn0

            if ToutCn00 == ToutCn00[1]:
                FlgError16 = 1
                break

        # 消費電力の計算
        Pw = (TinCh - ToutCh) * GCh / 60 * 1.0 * 10^3 * 4.186 / COP
        if Pw <= 0:
            Pw = 0

    else:
        ToutCh = TinCh
        ToutCn = TinCn
        COP = 0
        Pw = 0
        FlgError16 = 0

    return [ToutCh,ToutCn,COP,Pw,FlgError16]