# Generated with SMOP  0.41
from libsmop import *
# smop-master/simulation/FitnessfunctionGAPID.m

    
@function
def FitnessfunctionGAPID(i=None,PIDResults=None,*args,**kwargs):
    varargin = FitnessfunctionGAPID.varargin
    nargin = FitnessfunctionGAPID.nargin

    # PIDパラメータ最適化GAのための適応度関数
# global PFINVCDP1 PFINVCDP2 PFINVCDP3 PFINVCDP4 PFVlvCP2 PFINVCP2 PFINVCP1 PFINVNP
# global PFINVSCP1 PFINVSCP2 PFINVSCP3 PFINVSCP4 PFVlvCh1CHEX PFVlvSCP4 PFVlvChAHU
# global PFVlvHtAHU PFINVSHP1 PFINVSHP2 PFVlvSHP2 PFVlvHt1HHEX PFVlvHP1 PFINVHP1 PFVlvCT
    global GCDP1,SpGCDP1,GCDP2,SpGCDP2,GCDP3,SpGCDP3,GCDP4,SpGCDP4
    global PChHdr,SpPChHdr,GCP1,SpGCP1,ToutCn1NHEX,GCn1NHEX,SpToutCn1NHEX
    global GSCP1,SpGSCP1,GSCP2,SpGSCP2,GSCP3,SpGSCP3,GChAHU,SpGChAHU
    global SgChSt,ToutCh2CHEX,SpToutCh2CHEX,FlgFlgVlvCP2,FlgFlgINVSCP4,FlgFlgVlvSCP4
    global CalStep
    global FlgFlgVlvHP1,SpPHtHdr,PHtHdr,SpGSHP1,GSHP1
    global SgHtSt,FlgFlgINVSHP2,SpToutHt2HHEX,ToutHt2HHEX,FlgFlgVlvSHP2
    global SpGHtAHU,GHtAHU
    global FlgFlgVlvCT,SpToutVlvCT,ToutVlvCT
    global KpINVCDP1,TiINVCDP1,KpINVCDP2,TiINVCDP2,KpINVCDP3,TiINVCDP3,KpINVCDP4,TiINVCDP4
    global KpVlvCP2,TiVlvCP2,KpINVCP2,TiINVCP2,KpINVCP1,TiINVCP1,KpINVNP,TiINVNP
    global KpINVSCP1,TiINVSCP1,KpINVSCP2,TiINVSCP2,KpINVSCP3,TiINVSCP3,KpVlvCh1CHEX,TiVlvCh1CHEX
    global KpVlvSCP4,TiVlvSCP4,KpINVSCP4,TiINVSCP4,KpVlvChAHU,TiVlvChAHU
    global KpVlvHtAHU,TiVlvHtAHU,KpINVSHP1,TiINVSHP1,KpINVSHP2,TiINVSHP2,KpVlvSHP2,TiVlvSHP2,KpVlvHt1HHEX
    global TiVlvHt1HHEX,KpVlvHP1,TiVlvHP1,KpINVHP1,TiINVHP1,KpVlvCT,TiVlvCT
    global GCh2CHEX,GHt2HHEX
    global PFINVCDP1,PFINVCDP2,PFINVCDP3,PFINVCDP4,PFVlvCP2,PFINVCP2,PFINVCP1,PFINVNP
    global PFINVSCP1,PFINVSCP2,PFINVSCP3,PFINVSCP4,PFVlvCh1CHEX,PFVlvSCP4
    global PFVlvChAHU,PFVlvHtAHU,PFINVSHP1,PFINVSHP2,PFVlvSHP2
    global PFVlvHt1HHEX,PFVlvHP1,PFINVHP1,PFVlvCT
    KpINVCDP1=PIDResults(i,3)
# smop-master/simulation/FitnessfunctionGAPID.m:27
    TiINVCDP1=PIDResults(i,4)
# smop-master/simulation/FitnessfunctionGAPID.m:28
    KpINVCDP2=PIDResults(i,6)
# smop-master/simulation/FitnessfunctionGAPID.m:29
    TiINVCDP2=PIDResults(i,7)
# smop-master/simulation/FitnessfunctionGAPID.m:30
    KpINVCDP3=PIDResults(i,9)
# smop-master/simulation/FitnessfunctionGAPID.m:31
    TiINVCDP3=PIDResults(i,10)
# smop-master/simulation/FitnessfunctionGAPID.m:32
    KpINVCDP4=PIDResults(i,12)
# smop-master/simulation/FitnessfunctionGAPID.m:33
    TiINVCDP4=PIDResults(i,13)
# smop-master/simulation/FitnessfunctionGAPID.m:34
    KpVlvCP2=PIDResults(i,15)
# smop-master/simulation/FitnessfunctionGAPID.m:35
    TiVlvCP2=PIDResults(i,16)
# smop-master/simulation/FitnessfunctionGAPID.m:36
    KpINVCP2=PIDResults(i,18)
# smop-master/simulation/FitnessfunctionGAPID.m:37
    TiINVCP2=PIDResults(i,19)
# smop-master/simulation/FitnessfunctionGAPID.m:38
    KpINVCP1=PIDResults(i,21)
# smop-master/simulation/FitnessfunctionGAPID.m:39
    TiINVCP1=PIDResults(i,22)
# smop-master/simulation/FitnessfunctionGAPID.m:40
    KpINVNP=PIDResults(i,24)
# smop-master/simulation/FitnessfunctionGAPID.m:41
    TiINVNP=PIDResults(i,25)
# smop-master/simulation/FitnessfunctionGAPID.m:42
    KpINVSCP1=PIDResults(i,27)
# smop-master/simulation/FitnessfunctionGAPID.m:43
    TiINVSCP1=PIDResults(i,28)
# smop-master/simulation/FitnessfunctionGAPID.m:44
    KpINVSCP2=PIDResults(i,30)
# smop-master/simulation/FitnessfunctionGAPID.m:45
    TiINVSCP2=PIDResults(i,31)
# smop-master/simulation/FitnessfunctionGAPID.m:46
    KpINVSCP3=PIDResults(i,33)
# smop-master/simulation/FitnessfunctionGAPID.m:47
    TiINVSCP3=PIDResults(i,34)
# smop-master/simulation/FitnessfunctionGAPID.m:48
    KpINVSCP4=PIDResults(i,36)
# smop-master/simulation/FitnessfunctionGAPID.m:49
    TiINVSCP4=PIDResults(i,37)
# smop-master/simulation/FitnessfunctionGAPID.m:50
    KpVlvCh1CHEX=PIDResults(i,39)
# smop-master/simulation/FitnessfunctionGAPID.m:51
    TiVlvCh1CHEX=PIDResults(i,40)
# smop-master/simulation/FitnessfunctionGAPID.m:52
    KpVlvSCP4=PIDResults(i,42)
# smop-master/simulation/FitnessfunctionGAPID.m:53
    TiVlvSCP4=PIDResults(i,43)
# smop-master/simulation/FitnessfunctionGAPID.m:54
    KpVlvChAHU=PIDResults(i,45)
# smop-master/simulation/FitnessfunctionGAPID.m:55
    TiVlvChAHU=PIDResults(i,46)
# smop-master/simulation/FitnessfunctionGAPID.m:56
    KpVlvHtAHU=PIDResults(i,48)
# smop-master/simulation/FitnessfunctionGAPID.m:57
    TiVlvHtAHU=PIDResults(i,49)
# smop-master/simulation/FitnessfunctionGAPID.m:58
    KpINVSHP1=PIDResults(i,51)
# smop-master/simulation/FitnessfunctionGAPID.m:59
    TiINVSHP1=PIDResults(i,52)
# smop-master/simulation/FitnessfunctionGAPID.m:60
    KpINVSHP2=PIDResults(i,54)
# smop-master/simulation/FitnessfunctionGAPID.m:61
    TiINVSHP2=PIDResults(i,55)
# smop-master/simulation/FitnessfunctionGAPID.m:62
    KpVlvSHP2=PIDResults(i,57)
# smop-master/simulation/FitnessfunctionGAPID.m:63
    TiVlvSHP2=PIDResults(i,58)
# smop-master/simulation/FitnessfunctionGAPID.m:64
    KpVlvHt1HHEX=PIDResults(i,60)
# smop-master/simulation/FitnessfunctionGAPID.m:65
    TiVlvHt1HHEX=PIDResults(i,61)
# smop-master/simulation/FitnessfunctionGAPID.m:66
    KpVlvHP1=PIDResults(i,63)
# smop-master/simulation/FitnessfunctionGAPID.m:67
    TiVlvHP1=PIDResults(i,64)
# smop-master/simulation/FitnessfunctionGAPID.m:68
    KpINVHP1=PIDResults(i,66)
# smop-master/simulation/FitnessfunctionGAPID.m:69
    TiINVHP1=PIDResults(i,67)
# smop-master/simulation/FitnessfunctionGAPID.m:70
    KpVlvCT=PIDResults(i,69)
# smop-master/simulation/FitnessfunctionGAPID.m:71
    TiVlvCT=PIDResults(i,70)
# smop-master/simulation/FitnessfunctionGAPID.m:72
    # 初期値設定
    PFINVCDP1=0
# smop-master/simulation/FitnessfunctionGAPID.m:77
    PFINVCDP2=0
# smop-master/simulation/FitnessfunctionGAPID.m:78
    PFINVCDP3=0
# smop-master/simulation/FitnessfunctionGAPID.m:79
    PFINVCDP4=0
# smop-master/simulation/FitnessfunctionGAPID.m:80
    PFVlvCP2=0
# smop-master/simulation/FitnessfunctionGAPID.m:81
    PFINVCP2=0
# smop-master/simulation/FitnessfunctionGAPID.m:82
    PFINVCP1=0
# smop-master/simulation/FitnessfunctionGAPID.m:83
    PFINVNP=0
# smop-master/simulation/FitnessfunctionGAPID.m:84
    PFINVSCP1=0
# smop-master/simulation/FitnessfunctionGAPID.m:85
    PFINVSCP2=0
# smop-master/simulation/FitnessfunctionGAPID.m:86
    PFINVSCP3=0
# smop-master/simulation/FitnessfunctionGAPID.m:87
    PFINVSCP4=0
# smop-master/simulation/FitnessfunctionGAPID.m:88
    PFVlvCh1CHEX=0
# smop-master/simulation/FitnessfunctionGAPID.m:89
    PFVlvSCP4=0
# smop-master/simulation/FitnessfunctionGAPID.m:90
    PFVlvChAHU=0
# smop-master/simulation/FitnessfunctionGAPID.m:91
    PFVlvHtAHU=0
# smop-master/simulation/FitnessfunctionGAPID.m:92
    PFINVSHP1=0
# smop-master/simulation/FitnessfunctionGAPID.m:93
    PFINVSHP2=0
# smop-master/simulation/FitnessfunctionGAPID.m:94
    PFVlvSHP2=0
# smop-master/simulation/FitnessfunctionGAPID.m:95
    PFVlvHt1HHEX=0
# smop-master/simulation/FitnessfunctionGAPID.m:96
    PFVlvHP1=0
# smop-master/simulation/FitnessfunctionGAPID.m:97
    PFINVHP1=0
# smop-master/simulation/FitnessfunctionGAPID.m:98
    PFVlvCT=0
# smop-master/simulation/FitnessfunctionGAPID.m:99
    # 初期値の読み込み
    SetVariable
    # ファイル読み込む
    ReadFilesGAPID
    for CalStep in arange(0,10079).reshape(-1):
        #  CalStep = 1:1440 # 1日
#     CalStep
    # 入力(冷温モードは入力値)
        Input
        # 二次システム
        SecondarySystem
        # 一次ポンプシステム
        PrimarySystem
        # 冷却水ポンプシステム
        CondenserSystem
        # 熱の計算
        Heat
        # 消費電力の計算
        Power
        # 適応度関数の計算
#     if SpGCDP1 > 0.5
#         PFINVCDP1 = PFINVCDP1 + abs((GCDP1 - SpGCDP1) / SpGCDP1);
#     end
#     if SpGCDP2 > 0.5
#         PFINVCDP2 = PFINVCDP2 + abs((GCDP2 - SpGCDP2) / SpGCDP2);
#     end
#     if SpGCDP3 > 0.5
#         PFINVCDP3 = PFINVCDP3 + abs((GCDP3 - SpGCDP3) / SpGCDP3);
#     end
#     if SpGCDP4 > 0.5
#         PFINVCDP4 = PFINVCDP4 + abs((GCDP4 - SpGCDP4) / SpGCDP4);
#     end
#     if FlgFlgVlvCP2 == 1
#         if (SpGChAHU > 0.5)&&(SpPChHdr > 0)
#             PFVlvCP2 = PFVlvCP2 + abs((PChHdr - SpPChHdr) / SpPChHdr);
#         end
#     else
#         if (SpGChAHU > 0.5)&&(SpPChHdr > 0)
#             PFINVCP2 = PFINVCP2 + abs((PChHdr - SpPChHdr) / SpPChHdr);
#         end
#     end
#     if SpGCP1 > 0.5
#         PFINVCP1 = PFINVCP1 + abs((GCP1 - SpGCP1) / SpGCP1);
#     end
#     if GCn1NHEX > 0
#         if SpToutCn1NHEX > 0
#             PFINVNP = PFINVNP + abs((ToutCn1NHEX - SpToutCn1NHEX) / SpToutCn1NHEX);
#         end
#     end
#     if SpGSCP1 > 0.5
#         PFINVSCP1 = PFINVSCP1 + abs((GSCP1 - SpGSCP1) / SpGSCP1);
#     end
#     if SpGSCP2 > 0.5
#         PFINVSCP2 = PFINVSCP2 + abs((GSCP2 - SpGSCP2) / SpGSCP2);
#     end
#     if SpGSCP3 > 0.5
#         PFINVSCP3 = PFINVSCP3 + abs((GSCP3 - SpGSCP3) / SpGSCP3);
#     end
#     if (SgChSt == 1)||(SgChSt == 2)
#         if FlgFlgINVSCP4 == 1
#             if (GCh2CHEX > 0.5)&&(SpToutCh2CHEX > 0)
#                 PFINVSCP4 = PFINVSCP4 + abs((ToutCh2CHEX - SpToutCh2CHEX) / SpToutCh2CHEX);
#             end
#         else
#             if (GCh2CHEX > 0.5)&&(SpToutCh2CHEX > 0)
#                 PFVlvCh1CHEX = PFVlvCh1CHEX + abs((ToutCh2CHEX - SpToutCh2CHEX) / SpToutCh2CHEX);
#             end
#         end
#     else
#         if FlgFlgVlvSCP4 == 1
#             if (GCh2CHEX > 0.5)&&(SpToutCh2CHEX > 0)
#                 PFVlvSCP4 = PFVlvSCP4 + abs((ToutCh2CHEX - SpToutCh2CHEX) / SpToutCh2CHEX);
#             end
#         else
#             if (GCh2CHEX > 0.5)&&(SpToutCh2CHEX > 0)
#                 PFINVSCP4 = PFINVSCP4 + abs((ToutCh2CHEX - SpToutCh2CHEX) / SpToutCh2CHEX);
#             end
#         end
#     end
#     if SpGChAHU > 0.5
#         PFVlvChAHU = PFVlvChAHU + abs((GChAHU - SpGChAHU) / SpGChAHU);
#     end
#     
#     if FlgFlgVlvHP1 == 1
#         if (SpGHtAHU > 0.5)&&(SpPHtHdr > 0)
#             PFVlvHP1 = PFVlvHP1 + abs((PHtHdr - SpPHtHdr) / SpPHtHdr);
#         end
#     else
#         if (SpGHtAHU > 0.5)&&(SpPHtHdr > 0)
#             PFINVHP1 = PFINVHP1 + abs((PHtHdr - SpPHtHdr) / SpPHtHdr);
#         end
#     end
#     if SpGSHP1 > 0.5
#         PFINVSHP1 = PFINVSHP1 + abs((GSHP1 - SpGSHP1) / SpGSHP1);
#     end
#     if (SgHtSt == 1)||(SgHtSt == 2)
#         if FlgFlgINVSHP2 == 1
#             if (GHt2HHEX > 0)&&(SpToutHt2HHEX > 0)
#                 PFINVSHP2 = PFINVSHP2 + abs((ToutHt2HHEX - SpToutHt2HHEX) / SpToutHt2HHEX);
#             end
#         else
#             if (GHt2HHEX > 0)&&(SpToutHt2HHEX > 0)
#                 PFVlvHt1HHEX = PFVlvHt1HHEX + abs((ToutHt2HHEX - SpToutHt2HHEX) / SpToutHt2HHEX);
#             end
#         end
#     else
#         if FlgFlgVlvSHP2 == 1
#             if (GHt2HHEX > 0)&&(SpToutHt2HHEX > 0)
#                 PFVlvSHP2 = PFVlvSHP2 + abs((ToutHt2HHEX - SpToutHt2HHEX) / SpToutHt2HHEX);
#             end
#         else
#             if (GHt2HHEX > 0)&&(SpToutHt2HHEX > 0)
#                 PFINVSHP2 = PFINVSHP2 + abs((ToutHt2HHEX - SpToutHt2HHEX) / SpToutHt2HHEX);
#             end
#         end
#     end
#     if SpGHtAHU > 0.5
#         PFVlvHtAHU = PFVlvHtAHU + abs((GHtAHU - SpGHtAHU) / SpGHtAHU);
#     end
#     
#     if FlgFlgVlvCT == 1
#         if SpToutVlvCT > 0
#             PFVlvCT = PFVlvCT + abs((ToutVlvCT - SpToutVlvCT) / SpToutVlvCT);
#         end
#     end
    
    # 評価関数の代入
    PIDResults[i,1]=PFINVCDP1 + PFINVCDP2 + PFINVCDP3 + PFINVCDP4 + PFVlvCP2 + PFINVCP2 + PFINVCP1 + PFINVNP + PFINVSCP1 + PFINVSCP2 + PFINVSCP3 + PFINVSCP4 + PFVlvCh1CHEX + PFVlvSCP4 + PFVlvChAHU + PFVlvHtAHU + PFINVSHP1 + PFINVSHP2 + PFVlvSHP2 + PFVlvHt1HHEX + PFVlvHP1 + PFINVHP1 + PFVlvCT
# smop-master/simulation/FitnessfunctionGAPID.m:237
    PIDResults[i,2]=PFINVCDP1
# smop-master/simulation/FitnessfunctionGAPID.m:241
    PIDResults[i,5]=PFINVCDP2
# smop-master/simulation/FitnessfunctionGAPID.m:242
    PIDResults[i,8]=PFINVCDP3
# smop-master/simulation/FitnessfunctionGAPID.m:243
    PIDResults[i,11]=PFINVCDP4
# smop-master/simulation/FitnessfunctionGAPID.m:244
    PIDResults[i,14]=PFVlvCP2
# smop-master/simulation/FitnessfunctionGAPID.m:245
    PIDResults[i,17]=PFINVCP2
# smop-master/simulation/FitnessfunctionGAPID.m:246
    PIDResults[i,20]=PFINVCP1
# smop-master/simulation/FitnessfunctionGAPID.m:247
    PIDResults[i,23]=PFINVNP
# smop-master/simulation/FitnessfunctionGAPID.m:248
    PIDResults[i,26]=PFINVSCP1
# smop-master/simulation/FitnessfunctionGAPID.m:249
    PIDResults[i,29]=PFINVSCP2
# smop-master/simulation/FitnessfunctionGAPID.m:250
    PIDResults[i,32]=PFINVSCP3
# smop-master/simulation/FitnessfunctionGAPID.m:251
    PIDResults[i,35]=PFINVSCP4
# smop-master/simulation/FitnessfunctionGAPID.m:252
    PIDResults[i,38]=PFVlvCh1CHEX
# smop-master/simulation/FitnessfunctionGAPID.m:253
    PIDResults[i,41]=PFVlvSCP4
# smop-master/simulation/FitnessfunctionGAPID.m:254
    PIDResults[i,44]=PFVlvChAHU
# smop-master/simulation/FitnessfunctionGAPID.m:255
    PIDResults[i,47]=PFVlvHtAHU
# smop-master/simulation/FitnessfunctionGAPID.m:256
    PIDResults[i,50]=PFINVSHP1
# smop-master/simulation/FitnessfunctionGAPID.m:257
    PIDResults[i,53]=PFINVSHP2
# smop-master/simulation/FitnessfunctionGAPID.m:258
    PIDResults[i,56]=PFVlvSHP2
# smop-master/simulation/FitnessfunctionGAPID.m:259
    PIDResults[i,59]=PFVlvHt1HHEX
# smop-master/simulation/FitnessfunctionGAPID.m:260
    PIDResults[i,62]=PFVlvHP1
# smop-master/simulation/FitnessfunctionGAPID.m:261
    PIDResults[i,65]=PFINVHP1
# smop-master/simulation/FitnessfunctionGAPID.m:262
    PIDResults[i,68]=PFVlvCT
# smop-master/simulation/FitnessfunctionGAPID.m:263