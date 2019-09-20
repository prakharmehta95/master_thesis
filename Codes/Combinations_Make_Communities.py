# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:37:34 2019

@author: iA
"""

import pandas as pd
import itertools

subplots_final = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_CLEAN_100MWh_TOP4.xlsx')
subplot_combos_dem = pd.DataFrame(data = None)
temp_df_dem = pd.DataFrame(data = None)

subplot_combos_solar = pd.DataFrame(data = None)
temp_df_solar = pd.DataFrame(data = None)

#MAKE THE COMBINED SOLAR AND DEMAND DATA
for i in list(subplots_final.columns):
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
                temp_df_dem = df_demand[i] #from NPV_Calculation code
                temp_df_solar = df_solar_AC[i]
                #print('m = ',m)
                for n in m:
                    temp_name = temp_name + '_' +n
                    temp_df_dem = temp_df_dem + df_demand[n]
                    temp_df_solar = temp_df_solar + df_solar_AC[n]
                print('temp_name = ',temp_name)
                subplot_combos_dem[temp_name] = ""
                subplot_combos_dem[temp_name] = temp_df_dem
                subplot_combos_solar[temp_name] = ""
                subplot_combos_solar[temp_name] = temp_df_solar
            
            

#% saving community combinbations in a pickle
subplot_combos_dem.to_pickle('Community_TOP4_Combos_Demand.pickle')
subplot_combos_solar.to_pickle('Community_TOP4_Combos_Solar.pickle')

#%%make copies of these dataframes

subplot_combos_dem_copy = subplot_combos_dem
subplot_combos_solar_copy = subplot_combos_solar

##%% dataframes read again for getting all 13086 combinations 
                
#subplot_combos_dem = pd.read_pickle('Community_Combos_Demand.pickle')
#subplot_combos_solar= pd.read_pickle('Community_Combos_Solar.pickle')




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


#%% finding repeated combinations
import time
start = time.time()

#for demand dataframe
temp_list_names = []
for i in range(len(list_combos_demand_names_strings)):
    temp_str_1 = list_combos_demand_names_strings[i]
    print(i)
    #print("Next string: ",temp_str_1)
    for j in range(i,len(list_combos_demand_names_strings)):
        if i == j:
            continue
        
        temp_str_2 = list_combos_demand_names_strings[j]
        if set(temp_str_1) == set(temp_str_2):
            temp_list_names.append(list_combos_demand_names[j])
            #subplot_combos_dem.drop(columns = [list_combos_demand_names[j]])
        
#%% finding repeated combinations do the same for the solar dataframe
temp_list_names = []
for i in range(len(list_combos_solar_names_strings)):
    temp_str_1 = list_combos_solar_names_strings[i]
    print(i)
    #print("Next string: ",temp_str_1)
    for j in range(i,len(list_combos_solar_names_strings)):
        if i == j:
            continue
        
        temp_str_2 = list_combos_solar_names_strings[j]
        if set(temp_str_1) == set(temp_str_2):
            temp_list_names.append(list_combos_solar_names[j])
            #subplot_combos_dem.drop(columns = [list_combos_demand_names[j]])
        
        
end = time.time()
timetaken = end - start
print("TIme = ",timetaken)


#%% delete same combinations

subplot_combos_dem = subplot_combos_dem.drop(columns = temp_list_names)
subplot_combos_solar = subplot_combos_solar.drop(columns = temp_list_names)
#%% check if the repeated names list occurs in the deleted combinations df. If all occur, that means they were indeed duplicates and the right
# columns have been removed
ctr = 0
for i in temp_list_names:
    if i in list_combos_solar_names:
        ctr = ctr + 1

print(ctr) #should be 0 else the deleting did not take place properly
    
#%% export the possible combinations to a pickle and to a csv
import pickle
subplot_combos_dem.to_pickle('Community_TOP4_Combos_Demand_Clean.pickle')
subplot_combos_solar.to_pickle('Community_TOP4_Combos_Solar_Clean.pickle')

#infile = open('Community_Combos_Demand_Clean.pickle')
#clean versions without duplicates
#subplot_combos_dem = pd.read_pickle('Community_Combos_Demand_Clean.pickle')
#subplot_combos_solar = pd.read_pickle('Community_Combos_Solar_Clean.pickle')

#unclean versions with duplicates
#subplot_combos_dem = pd.read_pickle('Community_Combos_Demand.pickle')
#subplot_combos_solar = pd.read_pickle('Community_Combos_Solar.pickle')


#subplot_combos_dem.to_csv(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\Communities_Demands_Clean.csv')
#subplot_combos_solar.to_csv(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\Communities_Solar_Clean.csv')




#%%
for name in temp_list_names:
    subplot_combos_dem[name] = ""
    
#%%
temp_list_names_strings = []
for i in range(len(temp_list_names)):
    x = temp_list_names[i]
    temp_list_names_strings.append(x.split("_"))    
    
    
#%%
"""
since the NPV calculations did not contain the names of the duplicates(for faster calculations) and it is easier to have all the names,
hereI just compare the same names and assign the data to them
"""
    
Agents_Combos_NPVs = pd.read_pickle('Combos_nosubsidy_Agents_NPVs_Years.pickle')
Agents_Combos_Investment_Costs = pd.read_pickle('Combos_nosubsidy_Agents_TotalInvestmentCosts_Years.pickle')
Agents_Savings = pd.read_pickle('Combos_nosubsidy_Agents_Savings_Years.pickle')
Agents_NetSavings = pd.read_pickle('Combos_nosubsidy_Agents_NetSavings_Years.pickle')
Agents_OM_Costs = pd.read_pickle('Combos_nosubsidy_Agents_OM_Costs_Years.pickle')
Agents_Combos_PV_Investment_Costs = pd.read_pickle('Combos_nosubsidy_Agents_PVInvestmentCosts_Years.pickle')
Agents_Combos_Smart_Meter_Investment_Costs = pd.read_pickle('Combos_nosubsidy_Agents_SmartMeterCosts_Years.pickle')
Combinations_All_Info = pd.read_pickle('Combinations_All_Info.pickle')

#%%

list_combos_NPVs_names = list(Agents_Combos_NPVs.columns)
list_combos_NPVs_names_strings = []
for i in range(len(list_combos_NPVs_names)):
    x = list_combos_NPVs_names[i]
    list_combos_NPVs_names_strings.append(x.split("_")) 

#%% making sure that duplicates are actually not deleted from the dataframes, so including them again
temp_list_NPVs_names = []
for i in range(len(list_combos_NPVs_names_strings)):
#for i in range(20):
    temp_str_1 = list_combos_NPVs_names_strings[i]
    print(i) 
    #print("Next string: ",temp_str_1)
    for j in range(len(temp_list_names_strings)):
    #for j in range(50):    
        temp_str_2 = temp_list_names_strings[j]
        if set(temp_str_1) == set(temp_str_2):
            Agents_Combos_Investment_Costs[temp_list_names[j]] = ""
            Agents_Combos_Investment_Costs[temp_list_names[j]] = Agents_Combos_Investment_Costs[list_combos_NPVs_names[i]]
            #temp_list_NPVs_names.append(list_combos_NPVs_names[j])
    
#%% including duplicated again in investment costs 
for i in range(len(list_combos_NPVs_names_strings)):
#for i in range(20):
    temp_str_1 = list_combos_NPVs_names_strings[i]
    print(i)
    #print("Next string: ",temp_str_1)
    for j in range(len(temp_list_names_strings)):
    #for j in range(50):    
        temp_str_2 = temp_list_names_strings[j]
        if set(temp_str_1) == set(temp_str_2):
            Agents_Combos_PV_Investment_Costs[temp_list_names[j]] = ""
            Agents_Combos_PV_Investment_Costs[temp_list_names[j]] = Agents_Combos_PV_Investment_Costs[list_combos_NPVs_names[i]]
            Agents_Combos_NPVs[temp_list_names[j]] = ""
            Agents_Combos_NPVs[temp_list_names[j]] = Agents_Combos_NPVs[list_combos_NPVs_names[i]]
            Agents_Combos_Smart_Meter_Investment_Costs[temp_list_names[j]] = ""
            Agents_Combos_Smart_Meter_Investment_Costs[temp_list_names[j]] = Agents_Combos_Smart_Meter_Investment_Costs[list_combos_NPVs_names[i]]
            
            

#%%
for i in range(len(list_combos_NPVs_names_strings)):
#for i in range(20):
    temp_str_1 = list_combos_NPVs_names_strings[i]
    print(i)
    #print("Next string: ",temp_str_1)
    for j in range(len(temp_list_names_strings)):
    #for j in range(50):    
        temp_str_2 = temp_list_names_strings[j]
        if set(temp_str_1) == set(temp_str_2):
            Agents_Combos_Smart_Meter_Investment_Costs[temp_list_names[j]] = ""
            Agents_Combos_Smart_Meter_Investment_Costs[temp_list_names[j]] = Agents_Combos_Smart_Meter_Investment_Costs[list_combos_NPVs_names[i]]
            #temp_list_NPVs_names.append(list_combos_NPVs_names[j])

#%% saving the files as pickle

Agents_Combos_NPVs.to_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_NPVs_Years.pickle')

Agents_Combos_Investment_Costs.to_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_TotalInvestmentCosts_Years.pickle')

#Agents_Savings.to_pickle('Duplicate_Combos_nosubsidy_Agents_Savings_Years.pickle')

#Agents_NetSavings.to_pickle('Duplicate_Combos_nosubsidy_Agents_NetSavings_Years.pickle')

#Agents_OM_Costs.to_pickle('Duplicate_Combos_nosubsidy_Agents_OM_Costs_Years.pickle')

Agents_Combos_PV_Investment_Costs.to_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_PVInvestmentCosts_Years.pickle')

Agents_Combos_Smart_Meter_Investment_Costs.to_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_SmartMeterCosts_Years.pickle')
    


#%% Duplicating these files as well to have ALL possible combinations
 
Combos_SCRs = Agents_SCRs.transpose()
Combos_EWZ_Costs = Agents_EWZ_Costs.transpose()
Combos_Savings = Agents_Savings.transpose()
Combos_NetSavings = Agents_NetSavings.transpose()
Combos_OM_Costs = Agents_OM_Costs.transpose()

for i in range(len(list_combos_NPVs_names_strings)):
#for i in range(20):
    temp_str_1 = list_combos_NPVs_names_strings[i]
    print(i)
    #print("Next string: ",temp_str_1)
    for j in range(len(temp_list_names_strings)):
    #for j in range(50):    
        temp_str_2 = temp_list_names_strings[j]
        if set(temp_str_1) == set(temp_str_2):
            Combos_EWZ_Costs[temp_list_names[j]] = ""
            Combos_EWZ_Costs[temp_list_names[j]] = Combos_EWZ_Costs[list_combos_NPVs_names[i]]
            Combos_Savings[temp_list_names[j]] = ""
            Combos_Savings[temp_list_names[j]] = Combos_Savings[list_combos_NPVs_names[i]]
            Combos_NetSavings[temp_list_names[j]] = ""
            Combos_NetSavings[temp_list_names[j]] = Combos_NetSavings[list_combos_NPVs_names[i]]
            Combos_OM_Costs[temp_list_names[j]] = ""
            Combos_OM_Costs[temp_list_names[j]] = Combos_OM_Costs[list_combos_NPVs_names[i]]
            Combos_SCRs[temp_list_names[j]] = ""
            Combos_SCRs[temp_list_names[j]] = Combos_SCRs[list_combos_NPVs_names[i]]

#%% writing to pickle files

Combos_EWZ_Costs.to_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_EWZ_Costs.pickle')
Combos_Savings.to_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_Savings_Years.pickle')
Combos_NetSavings.to_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_NetSavings_Years.pickle')
Combos_OM_Costs.to_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_OM_Costs_Years.pickle')
Combos_SCRs.to_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_SCRs.pickle')

#%% taking the original combinations info and changing the PV sizes and subsidy for it - easier than duplicating the pickle('50_reduced_PV_Combinations_All_Info.pickle')

combos_latest = pd.read_pickle('Duplicate_Combinations_All_Info_commIDs.pickle')

combos_latest.Community_PV_Size = (combos_latest.Community_PV_Size/2).astype(int)

combos_latest['Community_PV_Subsidy'] = 0
list_temp_pv_subsidy = []   
for i in list_combos_demand_names:
    temp_pv_size = combos_latest.loc[i]['Community_PV_Size'] 
    if temp_pv_size < 30:
        temp_subsidy = 1600 + temp_pv_size*460
    elif 30 <= temp_pv_size < 100:
        temp_subsidy = 1600 + temp_pv_size*340
    if temp_pv_size >= 100:
        temp_subsidy = 1400 + temp_pv_size*300
    list_temp_pv_subsidy.append(temp_subsidy)

combos_latest['Community_PV_Subsidy'] = list_temp_pv_subsidy   

#%% save to pickle

#all community info with PV sizes reduced by 50%
combos_latest.to_pickle('50_Duplicate_Combinations_All_Info_commIDs.pickle')

combos_latest = pd.read_pickle('50_Duplicate_Combinations_All_Info_commIDs.pickle')
