def variable_input():
    import math
    import WetBulbTemperature
    from test import set_var
    from test import get_var
    # 値の入力
    # Nomenclature#####
    # ModeClHt      :運転モード（1:冷房モード、0:冷暖房モード）
    # ffmStep       :fifteen minutes を1分に変えるための変数
    # ModeClHt      :Mode Cooling Heating, 冷暖房モード（1:冷房、0:暖房）
    # GCh2Ld        :二次負荷流量[m3/min]
    # GHt2Ld        :二次負荷流量[m3/min]
    # TinCn2NHEX    :下水入口温度['C]
    # Tair          :外気温度['C]
    # RH            :相対湿度[#]
    # SgNHEXCT      :下水/冷却塔利用切換(下水:1,冷却塔:0)
    # SpToutCnNHEX  :下水熱交換器冷却水出口温度設定値



    global ffmStep
    global ModeClHt,GCh2Ld,GHt2Ld,TinCn2NHEX
    global SpToutCh2CHEX,SpToutHt2HHEX,SpToutChTR1,SpToutChTR2,SpToutChTR3,SpToutChTR4
    global MvGCh2Ld,dMvGCh2Ld,Tv1GCh2Ld,dTv1GCh2Ld
    global MvGHt2Ld,dMvGHt2Ld,Tv1GHt2Ld,dTv1GHt2Ld
    global MvTinCn2NHEX,dMvTinCn2NHEX,Tv1TinCn2NHEX,dTv1TinCn2NHEX
    global OrderTR1,OrderTR2,OrderTR3,OrderTR4
    global Tair,RH,SgNHEXCT,Twb,SpToutCn1NHEX


    CalStep = get_var('CalStep')
    day = get_var('day')
    hour = get_var('hour')
    minute = get_var('minute')
    month = get_var('month')
    year = get_var('year')
    Values = get_var('Values')



    # 元データが15分データであるため、1分データに換算する。
    ffmStep = math.floor(CalStep / 15) + 1

    # 冷温水モード
    ModeClHt = Values.iloc[ffmStep,1] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,1] * int(CalStep,15) / 15
    if ModeClHt < 1:
        ModeClHt = 0


    # 冷水負荷流量
    GCh2Ld = Values.iloc[ffmStep,2] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,2] * int(CalStep,15) / 15

    # 温水負荷流量
    GHt2Ld = Values.iloc[ffmStep,3] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,3] * int(CalStep,15) / 15

    # 下水温度
    TinCn2NHEX = Values.iloc[ffmStep,4] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,4] * int(CalStep,15) / 15

    # 外気温度
    Tair = Values.iloc[ffmStep,5] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,5] * int(CalStep,15) / 15

    # 相対湿度
    RH = Values.iloc[ffmStep,6] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,6] * int(CalStep,15) / 15

    # 冷水熱交換器二次出口設定温度
    SpToutCh2CHEX = Values.iloc[ffmStep,7] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,7] * int(CalStep,15) / 15

    # 温水熱交換器二次出口設定温度
    SpToutHt2HHEX = Values.iloc[ffmStep,8] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,8] * int(CalStep,15) / 15

    # 冷凍機冷水出口設定温度
    SpToutChTR1 = Values.iloc[ffmStep,9] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,9] * int(CalStep,15) / 15
    SpToutChTR2 = SpToutChTR1
    SpToutChTR3 = SpToutChTR1
    SpToutChTR4 = Values.iloc[ffmStep,10] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,10] * int(CalStep,15) / 15

    # 冷凍機運転順位
    OrderTR1 = Values.iloc[ffmStep,11]
    OrderTR2 = Values.iloc[ffmStep,12]
    OrderTR3 = Values.iloc[ffmStep,13]
    OrderTR4 = Values.iloc[ffmStep,14]

    # 下水/冷却塔利用切換
    SgNHEXCT = Values.iloc[ffmStep,15]

    # 下水熱交換器冷却水出口温度設定値
    SpToutCn1NHEX = Values.iloc[ffmStep,16] * (15 - int(CalStep,15)) / 15 + Values.iloc[ffmStep + 1,16] * int(CalStep,15) / 15


    # 外気湿球温度の計算
    [Twb] = WetBulbTemperature.wet_bulb_temperature(Tair,RH)

    # 測定誤差 what's the last three
    MvGCh2Ld = GCh2Ld * (1 + dMvGCh2Ld)
    MvGHt2Ld = GHt2Ld * (1 + dMvGHt2Ld)
    MvTinCn2NHEX = TinCn2NHEX + dMvTinCn2NHEX
    Tv1GCh2Ld = MvGCh2Ld + dTv1GCh2Ld
    Tv1GHt2Ld = MvGHt2Ld + dTv1GHt2Ld
    Tv1TinCn2NHEX = MvTinCn2NHEX + dTv1TinCn2NHEX

    # 日時のデータを作る
    minute += 1
    if minute == 60:
        minute = 0
        hour += 1
        if hour == 24:
            hour = 0

    if hour == 0 and minute == 0:
        day += 1

    if month == 1 or month == 3 or month == 5 or month == 7 \
            or month == 8 or month == 10 or month == 12:
        if day == 32:
            day = 1
            month += 1
            if month == 13:
                month = 1
    #             year = year + 1 ##for文にyearがあるからここで足す必要はない!!

    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day == 31:
            day = 1
            month += 1

    # 2月
    else:
        # うるう年
        if int(year,4) == 0:
            if day == 30:
                day = 1
                month += 1
        # 非うるう年
        else:
            if day == 29:
                day = 1
                month += 1

    # month = 7
    set_var(('ModeClHt', 'GCh2Ld', 'GHt2Ld', 'TinCn2NHEX'),(ModeClHt,GCh2Ld,GHt2Ld,TinCn2NHEX))
    set_var(('SpToutCh2CHEX', 'SpToutHt2HHEX', 'SpToutChTR1', 'SpToutChTR2', 'SpToutChTR3', 'SpToutChTR4'),(SpToutCh2CHEX, SpToutHt2HHEX, SpToutChTR1, SpToutChTR2, SpToutChTR3, SpToutChTR4))
    set_var(('MvGCh2Ld', 'dMvGCh2Ld', 'Tv1GCh2Ld', 'dTv1GCh2Ld'),(MvGCh2Ld, dMvGCh2Ld, Tv1GCh2Ld, dTv1GCh2Ld))
    set_var(('MvGHt2Ld', 'dMvGHt2Ld', 'Tv1GHt2Ld', 'dTv1GHt2Ld'),(MvGHt2Ld, dMvGHt2Ld, Tv1GHt2Ld, dTv1GHt2Ld))
    set_var(('MvTinCn2NHEX', 'dMvTinCn2NHEX', 'Tv1TinCn2NHEX', 'dTv1TinCn2NHEX'),(MvTinCn2NHEX, dMvTinCn2NHEX, Tv1TinCn2NHEX, dTv1TinCn2NHEX))
    set_var(('OrderTR1', 'OrderTR2', 'OrderTR3', 'OrderTR4'),(OrderTR1, OrderTR2, OrderTR3, OrderTR4))
    set_var(('Tair', 'RH', 'Twb', 'SgNHEXCT', 'SpToutCn1NHEX'),(Tair, RH, Twb, SgNHEXCT, SpToutCn1NHEX))
    set_var(('month','day','hour','minute'),(month,day,hour,minute))