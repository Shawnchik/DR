# Generated with SMOP  0.41
from libsmop import *
# smop-master/simulation/Crossover.m

    
@function
def Crossover(gene=None,*args,**kwargs):
    varargin = Crossover.varargin
    nargin = Crossover.nargin

    # GA�ɂ��������
# chromosome    :���F�́BPr��0~10��11�i�K�ł��邽�߁A2�i�@�ł�4���ƂȂ�B
# (����,0,0,0,0)
    
    # �T���v��
    chromosomeA=zeros(16,5)
# smop-master/simulation/Crossover.m:7
    # gene��k��(Pr,34~44��)�̕ϐ��ɂ���crossover���s��
    for k in arange(34,44).reshape(-1):
        # ��1���͏���
        for i in arange(1,16).reshape(-1):
            chromosomeA[i,1]=i
# smop-master/simulation/Crossover.m:14
        # ���8�ʂɂ��āAPr��10�i�@����2�i�@�ɕϊ�
        for i in arange(1,8).reshape(-1):
            # Pr��10�i�@����2�i�@�ɕϊ��B�����B�������Ȃ����������i10��1010�Ȃǁj
            a=str2double(dec2bin(gene(i,k)))
# smop-master/simulation/Crossover.m:20
            for m in arange(4,1,- 1).reshape(-1):
                chromosomeA[i,6 - m]=floor(rem(a,10 ** m) / 10 ** (m - 1))
# smop-master/simulation/Crossover.m:23
        # 8�̐��F�̂��烉���_����4�g��I������_���������邱�ƂŐV����8�g��������
        for i in arange(9,12).reshape(-1):
            # 1�ʂ���8�ʂ܂Ń����_���ɑI��
            a=floor(dot(rand,8) + 1)
# smop-master/simulation/Crossover.m:30
            b=floor(dot(rand,8) + 1)
# smop-master/simulation/Crossover.m:31
            while b == a:

                b=floor(dot(rand,8) + 1)
# smop-master/simulation/Crossover.m:33

            # ��_����
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
        # gene��2�i�@��10�i�@�ɕϊ����đ��
        for i in arange(9,16).reshape(-1):
            gene[i,k]=0
# smop-master/simulation/Crossover.m:48
            for m in arange(4,1,- 1).reshape(-1):
                gene[i,k]=gene(i,k) + dot(chromosomeA(i,6 - m),2 ** (m - 1))
# smop-master/simulation/Crossover.m:50
            # 0����10�܂Ŕ͈͊O�ɂ���ꍇ�͏㉺���l�Ƃ���
            if gene(i,k) < 0:
                gene[i,k]=0
# smop-master/simulation/Crossover.m:55
            else:
                if gene(i,k) > 10:
                    gene[i,k]=10
# smop-master/simulation/Crossover.m:57
    