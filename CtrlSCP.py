def ctrl_scp():
    import PID
    import CtrlNmSCP4
    import CtrlINVVlvSCP4
    # 冷房時冷水一次ポンプ、弁制御。蓄熱時と非蓄熱時との2パターンでポンプINVや弁開度を計算する。
    # Nomenclature
    # SgChSt        :冷水運転信号（0:放熱、1:蓄熱、2:追掛（蓄放熱））
    # SpGChTR1~3    :冷凍機冷水流量設定値
    # SpLFTR1~3     :冷凍機部分負荷率設定値（0~1,Load Factor）
    # WTNmSCP4      :SCP4増減台効果待ち時間[minute]
    # SpGCh1CHEX    :放熱用熱交換器一次側流量設定値[m3/min]
    global Tv1SpLFTR1,Tv1SpLFTR2,Tv1SpLFTR3
    global SpGSCP10,MvGSCP1,MvGSCP10,SigGSCP1,INVSCP1,INVSCP10
    global SpGSCP20,MvGSCP2,MvGSCP20,SigGSCP2,INVSCP2,INVSCP20
    global SpGSCP30,MvGSCP3,MvGSCP30,SigGSCP3,INVSCP3,INVSCP30
    global VlvCh1CHEX,VlvCh1CHEX0
    global SpToutCh2CHEX,SgTR4,FlgNmSCP4,NmSCP4
    global SpToutCh2CHEX0,MvToutCh2CHEX,MvToutCh2CHEX0,VlvSCP4,SigToutCh2CHEX,VlvSCP40
    global INVSCP4,FlgVlvSCP4,FlgFlgVlvSCP4,SgChSt,INVSCP40,FlgINVSCP4,FlgFlgINVSCP4
    global KpINVSCP1,TiINVSCP1,KpINVSCP2,TiINVSCP2,KpINVSCP3,TiINVSCP3
    global KpVlvCh1CHEX,TiVlvCh1CHEX,KpVlvSCP4,TiVlvSCP4,KpINVSCP4,TiINVSCP4
    global CvINVSCP1,CvINVSCP10,dCvINVSCP1,Tv1INVSCP1,dTv1INVSCP1
    global CvINVSCP2,CvINVSCP20,dCvINVSCP2,Tv1INVSCP2,dTv1INVSCP2
    global CvINVSCP3,CvINVSCP30,dCvINVSCP3,Tv1INVSCP3,dTv1INVSCP3
    global CvINVSCP4,CvINVSCP40,dCvINVSCP4,Tv1INVSCP4,dTv1INVSCP4
    global CvVlvSCP4,CvVlvSCP40,dCvVlvSCP4,Tv1VlvSCP4,dTv1VlvSCP4
    global CvVlvCh1CHEX,CvVlvCh1CHEX0,dCvVlvCh1CHEX,Tv1VlvCh1CHEX,dTv1VlvCh1CHEX
    global MvGCh2Ld,Tv1QST3,MvGCh2CHEX
    global SpGSCP1,SpGSCP2,SpGSCP3
    global FlgPIDINVSCP1,FlgPIDINVSCP2,FlgPIDINVSCP3,FlgPIDINVSCP4,FlgPIDVlvCh1CHEX,FlgPIDVlvSCP4
    global PFINVSCP1,PFINVSCP2,PFINVSCP3,PFVlvCh1CHEX
    # 蓄熱・追掛時
    if SgChSt == 1 or SgChSt == 2:
        # 冷凍機冷水ポンプ
        # 流量設定値
        SpGSCP1 = Tv1SpLFTR1 * 2.47
        SpGSCP2 = Tv1SpLFTR2 * 4.98
        SpGSCP3 = Tv1SpLFTR3 * 4.98
        # 目標流量になるようにポンプINVをPI制御(INV下限値0.4は設けていない)
        if SpGSCP1 > 0:
            [CvINVSCP1,SpGSCP10,MvGSCP10,SigGSCP1,FlgPIDINVSCP1] = \
                PID.pid(1.0,0.01,1,KpINVSCP1,TiINVSCP1,0,SpGSCP1,SpGSCP10,MvGSCP1,MvGSCP10,SigGSCP1,CvINVSCP1,1,FlgPIDINVSCP1)
            Tv1INVSCP1 = CvINVSCP1 + dTv1INVSCP1
            INVSCP1 = CvINVSCP1 + dCvINVSCP1

            if SpGSCP1 > 0.5:
                PFINVSCP1 = PFINVSCP1 + abs((MvGSCP1 - SpGSCP1) / SpGSCP1)

        else:
            INVSCP1 = 0
            INVSCP10 = 0
            CvINVSCP1 = 0
            CvINVSCP10 = 0
            Tv1INVSCP1 = 0

        if SpGSCP2 > 0:
            [CvINVSCP2,SpGSCP20,MvGSCP20,SigGSCP2,FlgPIDINVSCP2] = \
                PID.pid(1.0,0.01,1,KpINVSCP2,TiINVSCP2,0,SpGSCP2,SpGSCP20,MvGSCP2,MvGSCP20,SigGSCP2,CvINVSCP2,1,FlgPIDINVSCP2)
            Tv1INVSCP2 = CvINVSCP2 + dTv1INVSCP2
            INVSCP2 = CvINVSCP2 + dCvINVSCP2

            if SpGSCP2 > 0.5:
                PFINVSCP2 = PFINVSCP2 + abs((MvGSCP2 - SpGSCP2) / SpGSCP2)

        else:
            INVSCP2 = 0
            INVSCP20 = 0
            CvINVSCP2 = 0
            CvINVSCP20 = 0
            Tv1INVSCP2 = 0

        if SpGSCP3 > 0:
            [CvINVSCP3,SpGSCP30,MvGSCP30,SigGSCP3,FlgPIDINVSCP3] = \
                PID.pid(1.0,0.01,1,KpINVSCP3,TiINVSCP3,0,SpGSCP3,SpGSCP30,MvGSCP3,MvGSCP30,SigGSCP3,CvINVSCP3,1,FlgPIDINVSCP3)
            Tv1INVSCP3 = CvINVSCP3 + dTv1INVSCP3
            INVSCP3 = CvINVSCP3 + dCvINVSCP3

            if SpGSCP3 > 0.5:
                PFINVSCP3 = PFINVSCP3 + abs((MvGSCP3 - SpGSCP3) / SpGSCP3)

        else:
            INVSCP3 = 0
            INVSCP30 = 0
            CvINVSCP3 = 0
            CvINVSCP30 = 0
            Tv1INVSCP3 = 0

        # SCP4追掛運転制御
        # SCP4追掛け運転あり
        if FlgFlgINVSCP4 == 1:

            # ポンプ台数制御（流量による制御）
            CtrlNmSCP4.ctrl_nm_scp4()

            # SCP4のINVと、バイパス弁制御
            CtrlINVVlvSCP4.ctrl_inv_vlv_scp4()

    #         # 熱交換器用バルブ制御
    #         CvVlvCh1CHEX = 1
    #         Tv1VlvCh1CHEX = CvVlvCh1CHEX  + dTv1VlvCh1CHEX
    #         VlvCh1CHEX = CvVlvCh1CHEX + dCvVlvCh1CHEX
    #         if VlvCh1CHEX > 1
    #             VlvCh1CHEX = 1
    #         elseif VlvCh1CHEX < 0
    #             VlvCh1CHEX = 0
    #         end
    #         VlvCh1CHEX0 = VlvCh1CHEX
    #         CvVlvCh1CHEX0 = CvVlvCh1CHEX
            VlvCh1CHEX = 1
            CvVlvCh1CHEX = 1
            Tv1VlvCh1CHEX = 1

        # SCP4追掛け運転なし
        else:

            # ポンプ台数制御（流量による制御）
            CtrlNmSCP4.ctrl_nm_scp4()

            # INVSCP4
            INVSCP4 = 0
            CvINVSCP4 = 0
            INVSCP40 = 0
            CvINVSCP40 = 0
            Tv1INVSCP4 = 0
            # VlvSCP4
            CvVlvSCP4 = 1
            Tv1VlvSCP4 = CvVlvSCP4 + dTv1VlvSCP4
            VlvSCP4 = CvVlvSCP4 + dCvVlvSCP4
            if VlvSCP4 > 1:
                VlvSCP4 = 1
            elif VlvSCP4 < 0:
                VlvSCP4 = 0

            VlvSCP40 = VlvSCP4
            CvVlvSCP40 = CvVlvSCP4

    #         # 熱交換器用バルブ制御
    #         # 温度をみて二方弁を制御する。ここの制御が少しうまくいかないだけで一気に蓄熱槽の温度プロフィルが崩れる
    #         [CvVlvCh1CHEX,SpToutCh2CHEX0,MvToutCh2CHEX0,SigToutCh2CHEX,FlgPIDVlvCh1CHEX] = PID(1.0,0.001,1,KpVlvCh1CHEX,TiVlvCh1CHEX,0,SpToutCh2CHEX,SpToutCh2CHEX0,MvToutCh2CHEX,MvToutCh2CHEX0,SigToutCh2CHEX,CvVlvCh1CHEX0,-1,FlgPIDVlvCh1CHEX)
    #         Tv1VlvCh1CHEX = CvVlvCh1CHEX + dTv1VlvCh1CHEX
    #         VlvCh1CHEX = CvVlvCh1CHEX + dCvVlvCh1CHEX
    #         # 制約条件
    #         if CvVlvCh1CHEX > CvVlvCh1CHEX0 + 0.1
    #             VlvCh1CHEX = VlvCh1CHEX0 + 0.1
    #             CvVlvCh1CHEX = CvVlvCh1CHEX0 + 0.1
    #         elseif CvVlvCh1CHEX < CvVlvCh1CHEX0 - 0.1
    #             VlvCh1CHEX = VlvCh1CHEX0 - 0.1
    #             CvVlvCh1CHEX = CvVlvCh1CHEX0 - 0.1
    #         end
    #         if VlvCh1CHEX > 1
    #             VlvCh1CHEX = 1
    #         elseif VlvCh1CHEX < 0
    #             VlvCh1CHEX = 0
    #         end
    #         VlvCh1CHEX0 = VlvCh1CHEX
    #         CvVlvCh1CHEX0 = CvVlvCh1CHEX
    #
    #         if (MvGCh2CHEX > 0.25)&&(SpToutCh2CHEX > 0)
    #             PFVlvCh1CHEX = PFVlvCh1CHEX + abs(MvToutCh2CHEX - SpToutCh2CHEX) / SpToutCh2CHEX
    #         end

            VlvCh1CHEX = 1
            CvVlvCh1CHEX = 1
            Tv1VlvCh1CHEX = 1


    # 放熱時
    else:
        # 熱交換器二次側流量があるときに放熱する
        if MvGCh2CHEX > 0.01:

            # 一次放熱ポンプ
            # ポンプ台数制御（流量による制御）
            CtrlNmSCP4.ctrl_nm_scp4()

            # SCP4のINVと、バイパス弁制御
            CtrlINVVlvSCP4.ctrl_inv_vlv_scp4()


    #         # 熱交横二方弁制御(放熱時は全開)
    #         CvVlvCh1CHEX = 1
    #         Tv1VlvCh1CHEX = CvVlvCh1CHEX + dTv1VlvCh1CHEX
    #         VlvCh1CHEX = CvVlvCh1CHEX + dCvVlvCh1CHEX
    #         if VlvCh1CHEX > 1
    #             VlvCh1CHEX = 1
    #         elseif VlvCh1CHEX < 0
    #             VlvCh1CHEX = 0
    #         end
    #         VlvCh1CHEX0 = VlvCh1CHEX
    #         CvVlvCh1CHEX0 = CvVlvCh1CHEX
            VlvCh1CHEX = 1
            CvVlvCh1CHEX = 1
            Tv1VlvCh1CHEX = 1


            # 放熱時はSCP1~3を動かさない
            INVSCP1 = 0
            INVSCP10 = 0
            CvINVSCP1 = 0
            CvINVSCP10 = 0
            Tv1INVSCP1 = 0
            INVSCP2 = 0
            INVSCP20 = 0
            CvINVSCP2 = 0
            CvINVSCP20 = 0
            Tv1INVSCP2 = 0
            INVSCP3 = 0
            INVSCP30 = 0
            CvINVSCP3 = 0
            CvINVSCP30 = 0
            Tv1INVSCP3 = 0
            SpGSCP1 = 0
            SpGSCP2 = 0
            SpGSCP3 = 0
        #     # 追掛け用のフラグを0にしておく
        #     FlgFlgINVSCP4 = 0
        #     FlgINVSCP4 = zeros(1,10)

        # 熱交換器二次側流量がない場合は運転しない
        else:
            INVSCP1 = 0
            INVSCP10 = 0
            CvINVSCP1 = 0
            CvINVSCP10 = 0
            Tv1INVSCP1 = 0
            INVSCP2 = 0
            INVSCP20 = 0
            CvINVSCP2 = 0
            CvINVSCP20 = 0
            Tv1INVSCP2 = 0
            INVSCP3 = 0
            INVSCP30 = 0
            CvINVSCP3 = 0
            CvINVSCP30 = 0
            Tv1INVSCP3 = 0
            SpGSCP1 = 0
            SpGSCP2 = 0
            SpGSCP3 = 0
            VlvSCP4 = 0
            CvVlvSCP4 = 0
            VlvSCP40 = 0
            CvVlvSCP40 = 0
            Tv1VlvSCP4 = 0
            INVSCP4 = 0
            INVSCP40 = 0
            CvINVSCP4 = 0
            CvINVSCP40 = 0
            Tv1INVSCP4 = 0
            VlvCh1CHEX = 0
            CvVlvCh1CHEX = 0
            VlvCh1CHEX0 = 0
            CvVlvCh1CHEX0 = 0
            Tv1VlvCh1CHEX = 0
        end
    end

    # SCP4追掛運転フラグ（効果待ち時間30分）
    # 蓄熱時,追掛時
    if SgChSt == 1 or SgChSt == 2:
        if MvGCh2CHEX > 0.5 and FlgFlgINVSCP4 == 0 and MvToutCh2CHEX > SpToutCh2CHEX + 1 \
                and CvVlvCh1CHEX > 0.95:
            for i in range(30,2,-1):
                FlgINVSCP4[i] = FlgINVSCP4[i-1]
            FlgINVSCP4[1] = 1
        elif  (MvGCh2CHEX <= 0.5) or (FlgFlgINVSCP4 == 1 and MvToutCh2CHEX > SpToutCh2CHEX + 1 and CvVlvSCP4 > 0.95):
            for i in range(30,2,-1):
                FlgINVSCP4[i] = FlgINVSCP4[i-1]
            FlgINVSCP4[1] = -1

        else:
            for i in range(30,2,-1):
                FlgINVSCP4[i] = FlgINVSCP4[i-1]
            FlgINVSCP4[1] = 0

    # 放熱時には追掛けという概念がない
    elif SgChSt == 0:
        for i in range(30, 2, -1):
            FlgINVSCP4[i] = FlgINVSCP4[i - 1]
        FlgINVSCP4[1] = -1
    # フラグの入力
    if FlgINVSCP4 == 1:
        FlgFlgINVSCP4 = 1
    elif FlgINVSCP4 == -1:
        FlgFlgINVSCP4 = 0
