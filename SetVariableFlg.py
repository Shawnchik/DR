def set_variable_flg():
    import numpy as np
    from test import set_var
    from test import get_var

    set_var(('FlgFlgVlvCP2','FlgFlgVlvSCP4','FlgFlgVlvSHP2','FlgFlgINVSCP4','FlgFlgVlvHP1'),(0,0,0,0,0))
    set_var(('FlgVlvCP2'),np.zeros(5),1)
    set_var(('FlgSgTR4'),np.zeros(15),1)
    set_var(('FlgVlvSCP4'),np.zeros(15),1)
    set_var(('FlgINVSCP4'),np.zeros(30),1)
    set_var(('FlgVlvSHP2'),np.zeros(15),1)
    set_var(('FlgVlvHP1'),np.zeros(5),1)

    # フラグ ##################################################################
    # 台数制御フラグ
    set_var(('FlgUpNmCP2'),np.zeros(15),1)
    set_var(('FlgDwNmCP2'),np.zeros(15),1)
    set_var(('FlgUpNmSCP4'),np.zeros(15),1)
    set_var(('FlgDwNmSCP4'),np.zeros(15),1)
    set_var(('FlgUpNmNP'),np.zeros(15),1)
    set_var(('FlgDwNmNP'),np.zeros(15),1)

    set_var(('FlgUpNmHP1'),np.zeros(15),1)
    set_var(('FlgDwNmHP1'),np.zeros(15),1)
    set_var(('FlgUpNmSHP2'),np.zeros(15),1)
    set_var(('FlgDwNmSHP2'),np.zeros(15),1)

    set_var(('FlgUpNmTR1234'),np.zeros(15),1)
    set_var(('FlgDwNmTR1234'),np.zeros(15),1)
    set_var(('FlgUpNmCT'),np.zeros(15),1)
    set_var(('FlgDwNmCT'),np.zeros(15),1)

    set_var(('WTVlvCT','FlgFlgVlvCT'),(15,0))
    WTVlvCT = get_var('WTVlvCT')
    set_var(('FlgVlvCT'),np.zeros(WTVlvCT),1)

    set_var(('FlgINVSHP2'),np.zeros(30),1)
    set_var('FlgFlgINVSHP2',0)

    set_var(('FlgSpLFTR3'),np.zeros(10),1)

    # NP
    set_var(('FlgSpToutCn1NHEX'),np.zeros(60),1)
    set_var(('FlgNHEX','FlgFlgSpToutCn1NHEX'),(-1,1))

    # PID制御SIGリセットフラグ
    global FlgPIDINVNP,FlgPIDVlvCT
    time = 60
    set_var(('FlgPIDVlvCP2'),np.zeros(time),1)
    set_var(('FlgPIDINVCP2'),np.zeros(time),1)
    set_var(('FlgPIDINVCP1'),np.zeros(time),1)

    set_var(('FlgPIDVlvChAHU'),np.zeros(time),1)

    set_var(('FlgPIDVlvHP1'),np.zeros(time),1)
    set_var(('FlgPIDINVHP1'),np.zeros(time),1)

    set_var(('FlgPIDVlvHtAHU'),np.zeros(time),1)

    set_var(('FlgPIDINVSCP2'),np.zeros(time),1)
    set_var(('FlgPIDINVSCP3'),np.zeros(time),1)
    set_var(('FlgPIDINVSCP4'),np.zeros(time),1)
    set_var(('FlgPIDVlvCh1CHEX'),np.zeros(time),1)
    set_var(('FlgPIDVlvSCP4'),np.zeros(time),1)

    set_var(('FlgPIDINVSCP1'),np.zeros(time),1)

    set_var(('FlgPIDINVSHP1'),np.zeros(time),1)
    set_var(('FlgPIDINVSHP2'),np.zeros(time),1)
    set_var(('FlgPIDVlvHt1HHEX'),np.zeros(time),1)
    set_var(('FlgPIDVlvSHP2'),np.zeros(time),1)

    set_var(('FlgPIDINVCDP1'),np.zeros(time),1)
    set_var(('FlgPIDINVCDP2'),np.zeros(time),1)
    set_var(('FlgPIDINVCDP3'),np.zeros(time),1)
    set_var(('FlgPIDINVCDP4'),np.zeros(time),1)

    set_var(('FlgPIDINVNP'),np.zeros(time),1)
    set_var(('FlgPIDVlvCT'),np.zeros(time),1)

    # エラーフラグ
    set_var(('FlgError1','FlgError2','FlgError3','FlgError4','FlgError5','FlgError6'),(0,0,0,0,0,0))
    set_var(('FlgError7','FlgError8','FlgError9','FlgError10','FlgError11','FlgError12'),(0,0,0,0,0,0))
    set_var(('FlgError13','FlgError14','FlgError15'),(0,0,0))


