# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 13:52:49 2019

@author: prakh
"""
#%%
#from test_pass_try import y
from __main__ import *
print("y = ",y)
a = y*y
print("a = ",a)
#%%
def set_args(x):
    global y
    y = x*x
    print(y)
    return y


