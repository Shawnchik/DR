def flow_balance_ht2():
    import numpy as np
    import Branch0
    import Branch11
    # 温水二次系統の流量バランス
    # 入力値は各ポンプINVとバルブ開度Vlvである。
    # Nomenclature
    # GHt2HHEX      :熱交換器流量[m3/min]
    # GHtAHU        :AHU流量
    # GHP1          :ポンプ一台当たり流量
    # NmHP1         :ポンプ運転台数
    # INVHP1        :ポンプINV
    # VlvHP1        :ポンプバイパス弁開度(0:全閉,1:全開)
    # VlvHtAHU     :AHU二方弁開度(0:全閉,1:全開)

    global GHt2HHEX,GHtAHU,VlvHtAHU,GHP1,GVlvHP1,NmHP1,INVHP1,VlvHP1,PHP1,PHtHdr
    global KrPpHtAHU,KrHtAHU,c0HP1,c1HP1,c2HP1,c3HP1,c4HP1
    global KrPpHt2HHEX,KrHt2HHEX
    global FlgError11

    # INVが0の時は流量0とする
    if INVHP1 == 0:
        GHt2HHEX = 0
        GHtAHU = 0
        GHP1 = 0
        PHP1 = 0
        GVlvHP1 = 0
        dPHtAHU = 0
    else:
        #  whileに入るための初期値,二分法初期値
        GHtAHU = 0
        GHt2HHEX = 10
        GHtAHUmax = 20
        GHtAHUmin = 0
        GHtAHU00 = np.zeros(10)
        cnt = 0
        while GHt2HHEX * 2 - GHtAHU > 0.01 or GHt2HHEX * 2 - GHtAHU < - 0.01:

            cnt = cnt + 1

            # GHtAHUを仮定する
            GHtAHU = (GHtAHUmax + GHtAHUmin) / 2

            [dPHtAHU] = Branch0. branch0(GHtAHU/2,KrPpHtAHU,0,KrHtAHU,VlvHtAHU,800)

            # GHt2HHEX,GHP1を求める
            [GHt2HHEX,GHP1,GVlvHP1,PHP1] = Branch11.branch11(dPHtAHU,NmHP1,INVHP1,VlvHP1,121,c0HP1,c1HP1,c2HP1,c3HP1,c4HP1,KrPpHt2HHEX,KrHt2HHEX)

            #  各枝の流量が釣り合うまで二分法
            if GHt2HHEX * 2 - GHtAHU > 0:
                GHtAHUmin = GHtAHU
            elif GHt2HHEX * 2 - GHtAHU < 0:
                GHtAHUmax = GHtAHU

            FlgError11 = 0
            # 0.1で収束しない場合
            for i in range(10,2,-1):
                GHtAHU00[i] = GHtAHU00[i-1]
            GHtAHU00[1] = GHtAHU

            if GHtAHU00 == GHtAHU00[1]:
                FlgError11 = GHt2HHEX * 2 - GHtAHU
                break

            if cnt > 30:
                FlgError11 = 1
                break


    # ヘッダ間差圧
    PHtHdr = abs(dPHtAHU)

    # センサ誤差
    global MvGHt2HHEX,dMvGHt2HHEX,MvGHtAHU,dMvGHtAHU,MvGHP1,dMvGHP1,MvPHP1,dMvPHP1
    global Tv1GHt2HHEX,dTv1GHt2HHEX,Tv1GHtAHU,dTv1GHtAHU,Tv1GHP1,dTv1GHP1,Tv1PHP1,dTv1PHP1
    global MvPHtHdr,dMvPHtHdr,Tv1PHtHdr,dTv1PHtHdr
    MvGHt2HHEX = GHt2HHEX * (1 + dMvGHt2HHEX)
    MvGHtAHU = GHtAHU * (1 + dMvGHtAHU)
    MvGHP1 = GHP1 * (1 + dMvGHP1)
    MvPHP1 = PHP1 + dMvPHP1
    Tv1GHt2HHEX = MvGHt2HHEX + dTv1GHt2HHEX
    Tv1GHtAHU = MvGHtAHU + dTv1GHtAHU
    Tv1GHP1 = MvGHP1 + dTv1GHP1
    Tv1PHP1 = MvPHP1 + dTv1PHP1

    MvPHtHdr = PHtHdr + dMvPHtHdr
    Tv1PHtHdr = MvPHtHdr + dTv1PHtHdr



