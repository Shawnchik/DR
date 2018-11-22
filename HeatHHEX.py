def heat_hhex():
    import HEX
    # 一次二次温水熱交換器の熱に関する計算
    # Nomenclature
    # TinHt2HHEX        :冷水熱交二次入口温度['C]
    global TinHt2HHEX0,TinHt1HHEX0,TinHt2HHEX,ToutHtAHU0
    global GHt2HHEX,GHt1HHEX,ToutHt2HHEX,ToutHt1HHEX,ToutHt2HHEX0,ToutHt1HHEX0,FlgError14
    global MvToutHt2HHEX,dMvToutHt2HHEX,MvToutHt1HHEX,dMvToutHt1HHEX,Tv1ToutHt2HHEX,dTv1ToutHt2HHEX,Tv1ToutHt1HHEX,dTv1ToutHt1HHEX

    # TinHt1HHEXはHeatTRで計算済み
    # TinHt2HHEX
    TinHt2HHEX = ToutHtAHU0
    [ToutHt1HHEX,ToutHt2HHEX] = HEX.hex(GHt1HHEX,GHt2HHEX,TinHt1HHEX0,TinHt2HHEX0,992.25,ToutHt1HHEX0,ToutHt2HHEX0)


    # if GHt2HHEX > 0
    #     GHt2HHEX
    #     GHt1HHEX
    #     TinHt2HHEX0
    #     TinHt1HHEX0
    #     ToutHt2HHEX0
    #     ToutHt1HHEX0
    #     pause
    #
    # end



    # 上限設定
    FlgError14 = 0
    if ToutHt2HHEX > 60:
        ToutHt2HHEX = 60
        FlgError14 = 1

    # センサ誤差、DDC誤差
    MvToutHt2HHEX = ToutHt2HHEX + dMvToutHt2HHEX
    MvToutHt1HHEX = ToutHt1HHEX + dMvToutHt1HHEX
    Tv1ToutHt2HHEX = MvToutHt2HHEX + dTv1ToutHt2HHEX
    Tv1ToutHt1HHEX = MvToutHt1HHEX + dTv1ToutHt1HHEX