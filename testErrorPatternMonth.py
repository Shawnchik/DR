# Generated with SMOP  0.41
from libsmop import *
# smop-master/simulation/testErrorPatternMonth.m

    clc
    clear
    # 熱源システムのシミュレーション基準値を求める。誤差なし！！
# Nomenclature
# global ResultMonth
    
    ResultMonth=zeros(4,79)
# smop-master/simulation/testErrorPatternMonth.m:7
    OutputResultMonth=zeros(1000,79)
# smop-master/simulation/testErrorPatternMonth.m:8
    for m in arange(1,250).reshape(-1):
        m
        #     parfor ErrorPattern = 1 : 4
        for ErrorPattern in arange(1,1).reshape(-1):
            ErrorPattern
            SEPMResult=SubErrorPatternMonth
# smop-master/simulation/testErrorPatternMonth.m:18
            for i in arange(1,79).reshape(-1):
                ResultMonth[ErrorPattern,i]=SEPMResult(1,i)
# smop-master/simulation/testErrorPatternMonth.m:21
        for n in arange(dot((m - 1),4) + 1,dot(m,4)).reshape(-1):
            for i in arange(1,79).reshape(-1):
                OutputResultMonth[n,i]=ResultMonth(n - dot((m - 1),4),i)
# smop-master/simulation/testErrorPatternMonth.m:29
        csvwrite(concat(['OutputErrorMonth',num2str(dot(m,4)),'.csv']),OutputResultMonth,0,0)
    