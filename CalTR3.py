def cal_tr3(TinCh,SpToutCh,GCh,TinCn,GCn):
    import numpy as np
    global fault1
    # 冷凍機TR3の計算
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
        LF = (TinCh - ToutCh) * GCh / (10 * 2.47) * 100
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
            if ToutCn0 < 18:      # 18度以下は18度として計算
                COP = -4.4189 * pow(10,-8) * pow(LF,4) + 4.4225 * pow(10,-5) * pow(LF,3) - 9.5489 * pow(10,-3) * pow(LF,2) + 7.0278 * pow(10,-1) * LF - 2.9572
            elif ToutCn0 < 22:
                a = -4.4189 * pow(10,-8) * pow(LF,4) + 4.4225 * pow(10,-5) * pow(LF,3) - 9.5489 * pow(10,-3) * pow(LF,2) + 7.0278 * pow(10,-1) * LF - 2.9572
                b = -7.9437 * pow(10,-9) * pow(LF,4) + 1.4869 * pow(10,-5) * pow(LF,3) - 4.1783 * pow(10,-3) * pow(LF,2) + 3.7857 * pow(10,-1) * LF - 5.4983 * pow(10,-1)
                COP = b + (a - b) * (22 - ToutCn0) / 4
            elif ToutCn0 < 25:
                a = -7.9437 * pow(10,-9) * pow(LF,4) + 1.4869 * pow(10,-5) * pow(LF,3) - 4.1783 * pow(10,-3) * pow(LF,2) + 3.7857 * pow(10,-1) * LF - 5.4983 * pow(10,-1)
                b = 3.7958 * pow(10,-8) * pow(LF,4) + 1.9750 * pow(10,-6) * pow(LF,3) - 2.6172 * pow(10,-3) * pow(LF,2) + 3.0181 * pow(10,-1) * LF - 1.1491
                COP = b + (a - b) * (25 - ToutCn0) / 3
            elif ToutCn0 < 29:
                a = 3.7958 * pow(10,-8) * pow(LF,4) + 1.9750 * pow(10,-6) * pow(LF,3) - 2.6172 * pow(10,-3) * pow(LF,2) + 3.0181 * pow(10,-1) * LF - 1.1491
                b = 1.0699 * pow(10,-7) * pow(LF,4) - 2.0016 * pow(10,-5) * pow(LF,3) - 2.1684 * pow(10,-5) * pow(LF,2) + 1.7437 * pow(10,-1) * LF - 6.7618 * pow(10,-1)
                COP = b + (a - b) * (29 - ToutCn0) / 4
            elif ToutCn0 < 33:
                a = 1.0699 * pow(10,-7) * pow(LF,4) - 2.0016 * pow(10,-5) * pow(LF,3) - 2.1684 * pow(10,-5) * pow(LF,2) + 1.7437 * pow(10,-1) * LF - 6.7618 * pow(10,-1)
                b = 1.0188 * pow(10,-7) * pow(LF,4) - 2.2828 * pow(10,-5) * pow(LF,3) + 8.4220 * pow(10,-4) * pow(LF,2) + 1.0732 * pow(10,-1) * LF - 1.9916 * pow(10,-1)
                COP = b + (a - b) * (33 - ToutCn0) / 4
            elif ToutCn0 < 37:
                a = 1.0188 * pow(10,-7) * pow(LF,4) - 2.2828 * pow(10,-5) * pow(LF,3) + 8.4220 * pow(10,-4) * pow(LF,2) + 1.0732 * pow(10,-1) * LF - 1.9916 * pow(10,-1)
                b = 1.0141 * pow(10,-7) * pow(LF,4) - 2.4745 * pow(10,-5) * pow(LF,3) + 1.3768 * pow(10,-3) * pow(LF,2) + 6.3139 * pow(10,-2) * LF - 3.3371 * pow(10,-2)
                COP = b + (a - b) * (37 - ToutCn0) / 4
            else:                # 37度以上は37度として計算
                COP = 1.0141 * pow(10,-7) * pow(LF,4) - 2.4745 * pow(10,-5) * pow(LF,3) + 1.3768 * pow(10,-3) * pow(LF,2) + 6.3139 * pow(10,-2) * LF - 3.3371 * pow(10,-2)

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
        # if Pw > 0:
        #
        # else:
        #     Pw = 0
    else:
        ToutCh = TinCh
        ToutCn = TinCn
        COP = 0
        Pw = 0
        FlgError16 = 0

    return [ToutCh,ToutCn,COP,Pw,FlgError16]