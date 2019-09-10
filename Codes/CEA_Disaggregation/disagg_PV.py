# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:30:21 2019

@author: prakh

Solar PV Data Disaggregation according to roof sizes
"""

import pandas as pd


#%%



agent_areas = pd.read_excel(r'C:\Users\prakh\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Building_Data\LIST_AGENTS_FINAL.xlsx')
agent_list_final = list(agent_areas.Bldg_IDs)
agent_areas = agent_areas.set_index("Bldg_IDs")

og_bldg_stock = pd.read_excel(r'C:\Users\prakh\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Building_Data\OG_Wdkon_Bldg_Stock_Stats.xlsx')
og_bldg_stock = og_bldg_stock.set_index("EGID")
#og_bldg_stock.index = og_bldg_stock.index.map(str)
zones_splits =  pd.read_excel(r'C:\Users\prakh\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Building_Data\Buildings_EGIDs_Each_zone_v1.xlsx')


#%%
df_PV = pd.DataFrame(data = None)
for FileList in agent_list_final:
    print(FileList)
    zz = pd.read_csv(r"C:\Users\prakh\OneDrive - ETHZ\Thesis\PM\CEA Data\Sample 1650\outputs\data\potentials\solar\\" + FileList + '_PV.csv')
    df_PV[FileList] = zz.E_PV_gen_kWh
 

#%%

disagg_PV_df = pd.DataFrame(data = None)
for zone in agent_list_final:
    print(zone)
    temp_zone_splits = zones_splits[zone].dropna()   
    temp_egids = og_bldg_stock.loc[temp_zone_splits,:]
    list_egids = temp_egids.index.tolist()
    check_areas = temp_egids.Grundflache_EG.tolist()
    sum_grundflache_area = temp_egids.sum(skipna = True)
    if all(i > 0 for i in check_areas):
        total_area = sum_grundflache_area.Grundflache_EG
    else:
        total_area = sum_grundflache_area.Nutzflache
        #print(zone)
    
    cea_roof_area = agent_areas.loc[zone]['Aroof_m2']
    #print("cea_area = ",cea_area)
    temp_egids['Area_Roof_CEA'] = ""
    temp_areas_list = []
    
    #getting the actual areas of the roofs in proportion to the CEA
    for j in list_egids:
        if cea_roof_area != 0:
            if all(i > 0 for i in check_areas):
                area_prop_cea = (temp_egids.loc[j]['Grundflache_EG']/total_area)*cea_roof_area
                temp_areas_list.append(area_prop_cea)
            else:
                area_prop_cea = (temp_egids.loc[j]['Nutzflache']/total_area)*cea_roof_area
                temp_areas_list.append(area_prop_cea)
        else:
            if all(i > 0 for i in check_areas):
                area_prop_cea = temp_egids.loc[j]['Grundflache_EG']
                temp_areas_list.append(area_prop_cea)
            else:
                area_prop_cea = temp_egids.loc[j]['Nutzflache']
                temp_areas_list.append(area_prop_cea)
                
    temp_egids['Area_Roof_CEA'] = temp_areas_list
    
        
    
    #loop over bldgs
    #print("Last loop")
    for bldg in list_egids:
        #print(bldg)
        bldgname = str(bldg)
        bldgarea = temp_egids['Area_Roof_CEA'][bldg]
        #print("bldgarea = ",bldgarea)
        temp_bldg_name = 'PV_' + bldgname
        disagg_PV_df[temp_bldg_name] = ""
        disagg_PV_df[temp_bldg_name]    = df_PV[zone]*bldgarea/cea_roof_area
        


