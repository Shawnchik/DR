def branch11(dP,NmPmp,INV,VlvPmp,Cv_max,c0,c1,c2,c3,c4,KrPp,KrHEX):
    import numpy as np
    # ポンプを複数並列に有し、熱交換器を二つ並列に有する枝において、出入口圧力差、ポンプINV・バイパス弁弁開度から流量を計算する。
    # [熱交一台当たり流量,ポンプ流量,ポンプバイパス弁流量,ポンプ吐出圧] =
    # Branch11(出入口圧力差,ポンプ運転台数,ポンプINV,ポンプバイパス弁開度,ポンプ係数0次,ポンプ係数1次,ポンプ係数2次,ポンプ係数3次,ポンプ係数4次,配管抵抗係数,熱交換器抵抗係数)
    # 圧力は、圧力損失が負、ポンプによる加圧が正とする。
    # 流量は、ポンプの向きを正とする。
    # Nomenclature #####
    # dP            :枝の出入口圧力差[kPa]
    # dPHEX        :熱交換器前後の圧力差(=熱交換器バイパス弁前後の圧力差)[kPa]
    # dPPmp        :二次ポンプ前後の圧力差(=二次ポンプバイパス弁前後の圧力差)[kPa]
    # dPPp          :配管圧力損失
    # dPVlvHEX      :熱交換器バイパス弁圧力損失
    # dPVlvPmp      :ポンプバイパス弁圧力損失
    # maxG,minG     :流量の最大値、最小値(0.0)[m3/min]
    # NmPmp           :ポンプ運転台数
    # INV           :INVの回転数(0~1)
    # c0~c4         :ポンプ性能曲線の係数
    # c0n           :そのINV時の最大圧力（性能曲線の圧力切片）
    # KrHEX         :熱交換器圧損係数[kPa/(m3/min)^2]
    # KrPp          :配管圧損係数[kPa/(m3/min)^2]
    # G             :総流量[m3/min]
    # GPmp          :ポンプ一台あたりの流量[m3/min]
    # GHEX          :熱交換器流量[m3/min],一台あたりの流量。
    # Ph            :ポンプによる圧力[kPa]
    # Phn           :定格（INV=0)時換算の圧力
    # VlvPmp        :ポンプバイパス弁開度(0~1,0が全閉)[-]
    # VlvHEX        :熱交換器バイパス弁開度(0~1)[-]

    GHEX = 0
    GPmp = 0
    GVlvPmp = 0
    dPPmp = 0
    G00 = np.zeros(10)

    # dPが小さいとき、流量はなしとする!!!!!!!!!!!!!この条件が曲者！！
    if dP > 0:
        GHEX = 0
        GPmp = 0
        GVlvPmp = 0
        dPPmp = 0
    # dPが0kPa以上あるとき(圧力損失が負になっていないとき、つまりdPが正になっていないとき)
    else:
    #     c0n = c0 * INV^2
    #     #そのINVの値の時の最大圧力が要求圧力よりも大きい時（解が存在する時）。小さい場合は流量を流さない
    #     if c0n + dP >= 0

            # whileに入るための初期値,二分法初期値
            dPHEX = 10
            dPPp = 0
            dPPmp = 0
            Gmax = 80
            Gmin = 0
            cnt = 0
            dP0 = 100000
            while dP + dPPp + dPHEX + dPPmp > 0.001 or dP + dPPp + dPHEX + dPPmp < 0:

                cnt = cnt + 1

                # 流量の仮定
                G = (Gmax + Gmin) / 2
                GHEX = G / 2
    #             # 流量が小さくなったら、それで計算を終了させる!!!!!
    #             if G < 0.0001
    #                 GHEX = 0
    #                 GPmp = 0
    #                 GVlvPmp = 0
    #                 dPPmp = 0
    #                 break
    #             end
                # 配管の圧損[kPa]
                dPPp = - KrPp * G^2

                # 熱交換器前後
                dPHEX = - KrHEX * GHEX^2

                # 仮定したGでのポンプ揚程
                dPPmp = (c0 + c1 *  (G / NmPmp / INV) + c2 *  \
                         (G / NmPmp / INV)^2 + c3 *  (G / NmPmp / INV)^3 + c4 *  (G / NmPmp / INV)^4) * INV^2

                # 仮定したGで解が存在しない場合
                if dPPmp + dP + dPPp + dPHEX <= 0:
                    Gmax = G

                # 仮定したGで解が存在しうる場合
                else:
                    # ポンプ前後
                    # ポンプ前後について、熱交換器前後で仮定した総流量を用い、ポンプとポンプバイパス弁における流量を求め、ポンプ前後における圧力変化を求める。
                    # ポンプバイパス弁が閉じているとき
                    if VlvPmp < 0.001:
                        GVlvPmp = 0
                        GPmp = G / NmPmp
                        dPPmp = (c0 + c1 * (GPmp / INV) + c2 * (GPmp / INV)^2 + c3 * (GPmp / INV)^3 + c4 * (GPmp / INV)^4) * INV^2

                    # ポンプバイパス弁が開いているとき
                    else:
                        # whileに入るための初期値,二分法初期値
                        GPmp = 10
                        dPPmp = 10
                        dPVlvPmp = 0
                        GPmpmax = 30
                        GPmpmin = G / NmPmp
                        cnt1 = 0
                        while dPPmp + dPVlvPmp > 0.001 or dPPmp + dPVlvPmp < - 0.001:

                            cnt1 = cnt1 + 1

                            GPmp = (GPmpmax + GPmpmin) / 2

                            dPPmp = (c0 + c1 * (GPmp / INV) + c2 * (GPmp / INV)^2 + c3 * (GPmp / INV)^3 + c4 * (GPmp / INV)^4) * INV^2

                            GVlvPmp = NmPmp * GPmp - G

                            # 弁圧損計算。%%%%%%レンジアビリティRはバタフライバルブの20
                            R = 100
                            Cv = Cv_max * R^(VlvPmp - 1)
                            dPVlvPmp = - 1743 * (GVlvPmp * 1000 / 60)^2 / Cv^2

                            if dPPmp + dPVlvPmp > 0:
                                GPmpmin = GPmp
                            elif dPPmp + dPVlvPmp < 0:
                                GPmpmax = GPmp

                            # バルブに流れない場合
                            if GVlvPmp < 0.001:
                                break

                            if GPmpmax < GPmpmin + 0.001:
                                break

                            if cnt1 > 25:
                                break

                if dP + dPPp + dPHEX + dPPmp > 0:
                    Gmin = G
                elif dP + dPPp + dPHEX + dPPmp < 0:
                    Gmax = G

                # 0.1で収束しない場合
                for i in range(10,2,-1):
                    G00[i] = G00[i-1]
                G00[1] = G
                if G00 == G00[1]:
    #                 if (dP + dPPp + dPHEX + dPPmp < 5) && (dP + dPPp + dPHEX + dPPmp > - 5)
    #                     break
    #                 end
    #                     dP + dPPp + dPHEX + dPPmp
    #                     pause
                        break

                dP1 = dP + dPPp + dPHEX + dPPmp
                if abs(dP1 - dP0) < 0.001:
                    break
                dP0 = dP1

                if Gmax < Gmin + 0.001:
                    break

                if cnt > 25:
                    break

    #     #そのINVの値の時の最大圧力が要求圧力よりも小さい場合は水は流れない
    #     else
    #          GHEX = 0
    #          GPmp = 0
    #          GVlvPmp = 0
    #          dPPmp = 0
    #     end
    return [GHEX,GPmp,GVlvPmp,dPPmp]