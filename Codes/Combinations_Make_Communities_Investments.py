# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 10:12:36 2019

@author: iA
"""

"""
Created on Mon Apr 15 10:37:34 2019

@author: iA
"""

import pandas as pd
import itertools

subplots_final = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_CLEAN_100MWh.xlsx')
subplot_combos_dem = pd.DataFrame(data = None)
temp_df_dem = pd.DataFrame(data = None)

subplot_combos_solar = pd.DataFrame(data = None)
temp_df_solar = pd.DataFrame(data = None)

for i in list(subplots_final.columns):#['Z0054','Z0055']:#,'Z0055']:#,'Z0063']:#list(subplots_final.columns):
    if i == 0:
        continue
    temp_combos_list = []    
    temp_subplot_list = subplots_final[i].dropna()
    #for j in temp_subplot_list:
    for j in range(0,len(temp_subplot_list)):
        temp_combos = list(itertools.combinations(temp_subplot_list,len(temp_subplot_list)-j))
        print(temp_combos)
        temp_combos_list.append(temp_combos)
        #num_combos = 2**len(temp_combos_list)-1
        
        for k in range(len(temp_combos_list)):
            for m in temp_combos_list[k]:
                temp_name= i #take name of building here
                temp_df_dem = df_demand[i]
                temp_df_solar = df_solar_AC[i]
                print('m = ',m)
                for n in m:
                    temp_name = temp_name + '_' +n
                    temp_df_dem = temp_df_dem + df_demand[n]
                    temp_df_solar = temp_df_solar + df_solar_AC[n]
                print('temp_name = ',temp_name)
                subplot_combos_dem[temp_name] = ""
                subplot_combos_dem[temp_name] = temp_df_dem
                subplot_combos_solar[temp_name] = ""
                subplot_combos_solar[temp_name] = temp_df_solar
            
#%% agent information skeleton imported here
agents_info = pd.read_excel(r"C:\\Users\\iA\\OneDrive - ETHZ\\Thesis\\PM\\Data_Prep_ABM\\Skeleton_Updated_OLD_PV_Sizes.xlsx")
agents_info = agents_info.set_index('bldg_id')

#%% make names of the combos clear
import time
start = time.time()
list_combos_demand_names = list(subplot_combos_dem.columns)
list_combos_demand_names_strings = []

list_combos_solar_names = list(subplot_combos_solar.columns)
list_combos_solar_names_strings = []
for i in range(len(list_combos_demand_names)):
    x = list_combos_demand_names[i]
    list_combos_demand_names_strings.append(x.split("_"))

for i in range(len(list_combos_solar_names)):
    x = list_combos_solar_names[i]
    list_combos_solar_names_strings.append(x.split("_"))


    
#%% take in PV info, add PV sizes for those systems, make NPV shares for each building

#list_combos_demand_names.remove('Hour')
#list_combos_demand_names.remove('price_level')
#list_combos_demand_names.remove('Day')
subplot_combos_dem = pd.read_pickle('Community_TOP4_Combos_Demand.pickle')
subplot_combos_solar= pd.read_pickle('Community_TOP4_Combos_Solar.pickle')

Combos_Info_DUP_TOP4 = pd.DataFrame(data = None, index = list_combos_demand_names)
temp_PV_size_ALL_combos = []
share_PV_sys_ALL = []
temp_num_meters_ALL = []
share_meters_ALL = []
temp_names_list_y = []
temp_combo_plot_ID = []
temp_total_num_EGIDs_ALL = []
temp_total_num_Occupants_ALL = []
temp_total_demand_ALL = []
temp_total_area_ALL = []
temp_bldg_type_category_ALL = []

for i in range(len(list_combos_demand_names)):
    print(i)
    x = list_combos_demand_names[i]
    if x == 'Hour' or x == 'price_level' or x == 'Day':
        continue
    y = x.split("_")
    temp_names_list_y.append(y)
    temp_PV_size = 0
    temp_num_meters = 0
    share_PV_sys_temp_list = []
    share_meters_temp_list = []
    temp_bldg_type_category_list = []
    temp_total_num_EGIDs = 0
    temp_total_num_Occupants = 0
    temp_total_demand = 0
    temp_total_area = 0
    temp_bldg_type_category = ""
    
    for j in range(len(y)):
        temp_PV_size = temp_PV_size + agents_info.loc[y[j]]['PV_Size']
        temp_num_meters = temp_num_meters + agents_info.loc[y[j]]['Num_Smart_Meters']
        temp_total_num_EGIDs = temp_total_num_EGIDs +  agents_info.loc[y[j]]['Num_EGIDs']
        temp_total_num_Occupants = temp_total_num_Occupants +  agents_info.loc[y[j]]['Num_Occupants']
        temp_total_demand = temp_total_demand + agents_info.loc[y[j]]['GRID_MWhyr']
        temp_total_area = temp_total_area + agents_info.loc[y[j]]['Areas_Correct'] 
        #temp_bldg_type_category = temp_bldg_type_category  + '_' + agents_info.loc[y[j]]['Building_Type_Category']
        temp_bldg_type_category_list.append(agents_info.loc[y[j]]['Building_Type_Category'])
        
    for j in range(len(y)):
        share_meters_temp_list.append(agents_info.loc[y[j]]['Num_Smart_Meters']/temp_num_meters)
        share_PV_sys_temp_list.append(agents_info.loc[y[j]]['PV_Size']/temp_PV_size)
        #temp_bldg_type_category_list.append(temp_bldg_type_category)
        
    share_meters_ALL.append(share_meters_temp_list)
    share_PV_sys_ALL.append(share_PV_sys_temp_list)
    temp_bldg_type_category_ALL.append(temp_bldg_type_category_list)
    
    temp_total_num_EGIDs_ALL.append(temp_total_num_EGIDs)
    temp_total_num_Occupants_ALL.append(temp_total_num_Occupants)
    temp_total_demand_ALL.append(temp_total_demand)
    temp_total_area_ALL.append(temp_total_area)
    temp_PV_size_ALL_combos.append(temp_PV_size)
    temp_num_meters_ALL.append(temp_num_meters)
    temp_combo_plot_ID.append(agents_info.loc[y[0]]['Plot_ID'])



Combos_Info_DUP_TOP4['Plot_ID'] = ""
Combos_Info_DUP_TOP4['Plot_ID'] = temp_combo_plot_ID

Combos_Info_DUP_TOP4['Buildings_in_Community'] = ""
Combos_Info_DUP_TOP4['Buildings_in_Community'] = temp_names_list_y

Combos_Info_DUP_TOP4['Types_Community'] = ""
Combos_Info_DUP_TOP4['Types_Community'] = temp_bldg_type_category_ALL

Combos_Info_DUP_TOP4['Area_Community'] = ""
Combos_Info_DUP_TOP4['Area_Community'] = temp_total_area_ALL

Combos_Info_DUP_TOP4['Community_PV_Size'] = ""
Combos_Info_DUP_TOP4['Community_PV_Size'] = temp_PV_size_ALL_combos

Combos_Info_DUP_TOP4['Bldg_share_in_community'] = ""
Combos_Info_DUP_TOP4['Bldg_share_in_community'] = share_PV_sys_ALL

Combos_Info_DUP_TOP4['Community_Meters'] = ""
Combos_Info_DUP_TOP4['Community_Meters'] = temp_num_meters_ALL

Combos_Info_DUP_TOP4['Bldg_share_in_meters_community'] = ""
Combos_Info_DUP_TOP4['Bldg_share_in_meters_community'] = share_meters_ALL
    
Combos_Info_DUP_TOP4['Num_EGIDs'] = ""
Combos_Info_DUP_TOP4['Num_EGIDs'] = temp_total_num_EGIDs_ALL

Combos_Info_DUP_TOP4['Num_Occupants'] = ""
Combos_Info_DUP_TOP4['Num_Occupants'] = temp_total_num_Occupants_ALL

Combos_Info_DUP_TOP4['Demand_Year_MWh'] = ""
Combos_Info_DUP_TOP4['Demand_Year_MWh'] = temp_total_demand_ALL

#%% adding PV subsidy information for the PV systems

Combos_Info_DUP_TOP4['Community_PV_Subsidy'] = 0

list_temp_pv_subsidy = []   
for i in list_combos_demand_names:
    temp_pv_size = Combos_Info_DUP_TOP4.loc[i]['Community_PV_Size'] 
    if temp_pv_size < 30:
        temp_subsidy = 1600 + temp_pv_size*460
    elif 30 <= temp_pv_size < 100:
        temp_subsidy = 1600 + temp_pv_size*340
    if temp_pv_size >= 100:
        temp_subsidy = 1400 + temp_pv_size*300
    list_temp_pv_subsidy.append(temp_subsidy)

Combos_Info_DUP_TOP4['Community_PV_Subsidy'] = list_temp_pv_subsidy   

#%%
Combos_Info_DUP_TOP4.to_pickle('Duplicate_Combinations_TOP4_All_Info.pickle')
Combos_Info_DUP_TOP4.to_csv(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\Duplicate_Combinations_TOP4_All_Info.csv')
#%% adding community IDs to Combos_Info
Combos_Info = pd.read_pickle('Combinations_All_Info.pickle')
#Combos_Info['Community_ID'] = ""
temp_comm_id_list = []
temp_plot_id = Combos_Info.loc['Z0054_Z0055']['Plot_ID']
for i in list(Combos_Info.index):
    for j in list(Combos_Info.Plot_ID):    
        if temp_plot_id == j:
            ctr += 1

# this did not work, DONE IN ANOTHER FILE - community_IDs
            

            

 
#%% save to pickle
import pickle 

#Combos_Info.to_pickle('Duplicate_Combinations_All_Info.pickle')
Combos_Info.to_pickle('50_reduced_PV_Combinations_All_Info.pickle')
Combos_Info.to_csv(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\Combinations_All_Info.csv')
    
#%%

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
