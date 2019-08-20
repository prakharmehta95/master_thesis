# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%

import pandas as pd
from datetime import timedelta, date



#%%


agent_areas = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Building_Data\LIST_AGENTS_FINAL.xlsx')
agent_list_final = list(agent_areas.Bldg_IDs)
agent_areas = agent_areas.set_index("Bldg_IDs")

#import demands
df_demand_sys = pd.DataFrame(data = None)
df_demand_cool = pd.DataFrame(data = None)
heat_gain_epd = pd.DataFrame(data = None)
heat_gain_lpd = pd.DataFrame(data = None)
heat_gain_procd = pd.DataFrame(data = None)
heat_gain_od_sens = pd.DataFrame(data = None)
heat_gain_od_lat = pd.DataFrame(data = None)
heat_gain_od = pd.DataFrame(data = None)

for FileList in agent_list_final:
    print(FileList)
    zz = pd.read_csv(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\CEA Data\Sample 1650\outputs\data\demand\\" + FileList + '.csv')
    df_demand_sys[FileList] = ""
    df_demand_sys[FileList] = zz.E_sys_kWh
    df_demand_cool[FileList] = ""
    df_demand_cool[FileList] = zz.E_cs_kWh
    heat_gain_epd[FileList] = ""
    heat_gain_lpd[FileList] = ""
    heat_gain_od_sens[FileList] = ""
    heat_gain_od_lat[FileList] = ""
    heat_gain_epd[FileList] = zz.Q_gain_sen_app_kWh
    heat_gain_lpd[FileList] = zz.Q_gain_sen_light_kWh
    heat_gain_procd[FileList] = zz.Q_gain_sen_pro_kWh
    heat_gain_od_sens[FileList] = zz.Q_gain_sen_peop_kWh
    heat_gain_od_lat[FileList] = zz.Q_gain_lat_peop_kWh
    heat_gain_od[FileList] = zz.Q_gain_sen_peop_kWh + zz.Q_gain_lat_peop_kWh
    
#%%
og_bldg_stock = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Building_Data\OG_Wdkon_Bldg_Stock_Stats.xlsx')
og_bldg_stock = og_bldg_stock.set_index("EGID")
#og_bldg_stock.index = og_bldg_stock.index.map(str)
has_cooling = og_bldg_stock.has_elec_cooling #binary for bldgs - have or do not have electric cooling systems

zones_splits =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Building_Data\Buildings_EGIDs_Each_zone_v1.xlsx')
key_xfmn_bldgtype = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Key_StadtZurich_to_CEA.xlsx')
key_xfmn_bldgtype = key_xfmn_bldgtype.set_index('Type')

load_density =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Internal_Loads.xlsx')
load_density = load_density.set_index('CEA_Type')

#Probabilities of occupancy, elec, appliance
Prob_Gym        =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Gym.xlsx')
Prob_Hospital   =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Hospital.xlsx')
Prob_Hotel      =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Hotel.xlsx')
Prob_Industrial =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Industrial.xlsx')
Prob_Library    =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Library.xlsx')
Prob_Multi_Res  =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Multi_Res.xlsx')
Prob_Single_Res =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Single_Res.xlsx')
Prob_Office     =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Office.xlsx')
Prob_Parking    =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Parking.xlsx')
Prob_Restaurant =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Restaurant.xlsx')
Prob_Retail     =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Retail.xlsx')
Prob_School     =  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_School.xlsx')
Prob_Use_Monthly=  pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\Excel_Databases\Occupancy_Probabilities\Prob_Use_Monthly.xlsx')

#set index
Prob_Gym        = Prob_Gym.set_index('Hour')
Prob_Hospital   = Prob_Hospital.set_index('Hour')
Prob_Hotel      = Prob_Hotel.set_index('Hour')
Prob_Industrial = Prob_Industrial.set_index('Hour')
Prob_Multi_Res  = Prob_Multi_Res.set_index('Hour')  
Prob_Single_Res = Prob_Single_Res.set_index('Hour')  
Prob_Office     = Prob_Office.set_index('Hour')  
Prob_Parking    = Prob_Parking.set_index('Hour')  
Prob_Restaurant = Prob_Restaurant.set_index('Hour')  
Prob_Retail     = Prob_Retail.set_index('Hour')  
Prob_School     = Prob_School.set_index('Hour')  
Prob_Use_Monthly= Prob_Use_Monthly.set_index('Months')

  

#%%
for i in ['Z0003']:#,'Z0005']:#agent_list_final:
    temp_zone_splits = zones_splits[i].dropna()   
       
    temp_df = og_bldg_stock.loc[temp_zone_splits,:]
    list_egids = temp_df.index.tolist()
    
    sum_nutzflache_area = temp_df.sum(skipna = True)
    
    kkk = sum_nutzflache_area.Nutzflache
        
    cea_area = agent_areas.loc[i]['Af_m2']
    temp_df['Area_CEA'] = ""
    temp_areas_list = []
    
    for j in list_egids:
        area_prop_cea = (temp_df.loc[j]['Nutzflache']/kkk)*cea_area
        temp_areas_list.append(area_prop_cea)
                
    temp_df['Area_CEA'] = temp_areas_list
    temp_df['CEA_Type'] = ""
    temp_bldg_type_list = []
    for j in list_egids:
        temp_bldg_type = temp_df.loc[j]['GdbArt1N']
        temp_bldg_type = key_xfmn_bldgtype.loc[temp_bldg_type]['CEA']
        temp_bldg_type_list.append(temp_bldg_type)
        
    temp_df['CEA_Type'] = temp_bldg_type_list
    
#    for j in temp_zone_splits:
 #       print(j)
  


    
#%% calculate power densities times probabilities for every hour of the year for every building type

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)
        
ctr = 0
column_names = load_density.index.tolist()
epd_year_prob = pd.DataFrame(data = None, index = range(0,8760), columns = column_names)    #equipment(appliance) elec power density 
lpd_year_prob = pd.DataFrame(data = None, index = range(0,8760), columns = column_names)    #lighting elec power density
procd_year_prob = pd.DataFrame(data = None, index = range(0,8760), columns = column_names)  #process elec power density
od_year_prob = pd.DataFrame(data = None, index = range(0,8760), columns = column_names)     #occupant density, NOT elec power density - used for cooling demand only

for bldg_type in column_names:
    print("Building Type =",bldg_type)
    #choice of Prob_xxxx dataframe
    if bldg_type == 'GYM':
        prob_df = Prob_Gym
    elif bldg_type == 'HOSPITAL':
        prob_df = Prob_Hospital
    elif bldg_type == 'HOTEL':
        prob_df = Prob_Hotel
    elif bldg_type == 'INDUSTRIAL':
        prob_df = Prob_Industrial
    elif bldg_type == 'MULTI_RES':
        prob_df = Prob_Multi_Res
    elif bldg_type == 'OFFICE':
        prob_df = Prob_Office
    elif bldg_type == 'PARKING':
        prob_df = Prob_Parking
    elif bldg_type == 'RESTAURANT':
        prob_df = Prob_Restaurant
    elif bldg_type == 'RETAIL':
        prob_df = Prob_Retail
    elif bldg_type == 'SCHOOL':
        prob_df = Prob_School
    elif bldg_type == 'SINGLE_RES':
        prob_df = Prob_Single_Res

    
    epd_list = []
    lpd_list = []
    procd_list = []
    od_list = []
    start_date = date(2005, 1, 1)
    end_date = date(2006, 1, 1)
    for single_date in daterange(start_date, end_date):
        #print(single_date.strftime("%Y-%m-%d"))
        #print("Month of the year = ",single_date.strftime("%m"))
        #print("Day of the week = ",single_date.strftime("%w"))
        day = int(single_date.strftime("%w"))
        month = int(single_date.strftime("%m"))
        monthly_prob = Prob_Use_Monthly[bldg_type][month]
        for hour in range(1,25):
            #print(hour)       
            print("ctr = ",ctr)
            #print("demand = ",df_demand_sys['Z0003'][ctr])
            ctr = ctr + 1
            if day == 0: #sunday
                epd     = load_density['Ea_Wm2'][bldg_type]*prob_df['Sun_LA'][hour]*monthly_prob
                lpd     = load_density['El_Wm2'][bldg_type]*prob_df['Sun_LA'][hour]*monthly_prob
                procd   = load_density['Epro_Wm2'][bldg_type]*prob_df['Sun_Proc'][hour]*monthly_prob
                od      = load_density['Occup_m2p'][bldg_type]*prob_df['Sun'][hour]*monthly_prob
            if day == 6: #saturday
                epd     = load_density['Ea_Wm2'][bldg_type]*prob_df['Sat_LA'][hour]*monthly_prob
                lpd     = load_density['El_Wm2'][bldg_type]*prob_df['Sat_LA'][hour]*monthly_prob
                procd   = load_density['Epro_Wm2'][bldg_type]*prob_df['Sat_Proc'][hour]*monthly_prob
                od      = load_density['Occup_m2p'][bldg_type]*prob_df['Sat'][hour]*monthly_prob
            if day > 0 and day < 6 : #weekday
                epd     = load_density['Ea_Wm2'][bldg_type]*prob_df['Week_LA'][hour]*monthly_prob
                lpd     = load_density['El_Wm2'][bldg_type]*prob_df['Week_LA'][hour]*monthly_prob
                procd   = load_density['Epro_Wm2'][bldg_type]*prob_df['Week_Proc'][hour]*monthly_prob
                od      = load_density['Occup_m2p'][bldg_type]*prob_df['Week'][hour]*monthly_prob
            
            epd_list.append(epd)
            lpd_list.append(lpd)
            procd_list.append(procd)
            od_list.append(od)
            
    epd_year_prob[bldg_type]    = epd_list
    lpd_year_prob[bldg_type]    = lpd_list
    procd_year_prob[bldg_type]  = procd_list
    od_year_prob[bldg_type]     = od_list

    
  
#%% calculating the demands myself - initial calculations for the ratios



#ctr = 0
disagg_CEA_elec_final = pd.DataFrame(data = None)
disagg_CEA_cool_final = pd.DataFrame(data = None)
temp_total_gains = pd.DataFrame(data = None)

#loop over zones
for zone in agent_list_final:#['Z1757']:#['Z1753','Z1754','Z1755','Z1756','Z1757','Z1758','Z1759','Z1760','Z1761','Z1762','Z1763','Z1764','Z1765']:#agent_list_final:
    #print(zone)
    
    #COOLING--------------
    temp_total_gains["Total_gains"] = ""
    temp_total_gains["Total_gains"] = heat_gain_epd[zone] + heat_gain_lpd[zone] + heat_gain_procd[zone] + heat_gain_od[zone]
    temp_total_gains["epd_frac"] = ""
    temp_total_gains["lpd_frac"] = ""
    temp_total_gains["procd_frac"] = ""
    temp_total_gains["od_frac"] = ""
    temp_total_gains["epd_frac"]    = heat_gain_epd[zone]/temp_total_gains["Total_gains"]
    temp_total_gains["lpd_frac"]    = heat_gain_lpd[zone]/temp_total_gains["Total_gains"]
    temp_total_gains["procd_frac"]  = heat_gain_procd[zone]/temp_total_gains["Total_gains"]
    temp_total_gains["od_frac"]     = heat_gain_od[zone]/temp_total_gains["Total_gains"]
    
    
    
    #ELEC_SYS------------
    temp_zone_splits = zones_splits[zone].dropna()   
    temp_egids = og_bldg_stock.loc[temp_zone_splits,:]
    list_egids = temp_egids.index.tolist()
    check_areas = temp_egids.Nutzflache.tolist()
    sum_nutzflache_area = temp_egids.sum(skipna = True)
    if all(i > 0 for i in check_areas):
        total_area = sum_nutzflache_area.Nutzflache
    else:
        total_area = sum_nutzflache_area.Grundflache_EG
        print(zone)
    
    cea_area = agent_areas.loc[zone]['Af_m2']
    #print("cea_area = ",cea_area)
    temp_egids['Area_CEA'] = ""
    temp_areas_list = []
    
    for j in list_egids:
        if cea_area != 0:
            if all(i > 0 for i in check_areas):
                area_prop_cea = (temp_egids.loc[j]['Nutzflache']/total_area)*cea_area
                temp_areas_list.append(area_prop_cea)
            else:
                area_prop_cea = (temp_egids.loc[j]['Grundflache_EG']/total_area)*cea_area
                temp_areas_list.append(area_prop_cea)
        else:
            if all(i > 0 for i in check_areas):
                area_prop_cea = temp_egids.loc[j]['Nutzflache']
                temp_areas_list.append(area_prop_cea)
            else:
                area_prop_cea = temp_egids.loc[j]['Grundflache_EG']
                temp_areas_list.append(area_prop_cea)
                
    temp_egids['Area_CEA'] = temp_areas_list
    temp_egids['CEA_Type'] = ""
    temp_bldg_type_list = []
    for j in list_egids:
        temp_bldg_type = temp_egids.loc[j]['GdbArt1N']
        temp_bldg_type = key_xfmn_bldgtype.loc[temp_bldg_type]['CEA']
        temp_bldg_type_list.append(temp_bldg_type)
        
    temp_egids['CEA_Type'] = temp_bldg_type_list
    disagg_df = pd.DataFrame(data = None)
    disagg_wtdsum_cool_df = pd.DataFrame(data = None)
    sum_total_Esys = 0
    sum_totalwtdsum_Ecool = 0
    #loop over bldgs
    for bldg in list_egids:
        #print(bldg)
        bldgname = str(bldg)
        bldgtype = temp_egids['CEA_Type'][bldg]
        bldgarea = temp_egids['Area_CEA'][bldg]
        #print("bldgarea = ",bldgarea)
        temp_epd_name = 'epd_' + bldgname
        temp_lpd_name = 'lpd_' + bldgname
        temp_procd_name = 'procd_' + bldgname 
        temp_od_name = 'od_' + bldgname
        temp_total_Esys_name = 'total_' + bldgname
        disagg_df[temp_epd_name] = ""
        disagg_df[temp_lpd_name] = ""
        disagg_df[temp_procd_name] = ""
        disagg_df[temp_od_name] = ""
        disagg_df[temp_total_Esys_name] = ""
        disagg_df[temp_epd_name]    = epd_year_prob[bldgtype]*bldgarea
        disagg_df[temp_lpd_name]    = lpd_year_prob[bldgtype]*bldgarea
        disagg_df[temp_procd_name]  = procd_year_prob[bldgtype]*bldgarea 
        disagg_df[temp_od_name]     = od_year_prob[bldgtype]*bldgarea
        disagg_df[temp_total_Esys_name] = disagg_df[temp_epd_name] + disagg_df[temp_lpd_name]+disagg_df[temp_procd_name]
        sum_total_Esys = sum_total_Esys + disagg_df[temp_total_Esys_name]
    
        #COOOLING---------
        disagg_wtdsum_cool_df[bldgname] = ""
        disagg_wtdsum_cool_df[bldgname] = (disagg_df[temp_epd_name]*temp_total_gains["epd_frac"] + disagg_df[temp_lpd_name]*temp_total_gains["lpd_frac"] + 
                                             disagg_df[temp_procd_name]*temp_total_gains["procd_frac"] + disagg_df[temp_od_name]*temp_total_gains["od_frac"])
        sum_totalwtdsum_Ecool = sum_totalwtdsum_Ecool + disagg_wtdsum_cool_df[bldgname]
    
    
    
    disagg_df['total_Esys_disagg'] = ""
    disagg_df['total_Esys_disagg'] = sum_total_Esys
    disagg_wtdsum_cool_df['total_Ecool_wtdsum'] = ""
    disagg_wtdsum_cool_df['total_Ecool_wtdsum'] = sum_totalwtdsum_Ecool
    
    
    disagg_elec_ratios = pd.DataFrame(data = None)
    disagg_cool_ratios = pd.DataFrame(data = None)
    for bldg in list_egids:
        #print(bldg)
        bldgname = str(bldg)
        temp_ratio_name = 'ratio_' + bldgname
        temp_total_Esys_name = 'total_' + bldgname
        disagg_elec_ratios[bldg] = ""
        disagg_elec_ratios[bldg] = disagg_df[temp_total_Esys_name]/disagg_df['total_Esys_disagg']
        disagg_elec_ratios = disagg_elec_ratios.fillna(0)
        disagg_CEA_elec_final[bldg] = ""
        disagg_CEA_elec_final[bldg] = disagg_elec_ratios[bldg]*df_demand_sys[zone]
    
        #COOLING------
        disagg_cool_ratios[bldg] = ""
        disagg_cool_ratios[bldg] = disagg_wtdsum_cool_df[bldgname]/disagg_wtdsum_cool_df['total_Ecool_wtdsum']
        disagg_cool_ratios = disagg_cool_ratios.fillna(0)
        disagg_CEA_cool_final[bldg] = ""
        disagg_CEA_cool_final[bldg] = disagg_cool_ratios[bldg]*has_cooling[bldg]*df_demand_cool[zone]
    
#disagg_CEA_final.to_excel(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\CEA_Disaggregated_E_sys.xlsx')    
#disagg_CEA_final.to_pickle(r'C:\Users\iA\OneDrive - ETHZ\RA_SusTec\CEA_Disaggregation\Codes\CEA_Disaggregated_E_sys.pickle')
    
    
    
#%% checking for nans
        
        
nulls = disagg_CEA_cool_final.columns[disagg_CEA_cool_final.isna().any()].tolist()

nullbldgs = og_bldg_stock.loc[nulls,:]
null_index = nullbldgs.index
df_result = pd.DataFrame(disagg_CEA_cool_final, columns=null_index)
df_result_zones = pd.DataFrame(zones_splits, columns=null_index)
    
    
    
    
#%% for cooling electricity demand df_demand_cool

cols = disagg_CEA_cool_final.columns
bt = disagg_CEA_cool_final.apply(lambda x: x > 0)
bt.apply(lambda x: list(cols[x.values]), axis=1) 

res = disagg_CEA_cool_final[disagg_CEA_cool_final!=0].stack()
#%%
sum_cool = pd.DataFrame(data = None)

for i in list_egids:
    print(i)
    sum_cool[i] = ""
    su = 0
    su = disagg_CEA_cool_final.loc[:,i].sum()
    if su > 0.0:
        print(i)
#%%
mylist = []
x = disagg_df.loc[:, disagg_df.columns.str.contains('epd'.join(mylist))]

x = disagg_df.loc[:, disagg_df.columns.str.contains('epd')]
    






    