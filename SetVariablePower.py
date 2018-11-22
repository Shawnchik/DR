def set_variable_power():
    from test import set_var
    # 消費電力とポンプ効率
    # TR
    set_var(('PwTR1','PwTR2','PwTR3','PwTR4'),(0,0,0,0))

    # Power
    set_var(('PwCP1','nCP1','PwCP2','nCP2'),(0,1,0,1))
    set_var(('PwSCP1','nSCP1','PwSCP2','nSCP2','PwSCP3','nSCP3','PwSCP4','nSCP4'),(0,1,0,1,0,1,0,1))
    set_var(('PwCDP1','nCDP1','PwCDP2','nCDP2','PwCDP3','nCDP3','PwCDP4','nCDP4','PwNP','nNP'),(0,1,0,1,0,1,0,1))

    # 不確かさ
    # TR
    set_var(('MvPwTR1','MvPwTR2','MvPwTR3','MvPwTR4'),(0,0,0,0))
    set_var(('dMvPwTR1','dMvPwTR2','dMvPwTR3','dMvPwTR4'),(0,0,0,0))
    # Pump
    set_var(('MvPwCP1','MvPwCP2'),(0,0))
    set_var(('dMvPwCP1','dMvPwCP2'),(0,0))

    set_var(('MvPwSCP1','MvPwSCP2','MvPwSCP3','MvPwSCP4'),(0,0,0,0))
    set_var(('dMvPwSCP1','dMvPwSCP2','dMvPwSCP3','dMvPwSCP4'),(0,0,0,0))

    set_var(('MvPwCDP1','MvPwCDP2','MvPwCDP3','MvPwCDP4'),(0,0,0,0))
    set_var(('dMvPwCDP1','dMvPwCDP2','dMvPwCDP3','dMvPwCDP4'),(0,0,0,0))

    set_var(('MvPwNP','dMvPwNP'),(0,0))

    set_var(('MvPwHP1','MvPwSHP1','MvPwSHP2'),(0,0,0))
    set_var(('MvPwFCT1','MvPwFCT2','MvPwFCT3','MvPwPmpCT1','MvPwPmpCT2','MvPwPmpCT3'),(0,0,0,0,0,0))

    set_var(('dMvPwHP1','dMvPwSHP1','dMvPwSHP2'),(0,0,0))
    set_var(('dMvPwFCT1','dMvPwFCT2','dMvPwFCT3','dMvPwPmpCT1','dMvPwPmpCT2','dMvPwPmpCT3'),(0,0,0,0,0,0))

