def ctrl_vlv_ct():
    import PID
    # 冷却塔バイパス弁制御
    # Nomenclature
    # ToutVlvCT     :バイパス弁出口温度(バイパス弁を出て、冷却塔からの水とバイパスからの水が混ざった後の温度)['C]
    # VlvCT         :冷却塔バイパス弁開度(0:全閉,1:全開)

    global SpToutVlvCT,SpToutChTR1
    global CvVlvCT,SpToutVlvCT0,MvToutVlvCT0,SigToutVlvCT,Tv1VlvCT0,FlgPIDVlvCT,KpVlvCT,TiVlvCT
    global MvToutVlvCT,CvVlvCT0,Tv1VlvCT,dTv1VlvCT,VlvCT,dCvVlvCT,VlvCT0
    global FlgFlgVlvCT,FlgVlvCT,WTVlvCT
    global PFVlvCT
    # AHUへの負荷の割り当て
    SpToutVlvCT = SpToutChTR1 + 6

    if FlgFlgVlvCT == 1:
        # 設定温度になるように冷却塔バイパス弁をPI制御

        [CvVlvCT,SpToutVlvCT0,MvToutVlvCT0,SigToutVlvCT,FlgPIDVlvCT] = \
            PID.pid(1.0,0.001,1,KpVlvCT,TiVlvCT,0,SpToutVlvCT,SpToutVlvCT0,MvToutVlvCT,MvToutVlvCT0,SigToutVlvCT,CvVlvCT,1,FlgPIDVlvCT)
        Tv1VlvCT = CvVlvCT + dTv1VlvCT
        VlvCT = CvVlvCT + dCvVlvCT

        if SpToutVlvCT > 0:
            PFVlvCT = PFVlvCT + abs((MvToutVlvCT - SpToutVlvCT) / SpToutVlvCT)

    else:
        Tv1VlvCT = 0
        CvVlvCT = 0
        CvVlvCT0 = 0
        VlvCT = 0

    # バイパス弁フラグ
    # 効果待ち時間15分
    WTVlvCT = 15 #  ????ノウ　コメント？
    if MvToutVlvCT < SpToutVlvCT -1:
        for i in range(WTVlvCT,2,-1):
            FlgVlvCT[i] = FlgVlvCT[i-1]
        FlgVlvCT[1] = 1

    elif MvToutVlvCT > SpToutVlvCT + 1:
        for i in range(WTVlvCT,2,-1):
            FlgVlvCT[i] = FlgVlvCT[i-1]
        FlgVlvCT[1] = 0

    if FlgVlvCT == 1:
        FlgFlgVlvCT = 1
    elif FlgVlvCT == 0:
        FlgFlgVlvCT = 0






