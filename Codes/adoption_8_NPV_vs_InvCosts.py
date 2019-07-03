# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:58:04 2019

@author: iA
"""

#%%
"""
Initial libraries and data import
"""

#useful packages to work with
import random 
from random import seed
from random import gauss
import json        
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import networkx as nx

#ABM Packages
from mesa import Agent, Model #base classes
from Scheduler_StagedActivation_Random import StagedActivation_random
from mesa.datacollection import DataCollector #for data collection, of course


#SCENARIO SETTING

#scenario = "ZEV" #100MWh criteria for forming communities and also community size limit of 100MWh
#scenario = "no_ZEV"
scenario = "TOP4_no100MWh"
#scenario = 2 #no 100MWh criteria but max 4 neighbours considered in forming the communities
#scenario = 'laptop_top4'

print(scenario)

    
if scenario == "ZEV":
    '''
    100% size, 100 MWh Restriction, 100 MWh Community Restriction
    '''
    #---------setting up on the iA computer WITH OLD ORIGINAL PV SIZES---------
    #INFORMATION on agents and all combinations
    #data = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Skeleton_Updated_OLD_PV_Sizes.xlsx')#test_agents_skeleton.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
    data = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Skeleton_Updated_lessthan100MWh_100%PV.xlsx')#test_agents_skeleton.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
    Agents_Possibles_Combos = pd.read_pickle('Duplicate_Combinations_All_Info_commIDs.pickle')
    
    #list of all possible subplots i.e. neighbours to form a community with
    #global subplots_final
    subplots_final = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_CLEAN_100MWh.xlsx') 
    
    #profitability index for individual agents
    profitability_index = pd.read_pickle(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Profitability_Index_SCALED_less_than_100MWh_Demand.pickle")
    
    #NPV information
    Agents_Ind_NPVs = pd.read_pickle('Agents_IND_nosubsidy_NPVs_Years.pickle')
    Agents_Community_NPVs = pd.read_pickle('Duplicate_Combos_nosubsidy_Agents_NPVs_Years.pickle')
    Agents_Ind_SCRs = pd.read_pickle('Agents_IND_nosubsidy_SCR_Years.pickle')
    Agents_Community_SCRs = pd.read_pickle('Duplicate_Combos_nosubsidy_Agents_SCRs_Years.pickle')
    Agents_Ind_Investments = pd.read_pickle('Agents_IND_nosubsidy_InvestmentCosts_Years.pickle')
    ZEV = 1 #binary variable to turn on/off whether to have ZEV/no ZEV
    comm_limit = 1 #limit of 100 MWh for community size applies
    
elif scenario == "no_ZEV":
    '''
    100% size, 100 MWh Restriction, Communities cannot be formed
    '''
    #---------setting up on the iA computer WITH OLD ORIGINAL PV SIZES---------
    #INFORMATION on agents and all combinations
    #data = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Skeleton_Updated_OLD_PV_Sizes.xlsx')#test_agents_skeleton.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
    data = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Skeleton_Updated_lessthan100MWh_100%PV.xlsx')#test_agents_skeleton.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
    Agents_Possibles_Combos = pd.read_pickle('Duplicate_Combinations_All_Info_commIDs.pickle')
    
    #list of all possible subplots i.e. neighbours to form a community with
    #global subplots_final
    subplots_final = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_CLEAN_100MWh.xlsx') 
    
    #profitability index for individual agents
    profitability_index = pd.read_pickle(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Profitability_Index_SCALED_less_than_100MWh_Demand.pickle")
    
    #NPV information
    Agents_Ind_NPVs = pd.read_pickle('Agents_IND_nosubsidy_NPVs_Years.pickle')
    Agents_Community_NPVs = pd.read_pickle('Duplicate_Combos_nosubsidy_Agents_NPVs_Years.pickle')
    Agents_Ind_SCRs = pd.read_pickle('Agents_IND_nosubsidy_SCR_Years.pickle')
    Agents_Community_SCRs = pd.read_pickle('Duplicate_Combos_nosubsidy_Agents_SCRs_Years.pickle')
    Agents_Ind_Investments = pd.read_pickle('Agents_IND_nosubsidy_InvestmentCosts_Years.pickle')
    ZEV = 0 #community can't even be formed
    comm_limit = 1 #just to be consistent with code, this won't be used as ZEV = 0 for this scenario

elif scenario == "TOP4_no100MWh":
    '''
    100% size, no 100 MWh Restriction BUT max 4 neighbours to form a community with
    '''
    
    #INFORMATION on agents and all combinations
    data = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Skeleton_Updated_No_100MWh_Restriction.xlsx')#test_agents_skeleton.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
    Agents_Possibles_Combos = pd.read_pickle('Duplicate_Combinations_TOP4_All_Info_commIDs.pickle')
    Agents_Possibles_Combos = Agents_Possibles_Combos.rename(index=str, columns={"Unnamed: 0": "Name_Comm",})
    Agents_Possibles_Combos = Agents_Possibles_Combos.set_index('Name_Comm')
    #list of all possible subplots i.e. neighbours to form a community with
    #global subplots_final
    subplots_final = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_CLEAN_100MWh_TOP4.xlsx') 
    
    #profitability index for individual agents
    profitability_index = pd.read_pickle(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Profitability_Index_Scaled.pickle")
       
    #NPV information
    Agents_Ind_NPVs = pd.read_pickle('Agents_IND_nosubsidy_NPVs_Years.pickle')
    Agents_Community_NPVs = pd.read_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_NPVs_Years.pickle')
    Agents_Ind_SCRs = pd.read_pickle('Agents_IND_nosubsidy_SCR_Years.pickle')
    Agents_Community_SCRs = pd.read_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_SCRs.pickle')
    Agents_Ind_Investments = pd.read_pickle('Agents_IND_nosubsidy_InvestmentCosts_Years.pickle')
    
    #wholesale
    #Agents_Community_NPVs = pd.read_pickle('Duplicate_Combos_TOP4_wholesale_nosubsidy_Agents_NPVs_Years.pickle')
    #Agents_Ind_NPVs = pd.read_pickle('Agents_IND_wholesale_nosubsidy_NPVs_Years.pickle')
    #profitability_index = pd.read_pickle(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Profitability_Index_SCALED_wholesale.pickle")
    
    
    ZEV = 1 # communities can be formed
    comm_limit = 0 #no 100 MWh limit for community size
    
elif scenario == 'laptop_top4':
    '''
    100% size, no 100 MWh Restriction BUT max 4 neighbours to form a community with
    '''
    
    #---------setting up on the laptop WITH OLD ORIGINAL PV SIZES---------
    #INFORMATION on agents and all combinations
    data = pd.read_excel (r'C:\Users\prakh\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Skeleton_Updated_No_100MWh_Restriction.xlsx')#test_agents_skeleton.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
    Agents_Possibles_Combos = pd.read_pickle('Duplicate_Combinations_TOP4_All_Info_commIDs.pickle')
    Agents_Possibles_Combos = Agents_Possibles_Combos.rename(index=str, columns={"Unnamed: 0": "Name_Comm",})
    Agents_Possibles_Combos = Agents_Possibles_Combos.set_index('Name_Comm')
    #list of all possible subplots i.e. neighbours to form a community with
    #global subplots_final
    subplots_final = pd.read_excel (r'C:\Users\prakh\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_CLEAN_100MWh_TOP4.xlsx') 
    
    #profitability index for individual agents
    profitability_index = pd.read_pickle(r"C:\Users\prakh\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Profitability_Index_Scaled.pickle")
    
    #NPV information
    Agents_Ind_NPVs = pd.read_pickle('Agents_IND_nosubsidy_NPVs_Years.pickle')
    Agents_Community_NPVs = pd.read_pickle('Duplicate_Combos_TOP4_nosubsidy_Agents_NPVs_Years.pickle')
    


# =============================================================================
# WILL NEED MORE CHANGES FOR THE SCENARIOS to run on the laptop
# #---------setting up on Prakhar's laptop---------
# #INFORMATION on agents and all combinations
# data = pd.read_excel (r'C:\Users\prakh\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Skeleton_Updated.xlsx')#test_agents_skeleton.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
# Agents_Possibles_Combos = pd.read_pickle('Duplicate_Combinations_All_Info_commIDs.pickle')
# 
# #list of all possible subplots i.e. neighbours to form a community with
# global subplots_final
# subplots_final = pd.read_excel (r'C:\Users\prakh\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\subplots_CLEAN_100MWh.xlsx') 
# 
# #profitability index for individual agents
# profitability_index = pd.read_pickle(r"C:\Users\prakh\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Profitability_Index_Scaled.pickle")
# 
# #NPV information
# Agents_Ind_NPVs = pd.read_pickle('Agents_IND_nosubsidy_NPVs_Years.pickle')
# Agents_Community_NPVs = pd.read_pickle('Duplicate_Combos_nosubsidy_Agents_NPVs_Years.pickle')
# 
# =============================================================================

list_agents = list(data.loc[:,'bldg_id'])

list_installed_solar_bldgs_100MWh = ['Z0115','Z1720','Z1721']
list_installed_solar_bldgs_ALL = ['Z0115', 'Z0360', 'Z0398', 'Z0401', 'Z0402', 'Z0691', 'Z1565', 'Z1717', 'Z1719', 'Z1720', 'Z1721' ] 

agents_info = data  #just a copy of original data
agents_info['intention'] = 0
agents_info['Comm_NPV'] = 0
agents_info['Ind_NPV'] = 0
agents_info['IDs'] = ""
agents_info['IDs'] = agents_info['bldg_id']
agents_info['Reason'] = ""
agents_info = agents_info.set_index('bldg_id')
agents_info['Ind_SCR'] = 0
agents_info['Comm_SCR'] = 0

#print("agents_info being set")
agents_info['Adopt_IND'] = 0        #saves 1 if INDIVIDUAL adoption occurs, else stays 0
agents_info['Adopt_COMM'] = 0       #saves 1 if COMMUNITY  adoption occurs, else stays 0
agents_info['Community_ID'] = ""    #community ID of the community formed
agents_info['En_Champ'] = 0         #saves who is the energy champion of that community
agents_info['Year'] = 0             #saves year of adoption

agents_subplots = subplots_final
#Agents_Possibles_Combos['Adopt'] = 0 #saves 1 if COMMUNITY adoption occurs, else stays 0
#Agents_Possibles_Combos['Year'] = 0  #saves year of adoption

#not being used as of now
community_formation = pd.DataFrame(data = None) 

#solar_sizes_adopted = pd.DataFrame(data = None, columns = ['Year1','Year2','Year3','Year4'])

#check if this is needed - I think I am not using it as on 10 May version
global solar_sizes_temp_var
solar_sizes_temp_var = 0

def make_swn():
    '''
    to make random groups of small world networks 
    '''
    
    temp_df = pd.DataFrame(data = None, index = range(20),columns = range(1437))
    print("make swn called")
    #I set the seed for the swn in the function! - always fixed!
    if scenario == "ZEV" or scenario == "no_ZEV":
        G = nx.watts_strogatz_graph(716,10,0.5,2)#swn function with 10 closest peers - Dunbar number?? Other REF?
        for i in range(716):
            #print(i)
            l = list(G.adj[i])
            if len(l) < 10:
                for j in range(10-len(l)):
                    l.append(np.nan)
            #temp_df[i] = ""
            temp_df[i] = pd.Series(list(G.adj[i]))
        
        swn_ref_Z0003 = pd.read_csv('SWN_List_less_100MWh.csv')#key of changing numbers to building names/IDs
        
        #dictionary to replace numbers of the watts-stratogatz function with actual building names
        di = swn_ref_Z0003.Circular_List.to_dict()
        temp_df = temp_df.rename(columns = di)
        swn = pd.DataFrame(data = None) #holds all swns for all agents
        swn = temp_df
    
    elif scenario == "TOP4_no100MWh":
        G = nx.watts_strogatz_graph(1437,10,0.5,2)#swn function with 10 closest peers - Dunbar number?? Other REF?
        for i in range(1437):
            #print(i)
            l = list(G.adj[i])
            if len(l) < 10:
                for j in range(10-len(l)):
                    l.append(np.nan)
            #temp_df[i] = ""
            temp_df[i] = pd.Series(list(G.adj[i]))
        
        swn_ref_Z0003 = pd.read_csv('SWN_List.csv')#key of changing numbers to building names/IDs
        
        #dictionary to replace numbers of the watts-stratogatz function with actual building names
        di = swn_ref_Z0003.Circular_List.to_dict()
        temp_df = temp_df.rename(columns = di)
        swn = pd.DataFrame(data = None) #holds all swns for all agents
        swn = temp_df
    
    for i in swn.columns:
        swn[i] = temp_df[i].map(di)
    return swn


agents_peers = make_swn()





#%% AGENT code

c = 0
step_ctr = 0
#agents_info['intention'] = ""
#agents_info.set_index('bldg_id')

class tpb_agent(Agent):
    """Class for the agents. Agents are initialised in init, and the step_idea
    and step_decision methods execute what the agents are supposed to do
    """
    def tpb_agent(self):
        self.adopt_ind
    def __init__(self,unique_id,model,bldg_type,attitude,pp,intention,intention_yr,
                 swn_ratio,subplot_effect,total,counter,adopt_ind,adopt_comm,adopt_year,part_comm,en_champ,pv_size,dem_total,egids):
        '''
        maybe also attributes like: adopt_ind,adopt_comm
        Agent initialization
        
        Agents have attributes:
            unique_id   = Agent unique identification (Z0000, Z0001,...)
            bldg_type   = Type of the building 
            attitude    = Environmental attitude [0,1]
            network     = all other agents in their small world network --> MAYBE DO NOT NEED THIS
            pp          = payback period ratio - indicator of economic attractiveness [0,1]
            intention   = initial idea to adopt/not adopt solar: BOOLEAN 0|1
            swn_ratio   = ratio of people in small world network who install solar [0,1]
            total       = sum of the intention, from the stage1_intention function [0,1]
            counter     = to know number of times the agent crosses intention. Initialize to 0, if 1 then go to stage2,else do not go to stage2
                            also - if 0 or >1, then do not count in subplot effects!
            adopt_ind   = if agent adopts individual system BOOLEAN 0|1
            adopt_comm  = if agent adopts community system BOOLEAN 0|1
            ind_size    = 
            comm_size   =
            en_champ    = if this agent is the energy champion or nor 
        
        '''
        global calling_list
        calling_list = []
        super().__init__(unique_id,model) 
        
        self.bldg_type = bldg_type
        self.attitude = attitude
        #self.network = network
        #hhh = econ_attr
        self.pp = econ_attr(self)#pp#hhh#econ_attr#pp
        self.intention = intention
        self.intention_yr = intention
        self.swn_ratio = swn_ratio
        self.subplot_effect = subplot_effect
        self.total = total
        self.counter = counter
        self.adopt_ind = adopt_ind
        self.adopt_comm = adopt_comm
        self.adopt_year = adopt_year
        self.part_comm = part_comm
        self.en_champ = en_champ
        self.pv_size = pv_size
        self.dem_total = dem_total
        self.egids = egids
        
          
        #check_peers(self,self.unique_id) #need to write an initial check_peers function.MAYBE NOT NEEDED AT ALL
        
        #to calculate the intention at the START of the program. THIS can be based on any of the 3 agent variables
        #maybe best to randomly assign solar decision to a few buildings at the start, irrespective of variables?
        #OR, could assign to some buildings which are high on environmental attitude
        #AS OF NOW, DONE WITH THE CURRENT INTENTION FUNCTION
        # done because - initialize some buildings as having solar
        #OKAY - BUT NEED ANOTHER INITIALIZATION FUNCTION. IF I USE THIS IT FUCKS UP THE OTHER PARTS OF THE CODE
        #stage1_intention(self,self.unique_id, self.attitude,self.pp,self.swn_ratio)
        
    def step_idea(self):
        '''
        defines what the agent does in his step.
        StagedActivation is used now, this is the first stage.
        IDEA/INTENTION developments happens in this case
        '''
        
        # only run the step_idea if agent has not already adopted!
        if self.adopt_comm == 1 or self.adopt_ind == 1:
            self.intention = 0#do it again to be safe
        else:
            #only  call the intention calculation if solar has not been installed
            #print("*")
            #print("start of new agent uid = ",self.unique_id, "has intention = ",self.intention)
            calling_list.append(self.unique_id)
            check_peers(self,self.unique_id)
            check_neighbours_subplots(self,self.unique_id)
            self.pp = econ_attr(self)
            #to update the attitude
            #self.attitude = env_attitude(self, self.unique_id, self.attitude) #to update the environmental attitude
            stage1_intention(self,self.unique_id, self.attitude,self.pp,self.swn_ratio,self.subplot_effect)
            #check_peers(self,self.unique_id)
            #print(agents_all_list)
            #print("Updated attitude is: ", self.attitude)
            #print("intention for", self.unique_id, "is: ", self.intention)
            #print("counter   for",self.unique_id, "is: ", self.counter)
            #print(step_ctr)
            #print("****")
        
        
    def step_decision(self):
        """
        After developing the intention in the step_idea, agents make the final
        decision in this method.
        The NPV ranking scheme is also called from this one
        """
        #stage1_intention(self,self.unique_id, self.attitude,self.pp,self.swn_ratio)
        #decision_making(self):
        
        #only those agents whose intention is HIGH can go to decision making
        if self.intention == 1:# and self.counter == 1:
            global r
            r = 0
            #print("step_decision")
            stage2_decision(self,self.unique_id,self.intention)
            #print("Solar at end of year",step_ctr," is = ",temp_solar_num)
        
#%% MODEL code
        
        
class tpb(Model):
    '''
    Model setup. The main ABM runs from here.
    Called the FIRST time when the execution happens. Agents are initiated
    '''    
    #ORIGINAL
    #global agents_objects_list
    #agents_objects_list = [] #list of initialized agents
    global list_datacollector
    list_datacollector = []
    calling_list = []
    c = 0
    #step_ctr = 0
    
    def __init__(self,N,randomseed):
        print("--TPB MODEL CALLED--")
        agents_info['Adopt_IND'] = 0        #saves 1 if INDIVIDUAL adoption occurs, else stays 0
        agents_info['Adopt_COMM'] = 0       #saves 1 if COMMUNITY  adoption occurs, else stays 0
        agents_info['Community_ID'] = ""    #community ID of the community formed
        agents_info['Year'] = 0
        Agents_Possibles_Combos['Adopt'] = 0 #saves 1 if COMMUNITY adoption occurs, else stays 0
        Agents_Possibles_Combos['Year'] = 0  #saves year of adoption

        
        super().__init__()
        self.num_agents = N
        self.randomseed = randomseed
        #self.schedule = RandomActivation(self) 
        #self.schedule = SimultaneousActivation(self) 
        self.schedule = StagedActivation_random(self,stage_list = ['step_idea','step_decision'],
                                             shuffle = True, shuffle_between_stages = True,seed = self.randomseed) 
        #only called once so the seed is the same, meaning the agents are shuffled the same way every time
        #print(list2)
        #NEW agent object list declaration
        global agents_objects_list
        agents_objects_list = [] #list of initialized agents
        
        
        global norm_dist_env_attitude_list
        global step_ctr
        step_ctr = 0
        global i
        for i in list_agents:#['Z0003','Z0004','Z0054','Z0055','Z0056','Z1987']:#list_agents:          #range(len(agents_info)):
            
            global c#, intention
            intention = 0
            intention_yr = 0
            ratio = 0
            total = 0
            counter = 0
            subplot_effect = 0
            adopt_ind = 0
            adopt_comm = 0
            adopt_year = 0
            part_comm = 0
            en_champ = 0
            
            #agent creation
            a = tpb_agent(agents_info.loc[i]['IDs'],self,agents_info.loc[i]['Building_Type_Category'],env_attitude(agents_info.loc[i]['IDs']),#gauss(0.6,0.2),#env_attitude,
                          0,intention,intention_yr,#econ_attr(self)
                          ratio,subplot_effect,total,counter,
                          adopt_ind,adopt_comm,adopt_year,agents_info.loc[i]['Part_Comm_YN'],en_champ,agents_info.loc[i]['PV_Size'],
                          agents_info.loc[i]['GRID_MWhyr'],agents_info.loc[i]['Num_EGIDs'])
            
            agents_objects_list.append(a)
            self.schedule.add(a)
            c = c + 1
        

        
        #data collection
        self.datacollector = DataCollector(model_reporters = {"Individual_solar":cumulate_solar_ind,"Ind_PV_Installed":cumulate_solar_ind_sizes,
                                                              "Community_solar":cumulate_solar_comm,"Energy_Champions":cumulate_solar_champions,
                                                              "Comm_PV_Installed":cumulate_solar_comm_sizes,
                                                              "Agent_Type_Res":agent_type_res,"Agent_Type_Res_PV_Size":agent_type_res_CAP,
                                                              "Agent_Type_Comm":agent_type_comm,"Agent_Type_Comm_PV_Size":agent_type_comm_CAP,
                                                              "Agent_Type_Pub":agent_type_pub,"Agent_Type_Pub_PV_Size":agent_type_pub_CAP,
                                                              "EGIDs_greater_than_one":zone_egids,"EGIDs_greater_than_one_SIZE":zone_egids_size},
                agent_reporters = {"Building_ID":"unique_id","Building_Type":"bldg_type","Part_Comm":"part_comm",
                                   "PV_Size":"pv_size","Demand_MWhyr":"dem_total","Intention" : "intention",
                                   "Yearly_Intention":"intention_yr","Attitude" : "attitude","Payback Period" : "pp",
                                   "SWN Ratio":"swn_ratio","Intention_Sum": "total","Subplot Effect":"subplot_effect",
                                   "Individual":"adopt_ind","Community":"adopt_comm","Year_Adoption":"adopt_year","Energy_Champion":"en_champ"})
        
        self.running = True
        
        
    def step(self):
        #self.datacollector.collect(self)
        self.schedule.step()
        self.datacollector.collect(self) #collects data at the end of the step/year
        
        global step_ctr #so that I have counter used to change attribures based on the year
        
        step_ctr += 1
        #print("Step counter = ", step_ctr)
    
#%% MORE FUNCTIONS 
def agent_type_res(model):
    '''
    to find total number of RESIDENTIAL individual adoptions
    '''
    sum_agent_type_res_ind = 0
    for i in model.schedule.agents:
        if i.bldg_type == 'Residential':
            sum_agent_type_res_ind = sum_agent_type_res_ind + i.adopt_ind
    return sum_agent_type_res_ind

def agent_type_res_CAP(model):
    '''
    to find total CAPACITY of RESIDENTIAL individual adoptions
    '''
    sum_agent_type_res_ind_cap = 0
    for i in model.schedule.agents:
        if i.bldg_type == 'Residential' and i.adopt_ind == 1:
            sum_agent_type_res_ind_cap = sum_agent_type_res_ind_cap + i.pv_size
    return sum_agent_type_res_ind_cap
    

def agent_type_comm(model):
    '''
    to find total number of COMMERCIAL individual adoptions
    '''
    sum_agent_type_comm_ind = 0
    for i in model.schedule.agents:
        if i.bldg_type == 'Commercial':
            sum_agent_type_comm_ind = sum_agent_type_comm_ind + i.adopt_ind
    return sum_agent_type_comm_ind


def agent_type_comm_CAP(model):
    '''
    to find total CAPACITY of COMMERCIAL individual adoptions
    '''
    sum_agent_type_comm_ind_cap = 0
    for i in model.schedule.agents:
        if i.bldg_type == 'Commercial' and i.adopt_ind == 1:
            sum_agent_type_comm_ind_cap = sum_agent_type_comm_ind_cap + i.pv_size
    return sum_agent_type_comm_ind_cap

def agent_type_pub(model):
    '''
    to find total number of PUBLIC individual adoptions
    '''
    sum_agent_type_pub_ind = 0
    for i in model.schedule.agents:
        if i.bldg_type == 'Public':
            sum_agent_type_pub_ind = sum_agent_type_pub_ind + i.adopt_ind
    return sum_agent_type_pub_ind

def agent_type_pub_CAP(model):
    '''
    to find total CAPACITY of PUBLIC individual adoptions
    '''
    sum_agent_type_pub_ind_cap = 0
    for i in model.schedule.agents:
        if i.bldg_type == 'Public' and i.adopt_ind == 1:
            sum_agent_type_pub_ind_cap = sum_agent_type_pub_ind_cap + i.pv_size
    return sum_agent_type_pub_ind_cap

def zone_egids(model):
    '''
    to know if an individual adoption is actually like a community because of the CEA ZONES
    '''
    sum_EGID = 0
    for i in model.schedule.agents:
        if i.egids > 1:
            sum_EGID = sum_EGID + i.adopt_ind
    return sum_EGID

def zone_egids_size(model):
    '''
    to know if an individual adoption is actually like a community because of the CEA ZONES, getting SIZES
    '''
    sum_EGID = 0
    for i in model.schedule.agents:
        if i.egids > 1 and i.adopt_ind == 1:
            sum_EGID = sum_EGID + i.pv_size
    return sum_EGID

def cumulate_solar_ind(model):
    """
    To find the cumulative INDIVIDUAL installations at the end of every time step
    """
    #print("Cumulate Solar entered%%%%%%%%%%%%%%%%%")
    solar_sum_ind = 0
    for i in model.schedule.agents:
        solar_sum_ind = solar_sum_ind + i.adopt_ind
    #print("solar sum = ",solar_sum_ind,"~~~~~~~~~~~~~")
    #print(i)
    return solar_sum_ind
        
def cumulate_solar_comm(model):
    """
    To find the cumulative COMMUNITY "ALL buildings with installations" at the end of every time step
    """
    #print("Cumulate Solar entered%%%%%%%%%%%%%%%%%")
    solar_sum_comm = 0
    for i in model.schedule.agents:
        solar_sum_comm = solar_sum_comm + i.adopt_comm
    #print("solar sum = ",solar_sum_comm,"~~~~~~~~~~~~~")
    return solar_sum_comm  

def cumulate_solar_champions(model):
    """
    To find the cumulative COMMUNITY installations at the end of every time step
    """
    #print("Cumulate Solar entered%%%%%%%%%%%%%%%%%")
    solar_sum_champ = 0
    for i in model.schedule.agents:
        solar_sum_champ = solar_sum_champ + i.en_champ
    #print("solar sum = ",solar_sum_champ,"~~~~~~~~~~~~~")
    return solar_sum_champ        

def cumulate_solar_ind_sizes(model):
    """
    To find the cumulative COMMUNITY solar capacity at the end of every time step
    """
    #print("Cumulate Solar entered%%%%%%%%%%%%%%%%%")
    solar_sum_sizes = 0
    
    for i in model.schedule.agents:
        if i.adopt_ind == 1:
            solar_sum_sizes = solar_sum_sizes + i.pv_size
    #print("solar sum = ",solar_sum_sizes,"~~~~~~~~~~~~~")
    return solar_sum_sizes
 
def cumulate_solar_comm_sizes(model):
    """
    To find the cumulative COMMUNITY solar capacity at the end of every time step
    """
    #print("Cumulate Solar entered%%%%%%%%%%%%%%%%%")
    
    solar_comm_sizes = 0
    for i in model.schedule.agents:
        if i.adopt_comm == 1:
            solar_comm_sizes = solar_comm_sizes + i.pv_size
    #print("solar sum = ",solar_comm_sizes,"~~~~~~~~~~~~~")
    return solar_comm_sizes


def env_attitude(uid):#(self, uid, attitude):
    """
    To change the environmental attitude depending on the steps.
    NOT TO BE CHANGED IN MODEL v1.0!
    """
    uid = uid
    
    #if minergie building then set env attitude high by default
    if agents_info.loc[uid]['MINERGIE'] == 1:
        value = 0.95
    else:
        value = gauss(0.698,0.18)
    if value > 1:
        value = 1 #to keep it from going over 1
    return value


def econ_attr(self):
    """
    To update the payback ratio every step
    Takes data from a base excel?
    Enter the source of that excel
    """
    #print(step_ctr)
    uid = self.unique_id
    try:
        self.pp = profitability_index.loc[step_ctr][uid]
    except KeyError:
        self.pp = 0
    
    if self.pp < 0:
        self.pp = 0
        
    return self.pp

def check_peers(self,uid):
    """
    Checks how many other agents in the -SWN- have installed solar
    sets agent attribute swn_ratio (self.swn_ratio) accordingly
    
    Uses:
        agents_peers (it is a DataFrame) - list of all people in the SWN of each building
    """
    #print("*")
    #print("Check peers called")
    swn_with_solar = 0
    #print("Initialize swn_with_solar for ",self.unique_id," = ",swn_with_solar)
    temp_list = []
    temp_list = agents_peers[uid].values.tolist() #make a list of all peers of that particular agent with uid
    #print(temp_list)
    
    """
    Explanation of the for loops coming ahead:
        each agent considered by referencing its self.unique_id (or uid)
        for z in temp_list() --> z becomes one of the peers of building 'uid' 
            I run the next for loop in the range of all the agents:
                IF an agent has the same unique_id as z i.e. I have found peer#1 of 'uid'
                in the list of all agents then:
                    if the intention of that peer#1 is 1, advance count of swn_with_solar.
        Loop runs for all the peers which 'uid' has
        
        THEN - swn_ratio is calculated as:
            all peers in the swn with solar/all peers in the swn 
    """
    
    for z in temp_list:
        for y in range(len(agents_objects_list)): #checking all other agents in the simulation 
            if agents_objects_list[y].unique_id == z:
                #print("uid of peer = ",agents_objects_list[y].unique_id, "adopted solar = ", agents_objects_list[y].adopt_ind)
                
                if agents_objects_list[y].adopt_ind == 1 or agents_objects_list[y].adopt_comm == 1: 
                    swn_with_solar = swn_with_solar + 1
    
    #print("swn_with_solar = ",swn_with_solar)
    self.swn_ratio = (swn_with_solar/len(agents_peers.loc[:,self.unique_id]))
                     
def check_neighbours_subplots(self,uid):
    """
    Checks how many other agents in the --subplot = NEIGHBOURS-- have INTENTION/IDEA of installing solar
    sets agent attribute subplot_effect (self.subplot_effect) accordingly
    **WORKING WITH INTENTION as this is subplot peers**
    
    Uses:
        agents_subplots (it is a DataFrame) - list of all agents in the subplot of each building
    """
    if uid in agents_subplots.columns:
        temp_list_subplots = agents_subplots[uid].dropna().values.tolist()
        
        """
        Explanation of the for loops coming ahead:
            each agent considered by referencing its self.unique_id (or uid)
            for z in temp_list_subplots() --> z becomes one of the peers of building 'uid' 
                IF a neighbour has positive intention then:
                    advance subplot_effect_counter.
            Loop runs for all the neighbours which 'uid' has
            
            THEN - swn_ratio is calculated as:
                all peers in the swn with solar/all peers in the swn 
        """
        
        #initialize the counter to 0. This is to see how many of subplot neighbouts in total have intented to adopt solar this year
        subplot_effect_counter = 0
        
        for z in temp_list_subplots:
            for y in range(len(agents_objects_list)):
                if agents_objects_list[y].unique_id == z:
                    #print("bldg considered = ",uid, "intention of neighbour ", z, "is = ",agents_objects_list[y].intention)
                    if (agents_objects_list[y].intention == 1 and agents_objects_list[y].counter == 1):
                        #print("~~bldg considered = ",uid, "intention of neighbour ", z, "is = ",agents_objects_list[y].intention)
                        subplot_effect_counter += 1
            
        self.subplot_effect = (subplot_effect_counter/len(temp_list_subplots)) 
        #print("subplot_effect = ",self.subplot_effect)
    
 
#%%


import itertools

def stage1_intention(self, uid, attitude, pp,ratio,subplot_effect):
    """
    Intention development at the end of stage 1
    Considers the environmental attitude, payback period ratio and the swn_ratio
    Final intention at the end of every step saved as self.intention
    """
    
    if self.dem_total < 100000000000:# and self.egids == 1:# and self.pv_size < 10000001:# and self.part_comm == 1:
        #weights and thresholds for the intention function
        w_econ = 1/3
        w_swn = 1/3
        w_att = 1/3 #this needs to be varied for the sensitivity analysis
        w_subplot = 0.1
        threshold = 0.5
        
        #the basic intention function:
        total = w_att*attitude + w_econ*pp + w_swn*ratio + w_subplot*subplot_effect
        #print(total)
        self.total = total
        
        if scenario == "ZEV" or scenario == "no_ZEV":
            if self.unique_id in list_installed_solar_bldgs_100MWh:
                print(self.unique_id)
                total = 1
                self.total = total
                self.intention = 1
        elif scenario == "TOP4_no100MWh":
            if self.unique_id in list_installed_solar_bldgs_ALL:
                print(self.unique_id)
                total = 1
                self.total = total
                self.intention = 1
            
            
        if total > threshold:
            intention = 1
            #agents_info.update(pd.Series([intention], name  = 'intention', index = [uid]))
            #agents_info.loc[uid]['Solar'] = solar
            self.counter = self.counter + 1
            self.intention = intention
            self.intention_yr = intention
            #return self.intention
        else:
            intention = 0
            #agents_info.update(pd.Series([intention], name  = 'intention', index = [uid]))
            #agents_info.loc[uid]['Solar'] = solar
            self.intention = intention
            self.intention_yr = intention
            #agents_all_list.update(pd.Series([intention], name = 'Adoption Decision', index = [uid]))
            #return self.intention
            if step_ctr == 17:
                agents_info.update(pd.Series([0], name  = 'Adopt_IND', index = [self.unique_id]))
                agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                #agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                agents_info.update(pd.Series(["Intention<threshold"], name  = 'Reason', index = [self.unique_id]))
    else:
        self.intention = 0
    

def stage2_decision(self,uid,idea):
    """
    Decision made here after passing the intention stage
    """
    #print("STAGE 2 ENTERED...............................................")
    reduction = -0.0
    agents_adopting_community_list = []
    global solar_sizes_temp_var
    ind_npv = Agents_Ind_NPVs.loc[step_ctr][self.unique_id]
    
    if self.intention == 1 and (self.unique_id not in list_installed_solar_bldgs_ALL):
        '''
        let's say building A has passed
        it checks all the possible options
        starting from the best NPV, it checks if the other buildings have positive intention as well
        then it takes best NPV 
        --> if that is individual, then cool, end of case, adopt individual
        --> else if it involves other buildings then check if their ranks are among top 3, if yes then already include them as
            the community adoption.
            WHEN those buildings will be the agents making decisions, then if they have already said yes to a community system,
            then do not do the ranking etc for them, simply skip them... :)
        '''
        #
        temp_id = self.unique_id
        #find the npv to save it with the agent when he adopts
        
        #for teh agents which can actually form communities
        if self.part_comm == 1 and ZEV == 1:
            
            hh = []
            hhh =[]
            for i in range(len(agents_objects_list)):
                hh.append(agents_objects_list[i].unique_id)
                hhh.append(agents_objects_list[i].intention_yr)
                #print(agents_objects_list[i].unique_id)
                #print(agents_objects_list[i].intention_yr)
            
            zzz = pd.DataFrame(data = None) #temporary dataframe to hold agent information about intention
            zzz['unique_id'] = hh
            zzz['intention_yr'] = hhh
            zzz.set_index('unique_id')
            
            all_positive_intention_agents = zzz[zzz['intention_yr'] == 1]
            list_all_positive_intention_agents = all_positive_intention_agents.unique_id.tolist()
            pos_intent_comm_members = []
            
            possible_community_members_all = subplots_final[temp_id].dropna().values.tolist()
            
            #drop those which have already formed a community!
            possible_community_members = []
            for k in possible_community_members_all:
                for j in range(len(agents_objects_list)):
                    if k == agents_objects_list[j].unique_id:
                        if  agents_objects_list[j].adopt_ind == 1 or agents_objects_list[j].adopt_comm == 1:
                            continue #do nothing 
                        elif agents_objects_list[j].adopt_ind == 0 and agents_objects_list[j].adopt_comm == 0:
                            possible_community_members.append(k)
           
            for k in possible_community_members:
                if k in list_all_positive_intention_agents:
                    pos_intent_comm_members.append(k) #community members with positive intentions who can potentially form a community
            
            temp_pos_combos_list = []
            names_possible_combos_list = []
            
            #making the possible combinations with the agents who passed intention and who can form the community 
            for j in range(0,len(pos_intent_comm_members)):
                temp_pos_combos = list(itertools.combinations(pos_intent_comm_members,len(pos_intent_comm_members)-j))
                temp_pos_combos_list.append(temp_pos_combos)
                
                for k in range(len(temp_pos_combos_list)):
                    for m in temp_pos_combos_list[k]:
                        temp_name = temp_id #take name of building here
                        for n in m:
                            temp_name = temp_name + '_' +n
                        names_possible_combos_list.append(temp_name) #all possible combos which can be formed this year
            
            #g_df = dataframe to hold which combos can exist and which have positive NPVs
            g_df = pd.DataFrame(data = None,index = range(1))
            #for loop to find which of the combos can actually exist and which have positive NPVs
            for g in names_possible_combos_list:
                if g in list(Agents_Community_NPVs.columns):
                    if Agents_Community_NPVs.loc[step_ctr][g] > 0:
                        g_df[g] = ""
                        g_df.update(pd.Series([Agents_Community_NPVs.loc[step_ctr][g]], name  = g, index = [0]))
                        
            npvs_list = pd.DataFrame(data = None)
            npvs_list = g_df.loc[0,:] #take the 1st row of the temporary g_df dataframe as it contains all NPVs of all possible combinations
            npvs_list2 = pd.to_numeric(npvs_list)#, errors = 'coerce', axis=0)
            
            #check if there are communities which can be formed after all the filtering I have done previously
            if len(npvs_list) != 0:
                max_combo_npv = npvs_list2.idxmax(axis=1) #this is the community with the maximum positive NPV!
                                
                #*****NOW COMES THE ACTUAL COMMUNITY FORMATIONS*****
                #ZEV and no_ZEV scenario - only case where a community formation can be considered
                if Agents_Community_NPVs.loc[step_ctr][max_combo_npv] > 0 and comm_limit == 1 and Agents_Possibles_Combos.loc[max_combo_npv]['Demand_Year_MWh'] < 100:#) if scen_11 == 1 else True): #extra if is to neglect or consider community sizes
                    #if the npv is greater than 0 and if the demand sum of the buildings is less than 100 MWh, the self imposed limit
                    #print("Commmunty NPV being considered")
                    #compare with individual NPV and share of NPV here
                    temp_bb = json.loads(Agents_Possibles_Combos.loc[max_combo_npv]['Bldg_share_in_community'])
                    fraction_npv = temp_bb[0]
                    share_npv = fraction_npv*Agents_Community_NPVs.loc[step_ctr][max_combo_npv]
                    ind_npv = Agents_Ind_NPVs.loc[step_ctr][self.unique_id]
                    if scenario == "ZEV":
                        comm_scr = Agents_Community_SCRs.loc[max_combo_npv]['Year0']
                    else:
                        comm_scr = Agents_Community_SCRs.loc['Year0'][max_combo_npv]
                    ind_scr = Agents_Ind_SCRs.loc[self.unique_id]['Year0']
                    #print("Comparison:share =",share_npv, "vs ind = ",ind_npv)
                    if share_npv >= ind_npv: #shared npv better than individual npv so community adoption will happen
                        Agents_Possibles_Combos.update(pd.Series([1], name  = 'Adopt', index = [max_combo_npv]))
                        Agents_Possibles_Combos.update(pd.Series([2018+step_ctr], name  = 'Year', index = [max_combo_npv]))
                        #split into the names of agents
                        agents_adopting_comm = max_combo_npv.split("_")  
                        comm_id = Agents_Possibles_Combos.loc[max_combo_npv]['Comm_ID']
                        
                        #setting adoption as 1 for all the buildings involved in the community formation
                        for g in agents_adopting_comm:
                            if g == self.unique_id:
                                self.en_champ = 1 #setting the agent which is the energy champion - the first agent
                                agents_info.update(pd.Series([self.en_champ], name  = 'En_Champ', index = [self.unique_id]))
                            for h in range(len(agents_objects_list)):
                                if g == agents_objects_list[h].unique_id:
                                    agents_objects_list[h].adopt_comm = 1 #setting community adoption as 1 for all agents involved
                                    self.adopt_year = 2018 + step_ctr
                                    agents_objects_list[h].intention = 0 #setting intention as 0 for all agents involved
                                    agents_info.update(pd.Series([1], name  = 'Adopt_COMM', index = [g]))
                                    agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [g]))
                                    agents_info.update(pd.Series([comm_id], name  = 'Community_ID', index = [g]))
                                    agents_info.update(pd.Series([self.total], name  = 'intention', index = [g]))
                                    agents_info.update(pd.Series([share_npv], name  = 'Comm_NPV', index = [g]))
                                    agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [g]))
                                    agents_info.update(pd.Series(["Comm>Ind"], name  = 'Reason', index = [g]))
                                    agents_info.update(pd.Series([ind_scr], name  = 'Ind_SCR', index = [g]))
                                    agents_info.update(pd.Series([comm_scr], name  = 'Comm_SCR', index = [g]))
                        agents_adopting_community_list.append(agents_adopting_comm)
                        
                    
                    elif share_npv < ind_npv and ind_npv>reduction*Agents_Ind_Investments.loc[step_ctr][self.unique_id]:#0: #if the individual NPV is positive and better than shared NPV
                        Agents_Possibles_Combos.update(pd.Series([0], name  = 'Adopt', index = [max_combo_npv]))
                        self.adopt_ind = 1
                        self.adopt_year = 2018 + step_ctr
                        agents_info.update(pd.Series([1], name  = 'Adopt_IND', index = [self.unique_id]))
                        agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [self.unique_id]))
                        agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                        agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                        agents_info.update(pd.Series(["Ind>Comm"], name  = 'Reason', index = [self.unique_id]))
                    
                    elif share_npv < ind_npv and ind_npv<reduction*Agents_Ind_Investments.loc[step_ctr][self.unique_id]:#0: #if the individual NPV is negative but better than shared NPV
                        Agents_Possibles_Combos.update(pd.Series([0], name  = 'Adopt', index = [max_combo_npv]))
                        self.adopt_ind = 0
                        agents_info.update(pd.Series([0], name  = 'Adopt_IND', index = [self.unique_id]))
                        agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                        agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                        agents_info.update(pd.Series(["Ind_negative>Comm_negative"], name  = 'Reason', index = [self.unique_id]))
                        
                
                #ZEV and no_ZEV scenario but because of high demand, the community cannot be formed
                elif Agents_Community_NPVs.loc[step_ctr][max_combo_npv] > 0 and comm_limit == 1 and Agents_Possibles_Combos.loc[max_combo_npv]['Demand_Year_MWh'] >= 100: #and scen_11 == 1:
                    #individual will adopt as community cannot
                    ind_npv = Agents_Ind_NPVs.loc[step_ctr][self.unique_id]
                    if ind_npv>reduction*Agents_Ind_Investments.loc[step_ctr][self.unique_id]:#0:
                        self.adopt_ind = 1
                        self.adopt_year = 2018 + step_ctr
                        agents_info.update(pd.Series([1], name  = 'Adopt_IND', index = [self.unique_id]))
                        agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [self.unique_id]))
                        agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                        agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                        agents_info.update(pd.Series(["Demand_No_Comm_Possible"], name  = 'Reason', index = [self.unique_id]))
                    else:
                        self.adopt_ind = 0
                        agents_info.update(pd.Series([0], name  = 'Adopt_IND', index = [self.unique_id]))
                        agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                        agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                        agents_info.update(pd.Series(["Demand_No_Comm_Possible & Ind_Negative"], name  = 'Reason', index = [self.unique_id]))
                        #agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [self.unique_id]))
                    #community will not adopt
                    Agents_Possibles_Combos.update(pd.Series([0], name  = 'Adopt', index = [max_combo_npv]))
                    agents_adopting_comm = max_combo_npv.split("_")
                    comm_id = Agents_Possibles_Combos.loc[max_combo_npv]['Comm_ID']
                    for g in agents_adopting_comm:
                        #print(g)
                        for h in range(len(agents_objects_list)):
                            if g == agents_objects_list[h].unique_id:
                                agents_objects_list[h].adopt_comm = 0
                                agents_info.update(pd.Series([0], name  = 'Adopt_COMM', index = [g]))
                                #agents_info.update(pd.Series([comm_id], name  = 'Community_ID', index = [g]))
                    #Agents_Possibles_Combos.loc[max_combo_npv]['Adopt'] = 0
                
                #TOP4_no_100MWh scenario - no restriction based on 100MWh demand limit
                elif Agents_Community_NPVs.loc[step_ctr][max_combo_npv] > 0 and comm_limit == 0:
                    #if the npv is greater than 0 and if the demand sum of the buildings is less than 100 MWh, the self imposed limit
                    
                    #compare with individual NPV and share of NPV here
                    temp_bb = json.loads(Agents_Possibles_Combos.loc[max_combo_npv]['Bldg_share_in_community'])
                    fraction_npv = temp_bb[0]
                    share_npv = fraction_npv*Agents_Community_NPVs.loc[step_ctr][max_combo_npv]
                    ind_npv = Agents_Ind_NPVs.loc[step_ctr][self.unique_id]
                    #print("Comparison:share =",share_npv, "vs ind = ",ind_npv)
                    if scenario == "ZEV":
                        comm_scr = Agents_Community_SCRs.loc[max_combo_npv]['Year0']
                    else:
                        comm_scr = Agents_Community_SCRs.loc['Year0'][max_combo_npv]
                    ind_scr = Agents_Ind_SCRs.loc[self.unique_id]['Year0']
                    if share_npv >= ind_npv: #shared npv better than individual npv so community adoption will happen
                        Agents_Possibles_Combos.update(pd.Series([1], name  = 'Adopt', index = [max_combo_npv]))
                        Agents_Possibles_Combos.update(pd.Series([2018+step_ctr], name  = 'Year', index = [max_combo_npv]))
                        #split into the names of agents
                        agents_adopting_comm = max_combo_npv.split("_")  
                        comm_id = Agents_Possibles_Combos.loc[max_combo_npv]['Comm_ID']
                        
                        #setting adoption as 1 for all the buildings involved in the community formation
                        for g in agents_adopting_comm:
                            if g == self.unique_id:
                                self.en_champ = 1 #setting the agent which is the energy champion - the first agent
                                agents_info.update(pd.Series([self.en_champ], name  = 'En_Champ', index = [self.unique_id]))
                            for h in range(len(agents_objects_list)):
                                if g == agents_objects_list[h].unique_id:
                                    agents_objects_list[h].adopt_comm = 1 #setting community adoption as 1 for all agents involved
                                    self.adopt_year = 2018 + step_ctr
                                    agents_objects_list[h].intention = 0 #setting intention as 0 for all agents involved
                                    agents_info.update(pd.Series([1], name  = 'Adopt_COMM', index = [g]))
                                    agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [g]))
                                    agents_info.update(pd.Series([comm_id], name  = 'Community_ID', index = [g]))
                                    agents_info.update(pd.Series([self.total], name  = 'intention', index = [g]))
                                    agents_info.update(pd.Series([share_npv], name  = 'Comm_NPV', index = [g]))
                                    agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [g]))
                                    agents_info.update(pd.Series(["Comm>Ind"], name  = 'Reason', index = [g]))
                                    agents_info.update(pd.Series([ind_scr], name  = 'Ind_SCR', index = [g]))
                                    agents_info.update(pd.Series([comm_scr], name  = 'Comm_SCR', index = [g]))
                        agents_adopting_community_list.append(agents_adopting_comm)
                        
                    
                    elif share_npv < ind_npv and ind_npv>=reduction*Agents_Ind_Investments.loc[step_ctr][self.unique_id]: #if the individual NPV is positive and better than shared NPV
                        Agents_Possibles_Combos.update(pd.Series([0], name  = 'Adopt', index = [max_combo_npv]))
                        self.adopt_ind = 1
                        self.adopt_year = 2018 + step_ctr
                        agents_info.update(pd.Series([1], name  = 'Adopt_IND', index = [self.unique_id]))
                        agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [self.unique_id]))
                        agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                        agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                        agents_info.update(pd.Series(["Ind>Comm"], name  = 'Reason', index = [self.unique_id]))
                    elif share_npv < ind_npv and ind_npv<reduction*Agents_Ind_Investments.loc[step_ctr][self.unique_id]:#0: #if the individual NPV is negative but better than shared NPV
                        Agents_Possibles_Combos.update(pd.Series([0], name  = 'Adopt', index = [max_combo_npv]))
                        self.adopt_ind = 0
                        agents_info.update(pd.Series([0], name  = 'Adopt_IND', index = [self.unique_id]))
                        agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                        agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                        agents_info.update(pd.Series(["Ind_negative>Comm_negative"], name  = 'Reason', index = [self.unique_id]))
                
                #because of negative npv, the community cannot be formed
                elif Agents_Community_NPVs.loc[step_ctr][max_combo_npv] < 0:
                    
                    Agents_Possibles_Combos.update(pd.Series([0], name  = 'Adopt', index = [max_combo_npv]))
                    agents_adopting_comm = max_combo_npv.split("_")
                    comm_id = Agents_Possibles_Combos.loc[max_combo_npv]['Comm_ID']
                    
                    #form individual if npv > 0
                    if Agents_Ind_NPVs.loc[step_ctr][self.unique_id] > reduction*Agents_Ind_Investments.loc[step_ctr][self.unique_id]:#0:
                        self.adopt_ind = 1
                        self.adopt_year = 2018 + step_ctr
                        agents_info.update(pd.Series([1], name  = 'Adopt_IND', index = [self.unique_id]))
                        agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [self.unique_id]))
                        agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                        agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                        agents_info.update(pd.Series(["Ind>Negative_Comm"], name  = 'Reason', index = [self.unique_id]))
                        self.intention = 0
                        self.adopt_comm = 0
                    elif Agents_Ind_NPVs.loc[step_ctr][self.unique_id] < reduction*Agents_Ind_Investments.loc[step_ctr][self.unique_id]:#0:
                        self.adopt_ind = 0
                        agents_info.update(pd.Series([0], name  = 'Adopt_IND', index = [self.unique_id]))
                        agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                        agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                        agents_info.update(pd.Series(["Negative_Ind & Negative_Comm"], name  = 'Reason', index = [self.unique_id]))
                        self.intention = 0
                        self.adopt_comm = 0
                        
# =============================================================================
            
            #no other bldgs can make community so go for individual            
            elif len(npvs_list) == 0:
                if Agents_Ind_NPVs.loc[step_ctr][self.unique_id] > reduction*Agents_Ind_Investments.loc[step_ctr][self.unique_id]: #0:
                    self.adopt_ind = 1
                    self.adopt_year = 2018 + step_ctr
                    agents_info.update(pd.Series([1], name  = 'Adopt_IND', index = [self.unique_id]))
                    agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [self.unique_id]))
                    agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                    agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                    agents_info.update(pd.Series(["Positive_Ind & No_Comm_possible"], name  = 'Reason', index = [self.unique_id]))
                    self.intention = 0
                    self.adopt_comm = 0
                else:
                    self.adopt_ind = 0
                    agents_info.update(pd.Series([0], name  = 'Adopt_IND', index = [self.unique_id]))
                    agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                    agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                    agents_info.update(pd.Series(["Negative_Ind & No_Comm_possible"], name  = 'Reason', index = [self.unique_id]))
                    self.intention = 0
                    self.adopt_comm = 0
                
            self.intention = 0 #if you adopt your intention has to be zero for the next years
        
        #if only individual adoption is possible
        elif self.part_comm == 0:# or self.part_comm == 1:#ZEV == 0: #self.part_comm == 0 and ZEV == 0:# or self.part_comm == 1: #self.part_comm === 1 is so that there are no community adoptions
            
            #adopt if NPV > 0
            if Agents_Ind_NPVs.loc[step_ctr][self.unique_id] > reduction*Agents_Ind_Investments.loc[step_ctr][self.unique_id]:
                self.adopt_ind = 1
                self.adopt_year = 2018 + step_ctr
                agents_info.update(pd.Series([1], name  = 'Adopt_IND', index = [self.unique_id]))
                agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [self.unique_id]))
                agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                agents_info.update(pd.Series(["Only_Ind"], name  = 'Reason', index = [self.unique_id]))
                self.intention = 0
                self.adopt_comm = 0
            else:
                self.adopt_ind = 0
                agents_info.update(pd.Series([0], name  = 'Adopt_IND', index = [self.unique_id]))
                agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
                agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
                agents_info.update(pd.Series(["Negative_Only_Ind"], name  = 'Reason', index = [self.unique_id]))
                self.intention = 0
                self.adopt_comm = 0
                    
    elif self.intention != 1:
        print("*-*-*-*-*-*-*")
        self.adopt_ind = 0
        agents_info.update(pd.Series([0], name  = 'Adopt_IND', index = [self.unique_id]))
        agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
        #agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
        agents_info.update(pd.Series(["Intention<0.5"], name  = 'Reason', index = [self.unique_id]))
        self.intention = 0
        self.adopt_comm = 0         
        
    #to ensure the buildings with already installed solar are always counted as having installed solar at the start of the code
    if scenario == "ZEV" or  scenario == "no_ZEV":
        if self.unique_id in list_installed_solar_bldgs_100MWh:
            print(self.unique_id)
            self.adopt_ind = 1
            self.adopt_year = 2018 + step_ctr 
            self.intention = 0
            agents_info.update(pd.Series([1], name  = 'Adopt_IND', index = [self.unique_id]))
            agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [self.unique_id]))
            agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
            agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
            agents_info.update(pd.Series(["Existing"], name  = 'Reason', index = [self.unique_id]))
    elif scenario == "TOP4_no100MWh":
        if self.unique_id in list_installed_solar_bldgs_ALL:
            print(self.unique_id)
            self.adopt_ind = 1
            self.adopt_year = 2018 + step_ctr
            self.intention = 0
            agents_info.update(pd.Series([1], name  = 'Adopt_IND', index = [self.unique_id]))
            agents_info.update(pd.Series([2018+step_ctr], name  = 'Year', index = [self.unique_id]))
            agents_info.update(pd.Series([self.total], name  = 'intention', index = [self.unique_id]))
            agents_info.update(pd.Series([ind_npv], name  = 'Ind_NPV', index = [self.unique_id]))
            agents_info.update(pd.Series(["Existing"], name  = 'Reason', index = [self.unique_id]))
        
        
        
        
        
              
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


