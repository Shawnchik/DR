def output():
    import math
    import numpy as np
    # 値の出力
    global Results
    global CalStep,month,day,hour,minut,SgChSt
    global GCh2Ld,MvTinCn2NHEX,SpToutCn1NHEX
    global GCh2CHEX
    global SpGChAHU,GChAHU,VlvChAHU,SpGCP1
    global INVCP1,GCP1,PCP1,nCP1
    global SpPCP2,INVCP2,GCP2,PCP2,nCP2,NmCP2,VlvCP2,GVlvCP2
    global GCh1CHEX
    global INVSCP1,GSCP1,PSCP1,nSCP1
    global INVSCP2,GSCP2,PSCP2,nSCP2
    global INVSCP3,GSCP3,PSCP3,nSCP3
    global INVSCP4,GSCP4,PSCP4,nSCP4,NmSCP4,VlvSCP4,GVlvSCP4,VlvCh1CHEX
    global GCn1NHEX
    global INVCDP1,GCDP1,PCDP1,nCDP1
    global INVCDP2,GCDP2,PCDP2,nCDP2
    global INVCDP3,GCDP3,PCDP3,nCDP3
    global INVCDP4,GCDP4,PCDP4,nCDP4
    global GCn2NHEX
    global INVNP,GNP,PNP,nNP,NmNP
    global GST1,GST2,GST3
    global TinChAHU,ToutChAHU
    global TinChTR4,ToutChTR4
    global TinCh2CHEX,ToutCh2CHEX,TinCh1CHEX,ToutCh1CHEX
    global TinChTR1,ToutChTR1,TinChTR2,ToutChTR2,TinChTR3,ToutChTR3
    global TinCn1NHEX,ToutCn1NHEX
    global TinCnTR1,ToutCnTR1,TinCnTR2,ToutCnTR2,TinCnTR3,ToutCnTR3,TinCnTR4,ToutCnTR4
    global ToutCn2NHEX
    global TinST1,ToutST1,TST1,QST1,TinST2,ToutST2,TST2,QST2,TinST3,ToutST3,TST3,QST3
    global PwCP1,PwCP2
    global PwSCP1,PwSCP2,PwSCP3,PwSCP4
    global PwCDP1,PwCDP2,PwCDP3,PwCDP4,PwNP
    global PwTR1,PwTR2,PwTR3,PwTR4
    global COPTR1,COPTR2,COPTR3,COPTR4
    global MvToutCh2CHEX
    # ヘッダー間差圧
    global PChHdr,Tv2PChHdr,Tv1PChHdr,dTv2PChHdr
    Tv2PChHdr = Tv1PChHdr * (1 + dTv2PChHdr)

    global SpToutCh2CHEX
    SpTinChAHU = SpToutCh2CHEX
    global SpToutChTR1,SpToutChTR2,SpToutChTR3,SpToutChTR4
    # if SgChSt == 1
    #     SgChSt = 2
    # end

    i = math.floor(CalStep / 10080)
    # Results = [[],[]] done in set_variable_else
    # 二次側
    Results[CalStep - 10080 * i + 1][1] = GChAHU * 60
    Results[CalStep - 10080 * i + 1][2] = SpTinChAHU
    Results[CalStep - 10080 * i + 1][3] = TinChAHU
    Results[CalStep - 10080 * i + 1][4] = ToutChAHU
    Results[CalStep - 10080 * i + 1][5] = (ToutChAHU - TinChAHU) * GChAHU * 60 * pow(10,3) * 4.186 / pow(10,6) #[GJ]
    Results[CalStep - 10080 * i + 1][6] = PChHdr
    Results[CalStep - 10080 * i + 1][7] = MvToutCh2CHEX
    Results[CalStep - 10080 * i + 1][8] = GCh2CHEX * 2 * 60
    Results[CalStep - 10080 * i + 1][9] = INVCP2 * 100
    Results[CalStep - 10080 * i + 1][10] = NmCP2
    Results[CalStep - 10080 * i + 1][11] = GCh1CHEX * 2 * 60
    Results[CalStep - 10080 * i + 1][12] = INVSCP4 * 100
    Results[CalStep - 10080 * i + 1][13] = NmSCP4
    Results[CalStep - 10080 * i + 1][14] = TinCh1CHEX
    Results[CalStep - 10080 * i + 1][15] = ToutCh1CHEX
    # TR1
    Results[CalStep - 10080 * i + 1][16] = TinChTR1
    Results[CalStep - 10080 * i + 1][17] = SpToutChTR1
    Results[CalStep - 10080 * i + 1][18] = ToutChTR1
    Results[CalStep - 10080 * i + 1][19] = GSCP1 * 60
    Results[CalStep - 10080 * i + 1][20] = INVSCP1 * 100
    Results[CalStep - 10080 * i + 1][21] = TinCnTR1
    Results[CalStep - 10080 * i + 1][22] = ToutCnTR1
    Results[CalStep - 10080 * i + 1][23] = GCDP1 * 60
    Results[CalStep - 10080 * i + 1][24] = INVCDP1 * 100
    Results[CalStep - 10080 * i + 1][25] = (TinChTR1 - ToutChTR1) * GSCP1 * 60 * pow(10,3) * 4.186 / pow(10,6) #[GJ]
    Results[CalStep - 10080 * i + 1][26] = (ToutCnTR1 - TinCnTR1) * GCDP1 * 60 * pow(10,3) * 4.186 / pow(10,6) #[GJ]
    Results[CalStep - 10080 * i + 1][27] = COPTR1
    # TR2
    Results[CalStep - 10080 * i + 1][28] = TinChTR2
    Results[CalStep - 10080 * i + 1][29] = SpToutChTR2
    Results[CalStep - 10080 * i + 1][30] = ToutChTR2
    Results[CalStep - 10080 * i + 1][31] = GSCP2 * 60
    Results[CalStep - 10080 * i + 1][32] = INVSCP2 * 100
    Results[CalStep - 10080 * i + 1][33] = TinCnTR2
    Results[CalStep - 10080 * i + 1][34] = ToutCnTR2
    Results[CalStep - 10080 * i + 1][35] = GCDP2 * 60
    Results[CalStep - 10080 * i + 1][36] = INVCDP2 * 100
    Results[CalStep - 10080 * i + 1][37] = (TinChTR2 - ToutChTR2) * GSCP2 * 60 * pow(10,3) * 4.186 / pow(10,6) #[GJ]
    Results[CalStep - 10080 * i + 1][38] = (ToutCnTR2 - TinCnTR2) * GCDP2 * 60 * pow(10,3) * 4.186 / pow(10,6) #[GJ]
    Results[CalStep - 10080 * i + 1][39] = COPTR2
    # TR3
    Results[CalStep - 10080 * i + 1][40] = TinChTR3
    Results[CalStep - 10080 * i + 1][41] = SpToutChTR3
    Results[CalStep - 10080 * i + 1][42] = ToutChTR3
    Results[CalStep - 10080 * i + 1][43] = GSCP3 * 60
    Results[CalStep - 10080 * i + 1][44] = INVSCP3 * 100
    Results[CalStep - 10080 * i + 1][45] = TinCnTR3
    Results[CalStep - 10080 * i + 1][46] = ToutCnTR3
    Results[CalStep - 10080 * i + 1][47] = GCDP3 * 60
    Results[CalStep - 10080 * i + 1][48] = INVCDP3 * 100
    Results[CalStep - 10080 * i + 1][49] = (TinChTR3 - ToutChTR3) * GSCP3 * 60 * pow(10,3) * 4.186 / pow(10,6) #[GJ]
    Results[CalStep - 10080 * i + 1][50] = (ToutCnTR3 - TinCnTR3) * GCDP3 * 60 * pow(10,3) * 4.186 / pow(10,6) #[GJ]
    Results[CalStep - 10080 * i + 1][51] = COPTR3
    # TR4
    Results[CalStep - 10080 * i + 1][52] = TinChTR4
    Results[CalStep - 10080 * i + 1][53] = SpToutChTR4
    Results[CalStep - 10080 * i + 1][54] = ToutChTR4
    Results[CalStep - 10080 * i + 1][55] = GCP1 * 60
    Results[CalStep - 10080 * i + 1][56] = INVCP1 * 100
    Results[CalStep - 10080 * i + 1][57] = TinCnTR4
    Results[CalStep - 10080 * i + 1][58] = ToutCnTR4
    Results[CalStep - 10080 * i + 1][59] = GCDP4 * 60
    Results[CalStep - 10080 * i + 1][60] = INVCDP4 * 100
    Results[CalStep - 10080 * i + 1][61] = (TinChTR4 - ToutChTR4) * GCP1 * 60 * pow(10,3) * 4.186 / pow(10,6) #[GJ]
    Results[CalStep - 10080 * i + 1][62] = (ToutCnTR4 - TinCnTR4) * GCDP4 * 60 * pow(10,3) * 4.186 / pow(10,6) #[GJ]
    Results[CalStep - 10080 * i + 1][63] = COPTR4
    # 蓄熱槽温度
    Results[CalStep - 10080 * i + 1][64] = TST1[3]
    Results[CalStep - 10080 * i + 1][65] = TST1[8]
    Results[CalStep - 10080 * i + 1][66] = TST1[13]
    Results[CalStep - 10080 * i + 1][67] = TST1[18]
    Results[CalStep - 10080 * i + 1][68] = TST1[23]
    Results[CalStep - 10080 * i + 1][69] = TST1[28]
    Results[CalStep - 10080 * i + 1][70] = TST1[33]
    Results[CalStep - 10080 * i + 1][71] = TST1[38]
    Results[CalStep - 10080 * i + 1][72] = TST1[43]
    Results[CalStep - 10080 * i + 1][73] = TST1[48]
    Results[CalStep - 10080 * i + 1][74] = TST1[53]
    Results[CalStep - 10080 * i + 1][75] = TST1[58]
    Results[CalStep - 10080 * i + 1][76] = TST2[3]
    Results[CalStep - 10080 * i + 1][77] = TST2[8]
    Results[CalStep - 10080 * i + 1][78] = TST2[13]
    Results[CalStep - 10080 * i + 1][79] = TST2[18]
    Results[CalStep - 10080 * i + 1][80] = TST2[23]
    Results[CalStep - 10080 * i + 1][81] = TST2[28]
    Results[CalStep - 10080 * i + 1][82] = TST2[33]
    Results[CalStep - 10080 * i + 1][83] = TST2[38]
    Results[CalStep - 10080 * i + 1][84] = TST2[43]
    Results[CalStep - 10080 * i + 1][85] = TST2[48]
    Results[CalStep - 10080 * i + 1][86] = TST2[53]
    Results[CalStep - 10080 * i + 1][87] = TST2[58]
    Results[CalStep - 10080 * i + 1][88] = TST3[3]
    Results[CalStep - 10080 * i + 1][89] = TST3[8]
    Results[CalStep - 10080 * i + 1][90] = TST3[13]
    Results[CalStep - 10080 * i + 1][91] = TST3[18]
    Results[CalStep - 10080 * i + 1][92] = TST3[23]
    Results[CalStep - 10080 * i + 1][93] = TST3[28]
    Results[CalStep - 10080 * i + 1][94] = TST3[33]
    Results[CalStep - 10080 * i + 1][95] = TST3[38]
    Results[CalStep - 10080 * i + 1][96] = TST3[43]
    Results[CalStep - 10080 * i + 1][97] = TST3[48]
    Results[CalStep - 10080 * i + 1][98] = TST3[53]
    Results[CalStep - 10080 * i + 1][99] = TST3[58]
    # 下水熱交換器
    Results[CalStep - 10080 * i + 1][100] = SpToutCn1NHEX
    Results[CalStep - 10080 * i + 1][101] = ToutCn1NHEX
    Results[CalStep - 10080 * i + 1][102] = MvTinCn2NHEX
    Results[CalStep - 10080 * i + 1][103] = INVNP * 100
    Results[CalStep - 10080 * i + 1][104] = NmNP
    # 機器消費電力
    Results[CalStep - 10080 * i + 1][105] = PwSCP4 * NmSCP4
    Results[CalStep - 10080 * i + 1][106] = PwCP2 * NmCP2
    Results[CalStep - 10080 * i + 1][107] = PwTR1
    Results[CalStep - 10080 * i + 1][108] = PwTR2
    Results[CalStep - 10080 * i + 1][109] = PwTR3
    Results[CalStep - 10080 * i + 1][110] = PwTR4
    Results[CalStep - 10080 * i + 1][111] = PwSCP1
    Results[CalStep - 10080 * i + 1][112] = PwCDP1
    Results[CalStep - 10080 * i + 1][113] = PwSCP2
    Results[CalStep - 10080 * i + 1][114] = PwCDP2
    Results[CalStep - 10080 * i + 1][115] = PwSCP3
    Results[CalStep - 10080 * i + 1][116] = PwCDP3
    Results[CalStep - 10080 * i + 1][117] = PwCP1
    Results[CalStep - 10080 * i + 1][118] = PwCDP4
    Results[CalStep - 10080 * i + 1][119] = PwNP * NmNP










