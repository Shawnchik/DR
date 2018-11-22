def branch10(dp, inv, vlv_pp,cv_pp_max, vlv_tr, cv_tr_max, c0, c1, c2, c3, c4, kr_pp, kr_tr):
    import numpy as np
    # ポンプを一つ有する枝において、出入口圧力差とポンプINVから流量を求める計算
    # [総流量,冷凍機流量,冷凍機バイパス弁流量] =
    # Branch10(圧力差,ポンプINV,二方弁開度,バイパス弁開度,ポンプ係数0次,ポンプ係数1次,ポンプ係数2次,ポンプ係数3次,ポンプ係数4次,配管抵抗係数,冷凍機抵抗係数,流量最大値,流量最小値)
    # 圧力は、圧力損失が負、ポンプによる加圧が正とする。
    # 流量は、ポンプの向きを正とする。
    # Nomenclature #####
    # dP            :枝の出入口圧力差[kPa]
    # maxG,minG     :流量の最大値、最小値(0.0)[m3/min]
    # INV           :ポンプINV(0~1)
    # VlvPp         :配管用二方弁(1:全開,0:全閉)
    # VlvTR         :冷凍機用バイパス弁(1:全開,0:全閉)
    # c0~c4         :ポンプ性能曲線の係数
    # c0n           :そのINV時の最大圧力（性能曲線の圧力切片）
    # KrPp          :配管圧損係数[kPa/(m3/min)^2]
    # KrTR          :冷凍機圧損係数[kPa/(m3/min)^2]
    # G             :総流量[m3/min]
    # GTR           :冷凍機流量[m3/min]
    # GVlvTR        :冷凍機バイパス弁流量[m3/min]
    # dPPmp         :ポンプによる圧力[kPa]
    # dPPp          :配管による圧力損失[kPa]
    # dPVlv         :配管用二方弁による圧力損失[kPa]
    # dPVlvTR       :冷凍機バイパス弁による圧力損失[kPa]
    # V             :流速[m/s]

    g00 = np.zeros(10)

    # INVが0、dP>0、または二方弁が全閉の場合は流量0とする（計算しない）
    if inv == 0 or dp > 0 or vlv_pp == 0:
        g = 0.0
        gtr = 0.0
        g_vlv_tr = 0
        dp_pmp = 0
    else:
    #     c0n = c0 * INV^2
    #     #����INV�̒l�̎��̍ő刳�͂��v�����͂����傫�����i�������݂��鎞�j�B�������ꍇ�͗��ʂ𗬂��Ȃ�
    #     if c0n + dP >= 0

            # while�ɓ��邽�߂̏����l,�񕪖@�����l
        dp_vlv = 0
        dp_pmp = 1000
        dp_pp = 0
        dp_tr = 0
        gmin = 0
        gmax = 30
        gtr = 0
        g_vlv_tr = 0
        cnt = 0
        while dp_vlv + dp_pmp + dp_pp + dp_tr + dp > 0.0001 or dp_vlv + dp_pmp + dp_pp + dp_tr + dp < 0:
        # 二個目の条件が小なり0なのは、59行目の条件と合わせるため。
            cnt = cnt + 1

            g = (gmin + gmax) / 2
            gtr = g

            if g < 0.1:
               break

            dp_pp = - kr_pp * g^2

            # 弁圧損計算。レンジアビリティRはバタフライバルブの20
            R = 20
            cv = cv_pp_max * R^(vlv_pp - 1)
            dp_vlv = - 1743 * (g * 1000 / 60)^2 / cv^2
            dp_pmp = (c0 + c1 *  (g / inv) + c2 *  (g / inv)^2 + \
                      c3 *  (g / inv)^3 + c4 *  (g / inv)^4) * inv^2

            # 仮定したGで解が存在しない場合
            if dp_pmp + dp + dp_pp + dp_vlv <= 0:
                gmax = g

            # 仮定したGで解が存在しうる場合
            else:
                # 冷凍機バイパス弁が閉じている場合
                if vlv_tr < 0.02:
                    g_vlv_tr = 0
                    gtr = g
                    dp_tr = - kr_tr * gtr^2
                    dp_pmp = (c0 + c1 *  (gtr / inv) + c2 *  (gtr / inv)^2 + c3 *  (gtr / inv)^3 + c4 *  (gtr / inv)^4) * inv^2

                # 冷凍機バイパス弁が開いている場合
                else:
                    # whileに入るための初期値
                    gtr_min = g
                    gtr_max = 30
                    dp_tr = 0
                    dp_vlv_tr = 0
                    while dp_pmp + dp_tr + dp_vlv_tr > 1 or dp_pmp + dp_tr + dp_vlv_tr < - 1:
                        gtr = (gtr_min + gtr_max) / 2
                        g_vlv_tr = gtr - g
                        dp_pmp = (c0 + c1 * (gtr / inv) + c2 *  (gtr / inv)^2 + c3 *  (gtr / inv)^3 + c4 *  (gtr / inv)^4) * inv^2
                        dp_tr =  - kr_tr * gtr^2

                        # 弁圧損計算。流量係数の定格値Cv_maxは病院のHEXバイパス弁とレンジアビリティRはバタフライバルブの20
                        R = 20
                        cv = cv_tr_max * R^(vlv_tr - 1)
                        dp_vlv_tr = - 1743 * (g_vlv_tr * 1000 / 60)^2 / cv^2

                        if dp_pmp + dp_tr + dp_vlv_tr > 0:
                            gtr_min = gtr
                        elif dp_pmp + dp_tr + dp_vlv_tr < 0:
                            gtr_max = gtr

                         # バルブに流れない場合
                        if g_vlv_tr < 0.0001:
                            break

            if dp_vlv + dp_pmp + dp_pp + dp_tr + dp > 0:
                gmin = g
            elif dp_vlv + dp_pmp + dp_pp + dp_tr + dp < 0:
                gmax = g

            # 0.1で収束しない場合
            for i in range(10,2,-1):
                g00[i] = g00[i-1]

            g00[1] = g
            if g00 == g00[1]:
                break
            if cnt > 30:
                break



    #     #そのINVの値の時の最大圧力が要求圧力よりも小さい場合は水は流れない
    #     else
    #          G = 0
    #          GTR = 0.0
    #          GVlvTR = 0
    #          dPPmp = 0
    #     end
    return [g, gtr, g_vlv_tr, dp_pmp]