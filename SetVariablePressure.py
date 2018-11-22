def set_variable_pressure():
    from test import set_var
    # 圧力（本来は二次ヘッダー間差圧に関する圧力のみでよい？）
    set_var(('PChHdr','PHtHdr','PCP2','PHP1'),(0,0,0,0))

    # 不確かさ
    set_var(('MvPChHdr','MvPHtHdr','MvPCP1','MvPCP2','MvPHP1'), (0, 0, 0, 0, 0))

    set_var(('dMvPChHdr','dMvPHtHdr','dMvPCP1','dMvPCP2','dMvPHP1'), (0, 0, 0, 0, 0))

    set_var('PCP1',0)

    set_var(('PSCP1','PSCP2','PSCP3','PSCP4'),(0,0,0,0))

    set_var(('PSHP1','PSHP2'),(0,0))

    set_var(('PCDP1','PCDP2','PCDP3','PCDP4'),(0,0,0,0))

    set_var('PNP',0)



