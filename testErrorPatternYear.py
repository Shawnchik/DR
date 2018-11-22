# Generated with SMOP  0.41
from libsmop import *
# smop-master/simulation/testErrorPatternYear.m

    clc
    clear
    # 熱源システムのシミュレーション基準値を求める。誤差なし！！
# Nomenclature
# CalStep       :計算ステップ。ここでは1分
    global CalStep,year,ErrorPattern
    for ErrorPattern in arange(1,1000).reshape(-1):
        ErrorPattern
        # global変数の設定と、変数の初期値設定
        SetVariable
        # 測定の不確かさの発生
        ErrorOccur
        for year in arange(2007,2015).reshape(-1):
            # 日数計算
        # うるう年
            if rem(year,4) == 0:
                yearday=366
# smop-master/simulation/testErrorPatternYear.m:22
            else:
                yearday=365
# smop-master/simulation/testErrorPatternYear.m:25
            # ファイル読み込む
            ReadFilesErrorPattern
            #         # 1年間
#         for CalStep = 0 : yearday * 24 * 60 - 1
            # 1か月＋1週間
            for CalStep in arange(0,dot(dot((7 + 31),24),60) - 1).reshape(-1):
                #             CalStep
                # 入力(冷温モードは入力値)
                Input
                # PIパラメータの設定
                SetPIparameters
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
                # 出力
#             Output
#             OutputMonthlySCOP
                OutputErrorPatternMonth
                # ファイルに書き込む
                WriteFiles
                #     # 熱量に注目
        #     Output2
    
    # WriteFiles2