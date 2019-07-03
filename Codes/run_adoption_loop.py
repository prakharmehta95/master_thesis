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

from adoption_8_NPV_vs_InvCosts import *
from adoption_8_NPV_vs_InvCosts import scenario


number = 1437 #number of agents
years = 5 #how long should the ABM run for
d_gini_correct = {}
d_gini_model_correct = {}
d_agents_info_runs_correct = {}
d_combos_info_runs_correct = {}
att_seed = 3 #seed for the attitude gauss function 
runs = 1
randomseed = 22 #used to set the order of shuffling of agents withing the scheduler

print("Did you change the name of the final pickle storage file?")
for j in range(runs):
    print("run = ",j,"----------------------------------------------------------------")
    randomseed = randomseed + j*642 #642 is just any number to change the seed for every run 
    test = tpb(number,randomseed) #initializes by callng the model and setting up with the class init methods
    att_seed = att_seed + j*10 #seed for attitude changes in a new run
#print(test.num_agents)
#print(test.datacollector)

#runs = 2
#seed(3)
#for k in range(runs):
#    seed(3)
    for i in range(years):
        seed(att_seed) #for the environmental attitude which remains constant for an agent in a particular run
        print("YEAR:",i+1)
        test.step()
        temp_name_3 = "agents_info_" + str(j) + "_" + str(i)
        temp_name_4 = "combos_info_" + str(j) + "_" + str(i)
        
        #stores info across multiple Years and multiple runs
        t1 = pd.DataFrame.copy(agents_info)
        t2 = pd.DataFrame.copy(Agents_Possibles_Combos)
        d_agents_info_runs_correct[temp_name_3] = t1#agents_info
        d_combos_info_runs_correct[temp_name_4] = t2#Agents_Possibles_Combos
    
    temp_name = "gini_" + str(j)
    temp_name_2 = "gini_model_" + str(j)
    gini = test.datacollector.get_agent_vars_dataframe()
    gini_model = test.datacollector.get_model_vars_dataframe()
    
    #stores information across multiple runs
    d_gini_correct[temp_name] = gini
    d_gini_model_correct[temp_name_2] = gini_model
    
    #from adoption_8 import agents_objects_list
#from adoption_8 import possible_community_members
#from adoption_8 import names_possible_combos_list
#from adoption_8 import g_df
#gini.head()
#print(gini)

#from adoption_8 import calling_list

#Export data to pickle to save it!
#%%
#f = open("03June_ZEV_d_agents_info.pickle","wb")
pickle.dump(d_agents_info_runs_correct,f)
f.close()
#f = open("03June_ZEV_d_gini.pickle","wb")
pickle.dump(d_gini_correct,f)
f.close()
#f = open("03June_ZEV_d_combos_info_runs.pickle","wb")
pickle.dump(d_combos_info_runs_correct,f)
f.close()
#f = open("03June_ZEV_d_gini_model.pickle","wb")
pickle.dump(d_gini_model_correct,f)
f.close()



end = time.time()
print("Code Execution Time = ",end - start)
