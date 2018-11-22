def set_variable_uncertainity():
    from test import set_var
    # 通信にかかわる不確かさ
    # 温度
    # 流量
    # ポンプINV周波数
    # 弁開度
    # 消費電力
    # 圧力
    # 熱量

    # Tv1
    # 温度
    # ST
    set_var(('Tv1TST103','Tv1TST109','Tv1TST115','Tv1TST121','Tv1TST127','Tv1TST133','Tv1TST139','Tv1TST145','Tv1TST151','Tv1TST157'),\
            (0,0,0,0,0,0,0,0,0,0))
    set_var(('Tv1TST203','Tv1TST209','Tv1TST215','Tv1TST221','Tv1TST227','Tv1TST233','Tv1TST239','Tv1TST245','Tv1TST251','Tv1TST257'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    set_var(('Tv1TST303','Tv1TST309','Tv1TST315','Tv1TST321','Tv1TST327','Tv1TST333','Tv1TST339','Tv1TST345','Tv1TST351','Tv1TST357'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    set_var(('dTv1TST103','dTv1TST109','dTv1TST115','dTv1TST121','dTv1TST127','dTv1TST133','dTv1TST139','dTv1TST145','dTv1TST151','dTv1TST157'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    set_var(('dTv1TST203','dTv1TST209','dTv1TST215','dTv1TST221','dTv1TST227','dTv1TST233','dTv1TST239','dTv1TST245','dTv1TST251','dTv1TST257'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    set_var(('dTv1TST303','dTv1TST309','dTv1TST315','dTv1TST321','dTv1TST327','dTv1TST333','dTv1TST339','dTv1TST345','dTv1TST351','dTv1TST357'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    # TR
    set_var(('Tv1TinCnTR1','Tv1ToutCnTR1','Tv1TinChTR1','Tv1ToutChTR1'),(0,0,0,0))
    set_var(('Tv1TinCnTR2','Tv1ToutCnTR2','Tv1TinChTR2','Tv1ToutChTR2'),(0,0,0,0))
    set_var(('Tv1TinCnTR3','Tv1ToutCnTR3','Tv1TinChTR3','Tv1ToutChTR3'),(0,0,0,0))
    set_var(('Tv1TinCnTR4','Tv1ToutCnTR4','Tv1TinChTR4','Tv1ToutChTR4'),(0,0,0,0))

    set_var(('Tv1TinHtTR1','Tv1ToutHtTR1'),(0,0))

    set_var(('dTv1TinCnTR1','dTv1ToutCnTR1','dTv1TinChTR1','dTv1ToutChTR1'),(0,0,0,0))
    set_var(('dTv1TinCnTR2','dTv1ToutCnTR2','dTv1TinChTR2','dTv1ToutChTR2'),(0,0,0,0))
    set_var(('dTv1TinCnTR3','dTv1ToutCnTR3','dTv1TinChTR3','dTv1ToutChTR3'),(0,0,0,0))
    set_var(('dTv1TinCnTR4','dTv1ToutCnTR4','dTv1TinChTR4','dTv1ToutChTR4'),(0,0,0,0))

    set_var(('dTv1TinHtTR1','dTv1ToutHtTR1'),(0,0))

    # HEX,AHU
    set_var(('Tv1ToutCh2CHEX','Tv1ToutCh1CHEX'),(0,0))
    set_var(('Tv1ToutCn1NHEX','Tv1TinCn1NHEX','Tv1ToutCn2NHEX','Tv1TinCn2NHEX'),(0,0,0,0))
    set_var(('Tv1ToutHt2HHEX','Tv1ToutHt1HHEX'),(0,0))
    set_var(('Tv1TinChAHU','Tv1ToutChAHU'),(0,0))
    set_var(('Tv1TinHtAHU','Tv1ToutHtAHU'),(0,0))

    set_var(('dTv1ToutCh2CHEX','dTv1ToutCh1CHEX'),(0,0))
    set_var(('dTv1ToutCn1NHEX','dTv1TinCn1NHEX','dTv1ToutCn2NHEX','dTv1TinCn2NHEX'),(0,0,0,0))
    set_var(('dTv1ToutHt2HHEX','dTv1ToutHt1HHEX'),(0,0))
    set_var(('dTv1TinChAHU','dTv1ToutChAHU'),(0,0))
    set_var(('dTv1TinHtAHU','dTv1ToutHtAHU'),(0,0))

    # CT
    set_var(('Tv1TinCnCT1','Tv1TinCnCT2','Tv1TinCnCT3','Tv1ToutCnCT','Tv1ToutVlvCT'),(0,0,0,0,0))
    set_var(('dTv1TinCnCT1','dTv1TinCnCT2','dTv1TinCnCT3','dTv1ToutCnCT','dTv1ToutVlvCT'),(0,0,0,0,0))

    # 流量
    set_var(('Tv1GCh2Ld','Tv1GChAHU','Tv1GCh2CHEX','Tv1GCP1','Tv1GCP2','Tv1GVlvCP2'),(0,0,0,0,0,0))
    set_var('Tv1GCh1CHEX',0)
    set_var(('Tv1GSCP4','Tv1GVlvSCP4'),(0,0))
    set_var(('Tv1GSCP1','Tv1GSCP2','Tv1GSCP3'),(0,0,0))
    set_var(('Tv1GST123','Tv1GST1','Tv1GST2','Tv1GST3'),(0,0,0,0))
    set_var(('Tv1GCDP1','Tv1GCDP2','Tv1GCDP3','Tv1GCDP4'),(0,0,0,0))
    set_var('Tv1GCn1NHEX',0)
    set_var(('Tv1GNP','Tv1GCn2NHEX','Tv1GSw'),(0,0,0))
    set_var(('Tv1GHt2Ld','Tv1GHtAHU','Tv1GHt2HHEX','Tv1GHP1','Tv1GVlvHP1'),(0,0,0,0))
    set_var('Tv1GHt1HHEX',0)
    set_var(('Tv1GSHP2','Tv1GVlvSHP2'),(0,0))
    set_var('Tv1GSHP1',0)
    set_var(('Tv1GCnCT1','Tv1GCnCT2','Tv1GCnCT3','Tv1GVlvCT'),(0,0,0,0))

    set_var(('dTv1GCh2Ld','dTv1GChAHU','dTv1GCh2CHEX','dTv1GCP1','dTv1GCP2','dTv1GVlvCP2'),(0,0,0,0,0,0))
    set_var('dTv1GCh1CHEX',0)
    set_var(('dTv1GSCP4','dTv1GVlvSCP4'),(0,0))
    set_var(('dTv1GSCP1','dTv1GSCP2','dTv1GSCP3'),(0,0,0))
    set_var(('dTv1GST123','dTv1GST1','dTv1GST2','dTv1GST3'),(0,0,0,0))
    set_var(('dTv1GCDP1','dTv1GCDP2','dTv1GCDP3','dTv1GCDP4'),(0,0,0,0))
    set_var('dTv1GCn1NHEX',0)
    set_var(('dTv1GNP','dTv1GCn2NHEX','dTv1GSw'),(0,0,0))
    set_var(('dTv1GHt2Ld','dTv1GHtAHU','dTv1GHt2HHEX','dTv1GHP1','dTv1GVlvHP1'),(0,0,0,0,0))
    set_var('dTv1GHt1HHEX',0)
    set_var(('dTv1GSHP2','dTv1GVlvSHP2'),(0,0))
    set_var('dTv1GSHP1',0)
    set_var(('dTv1GCnCT1','dTv1GCnCT2','dTv1GCnCT3','dTv1GVlvCT'),(0,0,0,0))

    # ポンプINV周波数
    set_var(('Tv1INVCP1','Tv1INVCP2'),(0,0))
    set_var(('Tv1INVSCP1','Tv1INVSCP2','Tv1INVSCP3','Tv1INVSCP4'),(0,0,0,0))
    set_var(('Tv1INVCDP1','Tv1INVCDP2','Tv1INVCDP3','Tv1INVCDP4'),(0,0,0,0))
    set_var('Tv1INVNP',0)
    set_var('Tv1INVHP1',0)
    set_var(('Tv1INVSHP1','Tv1INVSHP2'),(0,0))

    set_var(('dTv1INVCP1','dTv1INVCP2'),(0,0))
    set_var(('dTv1INVSCP1','dTv1INVSCP2','dTv1INVSCP3','dTv1INVSCP4'),(0,0,0,0))
    set_var(('dTv1INVCDP1','dTv1INVCDP2','dTv1INVCDP3','dTv1INVCDP4'),(0,0,0,0))
    set_var('dTv1INVNP',0)
    set_var('dTv1INVHP1',0)
    set_var(('dTv1INVSHP1','dTv1INVSHP2'),(0,0))

    # 弁開度
    set_var(('Tv1VlvChAHU','Tv1VlvHtAHU'),(0,0))
    set_var(('Tv1VlvCP2','Tv1VlvHP1'),(0,0))
    set_var(('Tv1VlvSCP4','Tv1VlvCh1CHEX'),(0,0))
    set_var(('Tv1VlvSHP2','Tv1VlvHt1HHEX','Tv1VlvCT','Tv1VlvCT0'),(0,0,0,0))

    set_var(('dTv1VlvChAHU','dTv1VlvHtAHU'),(0,0))
    set_var(('dTv1VlvCP2','dTv1VlvHP1'),(0,0))
    set_var(('dTv1VlvSCP4','dTv1VlvCh1CHEX'),(0,0))
    set_var(('dTv1VlvSHP2','dTv1VlvHt1HHEX','dTv1VlvCT'),(0,0,0))

    # 消費電力
    set_var(('Tv1PwTR1','Tv1PwTR2','Tv1PwTR3','Tv1PwTR4'),(0,0,0,0))
    set_var(('Tv1PwCP1','Tv1PwCP2'),(0,0))
    set_var(('Tv1PwSCP1','Tv1PwSCP2','Tv1PwSCP3','Tv1PwSCP4'),(0,0,0,0))
    set_var(('Tv1PwCDP1','Tv1PwCDP2','Tv1PwCDP3','Tv1PwCDP4'),(0,0,0,0))
    set_var('Tv1PwNP',0)

    set_var(('dTv1PwTR1','dTv1PwTR2','dTv1PwTR3','dTv1PwTR4'),(0,0,0,0))
    set_var(('dTv1PwCP1','dTv1PwCP2'),(0,0))
    set_var(('dTv1PwSCP1','dTv1PwSCP2','dTv1PwSCP3','dTv1PwSCP4'),(0,0,0,0))
    set_var(('dTv1PwSCP1','dTv1PwSCP2','dTv1PwSCP3','dTv1PwSCP4'),(0,0,0,0))
    set_var(('dTv1PwCDP1','dTv1PwCDP2','dTv1PwCDP3','dTv1PwCDP4'),(0,0,0,0))
    set_var('dTv1PwNP',0)
    set_var(('dTv1PwHP1','dTv1PwSHP1','dTv1PwSHP2'),(0,0,0))
    set_var(('dTv1PwFCT1','dTv1PwFCT2','dTv1PwFCT3','dTv1PwPmpCT1','dTv1PwPmpCT2','dTv1PwPmpCT3'),(0,0,0,0,0,0))

    # 圧力
    set_var(('Tv1PChHdr','Tv1PHtHdr','Tv1PCP2','Tv1PHP1'),(0,0,0,0))

    set_var(('dTv1PChHdr','dTv1PHtHdr','dTv1PCP2','dTv1PHP1'),(0,0,0,0))

    # 熱量
    set_var(('Tv1QST1','Tv1QST2','Tv1QST3'),(100.3,80.37,90.17))

    set_var(('dTv1QST1','dTv1QST2','dTv1QST3'),(0,0,0))

    # Tv2
    # 温度
    # ST
    set_var(('Tv2TST103','Tv2TST109','Tv2TST115','Tv2TST121','Tv2TST127','Tv2TST133','Tv2TST139','Tv2TST145','Tv2TST151','Tv2TST157'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    set_var(('Tv2TST203','Tv2TST209','Tv2TST215','Tv2TST221','Tv2TST227','Tv2TST233','Tv2TST239','Tv2TST245','Tv2TST251','Tv2TST257'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    set_var(('Tv2TST303','Tv2TST309','Tv2TST315','Tv2TST321','Tv2TST327','Tv2TST333','Tv2TST339','Tv2TST345','Tv2TST351','Tv2TST357'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    set_var(('dTv2TST103','dTv2TST109','dTv2TST115','dTv2TST121','dTv2TST127','dTv2TST133','dTv2TST139','dTv2TST145','dTv2TST151','dTv2TST157'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    set_var(('dTv2TST203','dTv2TST209','dTv2TST215','dTv2TST221','dTv2TST227','dTv2TST233','dTv2TST239','dTv2TST245','dTv2TST251','dTv2TST257'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    set_var(('dTv2TST303','dTv2TST309','dTv2TST315','dTv2TST321','dTv2TST327','dTv2TST333','dTv2TST339','dTv2TST345','dTv2TST351','dTv2TST357'), \
            (0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

    # TR
    set_var(('Tv2TinCnTR1','Tv2ToutCnTR1','Tv2TinChTR1','Tv2ToutChTR1'),(0,0,0,0))
    set_var(('Tv2TinCnTR2','Tv2ToutCnTR2','Tv2TinChTR2','Tv2ToutChTR2'),(0,0,0,0))
    set_var(('Tv2ToutCnTR3','Tv2TinChTR3','Tv2ToutChTR3','Tv2TinCnTR3'),(0,0,0,0))
    set_var(('Tv2TinCnTR4','Tv2ToutCnTR4','Tv2TinChTR4','Tv2ToutChTR4'),(0,0,0,0))

    set_var(('Tv2TinHtTR1','Tv2ToutHtTR1'),(0,0))

    set_var(('dTv2TinCnTR1','dTv2ToutCnTR1','dTv2TinChTR1','dTv2ToutChTR1'),(0,0,0,0))
    set_var(('dTv2TinCnTR2','dTv2ToutCnTR2','dTv2TinChTR2','dTv2ToutChTR2'),(0,0,0,0))
    set_var(('dTv2TinCnTR3','dTv2ToutCnTR3','dTv2TinChTR3','dTv2ToutChTR3'),(0,0,0,0))
    set_var(('dTv2TinCnTR4','dTv2ToutCnTR4','dTv2TinChTR4','dTv2ToutChTR4'),(0,0,0,0))

    set_var(('dTv2TinHtTR1','dTv2ToutHtTR1'),(0,0))

    # HEX,AHU
    set_var(('Tv2ToutCh2CHEX','Tv2ToutCh1CHEX'),(0,0))
    set_var(('Tv2ToutCn1NHEX','Tv2ToutCn2NHEX','Tv2TinCn2NHEX'),(0,0,0))
    set_var(('Tv2ToutHt2HHEX','Tv2ToutHt1HHEX'),(0,0))
    set_var(('Tv2TinChAHU','Tv2ToutChAHU'),(0,0))
    set_var(('Tv2TinHtAHU','Tv2ToutHtAHU'),(0,0))

    set_var(('dTv2ToutCh2CHEX','dTv2ToutCh1CHEX'),(0,0))
    set_var(('dTv2ToutCn1NHEX','dTv2ToutCn2NHEX','dTv2TinCn2NHEX'),(0,0,0))
    set_var(('dTv2ToutHt2HHEX','dTv2ToutHt1HHEX'),(0,0))
    set_var(('dTv2TinChAHU','dTv2ToutChAHU'),(0,0))
    set_var(('dTv2TinHtAHU','dTv2ToutHtAHU'),(0,0))

    # 流量
    set_var(('Tv2GCh2Ld','Tv2GChAHU','Tv2GCh2CHEX','Tv2GCP1','Tv2GCP2','Tv2GVlvCP2'),(0,0,0,0,0,0))
    set_var('Tv2GCh1CHEX',0)
    set_var(('Tv2GSCP4','Tv2GVlvSCP4'),(0,0))
    set_var(('Tv2GSCP1','Tv2GSCP2','Tv2GSCP3'),(0,0,0))
    set_var(('Tv2GST123','Tv2GST1','Tv2GST2','Tv2GST3'),(0,0,0,0))
    set_var(('Tv2GCDP1','Tv2GCDP2','Tv2GCDP3','Tv2GCDP4'),(0,0,0,0))
    set_var('Tv2GCn1NHEX',0)
    set_var(('Tv2GNP','Tv2GCn2NHEX','Tv2GSw'),(0,0,0))
    set_var(('Tv2GHt2Ld','Tv2GHtAHU','Tv2GHt2HHEX','Tv2GHP1','Tv2GVlvHP1'),(0,0,0,0,0))
    set_var('Tv2GHt1HHEX',0)
    set_var(('Tv2GSHP2','Tv2GVlvSHP2'),(0,0))
    set_var('Tv2GSHP1',0)

    set_var(('dTv2GCh2Ld','dTv2GChAHU','dTv2GCh2CHEX','dTv2GCP1','dTv2GCP2','dTv2GVlvCP2'),(0,0,0,0,0,0))
    set_var('dTv2GCh1CHEX',0)
    set_var(('dTv2GSCP4','dTv2GVlvSCP4'),(0,0))
    set_var(('dTv2GSCP1','dTv2GSCP2','dTv2GSCP3'),(0,0,0))
    set_var(('dTv2GST123','dTv2GST1','dTv2GST2','dTv2GST3'),(0,0,0,0))
    set_var(('dTv2GCDP1','dTv2GCDP2','dTv2GCDP3','dTv2GCDP4'),(0,0,0,0))
    set_var('dTv2GCn1NHEX',0)
    set_var(('dTv2GNP','dTv2GCn2NHEX','dTv2GSw'),(0,0,0))
    set_var(('dTv2GHt2Ld','dTv2GHtAHU','dTv2GHt2HHEX','dTv2GHP1','dTv2GVlvHP1'),(0,0,0,0,0))
    set_var('dTv2GHt1HHEX',0)
    set_var(('dTv2GSHP2','dTv2GVlvSHP2'),(0,0))
    set_var('dTv2GSHP1',0)

    # ポンプINV周波数
    set_var(('Tv2INVCP1','Tv2INVCP2'),(0,0))
    set_var(('Tv2INVSCP1','Tv2INVSCP2','Tv2INVSCP3','Tv2INVSCP4'),(0,0,0,0))
    set_var(('Tv2INVCDP1','Tv2INVCDP2','Tv2INVCDP3','Tv2INVCDP4'),(0,0,0,0))
    set_var('Tv2INVNP',0)
    set_var('Tv2INVHP1',0)
    set_var(('Tv2INVSHP1','Tv2INVSHP2'),(0,0))

    set_var(('dTv2INVCP1','dTv2INVCP2'),(0,0))
    set_var(('dTv2INVSCP1','dTv2INVSCP2','dTv2INVSCP3','dTv2INVSCP4'),(0,0,0,0))
    set_var(('dTv2INVCDP1','dTv2INVCDP2','dTv2INVCDP3','dTv2INVCDP4'),(0,0,0,0))
    set_var('dTv2INVNP',0)
    set_var('dTv2INVHP1',0)
    set_var(('dTv2INVSHP1','dTv2INVSHP2'),(0,0))

    # 弁開度
    set_var(('Tv2VlvChAHU','Tv2VlvHtAHU'),(0,0))
    set_var(('Tv2VlvCP2','Tv2VlvHP1'),(0,0))
    set_var(('Tv2VlvSCP4','Tv2VlvCh1CHEX'),(0,0))
    set_var(('Tv2VlvSHP2','Tv2VlvHt1HHEX','Tv2VlvCT'),(0,0,0))

    set_var(('dTv2VlvChAHU','dTv2VlvHtAHU'),(0,0))
    set_var(('dTv2VlvCP2','dTv2VlvHP1'),(0,0))
    set_var(('dTv2VlvSCP4','dTv2VlvCh1CHEX'),(0,0))
    set_var(('dTv2VlvSHP2','dTv2VlvHt1HHEX','dTv2VlvCT'),(0,0,0))

    # 消費電力
    set_var(('Tv2PwTR1','Tv2PwTR2','Tv2PwTR3','Tv2PwTR4'),(0,0,0,0))
    set_var(('Tv2PwCP1','Tv2PwCP2'),(0,0))
    set_var(('Tv2PwSCP1','Tv2PwSCP2','Tv2PwSCP3','Tv2PwSCP4'),(0,0,0,0))
    set_var(('Tv2PwCDP1','Tv2PwCDP2','Tv2PwCDP3','Tv2PwCDP4'),(0,0,0,0))
    set_var('Tv2PwNP',0)

    set_var(('dTv2PwTR1','dTv2PwTR2','dTv2PwTR3','dTv2PwTR4'),(0,0,0,0))
    set_var(('dTv2PwCP1','dTv2PwCP2'),(0,0))
    set_var(('dTv2PwSCP1','dTv2PwSCP2','dTv2PwSCP3','dTv2PwSCP4'),(0,0,0,0))
    set_var(('dTv2PwCDP1','dTv2PwCDP2','dTv2PwCDP3','dTv2PwCDP4'),(0,0,0,0))
    set_var('dTv2PwNP',0)

    set_var(('dTv2PwHP1','dTv2PwSHP1','dTv2PwSHP2'),(0,0,0))
    set_var(('dTv2PwFCT1','dTv2PwFCT2','dTv2PwFCT3','dTv2PwPmpCT1','dTv2PwPmpCT2','dTv2PwPmpCT3'),(0,0,0,0,0,0))

    # 圧力
    set_var(('Tv2PChHdr','Tv2PHtHdr','Tv2PCP2','Tv2PHP1'),(0,0,0,0))
    set_var(('dTv2PChHdr','dTv2PHtHdr','dTv2PCP2','dTv2PHP1'),(0,0,0,0))

    # 熱量
    set_var(('Tv2QST1','Tv2QST2','Tv2QST3'),(100.3,80.37,90.17))

    set_var(('dTv2QST1','dTv2QST2','dTv2QST3'),(0,0,0))

