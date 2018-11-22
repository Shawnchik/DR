def ctrl_vlv_ht_ahu():
    import PID
    # 温水系統AHU二方弁制御
    # Nomenclature
    # SpGHtAHU      :温水系統AHU流量目標値[m3/min]
    # GHt2Ld        :温水系統負荷流量[m3/min]
    # VlvHtAHU      :温水系統AHU二方弁開度(0:全閉,1:全開)
    # SpGHtAHU0     :1時刻前の温水系統AHU流量目標値[m3/min]
    # GHtAHU0       :1時刻前の温水系統AHU流量[m3/min]
    # SigGHtAHU     :温水系統AHU流量制御PID計算における積分値（これが0になるように制御される）
    # GHtAHU        :温水系統AHU流量[m3/min]

    global SpGHtAHU,MvGHt2Ld,MvGHtAHU,SigGHtAHU,SpGHtAHU0,MvGHtAHU0,VlvHtAHU,VlvHtAHU0
    global KpVlvHtAHU,TiVlvHtAHU
    global Tv1VlvHtAHU,CvVlvHtAHU,dTv1VlvHtAHU,dCvVlvHtAHU,CvVlvHtAHU0
    global FlgPIDVlvHtAHU
    global PFVlvHtAHU
    # AHUへの負荷の割り当て
    SpGHtAHU = MvGHt2Ld
    if SpGHtAHU == 0:
        CvVlvHtAHU = 0
        CvVlvHtAHU0 = 0
        VlvHtAHU = 0
        VlvHtAHU0 = 0
        Tv1VlvHtAHU = 0
    else:
        [CvVlvHtAHU,SpGHtAHU0,MvGHtAHU0,SigGHtAHU,FlgPIDVlvHtAHU] = PID.pid(1.0,0.001,1,KpVlvHtAHU,TiVlvHtAHU,0,SpGHtAHU,SpGHtAHU0,MvGHtAHU,MvGHtAHU0,SigGHtAHU,CvVlvHtAHU,1,FlgPIDVlvHtAHU)
        Tv1VlvHtAHU = CvVlvHtAHU + dTv1VlvHtAHU
        VlvHtAHU = CvVlvHtAHU + dCvVlvHtAHU

        if SpGHtAHU > 0.5:
            PFVlvHtAHU = PFVlvHtAHU + abs((MvGHtAHU - SpGHtAHU) / SpGHtAHU)



