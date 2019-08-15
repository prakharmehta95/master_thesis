# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 18:50:30 2019

@author: iA

subplot formation based on ZEV regulations 

"""
import pandas as pd


#%% in subplots, only save those which are less than 100 MWh of annual demand

#read the correct excel!!
subplots = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_without_plotids_TOP4.xlsx')

agents_demands =  pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\Agents_demands.xlsx') 
agents_demands = agents_demands.set_index('Name')
list_agents_demands = list(subplots.columns)
subplots_clear = subplots
for i in list_agents_demands:
    if agents_demands.loc[i]['GRID_MWhyr']>100:
        print(i)
        subplots_clear = subplots_clear.drop(columns = i)

#%% in subplots_clear, remove any agents who have greater than 100 MWh of annual demand from subplots of other buildings
        # as they can never be part of any subplot!
import numpy as np     
for i in list(subplots_clear.columns):
    k = 0
    for j in list(subplots_clear[i].dropna()):
        
        try:
            if agents_demands.loc[j]['GRID_MWhyr'] > 100:
                subplots_clear.update(pd.Series([''], name  = i, index = [k]))
            k = k + 1
        except KeyError:
            subplots_clear.update(pd.Series([''], name  = i, index = [k]))
            pass
        
#%% replace empty string with nan

for i in list(subplots_clear.columns):
    subplots_clear[i].replace('', np.nan, inplace=True)
    
#%% 
    
import pandas as pd

#subplots_clear.to_excel("subplots_clear_TOP4.xlsx")
# =============================================================================
#!!!!!!!!!!!!!!export to excel, remove blank spaces, import again:!!!!!!!!!!!!!!!!

subplots_100MWh = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_clear_TOP4.xlsx') 

# =============================================================================
#

#all the possible subplots are in this excel
subplots_100MWh_all = subplots_100MWh
#remove those columns which are empty

for i in list(subplots_100MWh_all.columns):
    if len(subplots_100MWh_all[i].dropna()) == 0:
        subplots_100MWh_all = subplots_100MWh_all.drop(columns = i)
        

subplots_100MWh_all.to_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_100MWh_all_TOP4.xlsx')

#%% removing those buildings which are not part of the final 1437 buildings
list_agents = list(agents_demands.Name.dropna())

subplots_final_FINAL = pd.DataFrame(data = None,index = range(11),columns = list(subplots_100MWh_all.columns))
for i in list(subplots_100MWh_all.columns):
    subplots_final_FINAL[i] = ""
    if i == 0:
        continue
    k = 0
    for j in subplots_100MWh_all[i].dropna():
        if j in list_agents:
            subplots_final_FINAL.update(pd.Series([j],name = i, index = [k]))
            k = k + 1
        else:
            pass
#%% removing those columns which are empty

for i in list(subplots_final_FINAL.columns):
    subplots_final_FINAL[i].replace('', np.nan, inplace=True)

subplots_final_FINAL_cleaned = subplots_final_FINAL
            
for i in list(subplots_final_FINAL_cleaned.columns):
    if len(subplots_final_FINAL_cleaned[i].dropna()) == 0:
        subplots_final_FINAL_cleaned = subplots_final_FINAL_cleaned.drop(columns = i)

subplots_final_FINAL_cleaned.to_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_CLEAN_100MWh_TOP4.xlsx')
