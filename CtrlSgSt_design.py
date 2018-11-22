def ctrl_sg_st_design():
    # 蓄放熱運転モード制御
    # Nomenclature
    # SgChSt    :冷水蓄熱信号（1:蓄熱、0:蓄熱終了、2:追掛）
    # SgHtSt    :温水蓄熱信号（1:蓄熱、0:蓄熱終了、2:追掛）
    # Tv1SpQST1 :設定値用通信誤差を含む残蓄熱量[GJ]
    global ModeClHt,month,hour,minute,SgChSt,SgHtSt
    global Tv1QST1,Tv1QST2,Tv1QST3
    global SpLFTR1,SpLFTR2,SpLFTR3,SpLFTR4
    global num_case

    # 冷房運転時
    if ModeClHt == 1:

        SgHtSt = 0

        if num_case == 0:
    #         # ピークカット運転時(6月から9月にON)
    #         if (month >= 6)&&(month <= 9)
            if hour == 13 or hour == 14 or hour == 15:
                SgChSt = 0

            # 通常運転時間帯
            else:
                # 22時00分に蓄熱を開始する
                if hour == 22 and minute == 0:
                    SgChSt = 1

                # 蓄熱終了は、蓄熱槽出口温度は一度蓄熱槽内部の温度分布がくずれたら終わるため、残蓄熱量で行う
                if Tv1QST1 > 100.29 * 0.95 and Tv1QST2 > 80.37 * 0.95 and Tv1QST3 > 90.17 * 0.95:
                    SgChSt = 0

                # 8時00分に蓄熱を終了する
                if hour == 8 and minute == 0:
                    SgChSt = 0

                # 昼間に残蓄熱量が不足したら追掛け運転する
                if 8 <= hour < 22: #hour >=8 and hour < 22:
                    # ピークカット前(ピークカット間の負荷は最大で80GJ程度。そのため1割増しの88GJとした)
                    if hour <= 12:
                        if Tv1QST1 + Tv1QST2 + Tv1QST3 < 88:
                            SgChSt = 2

                    # ピークカット後
                    if hour >= 16:
                        if Tv1QST1 < 100.3 * 0.2 or Tv1QST2 < 80.37 * 0.2 or Tv1QST3 < 90.17 * 0.2:
                            SgChSt = 2


        if num_case == 1:
            # 7時00分に蓄熱を開始する
            if hour == 7 and minute == 0:
                SgChSt = 2

            # 蓄熱終了は、蓄熱槽出口温度は一度蓄熱槽内部の温度分布がくずれたら終わるため、残蓄熱量で行う
            if Tv1QST1 > 100.29 * 0.95 and Tv1QST2 > 80.37 * 0.95 and Tv1QST3 > 90.17 * 0.95:
                SgChSt = 0

            # 24時00分に蓄熱を終了する
            if hour == 24 and minute == 0:
                SgChSt = 0

            # 残蓄熱量が不足したら追掛け運転する
    #         if (hour >=8)&&(hour < 22)
            if Tv1QST1 < 100.3 * 0.2 or Tv1QST2 < 80.37 * 0.2 or Tv1QST3 < 90.17 * 0.2:
                    SgChSt = 2
    #         end



    #     # 非ピークカット運転時
    #     else:
    #         # 22時00分に蓄熱を開始する
    #         if hour == 22 and minute == 0:
    #             SgChSt = 1
    #
    #
    #         # 蓄熱終了は、蓄熱槽出口温度は一度蓄熱槽内部の温度分布がくずれたら終わるため、残蓄熱量で行う
    #         if Tv1QST1 > 100.3 * 0.95 and Tv1QST2 > 80.37 * 0.95 and Tv1QST3 > 90.17 * 0.95:
    #             SgChSt = 0
    #
    #
    #         # 8時00分に蓄熱を終了する
    #         if hour == 8 and minute == 0:
    #             SgChSt = 0
    #
    #
    #         # 昼間に残蓄熱量が不足したら追掛け運転する
    #         if hour >=8 and hour < 22:
    #             if Tv1QST1 < 100.3 * 0.3 or Tv1QST2 < 80.37 * 0.3or Tv1QST3 < 90.17 * 0.3:
    #                 SgChSt = 2


    # 冷暖房運転時
    else:
        # 冷水
        # 22時00分に蓄熱を開始する
        if hour == 22 and minute == 0:
            SgChSt = 1

        # 蓄熱終了は、蓄熱槽出口温度は一度蓄熱槽内部の温度分布がくずれたら終わるため、残蓄熱量で行う
        if Tv1QST1 > 100.3 * 0.95 and Tv1QST2 > 80.37 * 0.95:
            SgChSt = 0

        # 8時00分に蓄熱を終了する
        if hour == 8 and minute == 0:
            SgChSt = 0

        # 昼間に残蓄熱量が不足したら追掛け運転する
        if hour >=8 and hour < 22:
            if Tv1QST1 < 100.3 * 0.3 or Tv1QST2 < 80.37 * 0.3:
                SgChSt = 2

        # 温水
        # 22時00分に蓄熱を開始する
        if hour == 22 and minute == 0:
            SgHtSt = 1

        # 蓄熱終了は、蓄熱槽出口温度は一度蓄熱槽内部の温度分布がくずれたら終わるため、残蓄熱量で行う
        if Tv1QST3 > 90.17 * 0.9:
            SgHtSt = 0

        # 8時00分に蓄熱を終了する
        if hour == 8 and minute == 0:
            SgHtSt = 0

        # 昼間に残蓄熱量が不足したら追掛け運転する
        if hour >= 8 and hour < 22:
            if Tv1QST3 < 90.17 * 0.3:
                SgHtSt = 2
