# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:23:37 2019

@author: Prakhar Mehta
"""

"""
Results on 14 May for ZEV regulations used att_seed = 3; randomseed == 22 to begin with
"""
#%%
import pandas as pd
import time
start = time.time()
import pickle

#%%
#import the main ABM code
#from adoption_8_NPV_vs_InvCosts import *
#from adoption_8_NPV_vs_InvCosts import scenario
"""
define all parameters here
"""

scenario = "TOP4_no100MWh_retail"


#%%
"""
NPV Calculation call from here - calculates the NPVs of individual buildings
"""
#define the costs etc here which are read in the NPV_Calculation file:::

PV_price_baseline   = pd.read_excel(r'C:\Users\prakh\OneDrive - ETHZ\Thesis\PM\Data\Solar PV Cost Projections\PV_Prices.xlsx')
fit_high            = 8.5/100 #CHF per kWH
fit_low             = 4.45/100 #CHF per kWH
ewz_high_large      = 6/100 #CHF per kWh
ewz_low_large       = 5/100 #CHF per kWh
ewz_high_small      = 24.3/100 #CHF per kWh
ewz_low_small       = 14.4/100 #CHF per kWh
ewz_solarsplit_fee  = 4/100 #CHF per kWH      

#PV Panel Properties
PV_lifetime = 25 #years
PV_degradation = 0.994 #(0.6% every year)
OM_Cost_rate = 0.06 # CHF per kWh of solar PV production
disc_rate = 0.05

import NPV_Calculation

#from NPV_Calculation import PV_lifetime_double as pv_life_double
from NPV_Calculation import Agents_NPVs as Agents_Ind_NPVs
from NPV_Calculation import Agents_SCRs as Agents_Ind_SCRs
from NPV_Calculation import Agents_Investment_Costs as Agents_Ind_Investments



#%%
"""
Agent information read from excel, pickles etc...
"""

#check what info to load!
if scenario == "ZEV" or scenario == "no_ZEV":
    agents_info = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Skeleton_Updated_lessthan100MWh_100%PV.xlsx')
elif scenario == "TOP4_no100MWh_retail" or scenario == "TOP4_no100MWh_wholesale":
    agents_info = pd.read_excel(r"C:\\Users\\prakh\\OneDrive - ETHZ\\Thesis\\PM\\Data_Prep_ABM\\Skeleton_Updated_No_100MWh_Restriction.xlsx")

#check this!
agent_list_final = pd.read_excel(r'C:\Users\prakh\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\LIST_AGENTS_FINAL.xlsx')

#%%
number = 1437   #number of agents
years = 1    #how long should the ABM run for - ideally, 18 years from 2018 - 2035

#empty dictionaries to store results
results_agentlevel = {}
results_emergent = {}
d_gini_correct = {}
d_gini_model_correct = {}
d_agents_info_runs_correct = {}
d_combos_info_runs_correct = {}

att_seed = 3        #initial seed for the attitude gauss function. Used to reproduce results.  
runs = 1          #no of runs. 100 for a typical ABM simulation in this work
randomseed = 22     #initial seed used to set the order of shuffling of agents withing the scheduler

print("Did you change the name of the final pickle storage file?") #so that my results are not overwritten!
from adoption_8_NPV_vs_InvCosts import *
from adoption_8_NPV_vs_InvCosts import scenario

#main loop for the ABM simulation
for j in range(runs):
    print("run = ",j,"----------------------------------------------------------------")
    randomseed = randomseed + j*642     #642 is just any number to change the seed for every run 
    test = tpb(number,randomseed)       #initializes by calling the model from adoption_8_NPV_vs_InvCosts and setting up with the class init methods
    att_seed = att_seed + j*10          #seed for attitude changes in a new run


    for i in range(years):
        seed(att_seed)                  #for the environmental attitude which remains constant for an agent in a particular run
        print("YEAR:",i+1)
        test.step()
        temp_name_3 = "agents_info_" + str(j) + "_" + str(i)
        temp_name_4 = "combos_info_" + str(j) + "_" + str(i)
        
        #stores results across multiple Years and multiple runs
        t1 = pd.DataFrame.copy(agents_info)
        t2 = pd.DataFrame.copy(Agents_Possibles_Combos)
        d_agents_info_runs_correct[temp_name_3] = t1#agents_info
        d_combos_info_runs_correct[temp_name_4] = t2#Agents_Possibles_Combos
    
    temp_name = "gini_" + str(j)
    temp_name_2 = "gini_model_" + str(j)
    gini = test.datacollector.get_agent_vars_dataframe()
    gini_model = test.datacollector.get_model_vars_dataframe()
    
    #stores results across multiple runs
    results_agentlevel[temp_name] = gini
    results_emergent[temp_name_2] = gini_model
    


#%% Export data to pickle to save it!

#f = open("03June_ZEV_d_agents_info.pickle","wb") #enter name of the stored result file
pickle.dump(d_agents_info_runs_correct,f)
f.close()

#f = open("03June_ZEV_d_gini.pickle","wb") #enter name of the stored result file
pickle.dump(results_agentlevel,f)
f.close()

#f = open("03June_ZEV_d_combos_info_runs.pickle","wb") #enter name of the stored result file
pickle.dump(d_combos_info_runs_correct,f)
f.close()

#f = open("03June_ZEV_d_gini_model.pickle","wb") #enter name of the stored result file
pickle.dump(results_emergent,f)
f.close()



end = time.time()
print("Code Execution Time = ",end - start)

