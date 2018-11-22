def set_variable_q():
    from test import set_var
    # 熱量の初期値
    # TR
    set_var(('QTR1','QTR2','QTR3','QTR4'),(0,0,0,0))

    # ST
    set_var(('QST1','QST2','QST3'),(100.3,80.37,90.17))

    # 不確かさ
    set_var(('MvQST1','MvQST2','MvQST3'),(100.3,80.37,90.17))

    set_var(('dMvQST1','dMvQST2','dMvQST3'),(0,0,0))

    set_var('SigQChAHU',0)






