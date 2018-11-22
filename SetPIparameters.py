def set_pi_parameters():
    from test import set_var
    from test import get_var
    # Nomenclature#####
    # ModeClHt      :運転モード（1:冷房モード、0:冷暖房モード）
    # 比例ゲインKp、積分時間Ti#################################################
    global KpINVCDP1,TiINVCDP1,KpINVCDP2,TiINVCDP2,KpINVCDP3,TiINVCDP3,KpINVCDP4,TiINVCDP4
    global KpVlvCP2,TiVlvCP2,KpINVCP2,TiINVCP2,KpINVCP1,TiINVCP1
    global KpVlvHP1,TiVlvHP1,KpINVHP1,TiINVHP1
    global KpINVNP,TiINVNP
    global KpINVSCP1,TiINVSCP1,KpINVSCP2,TiINVSCP2,KpINVSCP3,TiINVSCP3
    global KpVlvCh1CHEX,TiVlvCh1CHEX,KpVlvSCP4,TiVlvSCP4,KpINVSCP4,TiINVSCP4
    global KpINVSHP1,TiINVSHP1
    global KpVlvHt1HHEX,TiVlvHt1HHEX,KpVlvSHP2,TiVlvSHP2,KpINVSHP2,TiINVSHP2
    global KpVlvChAHU,TiVlvChAHU
    global KpVlvHtAHU,TiVlvHtAHU
    global KpVlvCT,TiVlvCT,PIDparameters

    ModeClHt = get_var('ModeClHt')
    PIDparameters = get_var('PIDparameters')
    if ModeClHt == 0:
        i = 1
    elif ModeClHt == 1:
        i = 2

    KpINVCDP1 = PIDparameters(i,2)
    TiINVCDP1 = PIDparameters(i,3)
    KpINVCDP2 = PIDparameters(i,5)
    TiINVCDP2 = PIDparameters(i,6)
    KpINVCDP3 = PIDparameters(i,8)
    TiINVCDP3 = PIDparameters(i,9)
    KpINVCDP4 = PIDparameters(i,11)
    TiINVCDP4 = PIDparameters(i,12)
    KpVlvCP2 = PIDparameters(i,14)
    TiVlvCP2 = PIDparameters(i,15)
    KpINVCP2 = PIDparameters(i,17)
    TiINVCP2 = PIDparameters(i,18)
    KpINVCP1 = PIDparameters(i,20)
    TiINVCP1 = PIDparameters(i,21)
    KpINVNP = PIDparameters(i,23)*2
    # # 要チェック
    # KpINVNP = KpINVNP / 10
    # TiINVNP = PIDparameters(i,24)
    TiINVNP = PIDparameters(i,24)/3
    KpINVSCP1 = PIDparameters(i,26)
    TiINVSCP1 = PIDparameters(i,27)
    KpINVSCP2 = PIDparameters(i,29)
    TiINVSCP2 = PIDparameters(i,30)
    KpINVSCP3 = PIDparameters(i,32)
    TiINVSCP3 = PIDparameters(i,33)
    KpINVSCP4 = PIDparameters(i,35)
    # 要チェック
    KpINVSCP4 = KpINVSCP4 / 5
    TiINVSCP4 = PIDparameters(i,36)
    KpVlvCh1CHEX = PIDparameters(i,38)
    TiVlvCh1CHEX = PIDparameters(i,39)
    KpVlvSCP4 = PIDparameters(i,41)
    # 要チェック
    KpVlvSCP4 = KpVlvSCP4 / 10
    TiVlvSCP4 = PIDparameters(i,42)
    KpVlvChAHU = PIDparameters(i,44)
    TiVlvChAHU = PIDparameters(i,45)
    KpVlvHtAHU = PIDparameters(i,47)
    TiVlvHtAHU = PIDparameters(i,48)
    KpINVSHP1 = PIDparameters(i,50)
    TiINVSHP1 = PIDparameters(i,51)
    KpINVSHP2 = PIDparameters(i,53)
    TiINVSHP2 = PIDparameters(i,54)
    # 要チェック
    # KpVlvSHP2 = PIDparameters(i,56)
    KpVlvSHP2 = KpVlvSCP4
    # TiVlvSHP2 = PIDparameters(i,57)
    TiVlvSHP2 = TiVlvSCP4
    KpVlvHt1HHEX = PIDparameters(i,59)
    TiVlvHt1HHEX = PIDparameters(i,60)
    KpVlvHP1 = PIDparameters(i,62)
    TiVlvHP1 = PIDparameters(i,63)
    KpINVHP1 = PIDparameters(i,65)
    TiINVHP1 = PIDparameters(i,66)
    KpVlvCT = PIDparameters(i,68)
    TiVlvCT = PIDparameters(i,69)


