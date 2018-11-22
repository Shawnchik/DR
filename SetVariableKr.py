def set_variable_kr():
    from test import set_var

    # 抵抗係数 ################################################################
    # FlowBalanceCh2
    set_var(('KrPpChAHU', 'KrChAHU', 'KrPpCh2CHEX', 'KrCh2CHEX', 'KrPpChTR4', 'KrChTR4'),\
            (0.0140,0.214,0.0844,4.38,0.143,1.94))
    # FlowBalanceCh1
    set_var(('KrPpST', 'KrPpCh1CHEX', 'KrCh1CHEX', 'KrPpChTR1', 'KrChTR1', 'KrPpChTR2', 'KrChTR2', 'KrPpChTR3', 'KrChTR3'),\
            (0.245,0.0844,11.1,0.236,9.83,0.223,1.94,0.223,1.94))
    # FlowBalanceHt1,2
    set_var(('KrPpHtAHU', 'KrHtAHU','KrPpHt2HHEX','KrHt2HHEX','KrPpHt1HHEX','KrHt1HHEX','KrPpHtTR1','KrHtTR1'),\
            (0.0140,0.214,0.0225,0.858,0.0304,0.858,0.0629,9.83))
    # FlowBalanceCn
    set_var(('KrPpCn1NHEX','KrCn1NHEX','KrPpCnTR1','KrCnTR1','KrPpCnTR2','KrCnTR2','KrPpCnTR3','KrCnTR3','KrPpCnTR4','KrCnTR4'),\
            (0.0281,0.735,0.282,2.57,0.266,0.370,0.266,0.377,0.266,0.355))
    # FlowBalanceSw
    set_var(('KrPpSw','KrPpCn2NHEX','KrCn2NHEX'),(0.191,0.00507,0.2))
    # FlowBalanceCnCT
    set_var(('KrPpCT1','KrCnCT1','KrPpCT2','KrCnCT2','KrPpCT3','KrCnCT3','KrPpVlvCT'),\
            (0.0140,1.189,0.0140,0.528,0.0140,0.528,0.0140))

    set_var(('fault1','fault3'))

    # FlowBalanceCh2
    # KrPpChAHU = 0.0140
    # KrChAHU = 0.214
    # KrPpCh2CHEX = 0.0844
    # KrCh2CHEX = 4.38
    # KrPpChTR4 = 0.143
    # KrChTR4 = 1.94

    # FlowBalanceCh1
    # KrPpST = 0.245
    # KrPpCh1CHEX = 0.0844
    # KrCh1CHEX = 11.1
    # KrPpChTR1 = 0.236
    # KrChTR1 = 9.83
    # KrPpChTR2 = 0.223
    # KrChTR2 = 1.94
    # KrPpChTR3 = 0.223
    # KrChTR3 = 1.94

    # # FlowBalanceHt2
    # KrPpHtAHU = 0.0140
    # KrHtAHU = 0.214
    # KrPpHt2HHEX = 0.0225
    # KrHt2HHEX = 0.858
    # # FlowBalanceHt1
    # KrPpHt1HHEX = 0.0304
    # KrHt1HHEX = 0.858
    # KrPpHtTR1 = 0.0629
    # KrHtTR1 = 9.83

    # FlowBalanceCn
    # KrPpCn1NHEX = 0.0281
    # KrCn1NHEX = 0.735
    # KrPpCnTR1 = 0.282
    # KrCnTR1 = 2.57
    # KrPpCnTR2 = 0.266
    # KrCnTR2 = 0.370
    # KrPpCnTR3 = 0.266
    # KrCnTR3 = 0.377
    # KrPpCnTR4 = 0.266
    # KrCnTR4 = 0.355

    # # FlowBalanceSw
    # # KrPpSw = 0.291
    # KrPpSw = 0.191
    # KrPpCn2NHEX = 0.00507
    # # KrCn2NHEX = 0.735
    # KrCn2NHEX = 0.2

    # FlowBalanceCnCT
    # global KrPpCT1,KrCnCT1,KrPpCT2,KrCnCT2,KrPpCT3,KrCnCT3,KrPpVlvCT
    # KrPpCT1 = 0.0140
    # KrCnCT1 = 1.189
    # KrPpCT2 = 0.0140
    # KrCnCT2 = 0.528
    # KrPpCT3 = 0.0140
    # KrCnCT3 = 0.528
    # KrPpVlvCT = 0.0140

    # if fault1 == 1
    #     KrCnTR1 = KrCnTR1 * 1.2
    #     KrCnTR2 = KrCnTR2 * 1.2
    #     KrCnTR3 = KrCnTR3 * 1.2
    #     KrCnTR4 = KrCnTR4 * 1.2
    # end

    # if fault3 == 1
    #     KrCh1CHEX = KrCh1CHEX * 2
    #     KrCh2CHEX = KrCh2CHEX * 2
    # end