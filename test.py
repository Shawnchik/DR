#############################################
# *checked* csv file header must be replaced
# 12/30 dict for variable

# TODO check code resolution: 1. set a media to pass variable https://www.jianshu.com/p/6cee728f3490
# TODO link to second system
# TODO virables in lower case letter
# TODO add heat capacity for better DR
# TODO the problem of VARIABLE in multiple

# update
# 11/21 progress in SetPIparemeters

#############################################

import SetVariable
import ReadFiles
import Input
import SetPIparameters
import SetParameters
import SecondarySystem
import PrimarySystem
import CondenserSystem
import Heat
import Power
import Output
import WriteFiles

_no_var = object()

############################################
# variable's data set and functions


def set_var(rkey, rvalue=_no_var, ty=0):
    # ty = 1 is for one matrix input
    if ty == 0:
        i = 0
        if rvalue is _no_var:
            rvalue = ('')
        for key in rkey:
            if rvalue == '':
                VARIABLE[key] = ''
            elif type(rvalue) is int:
                VARIABLE[rkey] = rvalue
                break
            else:
                VARIABLE[key] = rvalue[i]
            i += 1
    elif ty == 1:
        VARIABLE[rkey] = rvalue

    # if value is _no_var:
    #   value = ''    # or [] ???
    # VARIABLE[key] = value


def del_var(key):
    try:
        del VARIABLE[key]
    except KeyError:
        print("key:'"+str(key)+"' no exist")


def get_var(key):
    # can only output one key or all in a time
    try:
        if key in 'all':
            return VARIABLE
        return VARIABLE[key]
    except KeyError:
        print("key:'" + str(key) + "' no exist")
###########################################

# # 設定値パラメータ最適化
# OptimizePr
#  熱源システムシミュレーション（2016年5月と6,7,8,9月）
#global CalStep,num_case,year,month,day,hour,minute
# global変数の設定と、変数の初期値設定


if __name__ == '__main__':

    VARIABLE = ()
    set_var('year', 0)
    set_var('num_case', 0)
    year = get_var('year')
    num_case = get_var('num_case')

    for year in range(2017,2018,1):
        print(year)
        for num_case in range(0,2,1):
            print(num_case)
            #############
            # need check
            #############

            # SetFaults
            SetVariable.set_variable()

            # ファイル読み込む
            ReadFiles.read_files()
            set_var('month',5)
            set_var('day',24)
            set_var('hour',21)
            set_var('minute',59)


            # 6月から9月の4ヶ月とその前の一週間を助走期間
            # 22時始まりとする!
            for CalStep in range(0,(7 + 122)*24*60 - 1):
                set_var('CalStep',CalStep)
                #             CalStep
                # 入力(冷温モードは入力値)
                Input.variable_input()
                # PIパラメータの設定
                SetPIparameters.set_pi_parameters()
                # 変更する設定値
                SetParameters.set_parameters()
                # 二次システム
                SecondarySystem.secondary_system()
                # 一次ポンプシステム
                PrimarySystem.primary_system()
                # 冷却水ポンプシステム
                CondenserSystem.condenser_system()
                # 熱の計算
                Heat.heat()
                # 消費電力の計算
                Power.power()
                # 出力
                Output.output()
                #         OutputMonthlySCOP
                # ファイルに書き込む
                WriteFiles.wrtite_files()


    