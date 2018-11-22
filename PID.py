def pid(pxmax, pxmin, t_step, kc, ti, td, s1, s0, p1, p0, sig, px, kg, flg):
    # (pxmax=None,pxmin=None,t_step=None,kc=None,ti=None,td=None,s1=None,\
    # s0=None,p1=None,p0=None,sig=None,px=None,kg=None,flg=None,*args,**kwargs):
    import numpy as np

    # PID制御
    # Nomenclature#####
    # PXmax,PXmin   :制御値の最大・最小範囲
    # TSTEP         :計算ステップ
    # Kc            :比例ゲイン
    # TI            :積分時間
    # TD            :微分時間
    # S1            :現時刻の制御する要素の設定値 (温度や圧力)  S0:前時刻
    # P1            :現時刻の制御する要素の値   P0:前時刻
    # SIG           :積分総和
    # PX            :現時刻の制御に使用する要素の値(回転率、バルブ開度など)
    # CTRL          :制御に使用する要素の制御量
    # Kg            :CTRLの量を制御する要素の設定値に落とし込むための係数。(-1か1)
    # Flg           :設定値に不全がある、または不具合で制御が長時間おかしくなっていた場合にSIGをリセットする
    # example; Kc=0.06,TSTEP=1,TI=20,TD=0

    # 前時刻の制御量
    px0 = px

    # 設定値がない（流量がない）場合、出力をOとする
    if s1 > 0.001:

        c_trl = kc * ((s1 - p1) + 1 / ti * sig * t_step + td * ((s1 - p1) - (s0 - p0)) / t_step)
        px = px0 + c_trl * kg

        if px > px0 + 0.05:
            px = px0 + 0.05
        elif px < px0 - 0.05:
            px = px0 - 0.05

        # 制御量は上下限値をもつ
        if px > pxmax:
            px = pxmax
        elif px < pxmin:
            px = pxmin
    else:
        px = 0.0

    sig = sig + s1 - p1
    s0 = s1
    p0 = p1

    # Flgについて。time時間制御が正常に行われなかったら（S1-P1の符号が同一）、不具合が起きているとしてSIGをリセットする。
    time = 60

    for i in range(time, 2, - 1):
        flg[i] = flg[i - 1]

    if s1 - p1 > 0:
        flg[1] = 1
    elif s1 - p1 < 0:
        flg[1] = - 1
    else:
        flg[1] = 0

    if flg == 1:
        sig = 0
        flg = np.zeros(time)

    if flg == - 1:
        sig = 0
        flg = np.zeros(time)

    return px, s0, p0, sig, flg
