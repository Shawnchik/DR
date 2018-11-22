def temperature():
    # 温度の時刻やりとり
    # Nomenclature
    # ~0        :前時刻

    global TinST1,TinST2,TinST3,ToutST1,ToutST2,ToutST3
    global TinChAHU,ToutChAHU,TinHtAHU,ToutHtAHU
    global TinChTR1,ToutChTR1,TinCnTR1,ToutCnTR1
    global TinChTR2,ToutChTR2,TinCnTR2,ToutCnTR2
    global TinChTR3,ToutChTR3,TinCnTR3,ToutCnTR3
    global TinChTR4,ToutChTR4,TinCnTR4,ToutCnTR4
    global TinCn1NHEX,ToutCn1NHEX,TinCn2NHEX,ToutCn2NHEX
    global TinCh1CHEX,ToutCh1CHEX,TinCh2CHEX,ToutCh2CHEX
    global TinHt1HHEX,ToutHt1HHEX,TinHt2HHEX,ToutHt2HHEX
    global TinST10,TinST20,TinST30,ToutST10,ToutST20,ToutST30,ToutST1230,ToutST123,TinST1230,TinST123
    global TinChAHU0,ToutChAHU0,TinHtAHU0,ToutHtAHU0
    global TinChTR10,ToutChTR10,TinCnTR10,ToutCnTR10
    global TinChTR20,ToutChTR20,TinCnTR20,ToutCnTR20
    global TinChTR30,ToutChTR30,TinCnTR30,ToutCnTR30
    global TinChTR40,ToutChTR40,TinCnTR40,ToutCnTR40
    global TinCn1NHEX0,ToutCn1NHEX0,TinCn2NHEX0,ToutCn2NHEX0
    global TinCh1CHEX0,ToutCh1CHEX0,TinCh2CHEX0,ToutCh2CHEX0
    global TinHt1HHEX0,ToutHt1HHEX0,TinHt2HHEX0,ToutHt2HHEX0
    global TinST120,TinST12,ToutST120,ToutST12,TinHtTR10,TinHtTR1,ToutHtTR10,ToutHtTR1
    global TinCnCT10,TinCnCT20,TinCnCT30,TinCnCT1,TinCnCT2,TinCnCT3
    global ToutCnCT10,ToutCnCT20,ToutCnCT30,ToutCnCT1,ToutCnCT2,ToutCnCT3
    global ToutCnCT0,ToutCnCT
    global ToutVlvCT0,ToutVlvCT

    # ST
    TinST10 = TinST1
    TinST20 = TinST2
    TinST30 = TinST3
    ToutST10 = ToutST1
    ToutST20 = ToutST2
    ToutST30 = ToutST3
    TinST1230 = TinST123
    ToutST1230 = ToutST123
    TinST120 = TinST12
    ToutST120 = ToutST12
    # AHU
    TinChAHU0 = TinChAHU
    ToutChAHU0 = ToutChAHU
    TinHtAHU0 = TinHtAHU
    ToutHtAHU0 = ToutHtAHU
    # TR
    TinChTR10 = TinChTR1
    ToutChTR10 = ToutChTR1
    TinHtTR10 = TinHtTR1
    ToutHtTR10 = ToutHtTR1
    TinCnTR10 = TinCnTR1
    ToutCnTR10 = ToutCnTR1
    TinChTR20 = TinChTR2
    ToutChTR20 = ToutChTR2
    TinCnTR20 = TinCnTR2
    ToutCnTR20 = ToutCnTR2
    TinChTR30 = TinChTR3
    ToutChTR30 = ToutChTR3
    TinCnTR30 = TinCnTR3
    ToutCnTR30 = ToutCnTR3
    TinChTR40 = TinChTR4
    ToutChTR40 = ToutChTR4
    TinCnTR40 = TinCnTR4
    ToutCnTR40 = ToutCnTR4
    # HEX
    TinCn1NHEX0 = TinCn1NHEX
    ToutCn1NHEX0 = ToutCn1NHEX
    TinCn2NHEX0 = TinCn2NHEX
    ToutCn2NHEX0 = ToutCn2NHEX
    TinCh1CHEX0 = TinCh1CHEX
    ToutCh1CHEX0 = ToutCh1CHEX
    TinCh2CHEX0 = TinCh2CHEX
    ToutCh2CHEX0 = ToutCh2CHEX
    TinHt1HHEX0 = TinHt1HHEX
    ToutHt1HHEX0 = ToutHt1HHEX
    TinHt2HHEX0 = TinHt2HHEX
    ToutHt2HHEX0 = ToutHt2HHEX

    # CT
    TinCnCT10 = TinCnCT1
    TinCnCT20 = TinCnCT2
    TinCnCT30 = TinCnCT3
    ToutCnCT10 = ToutCnCT1
    ToutCnCT20 = ToutCnCT2
    ToutCnCT30 = ToutCnCT3
    ToutCnCT0 = ToutCnCT
    ToutVlvCT0 = ToutVlvCT

