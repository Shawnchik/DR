def set_variable_else():
    import numpy as np
    from test import set_var
    # from test import get_var
    # その他

    # アウトプット用
    set_var(('Results', 'ResultMonth', 'ResultMonthly'))
    set_var('Results', np.zeros((10080,104), 1))
    set_var('ResultMonth', np.zeros((4,79)), 1)
    set_var('ResultMonthly', np.zeros((1,35)), 1)

    # 信号
    set_var(('SgChSt','SgHtSt','SgTR4','MinuteSt','HourSt'),(1,1,1,0,0,0))

    # # 年月日
    # global year,month,day
    # year = 2015
    # month = 1
    # day = 0

    # 運転台数
    set_var(('NmCP2','NmSCP4','NmNP','NmSHP2','NmHP1','NmTR1234','NmCT'),\
            (1, 1, 1, 1, 1, 1, 1))

    # 熱交換関係
    set_var(('UACT1','UACT2','UACT3'), (63354,126709,126709))

    # OutputMonthlyCOP
    set_var('CntMonth',0)

    # 負荷率設定値
    set_var(('SpLFTR1','SpLFTR2','SpLFTR3','SpLFTR4'),(0,0,0,0))

    # 不確かさ
    set_var(('Tv1SpLFTR1','Tv1SpLFTR2','Tv1SpLFTR3','Tv1SpLFTR4'),(0,0,0,0))
    set_var(('dTv1SpLFTR1','dTv1SpLFTR2','dTv1SpLFTR3','dTv1SpLFTR4'),(0,0,0,0))

    set_var('WBT',10)




















