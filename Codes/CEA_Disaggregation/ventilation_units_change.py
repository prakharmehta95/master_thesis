# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:23:11 2019

@author: iA
"""
#%%
def calc(v,p):
    vent = v*1000*p/3600
    return vent

a = float(input("enter vent:"))
b = float(input("enter persons: "))
vent = calc(a,b)
print(vent)



