def ctrl_vlv_ch_ahu():
    # 冷水系統AHU二方弁制御
    # Nomenclature
    # SpGChAHU      :冷水系統AHU流量目標値[m3/min]
    # GCh2Ld        :冷水系統負荷流量[m3/min]
    # VlvChAHU      :冷水系統AHU二方弁開度(0:全閉,1:全開)
    # SpGChAHU0     :1時刻前の冷水系統AHU流量目標値[m3/min]
    # GChAHU0       :1時刻前の冷水系統AHU流量[m3/min]
    # SigGChAHU     :冷水系統AHU流量制御PID計算における積分値（これが0になるように制御される）
    # GChAHU        :冷水系統AHU流量[m3/min]

    global SpGChAHU,SigGChAHU,SpGChAHU0,VlvChAHU,VlvChAHU0
    global KpVlvChAHU,TiVlvChAHU
    global MvGCh2Ld,MvGChAHU,MvGChAHU0
    global CvVlvChAHU,CvVlvChAHU0,dCvVlvChAHU,Tv1VlvChAHU,dTv1VlvChAHU
    global FlgPIDVlvChAHU
    global PFVlvChAHU
    # AHUへの負荷の割り当て
    SpGChAHU = MvGCh2Ld
    if SpGChAHU == 0:
        CvVlvChAHU = 0
        CvVlvChAHU0 = 0
        VlvChAHU = 0
        VlvChAHU0 = 0
        Tv1VlvChAHU = 0
    else:
        # 負荷流量になるようにAHU二方弁をPI制御
        [CvVlvChAHU,SpGChAHU0,MvGChAHU0,SigGChAHU,FlgPIDVlvChAHU] = PID(1.0,0.001,1,KpVlvChAHU,TiVlvChAHU,0,SpGChAHU,SpGChAHU0,MvGChAHU,MvGChAHU0,SigGChAHU,CvVlvChAHU,1,FlgPIDVlvChAHU)
        Tv1VlvChAHU = CvVlvChAHU + dTv1VlvChAHU
        VlvChAHU = CvVlvChAHU + dCvVlvChAHU

        if SpGChAHU > 0.5:
            PFVlvChAHU = PFVlvChAHU + abs((MvGChAHU - SpGChAHU) / SpGChAHU)




