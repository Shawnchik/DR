def ct(Gw,Twin,Ga,Tda,rh,UA):
    import Enthalpy
    import WetBulbTemperature
    import numpy as np
    import math
    # 冷却塔モデル
    # Nomenclature
    # cpw       :冷却水の比熱 [J/kg'C]
    # cpe       :交換空気の平均比熱 [J/kg'C]
    # cp        :湿り空気（外気）の比熱 [J/kg'C]
    # hin       :入口空気比エンタルピー [J/kg]
    # hout      :出口空気比エンタルピー [J/kg]
    # Twbin     :入口空気湿球温度 ['C]
    # Twbout    :出口空気湿球温度 ['C]
    # rh        :相対湿度 [#]
    # Gw        :冷却水流量[kg/s]
    # Ga        :風量[kg/s]
    # NmF       :ファン台数

    # 単位換算([m3/min] -> [kg/s])
    Gw = Gw * 10^3 / 60
    Ga = Ga * 1.293 / 60

    cpw = 4184
    cp = 1100

    # 乾球温度と湿球温度から外気比エンタルピーを求める
    [hin,_] = Enthalpy.enthalpy(Tda,rh)

    [Twbin] = WetBulbTemperature.wet_bulb_temperature(Tda,rh)

    # 湿球温度の飽和空気の比エンタルピーを求める

    # # 空気出口湿球温度の最大値は、冷却水入口温度である。
    # Twboutmax = Twin
    # #空気出口湿球温度の最小値は、空気入口湿球温度である。（冷却水が外気よりも高温という仮定）
    # Twboutmin = Twbin
    # おそらくここを以下2行のようにしないと発散する!?
    Twboutmax = max(Twin,Twbin)
    Twboutmin = min(Twin,Twbin)

    # 収束計算に入るための適当な初期値設定
    Twbout0 = 1
    Twbout = 0
    Twbout00 = np.zeros(10)
    while Twbout0 - Twbout < - 0.01 or Twbout0 - Twbout > 0.01:

        # 空気出口湿球温度の仮定
        Twbout0 = (Twboutmax + Twboutmin) / 2

        # 出口空気は飽和空気という仮定で、出口空気の比エンタルピーを求める。
        [hout,_] = Enthalpy.enthalpy(Twbout0,100)

        # 空気平均比熱cpeの計算
        dh = hout - hin
        dTwb = Twbout0 - Twbin
        cpe = dh / dTwb

        UAe = UA * cpe / cp

        Cw = Gw * cpw
        Ca = Ga * cpe

        Cmin = min(Cw,Ca)
        Cmax = max(Cw,Ca)

        NTU = UAe / Cmin

        eps = (1 - math.exp(-NTU * (1 - Cmin / Cmax))) / (1 - Cmin / Cmax * math.exp(-NTU * (1 - Cmin / Cmax)))

        Q = eps * Cmin * (Twin - Twbin)

        Twbout = Twbin + Q / Ca

        if Twbout < Twbout0:
            Twboutmax = Twbout0
        else:
            Twboutmin = Twbout0


        FlgError = 0
        # 収束しない場合
        for i in range(10,2,-1):
            Twbout00[i] = Twbout00[i-1]
        Twbout00[1] = Twbout0

        if Twbout00 == Twbout00[1]:
            FlgError = 1
            break

    Twout = Twin - Q / Cw
    return [Twout]
