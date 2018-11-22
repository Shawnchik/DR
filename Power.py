def power():
    import PowerPump
    # 消費電力の計算
    # Nomenclature#####
    # PwCP1     :CP1消費電力[kW]
    # nCP1      :CP1効率(0~1)
    # GCP1      :CP1一台当たり流量[m3/min]
    # PCP1      :CP1吐出圧[kPa]
    # INVCP1    :CP1INV(0~1)

    global PwCP1,nCP1,GCP1,PCP1,INVCP1,d0CP1,d1CP1,d2CP1,d3CP1,d4CP1
    global PwCP2,nCP2,GCP2,PCP2,INVCP2,d0CP2,d1CP2,d2CP2,d3CP2,d4CP2
    global PwSCP1,nSCP1,GSCP1,PSCP1,INVSCP1,d0SCP1,d1SCP1,d2SCP1,d3SCP1,d4SCP1
    global PwSCP2,nSCP2,GSCP2,PSCP2,INVSCP2,d0SCP2,d1SCP2,d2SCP2,d3SCP2,d4SCP2
    global PwSCP3,nSCP3,GSCP3,PSCP3,INVSCP3,d0SCP3,d1SCP3,d2SCP3,d3SCP3,d4SCP3
    global PwSCP4,nSCP4,GSCP4,PSCP4,INVSCP4,d0SCP4,d1SCP4,d2SCP4,d3SCP4,d4SCP4
    global PwHP1,nHP1,GHP1,PHP1,INVHP1,d0HP1,d1HP1,d2HP1,d3HP1,d4HP1
    global PwSHP1,nSHP1,GSHP1,PSHP1,INVSHP1,d0SHP1,d1SHP1,d2SHP1,d3SHP1,d4SHP1
    global PwSHP2,nSHP2,GSHP2,PSHP2,INVSHP2,d0SHP2,d1SHP2,d2SHP2,d3SHP2,d4SHP2
    global PwCDP1,nCDP1,GCDP1,PCDP1,INVCDP1,d0CDP1,d1CDP1,d2CDP1,d3CDP1,d4CDP1
    global PwCDP2,nCDP2,GCDP2,PCDP2,INVCDP2,d0CDP2,d1CDP2,d2CDP2,d3CDP2,d4CDP2
    global PwCDP3,nCDP3,GCDP3,PCDP3,INVCDP3,d0CDP3,d1CDP3,d2CDP3,d3CDP3,d4CDP3
    global PwCDP4,nCDP4,GCDP4,PCDP4,INVCDP4,d0CDP4,d1CDP4,d2CDP4,d3CDP4,d4CDP4
    global PwNP,nNP,GNP,PNP,INVNP,d0NP,d1NP,d2NP,d3NP,d4NP
    global MvPwCP1,dMvPwCP1,Tv1PwCP1,dTv1PwCP1
    global MvPwCP2,dMvPwCP2,Tv1PwCP2,dTv1PwCP2
    global MvPwSCP1,dMvPwSCP1,Tv1PwSCP1,dTv1PwSCP1
    global MvPwSCP2,dMvPwSCP2,Tv1PwSCP2,dTv1PwSCP2
    global MvPwSCP3,dMvPwSCP3,Tv1PwSCP3,dTv1PwSCP3
    global MvPwSCP4,dMvPwSCP4,Tv1PwSCP4,dTv1PwSCP4
    global MvPwCDP1,dMvPwCDP1,Tv1PwCDP1,dTv1PwCDP1
    global MvPwCDP2,dMvPwCDP2,Tv1PwCDP2,dTv1PwCDP2
    global MvPwCDP3,dMvPwCDP3,Tv1PwCDP3,dTv1PwCDP3
    global MvPwCDP4,dMvPwCDP4,Tv1PwCDP4,dTv1PwCDP4
    global MvPwNP,dMvPwNP,Tv1PwNP,dTv1PwNP
    global PwCPAll,PwSCPAll,PwCDPAll,PwNPAll,NmCP2,NmSCP4,NmNP
    global PwHPAll,NmHP1,PwSHPAll,NmSHP2
    global PwTRAll,PwTR1,PwTR2,PwTR3,PwTR4
    global PwFCT1,PwFCT2,PwFCT3,NmFCT1,NmFCT2,NmFCT3
    global PwPmpCT1,PwPmpCT2,PwPmpCT3,NmPmpCT1,NmPmpCT2,NmPmpCT3
    global PwCT
    global MvPwHP1,dMvPwHP1,MvPwSHP1,dMvPwSHP1,MvPwSHP2,dMvPwSHP2
    global MvPwFCT1,dMvPwFCT1,MvPwFCT2,dMvPwFCT2,MvPwFCT3,dMvPwFCT3
    global MvPwPmpCT1,dMvPwPmpCT1,MvPwPmpCT2,dMvPwPmpCT2,MvPwPmpCT3,dMvPwPmpCT3
    global Tv1PwHP1,dTv1PwHP1,Tv1PwSHP1,dTv1PwSHP1,Tv1PwSHP2,dTv1PwSHP2
    global Tv1PwFCT1,dTv1PwFCT1,Tv1PwFCT2,dTv1PwFCT2,Tv1PwFCT3,dTv1PwFCT3
    global Tv1PwPmpCT1,dTv1PwPmpCT1,Tv1PwPmpCT2,dTv1PwPmpCT2,Tv1PwPmpCT3,dTv1PwPmpCT3

    # ポンプ消費電力の計算
    [PwCP1,nCP1] = PowerPump.power_pump(GCP1,PCP1,INVCP1,d0CP1,d1CP1,d2CP1,d3CP1,d4CP1)
    [PwCP2,nCP2] = PowerPump.power_pump(GCP2,PCP2,INVCP2,d0CP2,d1CP2,d2CP2,d3CP2,d4CP2)
    [PwSCP1,nSCP1] = PowerPump.power_pump(GSCP1,PSCP1,INVSCP1,d0SCP1,d1SCP1,d2SCP1,d3SCP1,d4SCP1)
    [PwSCP2,nSCP2] = PowerPump.power_pump(GSCP2,PSCP2,INVSCP2,d0SCP2,d1SCP2,d2SCP2,d3SCP2,d4SCP2)
    [PwSCP3,nSCP3] = PowerPump.power_pump(GSCP3,PSCP3,INVSCP3,d0SCP3,d1SCP3,d2SCP3,d3SCP3,d4SCP3)
    [PwSCP4,nSCP4] = PowerPump.power_pump(GSCP4,PSCP4,INVSCP4,d0SCP4,d1SCP4,d2SCP4,d3SCP4,d4SCP4)
    [PwHP1,nHP1] = PowerPump.power_pump(GHP1,PHP1,INVHP1,d0HP1,d1HP1,d2HP1,d3HP1,d4HP1)
    [PwSHP1,nSHP1] = PowerPump.power_pump(GSHP1,PSHP1,INVSHP1,d0SHP1,d1SHP1,d2SHP1,d3SHP1,d4SHP1)
    [PwSHP2,nSHP2] = PowerPump.power_pump(GSHP2,PSHP2,INVSHP2,d0SHP2,d1SHP2,d2SHP2,d3SHP2,d4SHP2)
    [PwCDP1,nCDP1] = PowerPump.power_pump(GCDP1,PCDP1,INVCDP1,d0CDP1,d1CDP1,d2CDP1,d3CDP1,d4CDP1)
    [PwCDP2,nCDP2] = PowerPump.power_pump(GCDP2,PCDP2,INVCDP2,d0CDP2,d1CDP2,d2CDP2,d3CDP2,d4CDP2)
    [PwCDP3,nCDP3] = PowerPump.power_pump(GCDP3,PCDP3,INVCDP3,d0CDP3,d1CDP3,d2CDP3,d3CDP3,d4CDP3)
    [PwCDP4,nCDP4] = PowerPump.power_pump(GCDP4,PCDP4,INVCDP4,d0CDP4,d1CDP4,d2CDP4,d3CDP4,d4CDP4)
    [PwNP,nNP] = PowerPump.power_pump(GNP,PNP,INVNP,d0NP,d1NP,d2NP,d3NP,d4NP)

    # 冷却塔ファン動力の計算
    PwFCT1 = NmFCT1 * 5.5
    PwFCT2 = NmFCT2 * 5.5
    PwFCT3 = NmFCT3 * 5.5

    # 冷却塔散水ポンプ動力の計算
    PwPmpCT1 = NmPmpCT1 * 2.2
    PwPmpCT2 = NmPmpCT2 * 2.2
    PwPmpCT3 = NmPmpCT3 * 2.2

    # ポンプ消費電力合計
    PwCPAll = PwCP1 + PwCP2 * NmCP2
    PwSCPAll = PwSCP1 + PwSCP2 + PwSCP3 + PwSCP4 * NmSCP4
    PwHPAll = PwHP1 * NmHP1
    PwSHPAll = PwSHP1 + PwSHP2 * NmSHP2
    PwCDPAll = PwCDP1 + PwCDP2 + PwCDP3 + PwCDP4
    PwNPAll = PwNP * NmNP
    PwCT = PwFCT1 + PwFCT2 + PwFCT3 + PwPmpCT1 + PwPmpCT2 + PwPmpCT3
    # 冷凍機消費電力合計
    PwTRAll = PwTR1 + PwTR2 + PwTR3 + PwTR4

    # センサ誤差、DDC誤差
    MvPwCP1 = PwCP1 * (1 + dMvPwCP1)
    MvPwCP2 = PwCP2 * (1 + dMvPwCP2)
    MvPwSCP1 = PwSCP1 * (1 + dMvPwSCP1)
    MvPwSCP2 = PwSCP2 * (1 + dMvPwSCP2)
    MvPwSCP3 = PwSCP3 * (1 + dMvPwSCP3)
    MvPwSCP4 = PwSCP4 * (1 + dMvPwSCP4)
    MvPwCDP1 = PwCDP1 * (1 + dMvPwCDP1)
    MvPwCDP2 = PwCDP2 * (1 + dMvPwCDP2)
    MvPwCDP3 = PwCDP3 * (1 + dMvPwCDP3)
    MvPwCDP4 = PwCDP4 * (1 + dMvPwCDP4)
    MvPwNP = PwNP * (1 + dMvPwNP)
    MvPwHP1 = PwHP1 * (1 + dMvPwHP1)
    MvPwSHP1 = PwSHP1 * (1 + dMvPwSHP1)
    MvPwSHP2 = PwSHP2 * (1 + dMvPwSHP2)
    MvPwFCT1 = PwFCT1 * (1 + dMvPwFCT1)
    MvPwFCT2 = PwFCT2 * (1 + dMvPwFCT2)
    MvPwFCT3 = PwFCT3 * (1 + dMvPwFCT3)
    MvPwPmpCT1 = PwPmpCT1 * (1 + dMvPwPmpCT1)
    MvPwPmpCT2 = PwPmpCT2 * (1 + dMvPwPmpCT2)
    MvPwPmpCT3 = PwPmpCT3 * (1 + dMvPwPmpCT3)
    Tv1PwCP1 = MvPwCP1 + dTv1PwCP1
    Tv1PwCP2 = MvPwCP2 + dTv1PwCP2
    Tv1PwSCP1 = MvPwSCP1 + dTv1PwSCP1
    Tv1PwSCP2 = MvPwSCP2 + dTv1PwSCP2
    Tv1PwSCP3 = MvPwSCP3 + dTv1PwSCP3
    Tv1PwSCP4 = MvPwSCP4 + dTv1PwSCP4
    Tv1PwCDP1 = MvPwCDP1 + dTv1PwCDP1
    Tv1PwCDP2 = MvPwCDP2 + dTv1PwCDP2
    Tv1PwCDP3 = MvPwCDP3 + dTv1PwCDP3
    Tv1PwCDP4 = MvPwCDP4 + dTv1PwCDP4
    Tv1PwNP = MvPwNP + dTv1PwNP
    Tv1PwHP1 = MvPwHP1 + dTv1PwHP1
    Tv1PwSHP1 = MvPwSHP1 + dTv1PwSHP1
    Tv1PwSHP2 = MvPwSHP2 + dTv1PwSHP2
    Tv1PwFCT1 = MvPwFCT1 + dTv1PwFCT1
    Tv1PwFCT2 = MvPwFCT2 + dTv1PwFCT2
    Tv1PwFCT3 = MvPwFCT3 + dTv1PwFCT3
    Tv1PwPmpCT1 = MvPwPmpCT1 + dTv1PwPmpCT1
    Tv1PwPmpCT2 = MvPwPmpCT2 + dTv1PwPmpCT2
    Tv1PwPmpCT3 = MvPwPmpCT3 + dTv1PwPmpCT3

