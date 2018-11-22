def set_variable_temperature():
    import numpy as np
    from test import set_var
# 温度
    # ST
    set_var(('TinST0','ToutST0'),(5,15))
    # ST1
    set_var(('TinST1','TinST10','ToutST1','ToutST10'),(5,5,5,5))
    set_var('TfST1',np.ones(60) * 5,1)
    set_var('TST1',np.ones(60) * 5,1)
    # ST2
    set_var(('TinST2','TinST20','ToutST2','ToutST20'),(5,5,5,5))
    set_var('TfST2',np.ones(60) * 5,1)
    set_var('TST2',np.ones(60) * 5,1)
    # ST3
    set_var(('TfST3','TST3','TinST3','TinST30','ToutST3','ToutST30'),(5,5,5,5))
    set_var('TfST3',np.ones(60) * 5,1)
    set_var('TST3',np.ones(60) * 5,1)
    # ST123
    set_var(('ToutST12','ToutST120','ToutST123','ToutST1230','TinST123','TinST1230','TinST12','TinST120'),(5,5,5,5,5,5,5,5))
    # ChAHU # HtAHU
    set_var(('TinChAHU','ToutChAHU','TinChAHU0','ToutChAHU0','TinHtAHU','ToutHtAHU','ToutHtAHU0'),(7,7,17,17,43,33,33))
    # TR1
    set_var(('TinChTR1','ToutChTR1','TinCnTR1','ToutCnTR1'),(15,5,30,35))
    set_var(('TinHtTR1','ToutHtTR1'),(35,45))
    set_var(('TinHtTR10','ToutHtTR10'),(35,45))
    set_var(('TinChTR10','ToutChTR10','TinCnTR10','ToutCnTR10'),(15,5,30,35))
    # TR2
    set_var(('TinChTR2','ToutChTR2','TinCnTR2','ToutCnTR2'),(15,5,30,35))
    set_var(('TinChTR20','ToutChTR20','TinCnTR20','ToutCnTR20'),(15,5,30,35))
    # TR3
    set_var(('TinChTR3','ToutChTR3','TinCnTR3','ToutCnTR3'),(15,5,30,35))
    set_var(('TinChTR30','ToutChTR30','TinCnTR30','ToutCnTR30'),(15,5,30,35))
    # TR4
    set_var(('TinChTR4','ToutChTR4','TinCnTR4','ToutCnTR4'),(17,7,30,35))
    set_var(('TinChTR40','ToutChTR40','TinCnTR40','ToutCnTR40'),(17,7,30,35))
    # CHEX
    set_var(('TinCh1CHEX','ToutCh1CHEX','TinCh2CHEX','ToutCh2CHEX'),(5,15,17,7))
    set_var(('TinCh1CHEX0','ToutCh1CHEX0','TinCh2CHEX0','ToutCh2CHEX0'),(5,15,17,7))
    # HHEX
    set_var(('TinHt1HHEX','ToutHt1HHEX','TinHt2HHEX','ToutHt2HHEX'),(45,35,33,43))
    set_var(('TinHt1HHEX0','ToutHt1HHEX0','TinHt2HHEX0','ToutHt2HHEX0'),(45,35,33,43))
    # NHEX
    set_var(('TinCn1NHEX','ToutCn1NHEX','TinCn2NHEX','ToutCn2NHEX'),(35,30,28,34))
    set_var(('TinCn1NHEX0','ToutCn1NHEX0','TinCn2NHEX0','ToutCn2NHEX0'),(35,30,28,34))
    # CT
    set_var(('TinCnCT1','TinCnCT2','TinCnCT3'),(15,15,15))
    set_var(('ToutCnCT1','ToutCnCT2','ToutCnCT3'),(15,15,15))
    set_var(('ToutCnCT'),15)
    set_var(('TinCnCT10','TinCnCT20','TinCnCT30'),(15,15,15))
    set_var(('ToutCnCT10','ToutCnCT20','ToutCnCT30'),(15,15,15))
    set_var(('ToutCnCT0'),15)
    set_var(('ToutVlvCT0','ToutVlvCT'),(15,0))
    # ST
    set_var(('MvTST103','MvTST109','MvTST115','MvTST121','MvTST127','MvTST133','MvTST139','MvTST145','MvTST151','MvTST157'),\
            (0,0,0,0,0,0,0,0,0,0))
    set_var(('MvTST203','MvTST209','MvTST215','MvTST221','MvTST227','MvTST233','MvTST239','MvTST245','MvTST251','MvTST257'),\
            (0,0,0,0,0,0,0,0,0,0))
    set_var(('MvTST303','MvTST309','MvTST315','MvTST321','MvTST327','MvTST333','MvTST339','MvTST345','MvTST351','MvTST357'),\
            (0,0,0,0,0,0,0,0,0,0))
    set_var(('dMvTST103','dMvTST109','dMvTST115','dMvTST121','dMvTST127','dMvTST133','dMvTST139','dMvTST145','dMvTST151','dMvTST157'),\
            (0,0,0,0,0,0,0,0,0,0))
    set_var(('dMvTST203','dMvTST209','dMvTST215','dMvTST221','dMvTST227','dMvTST233','dMvTST239','dMvTST245','dMvTST251','dMvTST257'),\
            (0,0,0,0,0,0,0,0,0,0))
    set_var(('dMvTST303','dMvTST309','dMvTST315','dMvTST321','dMvTST327','dMvTST333','dMvTST339','dMvTST345','dMvTST351','dMvTST357'),\
            (0,0,0,0,0,0,0,0,0,0))
    # TR
    set_var(('MvTinCnTR1', 'MvToutCnTR1', 'MvTinChTR1', 'MvToutChTR1'),(0,0,0,0))
    set_var(('MvTinCnTR2', 'MvToutCnTR2', 'MvTinChTR2', 'MvToutChTR2'),(0,0,0,0))
    set_var(('MvTinCnTR3', 'MvToutCnTR3', 'MvTinChTR3', 'MvToutChTR3'),(0,0,0,0))
    set_var(('MvTinCnTR4', 'MvToutCnTR4', 'MvTinChTR4', 'MvToutChTR4'),(0,0,0,0))
    set_var(('MvTinHtTR1', 'MvToutHtTR1'),(0,0))
    set_var(('dMvTinCnTR1', 'dMvToutCnTR1', 'dMvTinChTR1', 'dMvToutChTR1'),(0,0,0,0))
    set_var(('dMvTinCnTR2', 'dMvToutCnTR2', 'dMvTinChTR2', 'dMvToutChTR2'),(0,0,0,0))
    set_var(('dMvTinCnTR3', 'dMvToutCnTR3', 'dMvTinChTR3', 'dMvToutChTR3'), (0, 0, 0, 0))
    set_var(('dMvTinCnTR4', 'dMvToutCnTR4', 'dMvTinChTR4', 'dMvToutChTR4'), (0, 0, 0, 0))
    set_var(('dMvTinHtTR1', 'dMvToutHtTR1'),(0,0))

    # HEX,AHU
    set_var(('MvToutCh2CHEX', 'MvToutCh1CHEX','MvToutCn1NHEX', 'MvToutCn2NHEX', 'MvTinCn2NHEX', 'MvTinCn1NHEX'),\
            (0,0,0,0,0,0))
    set_var(('MvToutHt2HHEX', 'MvToutHt1HHEX'),(0,0))
    set_var(('MvTinChAHU', 'MvToutChAHU','MvTinHtAHU', 'MvToutHtAHU'),(0,0,0,0))
    set_var(('dMvToutCh2CHEX', 'dMvToutCh1CHEX'), (0, 0))
    set_var(('dMvToutCn1NHEX', 'dMvToutCn2NHEX', 'dMvTinCn2NHEX', 'dMvTinCn1NHEX'),(0,0,0,0))
    set_var(('dMvToutHt2HHEX', 'dMvToutHt1HHEX'), (0, 0))
    set_var(('dMvTinChAHU', 'dMvToutChAHU','dMvTinHtAHU', 'dMvToutHtAHU'),(0,0,0,0))

    # CT
    set_var(('MvTinCnCT1', 'MvTinCnCT2', 'MvTinCnCT3','MvToutCnCT1', 'MvToutCnCT2', 'MvToutCnCT3'),\
            (0,0,0,0,0,0))
    set_var(('MvToutCnCT','MvToutCnCT0'), (0, 0))
    set_var(('MvTinCnCT10', 'MvTinCnCT20', 'MvTinCnCT30'), (0,0,0))
    set_var(('MvToutCnCT10', 'MvToutCnCT20', 'MvToutCnCT30'), (0,0,0))
    set_var(('MvToutVlvCT0', 'MvToutVlvCT'), (0, 0))
    set_var(('dMvTinCnCT1', 'dMvTinCnCT2', 'dMvTinCnCT3','dMvToutCnCT1', 'dMvToutCnCT2', 'dMvToutCnCT3'),\
            (0,0,0,0,0,0))
    set_var(('dMvToutCnCT','dMvToutCnCT0'), (0, 0))
    set_var(('dMvTinCnCT10', 'dMvTinCnCT20', 'dMvTinCnCT30'), (0,0,0))
    set_var(('dMvToutCnCT10', 'dMvToutCnCT20', 'dMvToutCnCT30'), (0,0,0))
    set_var(('dMvToutVlvCT0', 'dMvToutVlvCT'), (0, 0))
    set_var('fault4',0)


    # ST
    # TinST0 = 5
    # ToutST0 = 15

    # ST1
    # TfST1 = np.ones(60) * 5      # 槽分割数が60だから!!!
    # TST1 = np.ones(60) * 5
    # TinST1 = 5
    # TinST10 = 5
    # ToutST1 = 5
    # ToutST10 = 5

    # ST2
    # TfST2 = np.ones(60) * 5
    # TST2 = np.ones(60) * 5
    # TinST2 = 5
    # TinST20 = 5
    # ToutST2 = 5
    # ToutST20 = 5

    # ST3
    # TfST3 = np.ones(60) * 5
    # TST3 = np.ones(60) * 5
    # TinST3 = 5
    # TinST30 = 5
    # ToutST3 = 5
    # ToutST30 = 5

    # ST123
    # ToutST12 = 5
    # ToutST120 = 5
    # ToutST123 = 5
    # ToutST1230 = 5
    # TinST123 = 5
    # TinST1230 = 5
    # TinST12 = 5
    # TinST120 = 5

    # # ST
    # TinST0 = 7
    # ToutST0 = 17
    # # ST1
    # TfST1 = ones(1,60) * 7      # 槽分割数が60だから!!!
    # TST1 = ones(1,60) * 7
    # TinST1 = 7
    # TinST10 = 7
    # ToutST1 = 7
    # ToutST10 = 7
    # # ST2
    # TfST2 = ones(1,60) * 7
    # TST2 = ones(1,60) * 7
    # TinST2 = 7
    # TinST20 = 7
    # ToutST2 = 7
    # ToutST20 = 7
    # # ST3
    # TfST3 = ones(1,60) * 45
    # TST3 = ones(1,60) * 45
    # TinST3 = 45
    # TinST30 = 45
    # ToutST3 = 45
    # ToutST30 = 45
    # # ST123
    # ToutST12 = 7
    # ToutST120 = 7
    # ToutST123 = 7
    # ToutST1230 = 7
    # TinST123 = 7
    # TinST1230 = 7
    # TinST12 = 7
    # TinST120 = 7

    # ChAHU
    # TinChAHU = 7
    # TinChAHU0 = 7
    # ToutChAHU = 17
    # ToutChAHU0 = 17
    # HtAHU
    # TinHtAHU = 43
    # ToutHtAHU = 33
    # ToutHtAHU0 = 33

    # TR1
    # TinChTR1 = 15
    # ToutChTR1 = 5
    # TinCnTR1 = 30
    # ToutCnTR1 = 35
    # TinHtTR1 = 35
    # ToutHtTR1 = 45
    # TinChTR10 = 15
    # ToutChTR10 = 5
    # TinCnTR10 = 30
    # ToutCnTR10 = 35
    # TinHtTR10 = 35
    # ToutHtTR10 = 45
    # TR2
    # TinChTR2 = 15
    # ToutChTR2 = 5
    # TinCnTR2 = 30
    # ToutCnTR2 = 35
    # TinChTR20 = 15
    # ToutChTR20 = 5
    # TinCnTR20 = 30
    # ToutCnTR20 = 35
    # TR3
    # TinChTR3 = 15
    # ToutChTR3 = 5
    # TinCnTR3 = 30
    # ToutCnTR3 = 35
    # TinChTR30 = 15
    # ToutChTR30 = 5
    # TinCnTR30 = 30
    # ToutCnTR30 = 35
    # TR4
    # TinChTR4 = 17
    # ToutChTR4 = 7
    # TinCnTR4 = 30
    # ToutCnTR4 = 35
    # TinChTR40 = 17
    # ToutChTR40 = 7
    # TinCnTR40 = 30
    # ToutCnTR40 = 35
    # CHEX
    # TinCh1CHEX = 5
    # ToutCh1CHEX = 15
    # TinCh2CHEX = 17
    # ToutCh2CHEX = 7
    # TinCh1CHEX0 = 5
    # ToutCh1CHEX0 = 15
    # TinCh2CHEX0 = 17
    # ToutCh2CHEX0 = 7
    # HHEX
    # TinHt1HHEX = 45
    # ToutHt1HHEX = 35
    # TinHt2HHEX = 33
    # ToutHt2HHEX = 43
    # TinHt1HHEX0 = 45
    # ToutHt1HHEX0 = 35
    # TinHt2HHEX0 = 33
    # ToutHt2HHEX0 = 43
    # NHEX
    # TinCn1NHEX = 35
    # ToutCn1NHEX = 30
    # TinCn2NHEX = 28        # 入力値!
    # ToutCn2NHEX = 34
    # TinCn1NHEX0 = 35
    # ToutCn1NHEX0 = 30
    # TinCn2NHEX0 = 28
    # ToutCn2NHEX0 = 34
    # CT
    # global TinCnCT1,TinCnCT2,TinCnCT3
    # global ToutCnCT1,ToutCnCT2,ToutCnCT3
    # global ToutCnCT
    # global TinCnCT10,TinCnCT20,TinCnCT30
    # global ToutCnCT10,ToutCnCT20,ToutCnCT30
    # global ToutCnCT0
    # global ToutVlvCT0,ToutVlvCT
    # TinCnCT1 = 15
    # TinCnCT2 = 15
    # TinCnCT3 = 15
    # ToutCnCT1 = 15
    # ToutCnCT2 = 15
    # ToutCnCT3 = 15
    # ToutCnCT = 15
    # TinCnCT10 = 15
    # TinCnCT20 = 15
    # TinCnCT30 = 15
    # ToutCnCT10 = 15
    # ToutCnCT20 = 15
    # ToutCnCT30 = 15
    # ToutCnCT0 = 15
    # ToutVlvCT0 = 15
    # ToutVlvCT = 0



    # 計測の不確かさ
    # ST
    # global MvTST103, MvTST109, MvTST115, MvTST121, MvTST127, MvTST133, MvTST139, MvTST145, MvTST151, MvTST157
    # global MvTST203, MvTST209, MvTST215, MvTST221, MvTST227, MvTST233, MvTST239, MvTST245, MvTST251, MvTST257
    # global MvTST303, MvTST309, MvTST315, MvTST321, MvTST327, MvTST333, MvTST339, MvTST345, MvTST351, MvTST357
    # MvTST103 = 0
    # MvTST109 = 0
    # MvTST115 = 0
    # MvTST121 = 0
    # MvTST127 = 0
    # MvTST133 = 0
    # MvTST139 = 0
    # MvTST145 = 0
    # MvTST151 = 0
    # MvTST157 = 0
    # MvTST203 = 0
    # MvTST209 = 0
    # MvTST215 = 0
    # MvTST221 = 0
    # MvTST227 = 0
    # MvTST233 = 0
    # MvTST239 = 0
    # MvTST245 = 0
    # MvTST251 = 0
    # MvTST257 = 0
    # MvTST303 = 0
    # MvTST309 = 0
    # MvTST315 = 0
    # MvTST321 = 0
    # MvTST327 = 0
    # MvTST333 = 0
    # MvTST339 = 0
    # MvTST345 = 0
    # MvTST351 = 0
    # MvTST357 = 0
    # global dMvTST103, dMvTST109, dMvTST115, dMvTST121, dMvTST127, dMvTST133, dMvTST139, dMvTST145, dMvTST151, dMvTST157
    # global dMvTST203, dMvTST209, dMvTST215, dMvTST221, dMvTST227, dMvTST233, dMvTST239, dMvTST245, dMvTST251, dMvTST257
    # global dMvTST303, dMvTST309, dMvTST315, dMvTST321, dMvTST327, dMvTST333, dMvTST339, dMvTST345, dMvTST351, dMvTST357
    # dMvTST103 = 0
    # dMvTST109 = 0
    # dMvTST115 = 0
    # dMvTST121 = 0
    # dMvTST127 = 0
    # dMvTST133 = 0
    # dMvTST139 = 0
    # dMvTST145 = 0
    # dMvTST151 = 0
    # dMvTST157 = 0
    # dMvTST203 = 0
    # dMvTST209 = 0
    # dMvTST215 = 0
    # dMvTST221 = 0
    # dMvTST227 = 0
    # dMvTST233 = 0
    # dMvTST239 = 0
    # dMvTST245 = 0
    # dMvTST251 = 0
    # dMvTST257 = 0
    # dMvTST303 = 0
    # dMvTST309 = 0
    # dMvTST315 = 0
    # dMvTST321 = 0
    # dMvTST327 = 0
    # dMvTST333 = 0
    # dMvTST339 = 0
    # dMvTST345 = 0
    # dMvTST351 = 0
    # dMvTST357 = 0

    # TR
    # global MvTinCnTR1,MvToutCnTR1,MvTinChTR1,MvToutChTR1
    # global MvTinCnTR2,MvToutCnTR2,MvTinChTR2,MvToutChTR2
    # global MvTinCnTR3,MvToutCnTR3,MvTinChTR3,MvToutChTR3
    # global MvTinCnTR4,MvToutCnTR4,MvTinChTR4,MvToutChTR4
    # MvTinCnTR1 = 0
    # MvToutCnTR1 = 0
    # MvTinChTR1 = 0
    # MvToutChTR1 = 0
    # MvTinCnTR2 = 0
    # MvToutCnTR2 = 0
    # MvTinChTR2 = 0
    # MvToutChTR2 = 0
    # MvTinCnTR3 = 0
    # MvToutCnTR3 = 0
    # MvTinChTR3 = 0
    # MvToutChTR3 = 0
    # MvTinCnTR4 = 0
    # MvToutCnTR4 = 0
    # MvTinChTR4 = 0
    # MvToutChTR4 = 0
    # global MvTinHtTR1,MvToutHtTR1
    # MvTinHtTR1 = 0
    # MvToutHtTR1 = 0
    # global dMvTinCnTR1,dMvToutCnTR1,dMvTinChTR1,dMvToutChTR1
    # global dMvTinCnTR2,dMvToutCnTR2,dMvTinChTR2,dMvToutChTR2
    # global dMvTinCnTR3,dMvToutCnTR3,dMvTinChTR3,dMvToutChTR3
    # global dMvTinCnTR4,dMvToutCnTR4,dMvTinChTR4,dMvToutChTR4
    # dMvTinCnTR1 = 0
    # dMvToutCnTR1 = 0
    # dMvTinChTR1 = 0
    # dMvToutChTR1 = 0
    # dMvTinCnTR2 = 0
    # dMvToutCnTR2 = 0
    # dMvTinChTR2 = 0
    # dMvToutChTR2 = 0
    # dMvTinCnTR3 = 0
    # dMvToutCnTR3 = 0
    # dMvTinChTR3 = 0
    # dMvToutChTR3 = 0
    # dMvTinCnTR4 = 0
    # dMvToutCnTR4 = 0
    # dMvTinChTR4 = 0
    # dMvToutChTR4 = 0
    # global dMvTinHtTR1,dMvToutHtTR1
    # dMvTinHtTR1 = 0
    # dMvToutHtTR1 = 0
    # HEX,AHU
    # global MvToutCh2CHEX,MvToutCh1CHEX
    # global MvToutCn1NHEX,MvToutCn2NHEX,MvTinCn2NHEX,MvTinCn1NHEX
    # global MvToutHt2HHEX,MvToutHt1HHEX
    # global MvTinChAHU,MvToutChAHU
    # global MvTinHtAHU,MvToutHtAHU
    # MvToutCh2CHEX = 0
    # MvToutCh1CHEX = 0
    # MvToutCn1NHEX = 0
    # MvToutCn2NHEX = 0
    # MvTinCn2NHEX = 0
    # MvTinCn1NHEX = 0
    # MvToutHt2HHEX = 0
    # MvToutHt1HHEX = 0
    # MvTinChAHU = 0
    # MvToutChAHU = 0
    # MvTinHtAHU = 0
    # MvToutHtAHU = 0
    # global dMvToutCh2CHEX,dMvToutCh1CHEX
    # global dMvToutCn1NHEX,dMvToutCn2NHEX,dMvTinCn2NHEX,dMvTinCn1NHEX
    # global dMvToutHt2HHEX,dMvToutHt1HHEX
    # global dMvTinChAHU,dMvToutChAHU
    # global dMvTinHtAHU,dMvToutHtAHU
    # dMvToutCh2CHEX = 0
    # dMvToutCh1CHEX = 0
    # dMvToutCn1NHEX = 0
    # dMvToutCn2NHEX = 0
    # dMvTinCn2NHEX = 0
    # dMvTinCn1NHEX = 0
    # dMvToutHt2HHEX = 0
    # dMvToutHt1HHEX = 0
    # dMvTinChAHU = 0
    # dMvToutChAHU = 0
    # dMvToutHtAHU = 0
    # dMvTinHtAHU = 0

    # CT
    global MvTinCnCT1,MvTinCnCT2,MvTinCnCT3
    global MvToutCnCT1,MvToutCnCT2,MvToutCnCT3
    global MvToutCnCT
    global MvTinCnCT10,MvTinCnCT20,MvTinCnCT30
    global MvToutCnCT10,MvToutCnCT20,MvToutCnCT30
    global MvToutCnCT0
    global MvToutVlvCT0,MvToutVlvCT
    MvTinCnCT1 = 15
    MvTinCnCT2 = 15
    MvTinCnCT3 = 15
    MvToutCnCT1 = 15
    MvToutCnCT2 = 15
    MvToutCnCT3 = 15
    MvToutCnCT = 15
    MvTinCnCT10 = 15
    MvTinCnCT20 = 15
    MvTinCnCT30 = 15
    MvToutCnCT10 = 15
    MvToutCnCT20 = 15
    MvToutCnCT30 = 15
    MvToutCnCT0 = 15
    MvToutVlvCT0 = 15
    MvToutVlvCT = 0
    global dMvTinCnCT1,dMvTinCnCT2,dMvTinCnCT3
    global dMvToutCnCT1,dMvToutCnCT2,dMvToutCnCT3
    global dMvToutCnCT
    global dMvTinCnCT10,dMvTinCnCT20,dMvTinCnCT30
    global dMvToutCnCT10,dMvToutCnCT20,dMvToutCnCT30
    global dMvToutCnCT0
    global dMvToutVlvCT0,dMvToutVlvCT
    dMvTinCnCT1 = 0
    dMvTinCnCT2 = 0
    dMvTinCnCT3 = 0
    dMvToutCnCT1 = 0
    dMvToutCnCT2 = 0
    dMvToutCnCT3 = 0
    dMvToutCnCT = 0
    dMvTinCnCT10 = 0
    dMvTinCnCT20 = 0
    dMvTinCnCT30 = 0
    dMvToutCnCT10 = 0
    dMvToutCnCT20 = 0
    dMvToutCnCT30 = 0
    dMvToutCnCT0 = 0
    dMvToutVlvCT0 = 0
    dMvToutVlvCT = 0

    global fault4
    # if fault4 == 1
    #     dMvToutCh2CHEX = -1.0
    # end












