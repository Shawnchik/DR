# Generated with SMOP  0.41
from libsmop import *
# smop-master/simulation/TR_evaluate.m

    clc
    clear
    # BEMSデータに対してTRの性能低下率を算出
    TRs=csvread(concat(['BEMS_2015.csv']),0,0)
# smop-master/simulation/TR_evaluate.m:4
    global fault1
    fault1=0
# smop-master/simulation/TR_evaluate.m:7
    result=zeros(dot(dot(24,4),122),13)
# smop-master/simulation/TR_evaluate.m:9
    for i in arange(1,dot(dot(24,4),122)).reshape(-1):
        # TR1
        TinCh1=TRs(i,16)
# smop-master/simulation/TR_evaluate.m:13
        SpToutCh1=TRs(i,17)
# smop-master/simulation/TR_evaluate.m:14
        GCh1=TRs(i,19) / 60
# smop-master/simulation/TR_evaluate.m:15
        if GCh1 < dot(2.47,0.2):
            GCh1=0
# smop-master/simulation/TR_evaluate.m:17
        TinCn1=TRs(i,21)
# smop-master/simulation/TR_evaluate.m:19
        GCn1=TRs(i,23) / 60
# smop-master/simulation/TR_evaluate.m:20
        TinCh2=TRs(i,28)
# smop-master/simulation/TR_evaluate.m:22
        SpToutCh2=TRs(i,29)
# smop-master/simulation/TR_evaluate.m:23
        GCh2=TRs(i,31) / 60
# smop-master/simulation/TR_evaluate.m:24
        if GCh2 < dot(4.98,0.2):
            GCh2=0
# smop-master/simulation/TR_evaluate.m:26
        TinCn2=TRs(i,33)
# smop-master/simulation/TR_evaluate.m:28
        GCn2=TRs(i,35) / 60
# smop-master/simulation/TR_evaluate.m:29
        TinCh3=TRs(i,40)
# smop-master/simulation/TR_evaluate.m:31
        SpToutCh3=TRs(i,41)
# smop-master/simulation/TR_evaluate.m:32
        GCh3=TRs(i,43) / 60
# smop-master/simulation/TR_evaluate.m:33
        if GCh3 < dot(4.98,0.2):
            GCh3=0
# smop-master/simulation/TR_evaluate.m:35
        TinCn3=TRs(i,45)
# smop-master/simulation/TR_evaluate.m:37
        GCn3=TRs(i,47) / 60
# smop-master/simulation/TR_evaluate.m:38
        TinCh4=TRs(i,52)
# smop-master/simulation/TR_evaluate.m:40
        SpToutCh4=TRs(i,53)
# smop-master/simulation/TR_evaluate.m:41
        GCh4=TRs(i,55) / 60
# smop-master/simulation/TR_evaluate.m:42
        if GCh4 < dot(4.98,0.2):
            GCh4=0
# smop-master/simulation/TR_evaluate.m:44
        TinCn4=TRs(i,57)
# smop-master/simulation/TR_evaluate.m:46
        GCn4=TRs(i,59) / 60
# smop-master/simulation/TR_evaluate.m:47
        ToutCh1,ToutCn1,COP1,Pw1,FlgError1=CalTR1(TinCh1,SpToutCh1,GCh1,TinCn1,GCn1,nargout=5)
# smop-master/simulation/TR_evaluate.m:49
        ToutCh2,ToutCn2,COP2,Pw2,FlgError2=CalTR2(TinCh2,SpToutCh2,GCh2,TinCn2,GCn2,nargout=5)
# smop-master/simulation/TR_evaluate.m:50
        ToutCh3,ToutCn3,COP3,Pw3,FlgError3=CalTR3(TinCh3,SpToutCh3,GCh3,TinCn3,GCn3,nargout=5)
# smop-master/simulation/TR_evaluate.m:51
        ToutCh4,ToutCn4,COP4,Pw4,FlgError4=CalTR4(TinCh4,SpToutCh4,GCh4,TinCn4,GCn4,nargout=5)
# smop-master/simulation/TR_evaluate.m:52
        result[i,1]=COP1
# smop-master/simulation/TR_evaluate.m:53
        result[i,2]=COP2
# smop-master/simulation/TR_evaluate.m:54
        result[i,3]=COP3
# smop-master/simulation/TR_evaluate.m:55
        result[i,4]=COP4
# smop-master/simulation/TR_evaluate.m:56
        result[i,5]=TRs(i,27)
# smop-master/simulation/TR_evaluate.m:57
        result[i,6]=TRs(i,39)
# smop-master/simulation/TR_evaluate.m:58
        result[i,7]=TRs(i,51)
# smop-master/simulation/TR_evaluate.m:59
        result[i,8]=TRs(i,63)
# smop-master/simulation/TR_evaluate.m:60
        if result(i,1) > 0 and result(i,5) > 0:
            result[i,9]=dot((result(i,5) / result(i,1) - 1),100)
# smop-master/simulation/TR_evaluate.m:62
        if result(i,2) > 0 and result(i,6) > 0:
            result[i,10]=dot((result(i,6) / result(i,2) - 1),100)
# smop-master/simulation/TR_evaluate.m:65
        if result(i,3) > 0 and result(i,7) > 0:
            result[i,11]=dot((result(i,7) / result(i,3) - 1),100)
# smop-master/simulation/TR_evaluate.m:68
        if result(i,4) > 0 and result(i,8) > 0:
            result[i,12]=dot((result(i,8) / result(i,4) - 1),100)
# smop-master/simulation/TR_evaluate.m:71
        num=ceil(abs(result(i,9)) / 10000) + ceil(abs(result(i,10)) / 10000) + ceil(abs(result(i,11)) / 10000) + ceil(abs(result(i,12)) / 10000)
# smop-master/simulation/TR_evaluate.m:73
        if num > 0:
            result[i,13]=(result(i,9) + result(i,10) + result(i,11) + result(i,12)) / num
# smop-master/simulation/TR_evaluate.m:75
        else:
            result[i,13]=0
# smop-master/simulation/TR_evaluate.m:77
    
    csvwrite(concat(['TR_evaluate_2015.csv']),result,0,0)