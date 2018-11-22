def enthalpy(Tda,rh):
    import math
    # 乾球温度Tdaと相対湿度rhから比エンタルピーhを求める
    # h     :enthalpy [J/kg]
    # Tda   :Temperature of dry air ['C]
    # rh    :relative humidity [#]
    # cpd   :乾き空気の定圧比熱 [J / kg(DA)'C]
    # gamma :飽和水蒸気の蒸発潜熱 [J/kg]
    # cpv   :水蒸気の定圧比熱 [J / kg(DA)'C]
    # x     :絶対湿度 [kg/kg(DA)]

    cpd = 1007
    gamma = 2499 * pow(10,3)
    cpv = 1845

    # 飽和水蒸気圧Ps[mmHg]の計算
    c = 373.16 / (273.16 + Tda)
    b = c - 1
    a = -7.90298 * b + 5.02808 * math.log10(c) - 1.3816 * pow(10,-7) * (pow(10,(11.344 * b / c)) - 1) + 8.1328 * pow(10,-3) * (pow(10,(-3.49149 * b)) - 1)
    Ps = 760 * pow(10,a)

    x = 0.622 * (rh * Ps) / 100 / (760 - rh * Ps / 100)

    h = cpd * Tda + (gamma + cpv * Tda) * x
    return [h,x]

