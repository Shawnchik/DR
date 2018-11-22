def set_variable_picontrol():
    from test import set_var
    # PI制御 ##################################################################
    set_var(('VlvHtAHU','SigGHtAHU'),(1,0))
    # INVCP1
    set_var(('CvINVCP1','SpGCP10','MvGCP10','SigGCP1','INVCP1'),(0,0,0,0,0))
    # INVCP2
    set_var(('CvINVCP2','SpPCP20','MvPCP20','SigPCP2','INVCP2'),(0,0,0,0,0))

    set_var(('SpPChHdr','SpPChHdr0','SigPChHdr','PChHdr','MvPChHdr0'),(0,0,0,0,0))

    set_var(('GCh2CHEX'),0)

    # VlvChAHU
    set_var(('CvVlvChAHU','SpGChAHU0','MvGChAHU0','SigGChAHU','VlvChAHU'),(1,0,0,0,1))
    # VlvCP2
    set_var(('CvVlvCP2','VlvCP2'),(0,0))
    # INVSCP1
    set_var(('CvINVSCP1','SpGSCP10','MvGSCP10','SigGSCP1','INVSCP1'),(0,0,0,0,0))
    # INVSCP2
    set_var(('CvINVSCP2','SpGSCP20','MvGSCP20','SigGSCP2','INVSCP2'),(0,0,0,0,0))
    # INVSCP3
    set_var(('CvINVSCP3','SpGSCP30','MvGSCP30','SigGSCP3','INVSCP3'),(0,0,0,0,0))
    # VlvCh1CHEX
    set_var(('CvVlvCh1CHEX','SpToutCh2CHEX0','MvToutCh2CHEX0','SigToutCh2CHEX','VlvCh1CHEX'),(0,7,0,0,0))
    # INVSCP4
    set_var(('CvINVSCP4','INVSCP4'),(0,0))
    # VlvSCP4
    set_var(('CvVlvSCP4','VlvSCP4'),(0,0))
    # INVCDP1,2,3,4
    set_var(('CvINVCDP1','SpGCDP10','MvGCDP10','SigGCDP1','INVCDP1'), (0, 0, 0, 0, 0))
    set_var(('CvINVCDP2','SpGCDP20','MvGCDP20','SigGCDP2','INVCDP2'), (0, 0, 0, 0, 0))
    set_var(('CvINVCDP3','SpGCDP30','MvGCDP30','SigGCDP3','INVCDP3'), (0, 0, 0, 0, 0))
    set_var(('CvINVCDP4','SpGCDP40','MvGCDP40','SigGCDP4','INVCDP4'), (0, 0, 0, 0, 0))
    # INVNP
    set_var(('CvINVNP','SpToutCn1NHEX0','MvToutCn1NHEX0','SigToutCn1NHEX','INVNP'),(0, 0, 0, 0, 0))

    # VlvHtAHU     # INVSHP1
    set_var(('CvVlvHtAHU','SpGHtAHU0','MvGHtAHU0','MvGHtAHU','CvINVSHP1','SpGSHP10','MvGSHP10','SigGSHP1','INVSHP1'),\
            (1,0,0,0,0,0,0,0,0))
    set_var(('GHtAHU','GHtAHU0'),(0,0))


    # INVHP1
    set_var(('CvINVHP1', 'PHP1', 'SpPHP10', 'MvPHP10', 'SigPHP1', 'INVHP10', 'INVHP1', 'SpPHtHdr', 'SpPHtHdr0', 'SigPHtHdr'),\
            (0,0,0,0,0,0,0,50,50,0))
    # VlvHP1
    set_var(('MvPHtHdr', 'MvPHtHdr0', 'CvVlvHP1', 'VlvHP1','GHt2HHEX'),(0,0,0,0,0))

    # VlvHt1HHEX
    set_var(('CvVlvHt1HHEX','SpToutHt2HHEX0','MvToutHt2HHEX0','SigToutHt2HHEX','VlvHt1HHEX'),(0,43,43,0,0))

    # INVSHP2  # VlvSHP2
    set_var(('CvINVSHP2','INVSHP2','CvVlvSHP2','VlvSHP2'),(0,0,0,0))

    # VlvCT
    set_var(('Tv1VlvCT','SpToutVlvCT0','MvToutVlvCT0','SigToutVlvCT','SpToutVlvCT','MvToutVlvCT','CvVlvCT'),\
            (0,10,10,0,10,10,0))

    # 制御性PF 初期値設定
    set_var(('PFINVCDP1','PFINVCDP2','PFINVCDP3','PFINVCDP4','PFVlvCP2','PFINVCP2','PFINVCP1','PFINVNP'),\
            (0,0,0,0,0,0,0,0))
    set_var(('PFINVSCP1','PFINVSCP2','PFINVSCP3','PFINVSCP4','PFVlvCh1CHEX','PFVlvSCP4'),(0,0,0,0,0,0))
    set_var(('PFVlvChAHU','PFVlvHtAHU','PFINVSHP1','PFINVSHP2','PFVlvSHP2'),(0,0,0,0,0))
    set_var(('PFVlvHt1HHEX','PFVlvHP1','PFINVHP1','PFVlvCT'),(0,0,0,0))

    # INVCP1
    # CvINVCP1 = 0
    # SpGCP10 = 0
    # MvGCP10 = 0
    # SigGCP1 = 0
    # INVCP1 = 0

    # INVCP2
    # CvINVCP2 = 0
    # SpPCP20 = 0
    # MvPCP20 = 0
    # SigPCP2 = 0
    # INVCP2 = 0

    # SpPChHdr = 0
    # SpPChHdr0 = 0
    # SigPChHdr = 0
    # PChHdr = 0
    # MvPChHdr0 = 0

    # global GCh2CHEX
    # GCh2CHEX = 0

    # VlvCP2
    # CvVlvCP2 = 0
    # # SpPCP20 = 0
    # # MvPCP20 = 0
    # # SigPCP2 = 0
    # VlvCP2 = 0

    # VlvChAHU
    # CvVlvChAHU = 1
    # SpGChAHU0 = 0
    # MvGChAHU0 = 0
    # SigGChAHU = 0
    # VlvChAHU = 1

    # INVSCP1
    # CvINVSCP1 = 0
    # SpGSCP10 = 0
    # MvGSCP10 = 0
    # SigGSCP1 = 0
    # INVSCP1 = 0

    # INVSCP2
    # CvINVSCP2 = 0
    # SpGSCP20 = 0
    # MvGSCP20 = 0
    # SigGSCP2 = 0
    # INVSCP2 = 0

    # INVSCP3
    # CvINVSCP3 = 0
    # SpGSCP30 = 0
    # MvGSCP30 = 0
    # SigGSCP3 = 0
    # INVSCP3 = 0

    # VlvCh1CHEX
    # CvVlvCh1CHEX = 0
    # SpToutCh2CHEX0 = 7
    # MvToutCh2CHEX0 = 0
    # SigToutCh2CHEX = 0
    # VlvCh1CHEX = 0

    # INVSCP4
    # CvINVSCP4 = 0
    # # SpToutCh2CHEX0 = 0
    # # MvToutCh2CHEX0 = 0
    # # SigToutCh2CHEX = 0
    # INVSCP4 = 0

    # VlvSCP4
    # CvVlvSCP4 = 0
    # # SpToutCh2CHEX0 = 0
    # # MvToutCh2CHEX0 = 0
    # # SigToutCh2CHEX = 0
    # VlvSCP4 = 0

    # INVCDP1
    # CvINVCDP1 = 0
    # SpGCDP10 = 0
    # MvGCDP10 = 0
    # SigGCDP1 = 0
    # INVCDP1 = 0

    # INVCDP2
    # CvINVCDP2 = 0
    # SpGCDP20 = 0
    # MvGCDP20 = 0
    # SigGCDP2 = 0
    # INVCDP2 = 0

    # INVCDP3
    # CvINVCDP3 = 0
    # SpGCDP30 = 0
    # MvGCDP30 = 0
    # SigGCDP3 = 0
    # INVCDP3 = 0

    # INVCDP4
    # CvINVCDP4 = 0
    # SpGCDP40 = 0
    # MvGCDP40 = 0
    # SigGCDP4 = 0
    # INVCDP4 = 0

    # INVNP
    # CvINVNP = 0
    # SpToutCn1NHEX0 = 0
    # MvToutCn1NHEX0 = 0
    # SigToutCn1NHEX = 0
    # INVNP = 0

    # # VlvHtAHU
    # global CvVlvHtAHU,SpGHtAHU0,MvGHtAHU0,MvGHtAHU,CvINVSHP1,SpGSHP10,MvGSHP10,SigGSHP1,INVSHP1
    # global GHtAHU,GHtAHU0
    # CvVlvHtAHU = 1
    # SpGHtAHU0 = 0
    # MvGHtAHU0 = 0
    # MvGHtAHU = 0
    # SigGHtAHU = 0
    # VlvHtAHU = 1
    # GHtAHU = 0
    # GHtAHU0 = 0
    #
    # # INVSHP1
    # CvINVSHP1 = 0
    # SpGSHP10 = 0
    # MvGSHP10 = 0
    # SigGSHP1 = 0
    # INVSHP1 = 0

    # global CvINVHP1,PHP1,SpPHP10,MvPHP10,SigPHP1,INVHP10,INVHP1,SpPHtHdr,SpPHtHdr0,SigPHtHdr
    # global MvPHtHdr,MvPHtHdr0,CvVlvHP1,VlvHP1
    # # INVHP1
    # CvINVHP1 = 0
    # PHP1 = 0
    # SpPHP10 = 0
    # MvPHP10 = 0
    # SigPHP1 = 0
    # INVHP10 = 0
    # INVHP1 = 0
    # SpPHtHdr = 50
    # SpPHtHdr0 = 50
    # SigPHtHdr = 0
    # MvPHtHdr = 0
    # MvPHtHdr0 = 0
    #
    # global GHt2HHEX
    # GHt2HHEX = 0
    # # VlvHP1
    # CvVlvHP1 = 0
    # VlvHP1 = 0


    # global CvVlvHt1HHEX,SpToutHt2HHEX0,MvToutHt2HHEX0,SigToutHt2HHEX,VlvHt1HHEX
    # global CvINVSHP2,INVSHP2,CvVlvSHP2,VlvSHP2
    # # VlvHt1HHEX
    # CvVlvHt1HHEX = 0
    # SpToutHt2HHEX0 = 43
    # MvToutHt2HHEX0 = 43
    # SigToutHt2HHEX = 0
    # VlvHt1HHEX = 0
    # # INVSHP2
    # CvINVSHP2 = 0
    # INVSHP2 = 0
    # # VlvSHP2
    # CvVlvSHP2 = 0
    # VlvSHP2 = 0

    # # VlvCT
    # global Tv1VlvCT,SpToutVlvCT0,MvToutVlvCT0,SigToutVlvCT,SpToutVlvCT,MvToutVlvCT,CvVlvCT
    # Tv1VlvCT = 0
    # SpToutVlvCT0 = 10
    # MvToutVlvCT0 = 10
    # SigToutVlvCT = 0
    # SpToutVlvCT = 10
    # MvToutVlvCT = 10
    # CvVlvCT = 0


    # # 制御性PF
    # global PFINVCDP1,PFINVCDP2,PFINVCDP3,PFINVCDP4,PFVlvCP2,PFINVCP2,PFINVCP1,PFINVNP
    # global PFINVSCP1,PFINVSCP2,PFINVSCP3,PFINVSCP4,PFVlvCh1CHEX,PFVlvSCP4
    # global PFVlvChAHU,PFVlvHtAHU,PFINVSHP1,PFINVSHP2,PFVlvSHP2
    # global PFVlvHt1HHEX,PFVlvHP1,PFINVHP1,PFVlvCT
    # # 初期値設定
    # PFINVCDP1 = 0
    # PFINVCDP2 = 0
    # PFINVCDP3 = 0
    # PFINVCDP4 = 0
    # PFVlvCP2 = 0
    # PFINVCP2 = 0
    # PFINVCP1 = 0
    # PFINVNP = 0
    # PFINVSCP1 = 0
    # PFINVSCP2 = 0
    # PFINVSCP3 = 0
    # PFINVSCP4 = 0
    # PFVlvCh1CHEX = 0
    # PFVlvSCP4 = 0
    # PFVlvChAHU = 0
    # PFVlvHtAHU = 0
    # PFINVSHP1 = 0
    # PFINVSHP2 = 0
    # PFVlvSHP2 = 0
    # PFVlvHt1HHEX = 0
    # PFVlvHP1 = 0
    # PFINVHP1 = 0
    # PFVlvCT = 0





