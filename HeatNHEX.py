def heat_nhex():
    import HEX
    # 下水熱交換器の熱に関する計算
    # Nomenclature
    # TinCn1NHEX        :下水熱交一次入口温度['C]（冷却水側入口温度）
    # ToutCn1NHEX       :下水熱交一次出口温度['C]（冷却水側出口温度）
    # TinCn2NHEX        :下水熱交二次入口温度['C]（下水側入口温度）
    # ToutCn2NHEX       :下水熱交二次出口温度['C]（下水側出口温度）
    global GCn1NHEX,GCn2NHEX,TinCn1NHEX,TinCn2NHEX,ToutCn1NHEX,ToutCn2NHEX
    global ToutCnTR10,ToutCnTR20,ToutCnTR30,ToutCnTR40,FlgError9
    global TinCn1NHEX0,ToutCn1NHEX0,ToutCn2NHEX0
    global MvToutCn1NHEX,dMvToutCn1NHEX,Tv1ToutCn1NHEX,dTv1ToutCn1NHEX
    global MvToutCn2NHEX,dMvToutCn2NHEX,Tv1ToutCn2NHEX,dTv1ToutCn2NHEX
    global GCDP1,GCDP2,GCDP3,GCDP4
    global MvTinCn1NHEX,dMvTinCn1NHEX
    # 冷却水側入口温度の計算
    if GCn1NHEX > 0:
        TinCn1NHEX = (ToutCnTR10 * GCDP1 + ToutCnTR20 * GCDP2 + ToutCnTR30 * GCDP3 + ToutCnTR40 * GCDP4) / (GCDP1 + GCDP2 + GCDP3 + GCDP4)
    else:
        TinCn1NHEX = TinCn1NHEX0

    # 熱交換器の計算
    [ToutCn1NHEX,ToutCn2NHEX] = HEX.hex(GCn1NHEX,GCn2NHEX,TinCn1NHEX0,TinCn2NHEX,287,ToutCn1NHEX0,ToutCn2NHEX0)

    if GCn1NHEX == 0:
        ToutCn1NHEX = TinCn2NHEX + 1.0
        ToutCn2NHEX = TinCn2NHEX + 1.0


    # 上限設定
    FlgError9 = 0
    if ToutCn1NHEX > 45:
        ToutCn1NHEX = 45
        FlgError9 = 1

    # センサ誤差
    MvTinCn1NHEX = TinCn1NHEX + dMvTinCn1NHEX
    MvToutCn1NHEX = ToutCn1NHEX + dMvToutCn1NHEX
    MvToutCn2NHEX = ToutCn2NHEX + dMvToutCn2NHEX
    Tv1ToutCn1NHEX = MvToutCn1NHEX + dTv1ToutCn1NHEX
    Tv1ToutCn2NHEX = MvToutCn2NHEX + dTv1ToutCn2NHEX

    # 冷却塔に関する温度
    global TinCnCT10,TinCnCT20,TinCnCT30,TinCnCT1,TinCnCT2,TinCnCT3
    global ToutCnCT10,ToutCnCT20,ToutCnCT30,ToutCnCT1,ToutCnCT2,ToutCnCT3
    global ToutCnCT0,ToutCnCT,ToutVlvCT0,ToutVlvCT
    TinCnCT1 = TinCnCT10
    TinCnCT2 = TinCnCT20
    TinCnCT3 = TinCnCT30
    ToutCnCT1 = ToutCnCT10
    ToutCnCT2 = ToutCnCT20
    ToutCnCT3 = ToutCnCT30
    ToutCnCT = ToutCnCT0
    ToutVlvCT = ToutVlvCT0


    # センサ誤差
    global MvTinCnCT1,dMvTinCnCT1,MvTinCnCT2,dMvTinCnCT2,MvTinCnCT3,dMvTinCnCT3
    global MvToutCnCT1,dMvToutCnCT1,MvToutCnCT2,dMvToutCnCT2,MvToutCnCT3,dMvToutCnCT3
    global MvToutCnCT,dMvToutCnCT,MvToutVlvCT,dMvToutVlvCT
    MvTinCnCT1 = TinCnCT1 + dMvTinCnCT1
    MvTinCnCT2 = TinCnCT2 + dMvTinCnCT2
    MvTinCnCT3 = TinCnCT3 + dMvTinCnCT3
    MvToutCnCT1 = ToutCnCT1 + dMvToutCnCT1
    MvToutCnCT2 = ToutCnCT2 + dMvToutCnCT2
    MvToutCnCT3 = ToutCnCT3 + dMvToutCnCT3
    MvToutCnCT = ToutCnCT + dMvToutCnCT
    MvToutVlvCT = ToutVlvCT + dMvToutVlvCT
    global Tv1TinCnCT1,dTv1TinCnCT1,Tv1TinCnCT2,dTv1TinCnCT2,Tv1TinCnCT3,dTv1TinCnCT3
    global Tv1ToutCnCT1,dTv1ToutCnCT1,Tv1ToutCnCT2,dTv1ToutCnCT2,Tv1ToutCnCT3,dTv1ToutCnCT3
    global Tv1ToutCnCT,dTv1ToutCnCT,Tv1ToutVlvCT,dTv1ToutVlvCT
    global Tv1TinCn1NHEX,dTv1TinCn1NHEX
    Tv1TinCnCT1 = MvTinCnCT1 + dTv1TinCnCT1
    Tv1TinCnCT2 = MvTinCnCT2 + dTv1TinCnCT2
    Tv1TinCnCT3 = MvTinCnCT3 + dTv1TinCnCT3
    Tv1ToutCnCT1 = MvToutCnCT1 + dTv1ToutCnCT1
    Tv1ToutCnCT2 = MvToutCnCT2 + dTv1ToutCnCT2
    Tv1ToutCnCT3 = MvToutCnCT3 + dTv1ToutCnCT3
    Tv1ToutCnCT = MvToutCnCT + dTv1ToutCnCT
    Tv1ToutVlvCT = MvToutVlvCT + dTv1ToutVlvCT
    Tv1TinCn1NHEX = MvTinCn1NHEX + dTv1TinCn1NHEX

