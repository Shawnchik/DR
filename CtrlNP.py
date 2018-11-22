def ctrl_np():
    import CtrlNmNP
    import PID
    # 下水ポンプ台数・INV制御
    # Nomenclature
    # SpToutCn1NHEX     :下水熱交換器一次出口温度設定値['C]（冷却水側出口温度）
    # TinCn2NHEX        :下水熱交換器二次入口温度['C](下水温度、シミュレーションの入力値)
    # GCn1NHEX          :下水熱交換機一次流量[m3/min]（冷却水側流量）
    # WTNmNP            :NP増減台効果待ち時間[minute]
    global INVNP,FlgNmNP,NmNP
    global SpToutCn1NHEX0,SigToutCn1NHEX
    global INVNP0
    global KpINVNP,TiINVNP
    global MvTinCn2NHEX,MvTinCn1NHEX
    global CvINVNP,CvINVNP0,dCvINVNP,Tv1INVNP,dTv1INVNP
    global MvToutCn1NHEX,MvToutCn1NHEX0,MvGCn1NHEX
    global SpToutCn1NHEX
    global FlgPIDINVNP
    global PFINVNP
    global FlgSpToutCn1NHEX,FlgNHEX,FlgFlgSpToutCn1NHEX,fault2
    # # 下水熱交換器一次出口温度設定値
    # if  MvTinCn1NHEX > MvTinCn2NHEX
    #     for i = 60:-1:2
    #         FlgSpToutCn1NHEX(i) = FlgSpToutCn1NHEX(i-1);
    #     end
    #     FlgSpToutCn1NHEX(1) = 1;
    # else
    #     for i = 60:-1:2
    #         FlgSpToutCn1NHEX(i) = FlgSpToutCn1NHEX(i-1);
    #     end
    #     FlgSpToutCn1NHEX(1) = -1;
    # end
    #
    #
    # if FlgFlgSpToutCn1NHEX == -1
    #     if FlgSpToutCn1NHEX == 1
    #         SigToutCn1NHEX = 0;
    #     end
    # elseif FlgFlgSpToutCn1NHEX == 1
    #     if FlgSpToutCn1NHEX == -1
    #         SigToutCn1NHEX = 0;
    #     end
    # end
    #
    # if FlgSpToutCn1NHEX == 1
    #     FlgFlgSpToutCn1NHEX = 1;
    # elseif FlgSpToutCn1NHEX == -1
    #     FlgFlgSpToutCn1NHEX = -1;
    # end
    #
    # if FlgFlgSpToutCn1NHEX == 1
    #     SpToutCn1NHEX = MvTinCn2NHEX + 2;
    #     FlgNHEX = -1;
    # elseif FlgFlgSpToutCn1NHEX == -1
    #     SpToutCn1NHEX = MvTinCn2NHEX - 2;
    #     FlgNHEX = 1;
    # end


    SpToutCn1NHEX = MvTinCn2NHEX + 2.0

    # F2
    # if fault2 == 1
    #     SpToutCn1NHEX = MvTinCn2NHEX + 0.5
    # end


    # 下水ポンプ台数制御
    CtrlNmNP.ctrl_nm_np()

    # ポンプINV制御
    # バイパス弁はなく、INV下限値は設定しない（そもそも小流量にならない、流量を絞ることに意味がない）
    # 目標温度になるようにポンプINVをPI制御
    if MvGCn1NHEX > 0.5:        # この条件重要!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        [CvINVNP,SpToutCn1NHEX0,MvToutCn1NHEX0,SigToutCn1NHEX,FlgPIDINVNP] \
            = PID.pid(1.0,0.001,1,KpINVNP,TiINVNP,0,SpToutCn1NHEX,SpToutCn1NHEX0,MvToutCn1NHEX,MvToutCn1NHEX0,SigToutCn1NHEX,CvINVNP0,FlgNHEX,FlgPIDINVNP)
        Tv1INVNP = CvINVNP + dTv1INVNP
        INVNP = CvINVNP + dCvINVNP
        # 制約条件
        if CvINVNP > CvINVNP0 + 0.1:
            INVNP = INVNP0 + 0.1
            CvINVNP = CvINVNP0 + 0.1
        elif CvINVNP < CvINVNP0 - 0.1:
            INVNP = INVNP0 - 0.1
            CvINVNP = CvINVNP0 - 0.1

        if INVNP > 1:
            INVNP = 1
        elif INVNP < 0:
            INVNP = 0

        INVNP0 = INVNP
        CvINVNP0 = CvINVNP

        if MvGCn1NHEX > 0.25 and SpToutCn1NHEX > 0:
            PFINVNP = PFINVNP + abs(MvToutCn1NHEX - SpToutCn1NHEX) / SpToutCn1NHEX

    # 流量がないとき
    else:
        INVNP = 0
        INVNP0 = 0
        CvINVNP = 0
        CvINVNP0 = 0
        Tv1INVNP = 0




