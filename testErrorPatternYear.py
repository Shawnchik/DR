# Generated with SMOP  0.41
from libsmop import *
# smop-master/simulation/testErrorPatternYear.m

    clc
    clear
    # �M���V�X�e���̃V�~�����[�V������l�����߂�B�덷�Ȃ��I�I
# Nomenclature
# CalStep       :�v�Z�X�e�b�v�B�����ł�1��
    global CalStep,year,ErrorPattern
    for ErrorPattern in arange(1,1000).reshape(-1):
        ErrorPattern
        # global�ϐ��̐ݒ�ƁA�ϐ��̏����l�ݒ�
        SetVariable
        # ����̕s�m�����̔���
        ErrorOccur
        for year in arange(2007,2015).reshape(-1):
            # �����v�Z
        # ���邤�N
            if rem(year,4) == 0:
                yearday=366
# smop-master/simulation/testErrorPatternYear.m:22
            else:
                yearday=365
# smop-master/simulation/testErrorPatternYear.m:25
            # �t�@�C���ǂݍ���
            ReadFilesErrorPattern
            #         # 1�N��
#         for CalStep = 0 : yearday * 24 * 60 - 1
            # 1�����{1�T��
            for CalStep in arange(0,dot(dot((7 + 31),24),60) - 1).reshape(-1):
                #             CalStep
                # ����(�≷���[�h�͓��͒l)
                Input
                # PI�p�����[�^�̐ݒ�
                SetPIparameters
                # �񎟃V�X�e��
                SecondarySystem
                # �ꎟ�|���v�V�X�e��
                PrimarySystem
                # ��p���|���v�V�X�e��
                CondenserSystem
                # �M�̌v�Z
                Heat
                # ����d�͂̌v�Z
                Power
                # �o��
#             Output
#             OutputMonthlySCOP
                OutputErrorPatternMonth
                # �t�@�C���ɏ�������
                WriteFiles
                #     # �M�ʂɒ���
        #     Output2
    
    # WriteFiles2