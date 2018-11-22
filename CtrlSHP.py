def ctrl_shp():
    import PID
    import CtrlNmSHP2
    import CtrlINVVlvSHP2
    # 冷暖房時温水一次ポンプ、弁制御。蓄熱時と非蓄熱時との2パターンでポンプINVや弁開度を計算する。
    # Nomenclature
    # SgHtSt        :温水運転信号（0:放熱、1:蓄熱、2:追掛（蓄放熱））
    # SpGHtTR1      :冷凍機温水流量設定値
    # SpLFTR1~3     :冷凍機部分負荷率設定値（0~1,Load Factor）
    # WTNmSHP2      :SHP2増減台効果待ち時間[minute]
    # SpGHt1HHEX    :放熱用熱交換器一次側流量設定値[m3/min]
    global SgHtSt,Tv1SpLFTR1
    global CvINVSHP1,SpGSHP10,MvGSHP10,SigGSHP1,KpINVSHP1,TiINVSHP1,SpGSHP1,MvGSHP1,CvINVSHP10
    global Tv1INVSHP1,dTv1INVSHP1,INVSHP1,dCvINVSHP1,INVSHP10
    global FlgFlgINVSHP2
    global FlgFlgVlvSHP2,INVSHP2,dCvINVSHP2,Tv1INVSHP2,dTv1INVSHP2,CvINVSHP2
    global INVSHP20,CvINVSHP20,SpToutHt2HHEX,Tv1VlvSHP2,dTv1VlvSHP2,VlvSHP2,dCvVlvSHP2,VlvSHP20
    global SpToutHt2HHEX0,MvToutHt2HHEX0,SigToutHt2HHEX,KpINVSHP2,TiINVSHP2,MvToutHt2HHEX
    global KpVlvHt1HHEX,TiVlvHt1HHEX,FlgINVSHP2
    global CvVlvSHP2
    global KpVlvSHP2,TiVlvSHP2,CvVlvSHP20
    global CvVlvHt1HHEX,Tv1VlvHt1HHEX,dTv1VlvHt1HHEX,VlvHt1HHEX,dCvVlvHt1HHEX
    global VlvHt1HHEX0,CvVlvHt1HHEX0,NmSHP2,FlgVlvSHP2,MvGHt2Ld,Tv1QST3,ToutHt2HHEX
    global FlgPIDINVSHP1,FlgPIDINVSHP2,FlgPIDVlvHt1HHEX,FlgPIDVlvSHP2
    global PFINVSHP1,PFVlvHt1HHEX,GHt2HHEX
    global MvGHt2HHEX
    # 温水
    # 蓄熱または追掛時
    if SgHtSt == 1 or SgHtSt == 2:

        # 流量設定値
        SpGSHP1 = Tv1SpLFTR1 * 2.47
        # 目標流量になるようにTR1ポンプINVをPI制御
        if SpGSHP1 > 0:
            [CvINVSHP1,SpGSHP10,MvGSHP10,SigGSHP1,FlgPIDINVSHP1] = \
                PID.pid(1.0,0.01,1,KpINVSHP1,TiINVSHP1,0,SpGSHP1,SpGSHP10,MvGSHP1,MvGSHP10,SigGSHP1,CvINVSHP1,1,FlgPIDINVSHP1)
            Tv1INVSHP1 = CvINVSHP1 + dTv1INVSHP1
            INVSHP1 = Tv1INVSHP1 + dCvINVSHP1

            if SpGSHP1 > 0.5:
                PFINVSHP1 = PFINVSHP1 + abs((MvGSHP1 - SpGSHP1) / SpGSHP1)

        else:
            INVSHP1 = 0
            INVSHP10 = 0
            CvINVSHP1 = 0
            CvINVSHP10 = 0
            Tv1INVSHP1 = 0

        # 二次負荷があるときに追掛制御を行う
        if MvGHt2Ld > 0.01:
            # SHP2追掛運転制御
            # SHP2追掛け運転あり
            if FlgFlgINVSHP2 == 1:

                # ポンプSHP2台数制御（流量による制御）
                CtrlNmSHP2.ctrl_nm_shp2()

                # SHP2のINVと、バイパス弁制御
                CtrlINVVlvSHP2.ctrl_inv_vlv_shp2()

    #             # 熱交換器用バルブ制御
    #             CvVlvHt1HHEX = 1
    #             Tv1VlvHt1HHEX = CvVlvHt1HHEX  + dTv1VlvHt1HHEX
    #             VlvHt1HHEX = Tv1VlvHt1HHEX + dCvVlvHt1HHEX
    #             if VlvHt1HHEX > 1
    #                 VlvHt1HHEX = 1
    #             elseif VlvHt1HHEX < 0
    #                 VlvHt1HHEX = 0
    #             end
    #             VlvHt1HHEX0 = VlvHt1HHEX
    #             CvVlvHt1HHEX0 = CvVlvHt1HHEX
                VlvHt1HHEX = 1
                CvVlvHt1HHEX = 1
                Tv1VlvHt1HHEX = 1

            # SHP2追掛け運転なし
            else:
                # INVSHP2は停止、VlvSHP2は全開
                INVSHP2 = 0
                CvINVSHP2 = 0
                INVSHP20 = 0
                CvINVSHP20 = 0
                Tv1INVSHP2 = 0
                # VlvSHP2制御
                CvVlvSHP2 = 1
                Tv1VlvSHP2 = CvVlvSHP2 + dTv1VlvSHP2
                VlvSHP2 = Tv1VlvSHP2 + dCvVlvSHP2
                if VlvSHP2 > 1:
                    VlvSHP2 = 1
                elif VlvSHP2 < 0:
                    VlvSHP2 = 0
                VlvSHP20 = VlvSHP2
                CvVlvSHP20 = CvVlvSHP2

    #             # 熱交換器用バルブ制御
    #             # 温度をみて二方弁を制御する。ここの制御が少しうまくいかないだけで一気に蓄熱槽の温度プロフィルが崩れる
    #             SpToutHt2HHEX = 43
    #             [CvVlvHt1HHEX,SpToutHt2HHEX0,MvToutHt2HHEX0,SigToutHt2HHEX,FlgPIDVlvHt1HHEX] = PID(1.0,0.001,1,KpVlvHt1HHEX,TiVlvHt1HHEX,0,SpToutHt2HHEX,SpToutHt2HHEX0,MvToutHt2HHEX,MvToutHt2HHEX0,SigToutHt2HHEX,CvVlvHt1HHEX0,1,FlgPIDVlvHt1HHEX)
    #             Tv1VlvHt1HHEX = CvVlvHt1HHEX + dTv1VlvHt1HHEX
    #             VlvHt1HHEX = Tv1VlvHt1HHEX + dCvVlvHt1HHEX
    #             # 制約条件
    #             if CvVlvHt1HHEX > CvVlvHt1HHEX0 + 0.1
    #                 VlvHt1HHEX = VlvHt1HHEX0 + 0.1
    #                 CvVlvHt1HHEX = CvVlvHt1HHEX0 + 0.1
    #             elseif CvVlvHt1HHEX < CvVlvHt1HHEX0 - 0.1
    #                 VlvHt1HHEX = VlvHt1HHEX0 - 0.1
    #                 CvVlvHt1HHEX = CvVlvHt1HHEX0 - 0.1
    #             end
    #             if VlvHt1HHEX > 1
    #                 VlvHt1HHEX = 1
    #             elseif VlvHt1HHEX < 0
    #                 VlvHt1HHEX = 0
    #             end
    #             VlvHt1HHEX0 = VlvHt1HHEX
    #             CvVlvHt1HHEX0 = CvVlvHt1HHEX
    #
    #             if (GHt2HHEX > 0.25)&&(SpToutHt2HHEX > 0)
    #                 PFVlvHt1HHEX = PFVlvHt1HHEX + abs(MvToutHt2HHEX - SpToutHt2HHEX) / SpToutHt2HHEX
    #             end
                VlvHt1HHEX = 1
                CvVlvHt1HHEX = 1
                Tv1VlvHt1HHEX = 1


        # 二次負荷がない場合
        else:
            VlvSHP2 = 0
            CvVlvSHP2 = 0
            VlvSHP20 = 0
            CvVlvSHP20 = 0
            Tv1VlvSHP2 = 0
            INVSHP2 = 0
            INVSHP20 = 0
            CvINVSHP2 = 0
            CvINVSHP20 = 0
            Tv1INVSHP2 = 0
            VlvHt1HHEX = 0
            CvVlvHt1HHEX = 0
            VlvHt1HHEX0 = 0
            CvVlvHt1HHEX0 = 0
            Tv1VlvHt1HHEX = 0

    # 放熱時
    else:
        # 熱交換器二次側流量があるときに放熱する
        if MvGHt2HHEX > 0.01:

            # SHP2台数制御
            CtrlNmSHP2.ctrl_nm_shp2()

            # SHP2のINVと、バイパス弁制御
            CtrlINVVlvSHP2.ctrl_inv_vlv_shp2()

    #         # 熱交横二方弁制御(放熱時は全開)
    #         CvVlvHt1HHEX = 1
    #         Tv1VlvHt1HHEX = CvVlvHt1HHEX + dTv1VlvHt1HHEX
    #         VlvHt1HHEX = Tv1VlvHt1HHEX + dCvVlvHt1HHEX
    #         if VlvHt1HHEX > 1
    #             VlvHt1HHEX = 1
    #         elseif VlvHt1HHEX < 0
    #             VlvHt1HHEX = 0
    #         end
    #         VlvHt1HHEX0 = VlvHt1HHEX
    #         CvVlvHt1HHEX0 = CvVlvHt1HHEX
            VlvHt1HHEX = 1
            CvVlvHt1HHEX = 1
            Tv1VlvHt1HHEX = 1

            # 放熱時はSHP1を動かさない
            INVSHP1 = 0
            INVSHP10 = 0
            CvINVSHP1 = 0
            CvINVSHP10 = 0
            Tv1INVSHP1 = 0
            SpGSHP1 = 0

        # 熱交換器二次側流量がない場合は運転しない
        else:

            VlvSHP2 = 0
            CvVlvSHP2 = 0
            VlvSHP20 = 0
            CvVlvSHP20 = 0
            Tv1VlvSHP2 = 0
            INVSHP2 = 0
            INVSHP20 = 0
            CvINVSHP2 = 0
            CvINVSHP20 = 0
            Tv1INVSHP2 = 0
            INVSHP1 = 0
            INVSHP10 = 0
            CvINVSHP1 = 0
            CvINVSHP10 = 0
            Tv1INVSHP1 = 0
            SpGSHP1 = 0
            VlvHt1HHEX = 0
            CvVlvHt1HHEX = 0
            VlvHt1HHEX0 = 0
            CvVlvHt1HHEX0 = 0
            Tv1VlvHt1HHEX = 0


    # SHP2追掛運転フラグ（効果待ち時間5分）
    # 追掛・蓄熱時のみ。放熱時には追掛けという概念がない
    if SgHtSt == 2 or SgHtSt == 1:
        if MvGHt2HHEX > 0.5 and FlgFlgINVSHP2 == 0 and \
                MvToutHt2HHEX < SpToutHt2HHEX - 1 and CvVlvHt1HHEX > 0.95:
            for i in range(30,2,-1):
                FlgINVSHP2[i] = FlgINVSHP2[i-1]
            FlgINVSHP2[1] = 1

        elif (MvGHt2HHEX <= 0.5) or \
                (FlgFlgINVSHP2 == 1 and MvToutHt2HHEX > SpToutHt2HHEX + 1 and CvVlvSHP2 > 0.95):
            for i in range(30,2,-1):
                FlgINVSHP2[i] = FlgINVSHP2[i-1]
            FlgINVSHP2[1] = -1
        else:
            for i in range(30,2,-1):
                FlgINVSHP2[i] = FlgINVSHP2[i-1]
            FlgINVSHP2[1] = 0

    elif SgHtSt == 0:
        for i in range(30, 2, -1):
            FlgINVSHP2[i] = FlgINVSHP2[i - 1]
        FlgINVSHP2[1] = -1

    # フラグの入力
    if FlgINVSHP2 == 1:
        FlgFlgINVSHP2 = 1
    elif FlgINVSHP2 == -1:
        FlgFlgINVSHP2 = 0
