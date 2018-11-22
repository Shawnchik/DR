def heat_chex():
    import HEX
    # 一次二次冷水熱交換器の熱に関する計算
    # Nomenclature
    # TinCh2CHEX        :冷水熱交二次入口温度['C]
    global TinCh2CHEX0,TinCh1CHEX0
    global GCh2CHEX,GCh1CHEX,ToutCh2CHEX,ToutCh1CHEX,ToutCh2CHEX0,ToutCh1CHEX0,FlgError8
    global MvToutCh2CHEX,dMvToutCh2CHEX,Tv1ToutCh2CHEX,dTv1ToutCh2CHEX
    global MvToutCh1CHEX,dMvToutCh1CHEX,Tv1ToutCh1CHEX,dTv1ToutCh1CHEX
    global TinCh2CHEX,ToutChAHU0

    # TinCh1CHEXはHeatTRで計算済み
    # TinCh2CHEX
    TinCh2CHEX = ToutChAHU0

    [ToutCh2CHEX,ToutCh1CHEX] = HEX.hex(GCh2CHEX,GCh1CHEX,TinCh2CHEX0,TinCh1CHEX0,772.5,ToutCh2CHEX0,ToutCh1CHEX0)

    global fault3
    # if fault3 == 1
    #     [ToutCh2CHEX,ToutCh1CHEX] = HEX(GCh2CHEX,GCh1CHEX,TinCh2CHEX0,TinCh1CHEX0,772.5/2,ToutCh2CHEX0,ToutCh1CHEX0)
    # end

    # 上限設定
    FlgError8 = 0
    if ToutCh2CHEX > 25:
        ToutCh2CHEX = 25
        FlgError8 = 1
    elif ToutCh2CHEX < 3:
        ToutCh2CHEX = 3
        FlgError8 = 1

    # センサ誤差、DDC誤差
    MvToutCh2CHEX = ToutCh2CHEX + dMvToutCh2CHEX
    MvToutCh1CHEX = ToutCh1CHEX + dMvToutCh1CHEX
    Tv1ToutCh2CHEX = MvToutCh2CHEX + dTv1ToutCh2CHEX
    Tv1ToutCh1CHEX = MvToutCh1CHEX + dTv1ToutCh1CHEX