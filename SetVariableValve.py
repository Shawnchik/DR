def set_variable_valve():
    from test import set_var
    # 弁開度
    # 2次システム
    set_var(('VlvChAHU','VlvHtAHU'),(1,1))
    set_var(('VlvCP2','VlvHP1'),(0,0))

    # 1次システム
    set_var(('VlvSCP4','VlvCh1CHEX'),(0,0))
    set_var(('VlvSHP2','VlvHt1HHEX'),(0,0))

    # 冷却水システム
    set_var(('VlvCT','VlvCT0'),(0,0))

    # 不確かさ
    set_var(('CvVlvChAHU','CvVlvHtAHU'),(1,1))
    set_var(('CvVlvCP2','CvVlvHP1'),(0,0))
    set_var(('CvVlvSCP4','CvVlvCh1CHEX'),(0,1))
    set_var(('CvVlvSHP2','CvVlvHt1HHEX'),(0,1))
    set_var('CvVlvCT',0)

    set_var(('dCvVlvChAHU','dCvVlvHtAHU'),(0,0))
    set_var(('dCvVlvCP2','dCvVlvHP1'),(0,0))
    set_var(('dCvVlvSCP4','dCvVlvCh1CHEX'),(0,0))
    set_var(('dCvVlvSHP2','dCvVlvHt1HHEX'),(0,0))
    set_var('dCvVlvCT',0)

