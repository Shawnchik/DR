def set_parameters():
    from test import set_var
    # 感度分析のための変数を入力する
    # Nomenclature
    # Pr            :Parameterの値（0~10,11通り）
    global Pr
    global PrPChHdr,PrLFTR1,PrLFTR2,PrLFTR3,PrLFTR4
    global PrGCDP1,PrGCDP2,PrGCDP3,PrGCDP4,PrdTNHEX,PrSpTR4

    # 設定値変更
    # PrPChHdr = -25 + 5 * Pr(1,1)
    # PrLFTR1 = 0.9 + 0.02 * Pr(1,2)
    # PrLFTR2 = 0.9 + 0.02 * Pr(1,3)
    # PrLFTR3 = 0.9 + 0.02* Pr(1,4)
    # PrLFTR4 = 0.9 + 0.02 * Pr(1,5)
    # PrGCDP1 = 0.9 + 0.02 * Pr(1,6)
    # PrGCDP2 = 0.9 + 0.02 * Pr(1,7)
    # PrGCDP3 = 0.9 + 0.02 * Pr(1,8)
    # PrGCDP4 = 0.9 + 0.02 * Pr(1,9)
    # PrdTNHEX = 0.1 * Pr(1,10)
    # PrSpTR4 = 0.5 * Pr(1,11)

    # 基準値
    set_var(('PrPChHdr','PrLFTR1','PrLFTR2','PrLFTR3','PrLFTR4'),(0,1,1,1,1))
    set_var(('PrGCDP1','PrGCDP2','PrGCDP3','PrGCDP4','PrdTNHEX','PrSpTR4'),(1,1,1,1,0,5))



