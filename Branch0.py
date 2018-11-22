def branch0(g, krpp, krhex, kreq, vlv, cv_max):
    #[dP] =

    # ポンプのない枝(HEXのある枝）について、流量から圧力損失を求めるサブルーチン
    # [圧力損失] = Branch0(流量,配管圧損係数,熱交圧損係数,機器圧損係数,バルブ開度)
    # Nomenclature
    # G         :流量[m3/min]
    # dP        :枝の出入口圧力差[kPa]
    # KrPp      :管の圧損係数[kPa/(m3/min)^2]
    # KrHEX     :熱交の圧損係数[kPa/(m3/min)^2]
    # KrEq      :機器の圧損係数[kPa/(m3/min)^2]
    # GHEX      :熱交の流量[m3/min]
    # Vlv       :バルブ開度(1:全開,0:全閉)


    # 熱交換器は並列で、管路による抵抗の差（管路自体の抵抗も）は無視できるので、各熱交換器に等しく流れるとする
    GHEX = g / 2

    # (枝の圧損) = (管圧損) + (熱交圧損) + (機器圧損) + (バルブ圧損)

    # 弁圧損計算。流量係数の定格値Cv_maxはイオンの温度制御弁とレンジアビリティRはバタフライバルブの20
    # Cv_max = 2846

    # R = 20
    # R = 50
    R = 100
    Cv = cv_max * R^(vlv - 1)
    dPVlv = - 1743 * (g * 1000 / 60)^2 / Cv^2

    dP = - krpp * g^2 - krhex * GHEX^2 - kreq * g^2 + dPVlv

    return [dP]
