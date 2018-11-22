# Generated with SMOP  0.41
from libsmop import *
# smop-master/simulation/Crossover.m

    
@function
def Crossover(gene=None,*args,**kwargs):
    varargin = Crossover.varargin
    nargin = Crossover.nargin

    # GAにおける交叉
# chromosome    :染色体。Prは0~10の11段階であるため、2進法では4桁となる。
# (順位,0,0,0,0)
    
    # サンプル
    chromosomeA=zeros(16,5)
# smop-master/simulation/Crossover.m:7
    # geneのk列(Pr,34~44列)の変数についてcrossoverを行う
    for k in arange(34,44).reshape(-1):
        # 第1項は順位
        for i in arange(1,16).reshape(-1):
            chromosomeA[i,1]=i
# smop-master/simulation/Crossover.m:14
        # 上位8位について、Prを10進法から2進法に変換
        for i in arange(1,8).reshape(-1):
            # Prを10進法から2進法に変換。整数。しかしつながった数字（10→1010など）
            a=str2double(dec2bin(gene(i,k)))
# smop-master/simulation/Crossover.m:20
            for m in arange(4,1,- 1).reshape(-1):
                chromosomeA[i,6 - m]=floor(rem(a,10 ** m) / 10 ** (m - 1))
# smop-master/simulation/Crossover.m:23
        # 8つの染色体からランダムに4組を選択し一点交叉をすることで新たに8組生成する
        for i in arange(9,12).reshape(-1):
            # 1位から8位までランダムに選択
            a=floor(dot(rand,8) + 1)
# smop-master/simulation/Crossover.m:30
            b=floor(dot(rand,8) + 1)
# smop-master/simulation/Crossover.m:31
            while b == a:

                b=floor(dot(rand,8) + 1)
# smop-master/simulation/Crossover.m:33

            # 一点交叉
            for m in arange(1,2).reshape(-1):
                chromosomeA[i,1 + m]=chromosomeA(a,1 + m)
# smop-master/simulation/Crossover.m:37
                chromosomeA[i + 4,1 + m]=chromosomeA(b,1 + m)
# smop-master/simulation/Crossover.m:38
            for m in arange(3,4).reshape(-1):
                chromosomeA[i,1 + m]=chromosomeA(b,1 + m)
# smop-master/simulation/Crossover.m:41
                chromosomeA[i + 4,1 + m]=chromosomeA(a,1 + m)
# smop-master/simulation/Crossover.m:42
        # geneに2進法を10進法に変換して代入
        for i in arange(9,16).reshape(-1):
            gene[i,k]=0
# smop-master/simulation/Crossover.m:48
            for m in arange(4,1,- 1).reshape(-1):
                gene[i,k]=gene(i,k) + dot(chromosomeA(i,6 - m),2 ** (m - 1))
# smop-master/simulation/Crossover.m:50
            # 0から10まで範囲外にある場合は上下限値とする
            if gene(i,k) < 0:
                gene[i,k]=0
# smop-master/simulation/Crossover.m:55
            else:
                if gene(i,k) > 10:
                    gene[i,k]=10
# smop-master/simulation/Crossover.m:57
    