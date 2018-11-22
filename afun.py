#!/usr/bin/env python
# coding: utf-8

# In[ ]:

def a():
    from aconfig import x0
    global x0
    print('flg1')
    print(x0)
    xx = x0 + 1
    yy = x0 * 1
    x0 = x0 +5
    print(x0)
    return [xx,yy]

