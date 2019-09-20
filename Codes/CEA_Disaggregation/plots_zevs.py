# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:54:43 2019

@author: Prakhar

Filter out which buildings are in which plots

"""
#%%
import pandas as pd

plots = pd.read_csv(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\DG_GIS_Wiedikon\DataVisualization_newData\Plots_Possible_ZEVs_CSV.csv')

#%%
length = 105
zev = pd.DataFrame(data = None)
zev_new = pd.DataFrame(data = None, index = range(length))

for i in range(1083):
    name = 'P_' + str(i)
    print(name)    
    zev[name] = ""
    zev[name] = 0
    temp = []
    temp.append(list(plots.loc[plots.id == i,'EGID']))
    zev[name] = temp 


for i in range(1083):
    name = 'P_' + str(i)
    temp = []
    for j in range(len(zev[name][0])):
        temp.append(zev[name][0][j])
    #if len(temp) == 0:
    #    continue
    if len(temp) < length:
        for k in range(length-len(temp)):
            temp.append(0)
    zev_new[name] = ""
    zev_new[name] = temp


import math
for i in range(1,1083):
    name = 'P_' + str(i)
    if math.isnan(sum(zev_new[name])):
        del(zev_new[name])

zev_new.to_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Building_Data\Plots.xlsx')