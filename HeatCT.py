def heat_ct():
    import CT
    import HEX
    # 冷却塔利用時の温度計算
    # ToutCT        :冷却塔冷却水出口平均温度['C]
    # ModeClHt      :運転モード（1:冷房モード、0:冷暖房モード）
    global ToutCnCT1,ToutCnCT2,ToutCnCT3,GCnCT1,GCnCT2,GCnCT3
    global TinCnCT1,TinCnCT2,TinCnCT3,GFCT1,GFCT2,GFCT3
    global Tair,RH,UACT1,UACT2,UACT3
    global GCDP2,GCDP3,GCDP4,ToutCnTR20,ToutCnTR30,ToutCnTR40,ToutCnCT
    global TinCnCT10,TinCnCT20,TinCnCT30,ToutCnCT10,ToutCnCT20,ToutCnCT30
    global GVlvCT,ToutVlvCT,ToutVlvCT0,ToutCnCT0
    global ModeClHt
    # 下水熱交換器まわり
    global GCn1NHEX,TinCn1NHEX,TinCn1NHEX0,ToutCnTR10,ToutCn1NHEX,ToutCn2NHEX
    global GCn2NHEX,TinCn2NHEX,ToutCn1NHEX0,ToutCn2NHEX0,FlgError9
    global GCDP1
    # 冷暖房モード時
    if ModeClHt == 0:

        # 冷却塔まわり
        # 冷却水入口温度の計算
        if GCDP2 + GCDP3 + GCDP4 > 0:
            TinCnCT1 = (ToutCnTR20 * GCDP2 + ToutCnTR30 * GCDP3 + ToutCnTR40 * GCDP4) / (GCDP2 + GCDP3 + GCDP4)
            TinCnCT2 = TinCnCT1
            TinCnCT3 = TinCnCT1
        else:
            TinCnCT1 = TinCnCT10
            TinCnCT2 = TinCnCT20
            TinCnCT3 = TinCnCT30

        # CT1
        if GCnCT1 > 0:
            [ToutCnCT1] = CT.ct(GCnCT1,TinCnCT10,GFCT1,Tair,RH,UACT1)
        else:
            ToutCnCT1 = ToutCnCT10
        # CT2
        if GCnCT2 > 0:
            [ToutCnCT2] = CT.ct(GCnCT2,TinCnCT20,GFCT2,Tair,RH,UACT2)
        else:
            ToutCnCT2 = ToutCnCT20
        # CT3
        if GCnCT3 > 0:
            [ToutCnCT3] = CT.ct(GCnCT3,TinCnCT30,GFCT3,Tair,RH,UACT3)
        else:
            ToutCnCT3 = ToutCnCT30

        if GCnCT1 + GCnCT2 + GCnCT3 > 0:
            ToutCnCT = (ToutCnCT10 * GCnCT1 + ToutCnCT20 * GCnCT2 + ToutCnCT30 * GCnCT3) / (GCnCT1 + GCnCT2 + GCnCT3)

        # 出口温度
        if GCnCT1 + GCnCT2 + GCnCT3 + GVlvCT > 0:
            ToutVlvCT = (ToutCnCT10 * GCnCT1 + ToutCnCT20 * GCnCT2 + ToutCnCT30 * GCnCT3 + TinCnCT10 * GVlvCT) / (GCnCT1 + GCnCT2 + GCnCT3 + GVlvCT)
        else:
            ToutVlvCT = ToutVlvCT0

        # 冷却水入口温度の計算
        if GCn1NHEX > 0:
            TinCn1NHEX = ToutCnTR10
        else:
            TinCn1NHEX = TinCn1NHEX0

        # 熱交換器の計算
        [ToutCn1NHEX,ToutCn2NHEX] = HEX.hex(GCn1NHEX,GCn2NHEX,TinCn1NHEX0,TinCn2NHEX,635.18,ToutCn1NHEX0,ToutCn2NHEX0)


        # 上限設定
        FlgError9 = 0
        if ToutCn1NHEX > 45:
            ToutCn1NHEX = 45
            FlgError9 = 1

    # 冷房モード時
    else:

        # 冷却塔まわり
        # 冷却水入口温度の計算
        if GCDP1 + GCDP2 + GCDP3 + GCDP4 > 0:
            TinCnCT1 = (ToutCnTR10 * GCDP1 + ToutCnTR20 * GCDP2 + ToutCnTR30 * GCDP3 + ToutCnTR40 * GCDP4) / (GCDP1 + GCDP2 + GCDP3 + GCDP4)
            TinCnCT2 = TinCnCT1
            TinCnCT3 = TinCnCT1
        else:
            TinCnCT1 = TinCnCT10
            TinCnCT2 = TinCnCT20
            TinCnCT3 = TinCnCT30

        # CT1
        if GCnCT1 > 0:
            [ToutCnCT1] = CT.ct(GCnCT1,TinCnCT10,GFCT1,Tair,RH,UACT1)
        else:
            ToutCnCT1 = ToutCnCT10
        # CT2
        if GCnCT2 > 0:
            [ToutCnCT2] = CT.ct(GCnCT2,TinCnCT20,GFCT2,Tair,RH,UACT2)
        else:
            ToutCnCT2 = ToutCnCT20
        # CT3
        if GCnCT3 > 0:
            [ToutCnCT3] = CT.ct(GCnCT3,TinCnCT30,GFCT3,Tair,RH,UACT3)
        else:
            ToutCnCT3 = ToutCnCT30

        if GCnCT1 + GCnCT2 + GCnCT3 > 0:
            ToutCnCT = (ToutCnCT10 * GCnCT1 + ToutCnCT20 * GCnCT2 + ToutCnCT30 * GCnCT3) / (GCnCT1 + GCnCT2 + GCnCT3)

        # 出口温度
        if GCnCT1 + GCnCT2 + GCnCT3 + GVlvCT > 0:
            ToutVlvCT = (ToutCnCT10 * GCnCT1 + ToutCnCT20 * GCnCT2 + ToutCnCT30 * GCnCT3 + TinCnCT10 * GVlvCT) / (GCnCT1 + GCnCT2 + GCnCT3 + GVlvCT)
        else:
            ToutVlvCT = ToutVlvCT0


    # センサ誤差
    global MvTinCnCT1,dMvTinCnCT1,MvTinCnCT2,dMvTinCnCT2,MvTinCnCT3,dMvTinCnCT3
    global MvToutCnCT1,dMvToutCnCT1,MvToutCnCT2,dMvToutCnCT2,MvToutCnCT3,dMvToutCnCT3
    global MvToutCnCT,dMvToutCnCT,MvToutVlvCT,dMvToutVlvCT
    global MvTinCn1NHEX,dMvTinCn1NHEX,MvToutCn1NHEX,dMvToutCn1NHEX,MvToutCn2NHEX,dMvToutCn2NHEX
    MvTinCnCT1 = TinCnCT1 + dMvTinCnCT1
    MvTinCnCT2 = TinCnCT2 + dMvTinCnCT2
    MvTinCnCT3 = TinCnCT3 + dMvTinCnCT3
    MvToutCnCT1 = ToutCnCT1 + dMvToutCnCT1
    MvToutCnCT2 = ToutCnCT2 + dMvToutCnCT2
    MvToutCnCT3 = ToutCnCT3 + dMvToutCnCT3
    MvToutCnCT = ToutCnCT + dMvToutCnCT
    MvToutVlvCT = ToutVlvCT + dMvToutVlvCT
    MvTinCn1NHEX = TinCn1NHEX + dMvTinCn1NHEX
    MvToutCn1NHEX = ToutCn1NHEX + dMvToutCn1NHEX
    MvToutCn2NHEX = ToutCn2NHEX + dMvToutCn2NHEX
    global Tv1TinCnCT1,dTv1TinCnCT1,Tv1TinCnCT2,dTv1TinCnCT2,Tv1TinCnCT3,dTv1TinCnCT3
    global Tv1ToutCnCT1,dTv1ToutCnCT1,Tv1ToutCnCT2,dTv1ToutCnCT2,Tv1ToutCnCT3,dTv1ToutCnCT3
    global Tv1ToutCnCT,dTv1ToutCnCT,Tv1ToutVlvCT,dTv1ToutVlvCT
    global Tv1TinCn1NHEX,dTv1TinCn1NHEX,Tv1ToutCn1NHEX,dTv1ToutCn1NHEX,Tv1ToutCn2NHEX,dTv1ToutCn2NHEX
    Tv1TinCnCT1 = MvTinCnCT1 + dTv1TinCnCT1
    Tv1TinCnCT2 = MvTinCnCT2 + dTv1TinCnCT2
    Tv1TinCnCT3 = MvTinCnCT3 + dTv1TinCnCT3
    Tv1ToutCnCT1 = MvToutCnCT1 + dTv1ToutCnCT1
    Tv1ToutCnCT2 = MvToutCnCT2 + dTv1ToutCnCT2
    Tv1ToutCnCT3 = MvToutCnCT3 + dTv1ToutCnCT3
    Tv1ToutCnCT = MvToutCnCT + dTv1ToutCnCT
    Tv1ToutVlvCT = MvToutVlvCT + dTv1ToutVlvCT
    Tv1TinCn1NHEX = MvTinCn1NHEX + dTv1TinCn1NHEX
    Tv1ToutCn1NHEX = MvToutCn1NHEX + dTv1ToutCn1NHEX
    Tv1ToutCn2NHEX = MvToutCn2NHEX + dTv1ToutCn2NHEX






