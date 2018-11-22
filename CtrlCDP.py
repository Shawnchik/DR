def ctrl_cdp():
    import PID
    # 冷却水ポンプ制御
    # Nonmenclature
    # SpLFTR1~4         :TR1~4設定負荷率(0~1)
    # SpGCDP1~4         :TR1~4冷却水流量設定値[m3/min]
    # GCDP1~4           :TR1~4冷却水流量[m3/min]
    global ModeClHt
    global SpLFTR1,SpLFTR2,SpLFTR3,SpLFTR4
    global SpGCDP10,SpGCDP20,SpGCDP30,SpGCDP40
    global SigGCDP1,SigGCDP2,SigGCDP3,SigGCDP4
    global INVCDP1,INVCDP2,INVCDP3,INVCDP4
    global INVCDP10,INVCDP20,INVCDP30,INVCDP40
    global KpINVCDP1,TiINVCDP1,KpINVCDP2,TiINVCDP2,KpINVCDP3,TiINVCDP3,KpINVCDP4,TiINVCDP4
    global MvGCDP1,MvGCDP10,CvINVCDP1,CvINVCDP10,dCvINVCDP1,Tv1INVCDP1,dTv1INVCDP1
    global MvGCDP2,MvGCDP20,CvINVCDP2,CvINVCDP20,dCvINVCDP2,Tv1INVCDP2,dTv1INVCDP2
    global MvGCDP3,MvGCDP30,CvINVCDP3,CvINVCDP30,dCvINVCDP3,Tv1INVCDP3,dTv1INVCDP3
    global MvGCDP4,MvGCDP40,CvINVCDP4,CvINVCDP40,dCvINVCDP4,Tv1INVCDP4,dTv1INVCDP4
    global SpGCDP1,SpGCDP2,SpGCDP3,SpGCDP4
    global FlgPIDINVCDP1,FlgPIDINVCDP2,FlgPIDINVCDP3,FlgPIDINVCDP4
    global PFINVCDP1,PFINVCDP2,PFINVCDP3,PFINVCDP4
    global PrGCDP1,PrGCDP2,PrGCDP3,PrGCDP4
    global CvINVSCP1,CvINVSCP2,CvINVSCP3,CvINVCP1
    # 冷却水ポンプは定格運転とする。
    # 流量設定値
    if ModeClHt == 1:
    #     if SpLFTR1 > 0
        if CvINVSCP1 > 0:
            SpGCDP1 = 5.892 * 0.8
    #         SpGCDP1 = SpGCDP1 * PrGCDP1
        else:
            SpGCDP1 = 0

    else:
        if SpLFTR1 > 0:
    #         SpGCDP1 = 2.47
            SpGCDP1 = 5.0
            SpGCDP1 = SpGCDP1 * PrGCDP1
        else:
            SpGCDP1 = 0

    # if SpLFTR2 > 0
    if CvINVSCP2 > 0:
        SpGCDP2 = 11.738
        SpGCDP2 = SpGCDP2 * PrGCDP2
    else:
        SpGCDP2 = 0

    # if SpLFTR3 > 0
    if CvINVSCP3 > 0:
        SpGCDP3 = 11.83 * 0.8
    #     SpGCDP3 = SpGCDP3 * PrGCDP3
    else:
        SpGCDP3 = 0

    # if SpLFTR4 > 0
    if CvINVCP1 > 0:
        SpGCDP4 = 11.623
        SpGCDP4 = SpGCDP4 * PrGCDP4
    else:
        SpGCDP4 = 0

    # 目標流量になるようにポンプINVをPI制御(INVに下限値は設けていない)
    # INVCDP1~4制御
    if SpGCDP1 > 0:
        [CvINVCDP1,SpGCDP10,MvGCDP10,SigGCDP1,FlgPIDINVCDP1] = \
            PID.pid(1.0,0.001,1,KpINVCDP1,TiINVCDP1,0,SpGCDP1,SpGCDP10,MvGCDP1,MvGCDP10,SigGCDP1,CvINVCDP1,1,FlgPIDINVCDP1)
        Tv1INVCDP1 = CvINVCDP1 + dTv1INVCDP1
        INVCDP1 = CvINVCDP1 + dCvINVCDP1

        if SpGCDP1 > 0.5:
            PFINVCDP1 = PFINVCDP1 + abs((MvGCDP1 - SpGCDP1) / SpGCDP1)


    else:
        INVCDP1 = 0
        CvINVCDP1 = 0
        Tv1INVCDP1 = 0

    if SpGCDP2 > 0:
        [CvINVCDP2,SpGCDP20,MvGCDP20,SigGCDP2,FlgPIDINVCDP2] = \
            PID.pid(1.0,0.001,1,KpINVCDP2,TiINVCDP2,0,SpGCDP2,SpGCDP20,MvGCDP2,MvGCDP20,SigGCDP2,CvINVCDP2,1,FlgPIDINVCDP2)
        Tv1INVCDP2 = CvINVCDP2 + dTv1INVCDP2
        INVCDP2 = CvINVCDP2 + dCvINVCDP2

        if SpGCDP2 > 0.5:
            PFINVCDP2 = PFINVCDP2 + abs((MvGCDP2 - SpGCDP2) / SpGCDP2)

    else:
        INVCDP2 = 0
        CvINVCDP2 = 0
        Tv1INVCDP2 = 0

    if SpGCDP3 > 0:
        [CvINVCDP3,SpGCDP30,MvGCDP30,SigGCDP3,FlgPIDINVCDP3] = \
            PID.pid(1.0,0.001,1,KpINVCDP3,TiINVCDP3,0,SpGCDP3,SpGCDP30,MvGCDP3,MvGCDP30,SigGCDP3,CvINVCDP3,1,FlgPIDINVCDP3)
        Tv1INVCDP3 = CvINVCDP3  + dTv1INVCDP3
        INVCDP3 = CvINVCDP3 + dCvINVCDP3

        if SpGCDP3 > 0.5:
            PFINVCDP3 = PFINVCDP3 + abs((MvGCDP3 - SpGCDP3) / SpGCDP3)

    else:
        INVCDP3 = 0
        CvINVCDP3 = 0
        Tv1INVCDP3 = 0

    if SpGCDP4 > 0:
        [CvINVCDP4,SpGCDP40,MvGCDP40,SigGCDP4,FlgPIDINVCDP4] = \
            PID.pid(1.0,0.001,1,KpINVCDP4,TiINVCDP4,0,SpGCDP4,SpGCDP40,MvGCDP4,MvGCDP40,SigGCDP4,CvINVCDP4,1,FlgPIDINVCDP4)
        Tv1INVCDP4 = CvINVCDP4 + dTv1INVCDP4
        INVCDP4 = CvINVCDP4 + dCvINVCDP4

        if SpGCDP4 > 0.5:
            PFINVCDP4 = PFINVCDP4 + abs((MvGCDP4 - SpGCDP4) / SpGCDP4)

    else:
        INVCDP4 = 0
        CvINVCDP4 = 0
        Tv1INVCDP4 = 0


