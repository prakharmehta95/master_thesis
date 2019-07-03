# -*- coding: utf-8 -*-
"""
Created on Tue May 28 14:21:29 2019

@author: prakh
"""
#%%
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt
#%%

hist_proj = [827,1654,2481,3308,4135]#,4962,5790,6617,7444,8271,9098,9925,10752,11580,12407,13234,14061,14888]
#hist_proj_noZEV = [226,452,679,905,1132]#,1358,1585,1811,2038,2264,2490,2717,2943,3170,3396,3623,3849,4076]
plt.figure(1)
#plt.plot(hist_proj)
x = range(2018,2023,1)

#plt.xa
list_pv = d_gini_model_correct['gini_model_0'].Ind_PV_Installed
#list_pv = list_pv-336
print(list_pv)

y_actual = hist_proj
#y_actual = hist_proj_noZEV
y_predicted = d_gini_model_correct['gini_model_0'].Ind_PV_Installed
rms = sqrt(mean_squared_error(y_actual, y_predicted))
print("RMSE = ",rms)

#plt.figure(1)
plt.plot(x,hist_proj)
plt.plot(x,list_pv)

plt.xlabel("Year")
plt.ylabel("Individual PV Capacity (kWp)")
plt.xticks(np.arange(2018, 2023, step=1))
plt.tick_params(axis = 'x', rotation = 0)
plt.legend(["Extrapolated Historical Trend","Typical ABM Run"])


#%%

Agents_Ind_NPVs.to_excel("Ind_NPVs.xlsx")
