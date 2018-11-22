def heat_tr():
    import CalTR1
    import CalTR2
    import CalTR3
    import CalTR4
    import CalTR1Ht
    # 冷凍機の熱に関する計算。COPと消費電力もここで計算
    # Nomenclature
    # ToutAHU      :AHU出口温度['C]
    global ModeClHt
    global TinChTR1,TinChTR2,TinChTR3,TinChTR4,ToutChTR10,ToutChTR20,ToutChTR30
    global ToutChTR1,ToutChTR2,ToutChTR3,ToutChTR4,TinChTR10,TinChTR20,TinChTR30,TinChTR40
    global GCh1CHEX,TinCh1CHEX,ToutCh1CHEX0,ToutChAHU0
    global TinCnTR1,TinCnTR2,TinCnTR3,TinCnTR4,ToutCn1NHEX0
    global ToutCnTR1,COPTR1,PwTR1
    global ToutCnTR2,COPTR2,PwTR2
    global ToutCnTR3,COPTR3,PwTR3
    global ToutCnTR4,COPTR4,PwTR4
    global ToutST1230
    global GSCP1,GSCP2,GSCP3,GCP1
    global GCDP1,GCDP2,GCDP3,GCDP4
    global MvTinCnTR1,Tv1TinCnTR1,MvToutCnTR1,Tv1ToutCnTR1,MvTinChTR1,Tv1TinChTR1,MvToutChTR1,Tv1ToutChTR1,MvPwTR1,Tv1PwTR1
    global MvTinCnTR2,Tv1TinCnTR2,MvToutCnTR2,Tv1ToutCnTR2,MvTinChTR2,Tv1TinChTR2,MvToutChTR2,Tv1ToutChTR2,MvPwTR2,Tv1PwTR2
    global MvTinCnTR3,Tv1TinCnTR3,MvToutCnTR3,Tv1ToutCnTR3,MvTinChTR3,Tv1TinChTR3,MvToutChTR3,Tv1ToutChTR3,MvPwTR3,Tv1PwTR3
    global MvTinCnTR4,Tv1TinCnTR4,MvToutCnTR4,Tv1ToutCnTR4,MvTinChTR4,Tv1TinChTR4,MvToutChTR4,Tv1ToutChTR4,MvPwTR4,Tv1PwTR4
    global dMvTinCnTR1,dTv1TinCnTR1,dMvToutCnTR1,dTv1ToutCnTR1,dMvTinChTR1,dTv1TinChTR1,dMvToutChTR1,dTv1ToutChTR1,dMvPwTR1,dTv1PwTR1
    global dMvTinCnTR2,dTv1TinCnTR2,dMvToutCnTR2,dTv1ToutCnTR2,dMvTinChTR2,dTv1TinChTR2,dMvToutChTR2,dTv1ToutChTR2,dMvPwTR2,dTv1PwTR2
    global dMvTinCnTR3,dTv1TinCnTR3,dMvToutCnTR3,dTv1ToutCnTR3,dMvTinChTR3,dTv1TinChTR3,dMvToutChTR3,dTv1ToutChTR3,dMvPwTR3,dTv1PwTR3
    global dMvTinCnTR4,dTv1TinCnTR4,dMvToutCnTR4,dTv1ToutCnTR4,dMvTinChTR4,dTv1TinChTR4,dMvToutChTR4,dTv1ToutChTR4,dMvPwTR4,dTv1PwTR4
    global TinST123
    global TinST12,ToutST120
    global GSHP1,GHt1HHEX,TinHt1HHEX,ToutHtTR10,TinHtTR1,ToutHt1HHEX0,ToutST30,TinST3,TinHtTR10,ToutHtTR
    global SpToutChTR1,SpToutChTR2,SpToutChTR3,SpToutChTR4
    global FlgError16,FlgError17,FlgError18,FlgError19
    global SgNHEXCT,ToutCnCT0
    global TinCnTR10,TinCnTR20,TinCnTR30,TinCnTR40,GCnCT1,GCnCT2,GCnCT3,GVlvCT
    global TinCnCT10,ToutVlvCT,ToutVlvCT0

    # 冷凍機冷水入口温度の計算
    # 冷房モード時
    if ModeClHt == 1:
        # 冷水一次系統で流量が存在する場合に計算する。
        if GCh1CHEX * 2 + GSCP3 + GSCP2 + GSCP1 > 0:
            # 熱交流量がない場合
            if GCh1CHEX * 2 == 0:
                if GSCP3 > 0:
                    TinChTR3 = ToutST1230
                if GSCP2 > 0:
                    TinChTR2 = ToutST1230
                if GSCP1 > 0:
                    TinChTR1 = ToutST1230
                TinST123 = (ToutChTR10 * GSCP1 + ToutChTR20 * GSCP2 + ToutChTR30 * GSCP3) / (GSCP3 + GSCP2 + GSCP1)
            # 冷凍機流量がない場合
            elif GSCP3 + GSCP2 + GSCP1 == 0:
                TinCh1CHEX = ToutST1230
                TinST123 = ToutCh1CHEX0
        # その他
            elif GSCP1 == 0 and GSCP2 > 0 and GSCP3 > 0:
                if GSCP3 + GSCP2 < GCh1CHEX * 2:
                    TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutChTR20 * GSCP2 + ToutST1230 * (GCh1CHEX * 2 - GSCP3 - GSCP2))\
                                 / (GCh1CHEX * 2)
                    TinChTR3 = ToutCh1CHEX0
                    TinChTR2 = ToutCh1CHEX0
                    TinST123 = ToutCh1CHEX0
                else:
                    if GCh1CHEX * 2 < GSCP3:
                        TinCh1CHEX = ToutChTR30
                        TinChTR3 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST1230 * (GSCP3 - GCh1CHEX * 2)) / GSCP3
                        TinChTR2 = ToutST1230
                        TinST123 = (ToutChTR30 * (GSCP3 - GCh1CHEX * 2) + ToutChTR20 * GSCP2)\
                                   / (GSCP3 + GSCP2 - GCh1CHEX * 2)
                    else:
                        TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutChTR20 * (GCh1CHEX * 2 - GSCP3)) / (GCh1CHEX * 2)
                        TinChTR3 = ToutCh1CHEX0
                        TinChTR2 = (ToutCh1CHEX0 * (GCh1CHEX * 2 - GSCP3) + ToutST1230 * (GSCP2 - (GCh1CHEX * 2 - GSCP3))) \
                                   / GSCP2
                        TinST123 = ToutChTR20

            elif GSCP1 > 0 and GSCP2 == 0 and GSCP3 > 0:
                if GSCP3 + GSCP1 < GCh1CHEX * 2:
                    TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutChTR10 * GSCP1 + ToutST1230 * (GCh1CHEX * 2 - GSCP3 - GSCP1)) \
                                 / (GCh1CHEX * 2)
                    TinChTR3 = ToutCh1CHEX0
                    TinChTR1 = ToutCh1CHEX0
                    TinST123 = ToutCh1CHEX0
                else:
                    if GCh1CHEX * 2 < GSCP3:
                        TinCh1CHEX = ToutChTR30
                        TinChTR3 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST1230 * (GSCP3 - GCh1CHEX * 2)) / GSCP3
                        TinChTR1 = ToutST1230
                        TinST123 = (ToutChTR30 * (GSCP3 - GCh1CHEX * 2) + ToutChTR10 * GSCP1) / (GSCP3 + GSCP1 - GCh1CHEX * 2)
                    else:
                        TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutChTR10 * (GCh1CHEX * 2 - GSCP3)) / (GCh1CHEX * 2)
                        TinChTR3 = ToutCh1CHEX0
                        TinChTR1 = (ToutCh1CHEX0 * (GCh1CHEX * 2 - GSCP3) + ToutST1230 * (GSCP1 - (GCh1CHEX * 2 - GSCP3)))\
                                   / GSCP1
                        TinST123 = ToutChTR10

            elif GSCP1 > 0 and GSCP2 > 0 and GSCP3 == 0:
                if GSCP2 + GSCP1 < GCh1CHEX * 2:
                    TinCh1CHEX = (ToutChTR20 * GSCP2 + ToutChTR10 * GSCP1 + ToutST1230 * (GCh1CHEX * 2 - GSCP2 - GSCP1))\
                                 / (GCh1CHEX * 2)
                    TinChTR2 = ToutCh1CHEX0
                    TinChTR1 = ToutCh1CHEX0
                    TinST123 = ToutCh1CHEX0
                else:
                    if GCh1CHEX * 2 < GSCP2:
                        TinCh1CHEX = ToutChTR20
                        TinChTR2 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST1230 * (GSCP2 - GCh1CHEX * 2)) / GSCP2
                        TinChTR1 = ToutST1230
                        TinST123 = (ToutChTR20 * (GSCP2 - GCh1CHEX * 2) + ToutChTR10 * GSCP1) / (GSCP2 + GSCP1 - GCh1CHEX * 2)
                    else:
                        TinCh1CHEX = (ToutChTR20 * GSCP2 + ToutChTR10 * (GCh1CHEX * 2 - GSCP2)) / (GCh1CHEX * 2)
                        TinChTR2 = ToutCh1CHEX0
                        TinChTR1 = (ToutCh1CHEX0 * (GCh1CHEX * 2 - GSCP2) + ToutST1230 * (GSCP1 - (GCh1CHEX * 2 - GSCP2))) / GSCP1
                        TinST123 = ToutChTR10

            elif GSCP1 > 0 and GSCP2 == 0 and GSCP3 == 0:
                if GCh1CHEX * 2 < GSCP1:
                    TinCh1CHEX = ToutChTR10
                    TinChTR1 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST1230 * (GSCP1 - GCh1CHEX * 2)) / GSCP1
                    TinST123 = ToutChTR10
                else:
                    TinCh1CHEX = (ToutChTR10 * GSCP1 + ToutST1230 * (GCh1CHEX * 2 - GSCP1)) / (GCh1CHEX * 2)
                    TinChTR1 = ToutCh1CHEX0
                    TinST123 = ToutCh1CHEX0

            elif GSCP1 == 0 and GSCP2 > 0 and GSCP3 == 0:
                if GCh1CHEX * 2 < GSCP2:
                    TinCh1CHEX = ToutChTR20
                    TinChTR2 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST1230 * (GSCP2 - GCh1CHEX * 2)) / GSCP2
                    TinST123 = ToutChTR20
                else:
                    TinCh1CHEX = (ToutChTR20 * GSCP2 + ToutST1230 * (GCh1CHEX * 2 - GSCP2)) / (GCh1CHEX * 2)
                    TinChTR2 = ToutCh1CHEX0
                    TinST123 = ToutCh1CHEX0

            elif GSCP1 == 0 and GSCP2 == 0 and GSCP3 > 0:
                if GCh1CHEX * 2 < GSCP3:
                    TinCh1CHEX = ToutChTR30
                    TinChTR3 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST1230 * (GSCP3 - GCh1CHEX * 2)) / GSCP3
                    TinST123 = ToutChTR30
                else:
                    TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutST1230 * (GCh1CHEX * 2 - GSCP3)) / (GCh1CHEX * 2)
                    TinChTR3 = ToutCh1CHEX0
                    TinST123 = ToutCh1CHEX0
            # 全ての流量がある場合
            else:
                if GSCP3 + GSCP2 + GSCP1 < GCh1CHEX * 2:
                    TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutChTR20 * GSCP2 + ToutChTR10 * GSCP1 + ToutST1230 * (GCh1CHEX * 2 - GSCP3 - GSCP2 - GSCP1))\
                                 / (GCh1CHEX * 2)
                    TinChTR3 = ToutCh1CHEX0
                    TinChTR2 = ToutCh1CHEX0
                    TinChTR1 = ToutCh1CHEX0
                    TinST123 = ToutCh1CHEX0
                else:
                    if GCh1CHEX * 2 < GSCP3:
                        TinCh1CHEX = ToutChTR30
                        TinChTR3 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST1230 * (GSCP3 - GCh1CHEX * 2)) / GSCP3
                        TinChTR2 = ToutST1230
                        TinChTR1 = ToutST1230
                        TinST123 = (ToutChTR30 * (GSCP3 - GCh1CHEX * 2) + ToutChTR20 * GSCP2 + ToutChTR10 * GSCP1)\
                                   / (GSCP3 + GSCP2 + GSCP1 - GCh1CHEX * 2)
                    elif GCh1CHEX * 2 < GSCP3 + GSCP2:
                        TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutChTR20 * (GCh1CHEX * 2 - GSCP3)) / (GCh1CHEX * 2)
                        TinChTR3 = ToutCh1CHEX0
                        TinChTR2 = (ToutCh1CHEX0 * (GCh1CHEX * 2 - GSCP3) + ToutST1230 * (GSCP2 - (GCh1CHEX * 2 - GSCP3))) / GSCP2
                        TinChTR1 = ToutST1230
                        TinST123 = (ToutChTR20 * (GSCP2 - (GCh1CHEX * 2 - GSCP3)) + ToutChTR10 * GSCP1)\
                                   / (GSCP3 + GSCP2 + GSCP1 - GCh1CHEX * 2)
                    elif GCh1CHEX * 2 < GSCP3 + GSCP2 + GSCP1:
                        TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutChTR20 * GSCP2 + ToutChTR10 * (GCh1CHEX * 2 - GSCP3 - GSCP2)) / (GCh1CHEX * 2)
                        TinChTR3 = ToutCh1CHEX0
                        TinChTR2 = ToutCh1CHEX0
                        TinChTR1 = (ToutCh1CHEX0 * (GCh1CHEX * 2 - GSCP3 - GSCP2) + ToutST1230 * (GSCP1 - (GCh1CHEX * 2 - GSCP3 - GSCP2)))\
                                   / GSCP1
                        TinST123 = ToutChTR10

        # 冷凍機冷却水入口温度の計算
        # 冷却塔非利用時
        if SgNHEXCT == 1:
            if GCDP1 > 0:
                TinCnTR1 = ToutCn1NHEX0
            else:
                TinCnTR1 = TinCnTR10

            if GCDP2 > 0:
                TinCnTR2 = ToutCn1NHEX0
            else:
                TinCnTR2 = TinCnTR20

            if GCDP3 > 0:
                TinCnTR3 = ToutCn1NHEX0
            else:
                TinCnTR3 = TinCnTR30

            if GCDP4 > 0:
                TinCnTR4 = ToutCn1NHEX0
            else:
                TinCnTR4 = TinCnTR40

        # 冷却塔利用時
        else:
            if GCDP1 > 0:
                TinCnTR1 = ToutCn1NHEX0
            else:
                TinCnTR1 = TinCnTR10

            if GCDP2 > 0:
                TinCnTR2 = ToutVlvCT0
            else:
                TinCnTR2 = TinCnTR20

            if GCDP3 > 0:
                TinCnTR3 = ToutVlvCT0
            else:
                TinCnTR3 = TinCnTR30

            if GCDP4 > 0:
                TinCnTR4 = ToutVlvCT0
            else:
                TinCnTR4 = TinCnTR40

        # 冷凍機冷却水出口温度の計算
        [ToutChTR1, ToutCnTR1, COPTR1, PwTR1, FlgError16] = CalTR1.cal_tr1(TinChTR10, SpToutChTR1, GSCP1, TinCnTR1, GCDP1)
        [ToutChTR2, ToutCnTR2, COPTR2, PwTR2, FlgError17] = CalTR2.cal_tr2(TinChTR20, SpToutChTR2, GSCP2, TinCnTR2, GCDP2)
        [ToutChTR3, ToutCnTR3, COPTR3, PwTR3, FlgError18] = CalTR3.cal_tr3(TinChTR30, SpToutChTR3, GSCP3, TinCnTR3, GCDP3)
        [ToutChTR4, ToutCnTR4, COPTR4, PwTR4, FlgError19] = CalTR4.cal_tr4(TinChTR40, SpToutChTR4, GCP1, TinCnTR4, GCDP4)
        TinHtTR1 = 0
        ToutHtTR1 = 0

    # 冷暖房モード時
    else:
        # 冷水温度
        if GCh1CHEX * 2 + GSCP3 + GSCP2 > 0:
            if GSCP2 > 0 and GSCP3 > 0:
                if GSCP3 + GSCP2 < GCh1CHEX * 2:
                    TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutChTR20 * GSCP2 + ToutST120 * (GCh1CHEX * 2 - GSCP3 - GSCP2)) /(GCh1CHEX * 2)
                    TinChTR3 = ToutCh1CHEX0
                    TinChTR2 = ToutCh1CHEX0
                    TinST12 = ToutCh1CHEX0
                else:
                    if GCh1CHEX * 2 < GSCP3:
                        TinCh1CHEX = ToutChTR30
                        TinChTR3 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST120 * (GSCP3 - GCh1CHEX * 2)) / GSCP3
                        TinChTR2 = ToutST120
                        TinST12 = (ToutChTR30 * (GSCP3 - GCh1CHEX * 2) + ToutChTR20 * GSCP2) / (GSCP3 + GSCP2 - GCh1CHEX * 2)
                    else:
                        TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutChTR20 * (GCh1CHEX * 2 - GSCP3)) / (GCh1CHEX * 2)
                        TinChTR3 = ToutCh1CHEX0
                        TinChTR2 = (ToutCh1CHEX0 * (GCh1CHEX * 2 - GSCP3) + ToutST120 * (GSCP2 - (GCh1CHEX * 2 - GSCP3))) / GSCP2
                        TinST12 = ToutChTR20

            elif GSCP2 > 0 and GSCP3 == 0:
                if GCh1CHEX * 2 < GSCP2:
                    TinCh1CHEX = ToutChTR20
                    TinChTR2 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST120 * (GSCP2 - GCh1CHEX * 2)) / GSCP2
                    TinST12 = ToutChTR20
                else:
                    TinCh1CHEX = (ToutChTR20 * GSCP2 + ToutST120 * (GCh1CHEX * 2 - GSCP2)) / (GCh1CHEX * 2)
                    TinChTR2 = ToutCh1CHEX0
                    TinST12 = ToutCh1CHEX0
            elif GSCP2 == 0 and GSCP3 > 0:
                if GCh1CHEX * 2 < GSCP3:
                    TinCh1CHEX = ToutChTR30
                    TinChTR3 = (ToutCh1CHEX0 * GCh1CHEX * 2 + ToutST120 * (GSCP3 - GCh1CHEX * 2)) / GSCP3
                    TinST12 = ToutChTR30
                else:
                    TinCh1CHEX = (ToutChTR30 * GSCP3 + ToutST120 * (GCh1CHEX * 2 - GSCP3)) / (GCh1CHEX * 2)
                    TinChTR3 = ToutCh1CHEX0
                    TinST12 = ToutCh1CHEX0
            else:
                TinCh1CHEX = ToutST120
                TinST12 = ToutCh1CHEX0

        if GCP1 > 0:
            TinChTR4 = ToutChAHU0

        # 温水
        if GHt1HHEX * 2 + GSHP1 > 0:
            if GSHP1 > 0:
                if GHt1HHEX * 2 < GSHP1:
                    TinHt1HHEX = ToutHtTR10
                    TinHtTR1 = (ToutHt1HHEX0 * GHt1HHEX * 2 + ToutST30 * (GSHP1 - GHt1HHEX * 2)) / GSHP1
                    TinST3 = ToutHtTR10
                else:
                    TinHt1HHEX = (ToutHtTR10 * GSHP1 + ToutST30 * (GHt1HHEX * 2 - GSHP1)) / (GHt1HHEX * 2)
                    TinHtTR1 = ToutHt1HHEX0
                    TinST3 = ToutHt1HHEX0
            else:
                TinHt1HHEX = ToutST30
                TinST3 = ToutHt1HHEX0

        # 冷凍機冷却水入口温度の計算
        # 冷却塔非利用時
        if SgNHEXCT == 1:
            if GCDP1 > 0:
                TinCnTR1 = ToutCn1NHEX0
            else:
                TinCnTR1 = TinCnTR10

            if GCDP2 > 0:
                TinCnTR2 = ToutCn1NHEX0
            else:
                TinCnTR2 = TinCnTR20

            if GCDP3 > 0:
                TinCnTR3 = ToutCn1NHEX0
            else:
                TinCnTR3 = TinCnTR30

            if GCDP4 > 0:
                TinCnTR4 = ToutCn1NHEX0
            else:
                TinCnTR4 = TinCnTR40

        # 冷却塔利用時
        else:
            if GCDP1 > 0:
                TinCnTR1 = ToutCn1NHEX0
            else:
                TinCnTR1 = TinCnTR10

            if GCDP2 > 0:
                TinCnTR2 = ToutVlvCT0
            else:
                TinCnTR2 = TinCnTR20

            if GCDP3 > 0:
                TinCnTR3 = ToutVlvCT0
            else:
                TinCnTR3 = TinCnTR30

            if GCDP4 > 0:
                TinCnTR4 = ToutVlvCT0
            else:
                TinCnTR4 = TinCnTR40


        # 冷凍機冷却水出口温度の計算
        [ToutHtTR1, ToutCnTR1, COPTR1, PwTR1] = CalTR1Ht.cal_tr1_ht(TinHtTR10, GSHP1, TinCnTR1, GCDP1)
        [ToutChTR2, ToutCnTR2, COPTR2, PwTR2, FlgError17] = CalTR2.cal_tr2(TinChTR20, SpToutChTR2, GSCP2, TinCnTR2, GCDP2)
        [ToutChTR3, ToutCnTR3, COPTR3, PwTR3, FlgError18] = CalTR3.cal_tr3(TinChTR30, SpToutChTR3, GSCP3, TinCnTR3, GCDP3)
        [ToutChTR4, ToutCnTR4, COPTR4, PwTR4, FlgError19] = CalTR4.cal_tr4(TinChTR40, SpToutChTR4, GCP1, TinCnTR4, GCDP4)

        TinChTR1 = 0
        ToutChTR1 = 0

    global MvTinHtTR1,dMvTinHtTR1,Tv1TinHtTR1,dTv1TinHtTR1,MvToutHtTR1,dMvToutHtTR1,Tv1ToutHtTR1,dTv1ToutHtTR1
    # センサ誤差
    MvTinCnTR1 = TinCnTR1 + dMvTinCnTR1
    MvTinCnTR2 = TinCnTR2 + dMvTinCnTR2
    MvTinCnTR3 = TinCnTR3 + dMvTinCnTR3
    MvTinCnTR4 = TinCnTR4 + dMvTinCnTR4
    Tv1TinCnTR1 = MvTinCnTR1 + dTv1TinCnTR1
    Tv1TinCnTR2 = MvTinCnTR2 + dTv1TinCnTR2
    Tv1TinCnTR3 = MvTinCnTR3 + dTv1TinCnTR3
    Tv1TinCnTR4 = MvTinCnTR4 + dTv1TinCnTR4
    MvToutCnTR1 = ToutCnTR1 + dMvToutCnTR1
    MvToutCnTR2 = ToutCnTR2 + dMvToutCnTR2
    MvToutCnTR3 = ToutCnTR3 + dMvToutCnTR3
    MvToutCnTR4 = ToutCnTR4 + dMvToutCnTR4
    Tv1ToutCnTR1 = MvToutCnTR1 + dTv1ToutCnTR1
    Tv1ToutCnTR2 = MvToutCnTR2 + dTv1ToutCnTR2
    Tv1ToutCnTR3 = MvToutCnTR3 + dTv1ToutCnTR3
    Tv1ToutCnTR4 = MvToutCnTR4 + dTv1ToutCnTR4
    MvTinChTR1 = TinChTR1 + dMvTinChTR1
    MvTinHtTR1 = TinHtTR1 + dMvTinHtTR1
    MvTinChTR2 = TinChTR2 + dMvTinChTR2
    MvTinChTR3 = TinChTR3 + dMvTinChTR3
    MvTinChTR4 = TinChTR4 + dMvTinChTR4
    Tv1TinChTR1 = MvTinChTR1 + dTv1TinChTR1
    Tv1TinHtTR1 = MvTinHtTR1 + dTv1TinHtTR1
    Tv1TinChTR2 = MvTinChTR2 + dTv1TinChTR2
    Tv1TinChTR3 = MvTinChTR3 + dTv1TinChTR3
    Tv1TinChTR4 = MvTinChTR4 + dTv1TinChTR4
    MvToutChTR1 = ToutChTR1 + dMvToutChTR1
    MvToutHtTR1 = ToutHtTR1 + dMvToutHtTR1
    MvToutChTR2 = ToutChTR2 + dMvToutChTR2
    MvToutChTR3 = ToutChTR3 + dMvToutChTR3
    MvToutChTR4 = ToutChTR4 + dMvToutChTR4
    Tv1ToutChTR1 = MvToutChTR1 + dTv1ToutChTR1
    Tv1ToutHtTR1 = MvToutHtTR1 + dTv1ToutHtTR1
    Tv1ToutChTR2 = MvToutChTR2 + dTv1ToutChTR2
    Tv1ToutChTR3 = MvToutChTR3 + dTv1ToutChTR3
    Tv1ToutChTR4 = MvToutChTR4 + dTv1ToutChTR4
    MvPwTR1 = PwTR1 * (1 + dMvPwTR1)
    MvPwTR2 = PwTR2 * (1 + dMvPwTR2)
    MvPwTR3 = PwTR3 * (1 + dMvPwTR3)
    MvPwTR4 = PwTR4 * (1 + dMvPwTR4)
    Tv1PwTR1 = MvPwTR1 + dTv1PwTR1
    Tv1PwTR2 = MvPwTR2 + dTv1PwTR2
    Tv1PwTR3 = MvPwTR3 + dTv1PwTR3
    Tv1PwTR4 = MvPwTR4 + dTv1PwTR4








