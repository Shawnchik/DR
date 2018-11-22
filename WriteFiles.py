def write_files():
    import pandas as pd
    # ファイルに書き込む
    # Nomenclature#
    # Results       :出力値の行列

    global Results,CalStep,ErrorPattern,year,num_case
    global monthCOP

    df_re = pd.DataFrame(Results) # list to dataframe
    # 一行目を書き込む場合はここで書き込む

    # 二行目以降
    if int(CalStep + 1,10080) == 0:
        i = (CalStep + 1) / 10080
        if i < 10:
            if num_case < 10:
                name = "Result/".join(str(year), 'Case0',str(num_case),'0',str(i),'.csv')
                pd.DataFrame.to_csv(name)
                #csvwrite(['C:\Users\shhmy\Google �h���C�u\Project\HITACHI\2018\180723�ł����킹\simulation\Result\',num2str(year),'Case0',num2str(num_case),'0',num2str(i),'.csv'],Results,0,0)
            else:
                name = "Result/".join(str(year), 'Case', str(num_case), '0', str(i), '.csv')
                pd.DataFrame.to_csv(name)
                #csvwrite(['C:\Users\shhmy\Google �h���C�u\Project\HITACHI\2018\180723�ł����킹\simulation\Result\',num2str(year),'Case',num2str(num_case),'0',num2str(i),'.csv'],Results,0,0)
        else:
            if num_case < 10:
                name = "Result/".join(str(year), 'Case0',str(num_case),'0',str(i),'.csv')
                pd.DataFrame.to_csv(name)
                #csvwrite(['C:\Users\shhmy\Google �h���C�u\Project\HITACHI\2018\180723�ł����킹\simulation\Result\',num2str(year),'Case0',num2str(num_case),num2str(i),'.csv'],Results,0,0)
            else:
                name = "Result/".join(str(year), 'Case', str(num_case), '0', str(i), '.csv')
                pd.DataFrame.to_csv(name)
                #csvwrite(['C:\Users\shhmy\Google �h���C�u\Project\HITACHI\2018\180723�ł����킹\simulation\Result\',num2str(year),'Case',num2str(num_case),num2str(i),'.csv'],Results,0,0)

        Results = 0

    elif CalStep == (7 + 122) * 24 * 60 - 1:
        if num_case < 10:
            name = "Result/".join(str(year), 'Case0', str(num_case), '19.csv')
            pd.DataFrame.to_csv(name)
            # csvwrite(['C:\Users\shhmy\Google �h���C�u\Project\HITACHI\2018\180723�ł����킹\simulation\Result\',num2str(year),'Case0',num2str(num_case),'19.csv'],Results,0,0)
        else:
            name = "Result/".join(str(year), 'Case', str(num_case), '19.csv')
            pd.DataFrame.to_csv(name)
            # csvwrite(['C:\Users\shhmy\Google �h���C�u\Project\HITACHI\2018\180723�ł����킹\simulation\Result\',num2str(year),'Case',num2str(num_case),'19.csv'],Results,0,0)
        Results = 0

        #上の行をzeros(10080,220)とかにする！！！！

    # if CalStep == (31 + 30) * 24 * 60 - 1
    #
    #     csvwrite(['OutputWeek09.csv'],Results,0,0)
    #
    # end

    # if CalStep == 54719
    #     csvwrite(['OutputWeek',num2str(6),'.csv'],Results,0,0)
    #
    #     Results = 0
    #     #��̍s��zeros(10080,220)�Ƃ��ɂ���I�I�I�I
    # end

    # if CalStep == 54719
    #     if rem(ErrorPattern,10) == 0
    #         csvwrite(['OutputEP',num2str(ErrorPattern),'.csv'],Results,0,0)
    #     end
    # end

