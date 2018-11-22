def set_variable_flowrate():
    from test import set_var
    # 流量
    # 冷水2次系統
    set_var(('GCh2Ld','GChAHU','GCh2CHEX','GCP1','GCP2','GVlvCP2'),(0,0,0,0,0,0))

    # 冷水1次系統
    set_var(('GCh1CHEX','GSCP4','GVlvSCP4'),(0,0,0))
    set_var(('GSCP1','GSCP2','GSCP3'),(0,0,0))
    set_var(('GST123','GST1','GST2','GST3'),(0,0,0,0))

    # 冷却水系統
    set_var(('GCDP1','GCDP2','GCDP3','GCDP4','GVlvCT'),(0,0,0,0))
    set_var('GCn1NHEX',0)

    # 下水系統
    set_var(('GNP','GCn2NHEX','GSw'),(0,0,0))

    # 温水2次系統
    set_var(('GHt2Ld','GHtAHU','GHt2HHEX','GHP1','GVlvHP1'),(0,0,0,0))

    # 温水1次系統
    set_var(('GHt1HHEX','GSHP2','GVlvSHP2','GSHP1'),(0,0,0,0))

    # 不確かさ
    set_var(('MvGCh2Ld','MvGChAHU','MvGCh2CHEX','MvGCP1','MvGCP2','MvGVlvCP2'),(0,0,0,0,0,0))
    set_var('MvGCh1CHEX',0)
    set_var(('MvGSCP4','MvGVlvSCP4'),(0,0))
    set_var(('MvGSCP1','MvGSCP2','MvGSCP3'),(0,0,0))
    set_var(('MvGST123','MvGST1','MvGST2','MvGST3'),(0,0,0,0))
    set_var(('MvGCDP1','MvGCDP2','MvGCDP3','MvGCDP4'),(0,0,0,0))
    set_var('MvGCn1NHEX',0)
    set_var(('MvGNP','MvGCn2NHEX','MvGSw'),(0,0,0))
    set_var(('MvGHt2Ld','MvGHtAHU','MvGHt2HHEX','MvGHP1','MvGVlvHP1'),(0,0,0,0,0))
    set_var('MvGHt1HHEX',0)
    set_var(('MvGSHP2','MvGVlvSHP2'),(0,0))
    set_var(('MvGSHP1','MvGVlvCT'),(0,0))

    set_var(('dMvGCh2Ld','dMvGChAHU','dMvGCh2CHEX','dMvGCP1','dMvGCP2','dMvGVlvCP2'),(0,0,0,0,0,0))
    set_var('dMvGCh1CHEX',0)
    set_var(('dMvGSCP4','dMvGVlvSCP4'),(0,0))
    set_var(('dMvGSCP1','dMvGSCP2','dMvGSCP3'),(0,0,0))
    set_var(('dMvGST123','dMvGST1','dMvGST2','dMvGST3'),(0,0,0,0))
    set_var(('dMvGCDP1','dMvGCDP2','dMvGCDP3','dMvGCDP4'),(0,0,0,0))
    set_var('dMvGCn1NHEX',0)
    set_var(('dMvGNP','dMvGCn2NHEX','dMvGSw'),(0,0,0))
    set_var(('dMvGHt2Ld','dMvGHtAHU','dMvGHt2HHEX','dMvGHP1','dMvGVlvHP1'),(0,0,0,0,0))
    set_var('dMvGHt1HHEX',0)
    set_var(('dMvGSHP2','dMvGVlvSHP2'),(0,0))
    set_var(('dMvGSHP1','dMvGVlvCT'),(0,0))

