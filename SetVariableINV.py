def set_variable_inv():
    from test import set_var
    # ポンプINV周波数
    # CtrlCP
    set_var(('INVCP2','INVCP1'),(0,0))

    # SCP
    set_var(('INVSCP1','INVSCP2','INVSCP3','INVSCP4'), (0,0,0,0))

    # CDP
    set_var(('INVCDP1','INVCDP2','INVCDP3','INVCDP4'), (0,0,0,0))

    # CtrlNP
    set_var('INVNP',0)

    # HP
    set_var('INVHP1',0)

    # SHP
    set_var(('INVSHP1','INVSHP2'), (0, 0))

    # 不確かさ
    set_var(('CvINVCP1','CvINVCP2'), (0, 0))
    set_var(('CvINVSCP1','CvINVSCP2','CvINVSCP3','CvINVSCP4'), (0,0,0,0))
    set_var(('CvINVSCP1','CvINVSCP2','CvINVSCP3','CvINVSCP4'), (0,0,0,0))
    set_var(('CvINVCDP1','CvINVCDP2','CvINVCDP3','CvINVCDP4'), (0,0,0,0))
    set_var('CvINVNP',0)
    set_var('CvINVHP1',0)
    set_var(('CvINVSHP1','CvINVSHP2'), (0, 0))

    set_var(('dCvINVCP1','dCvINVCP2'), (0, 0))
    set_var(('dCvINVSCP1','dCvINVSCP2','dCvINVSCP3','dCvINVSCP4'), (0,0,0,0))
    set_var(('dCvINVCDP1','dCvINVCDP2','dCvINVCDP3','dCvINVCDP4'), (0,0,0,0))
    set_var('dCvINVNP',0)
    set_var('dCvINVHP1',0)
    set_var(('dCvINVSHP1','dCvINVSHP2'), (0, 0))



