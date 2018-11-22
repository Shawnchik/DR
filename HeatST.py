def heat_st():
    import StorageTank
    # 蓄熱槽の温度と残蓄熱量の計算
    # TST       :蓄熱槽内層温度['C]
    # TfST      :1時刻前の蓄熱槽内層温度['C]
    # QST       :残蓄熱量[GJ]
    global ModeClHt
    global ToutST1,QST1,TST1,TfST1,GST1,TinST1,TinST10
    global ToutST2,QST2,TST2,TfST2,GST2,TinST2,TinST20
    global ToutST3,QST3,TST3,TfST3,GST3,TinST3,TinST30
    global ToutST123,ToutST1230,ToutST10,ToutST20,ToutST30
    global MvQST1,Tv1QST1,dTv1QST1,MvQST2,Tv1QST2,dTv1QST2,MvQST3,Tv1QST3,dTv1QST3
    global TinST1230
    global TinST12,ToutST12,ToutST120
    global SpToutChTR1
    # 蓄熱槽入口温度計算
    # 冷房モード時
    if ModeClHt == 1:

        TinST1 = TinST1230
        TinST2 = TinST1230
        TinST3 = TinST1230

    # 冷暖房モード時
    else:
        # 冷水
        TinST1 = TinST12
        TinST2 = TinST12

        # 温水
        # HeatTRでTinST3は計算済み

    # 蓄熱槽出口温度
    # 冷房モード時
    if ModeClHt == 1:
        if abs(GST1) + abs(GST2) + abs(GST3) > 0:
            ToutST123 = (ToutST1 * abs(GST1) + ToutST2 * abs(GST2) + ToutST3 * abs(GST3)) / (abs(GST1) + abs(GST2) + abs(GST3))

    # 冷暖房モード時
    else:
        # 冷水
        if abs(GST1) + abs(GST2) > 0:
            ToutST12 = (ToutST1 * abs(GST1) + ToutST2 * abs(GST2)) / (abs(GST1) + abs(GST2))

        # 温水
        # 下で計算している


    # 蓄熱槽内温度、残蓄熱量計算
    # 冷房モード時
    if ModeClHt == 1:
        # ST1
        if GST1 > 0:
            [ToutST1,QST1,TST1,TfST1] = StorageTank.storage_tank(1,-1,GST1,TinST10,TfST1,399.3,SpToutChTR1)
        else:
            [ToutST1,QST1,TST1,TfST1] = StorageTank.storage_tank(1,1,-1 * GST1,TinST10,TfST1,399.3,SpToutChTR1)
        # ST2
        if GST2 > 0:
            [ToutST2,QST2,TST2,TfST2] = StorageTank.storage_tank(1,-1,GST2,TinST20,TfST2,320,SpToutChTR1)
        else:
            [ToutST2,QST2,TST2,TfST2] = StorageTank.storage_tank(1,1,-1 * GST2,TinST20,TfST2,320,SpToutChTR1)
        # ST3(冷温水切替可)
        if GST3 > 0:
            [ToutST3,QST3,TST3,TfST3] = StorageTank.storage_tank(1,-1,GST3,TinST30,TfST3,359,SpToutChTR1)
        else:
            [ToutST3,QST3,TST3,TfST3] = StorageTank.storage_tank(1,1,-1 * GST3,TinST30,TfST3,359,SpToutChTR1)


    # 冷暖房モード時
    else:
        # ST1
        if GST1 > 0:
            [ToutST1,QST1,TST1,TfST1] = StorageTank.storage_tank(1,-1,GST1,TinST10,TfST1,399.3,SpToutChTR1)
        else:
            [ToutST1,QST1,TST1,TfST1] = StorageTank.storage_tank(1,1,-1 * GST1,TinST10,TfST1,399.3,SpToutChTR1)
        # ST2
        if GST2 > 0:
            [ToutST2,QST2,TST2,TfST2] = StorageTank.storage_tank(1,-1,GST2,TinST20,TfST2,320,SpToutChTR1)
        else:
            [ToutST2,QST2,TST2,TfST2] = StorageTank.storage_tank(1,1,-1 * GST2,TinST20,TfST2,320,SpToutChTR1)
        # ST3(温水モード)
        if GST3 > 0:
            [ToutST3,QST3,TST3,TfST3] = StorageTank.storage_tank(-1,-1,GST3,TinST30,TfST3,359,45)
        else:
            [ToutST3,QST3,TST3,TfST3] = StorageTank.storage_tank(-1,1,-1 * GST3,TinST30,TfST3,359,45)

    # MvQST1
    global MvTST103,MvTST109,MvTST115,MvTST121,MvTST127,MvTST133,MvTST139,MvTST145,MvTST151,MvTST157
    global dMvTST103,dMvTST109,dMvTST115,dMvTST121,dMvTST127,dMvTST133,dMvTST139,dMvTST145,dMvTST151,dMvTST157

    MvTST103 = TST1(3) + dMvTST103
    MvTST109 = TST1(9) + dMvTST109
    MvTST115 = TST1(15) + dMvTST115
    MvTST121 = TST1(21) + dMvTST121
    MvTST127 = TST1(27) + dMvTST127
    MvTST133 = TST1(33) + dMvTST133
    MvTST139 = TST1(39) + dMvTST139
    MvTST145 = TST1(45) + dMvTST145
    MvTST151 = TST1(51) + dMvTST151
    MvTST157 = TST1(57) + dMvTST157
    MvQST1 = 0
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST103) * 399.3 * 0.6 * 4.186 / 10^3
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST109) * 399.3 * 0.6 * 4.186 / 10^3
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST115) * 399.3 * 0.6 * 4.186 / 10^3
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST121) * 399.3 * 0.6 * 4.186 / 10^3
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST127) * 399.3 * 0.6 * 4.186 / 10^3
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST133) * 399.3 * 0.6 * 4.186 / 10^3
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST139) * 399.3 * 0.6 * 4.186 / 10^3
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST145) * 399.3 * 0.6 * 4.186 / 10^3
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST151) * 399.3 * 0.6 * 4.186 / 10^3
    MvQST1 = MvQST1 + (SpToutChTR1 + 10 - MvTST157) * 399.3 * 0.6 * 4.186 / 10^3
    # MvQST2
    global MvTST203,MvTST209,MvTST215,MvTST221,MvTST227,MvTST233,MvTST239,MvTST245,MvTST251,MvTST257
    global dMvTST203,dMvTST209,dMvTST215,dMvTST221,dMvTST227,dMvTST233,dMvTST239,dMvTST245,dMvTST251,dMvTST257
    MvTST203 = TST2(3) + dMvTST203
    MvTST209 = TST2(9) + dMvTST209
    MvTST215 = TST2(15) + dMvTST215
    MvTST221 = TST2(21) + dMvTST221
    MvTST227 = TST2(27) + dMvTST227
    MvTST233 = TST2(33) + dMvTST233
    MvTST239 = TST2(39) + dMvTST239
    MvTST245 = TST2(45) + dMvTST245
    MvTST251 = TST2(51) + dMvTST251
    MvTST257 = TST2(57) + dMvTST257
    MvQST2 = 0
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST203) * 320 * 0.6 * 4.186 / 10^3
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST209) * 320 * 0.6 * 4.186 / 10^3
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST215) * 320 * 0.6 * 4.186 / 10^3
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST221) * 320 * 0.6 * 4.186 / 10^3
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST227) * 320 * 0.6 * 4.186 / 10^3
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST233) * 320 * 0.6 * 4.186 / 10^3
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST239) * 320 * 0.6 * 4.186 / 10^3
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST245) * 320 * 0.6 * 4.186 / 10^3
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST251) * 320 * 0.6 * 4.186 / 10^3
    MvQST2 = MvQST2 + (SpToutChTR1 + 10 - MvTST257) * 320 * 0.6 * 4.186 / 10^3
    # MvQST3
    global MvTST303,MvTST309,MvTST315,MvTST321,MvTST327,MvTST333,MvTST339,MvTST345,MvTST351,MvTST357
    global dMvTST303,dMvTST309,dMvTST315,dMvTST321,dMvTST327,dMvTST333,dMvTST339,dMvTST345,dMvTST351,dMvTST357
    MvTST303 = TST3(3) + dMvTST303
    MvTST309 = TST3(9) + dMvTST309
    MvTST315 = TST3(15) + dMvTST315
    MvTST321 = TST3(21) + dMvTST321
    MvTST327 = TST3(27) + dMvTST327
    MvTST333 = TST3(33) + dMvTST333
    MvTST339 = TST3(39) + dMvTST339
    MvTST345 = TST3(45) + dMvTST345
    MvTST351 = TST3(51) + dMvTST351
    MvTST357 = TST3(57) + dMvTST357
    # 冷房モード時
    if ModeClHt == 1:
        MvQST3 = 0
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST303) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST309) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST315) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST321) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST327) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST333) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST339) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST345) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST351) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (SpToutChTR1 + 10 - MvTST357) * 359 * 0.6 * 4.186 / 10^3
    # 冷暖房モード時
    else:
        MvQST3 = 0
        MvQST3 = MvQST3 + (MvTST303 - 35.0) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (MvTST309 - 35.0) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (MvTST315 - 35.0) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (MvTST321 - 35.0) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (MvTST327 - 35.0) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (MvTST333 - 35.0) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (MvTST339 - 35.0) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (MvTST345 - 35.0) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (MvTST351 - 35.0) * 359 * 0.6 * 4.186 / 10^3
        MvQST3 = MvQST3 + (MvTST357 - 35.0) * 359 * 0.6 * 4.186 / 10^3


    # 測定誤差
    Tv1QST1 = MvQST1 + dTv1QST1
    Tv1QST2 = MvQST2 + dTv1QST2
    Tv1QST3 = MvQST3 + dTv1QST3




