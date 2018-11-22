def heat_ahu():
    # AHUの熱に関する計算。様々なパターンに対して、システムの処理する熱量が同じになるようにする。
    # Nomenclature
    # TinAHU        :AHU入口温度[m3/min]
    # ToutAHU       :AHU出口温度[m3/min]
    # QAHU          :AHU処理熱量[kW](ここでは簡単のため、K * m3/min)
    # QCh2          :冷水供給熱量[GJ/min]
    global TinChAHU,ToutChAHU,ToutCh2CHEX0,ToutChTR40
    global GCh2CHEX,GCP1,GCh2Ld,FlgError7
    global MvTinChAHU,dMvTinChAHU,Tv1TinChAHU,dTv1TinChAHU
    global MvToutChAHU,dMvToutChAHU,Tv1ToutChAHU,dTv1ToutChAHU
    global GHt2HHEX,TinHtAHU,ToutHt2HHEX0,ToutHtAHU,GHt2Ld,GHtAHU,FlgError13
    global MvTinHtAHU,dMvTinHtAHU,Tv1TinHtAHU,dTv1TinHtAHU
    global MvToutHtAHU,dMvToutHtAHU,Tv1ToutHtAHU,dTv1ToutHtAHU
    global SigQChAHU

    # 冷水系統AHU
    if GCh2CHEX * 2 + GCP1 > 0:
        TinChAHU = (ToutCh2CHEX0 * GCh2CHEX * 2 + ToutChTR40 * GCP1) / (GCh2CHEX * 2 + GCP1)
        ToutChAHU = TinChAHU + GCh2Ld * 10 / (GCh2CHEX * 2 + GCP1)
        ToutChAHU = ToutChAHU + SigQChAHU / (GCh2CHEX * 2 + GCP1)

    # 上限設定
    FlgError7 = 0
    if ToutChAHU > 30:
        SigQChAHU = (ToutChAHU - 30) * (GCh2CHEX * 2 + GCP1)
        ToutChAHU = 30
        FlgError7 = 1
    else:
        SigQChAHU = 0

    # センサ誤差、DDC誤差
    MvTinChAHU = TinChAHU + dMvTinChAHU
    MvToutChAHU = ToutChAHU + dMvToutChAHU
    Tv1TinChAHU = MvTinChAHU + dTv1TinChAHU
    Tv1ToutChAHU = MvToutChAHU + dTv1ToutChAHU


    # 温水系統AHU
    if GHt2HHEX * 2 > 0:
        TinHtAHU = ToutHt2HHEX0
        ToutHtAHU = TinHtAHU - GHt2Ld / GHtAHU * 10
    # 下限設定
    FlgError13 = 0
    if ToutHtAHU < 15:
        ToutHtAHU = 15
        FlgError13 = 1

    # センサ誤差、DDC誤差
    MvTinHtAHU = TinHtAHU + dMvTinHtAHU
    MvToutHtAHU = ToutHtAHU + dMvToutHtAHU
    Tv1TinHtAHU = MvTinHtAHU + dTv1TinHtAHU
    Tv1ToutHtAHU = MvToutHtAHU + dTv1ToutHtAHU

