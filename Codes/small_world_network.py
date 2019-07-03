# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:44:12 2019

@author: prakh
"""
agents_all_list =  pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\test_agents_ALL.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
import networkx as nx
import pandas as pd
from random import seed
import random
import numpy as np

watts_strogatz = nx.watts_strogatz_graph(100,2,0.5)
nx.nodes(watts_strogatz)
ggg = nx.Graph.neighbors(watts_strogatz, 1)
[n for n in ggg(0)]

#seed(1)
temp_df = pd.DataFrame(data = None, index = range(20))
G2 = nx.watts_strogatz_graph(10,2,0.5,2)
#G = nx.DiGraph(['a','b','c','d'])#nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.watts_strogatz_graph(1437,20,0.5,1)#nx.path_graph(4)  # or DiGraph, MultiGraph, MultiDiGraph, etc
#G = nx.Graph([(1,2),(3,4)])
#list(G.nodes)
#aa = list(G.edges)
for i in range(1437):
    print(i)
    l = list(G.adj[i])
    if len(l) < 20:
        for j in range(20-len(l)):
            l.append(np.nan)
    #naam = 'bldg' + str(i)
    #temp_df[naam] = ""
    #temp_df[naam] = pd.Series(list(G.adj[i]))
    temp_df[i] = ""
    temp_df[i] = pd.Series(list(G.adj[i]))



ctr = 0
for i in list_agents:
    a = [n for n in G.neighbors(ctr)]
    print(len(a))
    #temp_df[i] = ""
    #temp_df[i] = a
    ctr = ctr + 1
a

#%% make a random list of agents
temp = pd.DataFrame(data = None)
list_agents = agents_all_list.bldg_id.tolist()
ppp = []
for i in range(len(agents_all_list)):
    ppp = random.choices(list_agents,k =5)
    temp[agents_all_list.loc[i]['bldg_id']] = ""
    temp[agents_all_list.loc[i]['bldg_id']] = ppp

#%%

dist_list = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\test_swn_data_real.xlsx')

dist = []
dist = dist_list.Distance.tolist()

new_df = pd.DataFrame(data = None, index = range(1437))
new_df['Building_ID'] = ""
new_df['Number'] = ""
new1 = []
new2 = []
for i in range(0,1437,2):
    new1.append(dist_list.loc[i]['Building_ID'])
    new2.append(dist_list.loc[i+1]['Building_ID'])

new2.reverse()

swn_list = new1 + new2

swn_ref_Z0003 = pd.DataFrame(data = None)
swn_ref_Z0003["Circular_List"] = swn_list

swn_ref_Z0003.to_csv('SWN_List.csv')

swn_ref_Z0003["Ref_Number"] = ""
num_list = [i for i in range(1437)]
swn_ref_Z0003["Ref_Number"] = num_list

#%%

di = swn_ref_Z0003.Circular_List.to_dict()

temp_df = temp_df.rename(columns = di)

temp_df_2 = pd.DataFrame(data = None)

temp_df_2 = temp_df
for i in temp_df_2.columns:
    #naam = 'bldg' + str(i)
    #print(naam)
    temp_df_2[i] = temp_df[i].map(di)
#%%
for z in range(1437):
    naam = 'bldg' + str(i)
    temp_df_2.rename(columns = {naam:di})
#%%
temp_df_3 = pd.DataFrame(data = None, columns = swn_ref_Z0003.Circular_List.tolist())

temp_df_3 = temp_df_2

lll = swn_ref_Z0003.Circular_List.tolist()

for z in range(1437):
    naam = 'bldg' + str(i)
    temp_df_3.rename(columns = {naam: lll[i]})


#%% working model of SWN

temp_df = pd.DataFrame(data = None, index = range(20))

G = nx.watts_strogatz_graph(1437,20,0.5,2)
for i in range(1437):
    print(i)
    l = list(G.adj[i])
    if len(l) < 20:
        for j in range(20-len(l)):
            l.append(np.nan)
    temp_df[i] = ""
    temp_df[i] = pd.Series(list(G.adj[i]))

swn_ref_Z0003= pd.read_csv('SWN_List.csv')

#dictionary to replace numbers of the watts-stratogatz function with actual building names
di = swn_ref_Z0003.Circular_List.to_dict()

temp_df = temp_df.rename(columns = di)

swn = pd.DataFrame(data = None)

swn = temp_df
for i in swn.columns:
    swn[i] = temp_df[i].map(di)