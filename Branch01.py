def branch01(dP,KrPp,KrHEX,KrEq,Vlv,Cv_max,R):
    import numpy as np
    # ポンプのない枝(HEXが二つ）について、圧力損失から流量を求めるサブルーチン
    # [流量] = Branch0(圧力損失,配管圧損係数,熱交圧損係数,機器圧損係数,バルブ開度)
    # Nomenclature
    # G         :流量[m3/min]
    # GHEX      :熱交換器流量[m3/min]
    # dP        :枝の出入口圧力差[kPa]
    # KrPp      :管の圧損係数[kPa/(m3/min)^2]
    # KrHEX     :熱交の圧損係数[kPa/(m3/min)^2]
    # KrEq      :機器の圧損係数[kPa/(m3/min)^2]
    # GHEX      :熱交の流量[m3/min]
    # Vlv       :バルブ開度(1:全開,0:全閉)
    # dP0       :二分法用仮定の圧力差
    global FlgError4

    G100 = np.zeros(10)

    # 出入口圧力差がない、またはバルブがほぼ閉じている場合は流量0とする
    if dP > 0 or Vlv == 0:
        G = 0
        GHEX = 0
        FlgError4 = 0
    else:
        # whileに入るための初期値,二分法初期値
        Gmax = 30
        Gmin = 0
        dP0 = 10
        cnt = 0
        while dP - dP0 > 0.001 or dP - dP0 < - 0.001:

            cnt = cnt + 1

            G = (Gmax + Gmin) / 2
            GHEX = G / 2

            # (枝の圧損) = (管圧損) + (熱交圧損) + (機器圧損) + (バルブ圧損)

            # 弁圧損計算。レンジアビリティRはバタフライバルブの20
    #         R = 20
            Cv = Cv_max * R^(Vlv - 1)
            dPVlv = - 1743 * (G * 1000 / 60)^2 / Cv^2

            dP0 = - KrPp * G^2 - KrHEX * GHEX^2 - KrEq * G^2 + dPVlv

            if dP - dP0 > 0:
                Gmax = G
            else:
                Gmin = G

            # 0.001で収束しない場合
            for i in range(10,2,-1):
                G100[i] = G100[i-1]
            G100[1] = G
            FlgError4 = 0

            if G100 == G100[1]:
                FlgError4 = dP - dP0
                break

            if G > 29.9:
                FlgError4 = 1
                break

            if cnt > 30:
                FlgError4 = 1
                break

    return [G,GHEX]
