def read_files():
    import pandas as pd
    from test import set_var
    from test import get_var

    # ファイルを開く
    # Nomenclature#####
    # Values      :熱交換器バイパス弁開度(0~1,0が全閉)[-]

    year = get_var('year')
    name = "".join(('Input', str(year), '69.csv'))
    set_var('Values',pd.read_csv(name))
    set_var('PIDparameters',pd.read_csv('InputPIDparameters.csv'))
    print(year)
    # ファイルを読み込む
    # Values = pd.(['Input201656.csv'],1,1)

    # Values = pd.read_csv(name)
    # PIDparameters = pd.read_csv('InputPIDparameters.csv')
