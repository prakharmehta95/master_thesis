# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 22:38:03 2019

@author: iA
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 12 17:57:48 2019

@author: iA
"""

#%%
import pandas as pd
import numpy as np

d_agents_info = pd.read_pickle(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Wholesale Prices\ALL_wholesale_recalibrated_29MAY_d_agents_info.pickle")
d_gini = pd.read_pickle(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Wholesale Prices\ALL_wholesale_recalibrated_29MAY_d_gini.pickle")
d_gini_model = pd.read_pickle(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Wholesale Prices\ALL_wholesale_recalibrated_29MAY_d_gini_model.pickle")
d_combos_info = pd.read_pickle(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Wholesale Prices\ALL_wholesale_recalibrated_29MAY_d_combos_info_runs.pickle")
#%%

'''
INDIVIDUAL
'''

import matplotlib.pyplot as plt
import statistics as stats
import pandas as pd
from operator import add
d_gini_model_correct = d_gini_model

length = len(d_gini_model_correct)
ranking_df = pd.DataFrame(data = None, index = range(length))
rank_list_ind = []
rank_list_comm = []

avg_df = pd.DataFrame(data = None, columns = d_gini_model_correct['gini_model_0'].columns)#pd.Series(0)
avg_df["Individual_solar"] = 0
avg_df["Ind_PV_Installed"] = 0
avg_df["Community_solar"] = 0
avg_df["Comm_PV_Installed"] = 0
avg_df["Energy_Champions"] = 0
avg_df["Agent_Type_Res"] = 0
avg_df["Agent_Type_Res_PV_Size"] = 0
avg_df["Agent_Type_Comm"] = 0
avg_df["Agent_Type_Comm_PV_Size"] = 0
avg_df["Agent_Type_Pub"] = 0
avg_df["Agent_Type_Pub_PV_Size"] = 0
avg_df["EGIDs_greater_than_one"] = 0
aaa = [i-i for i in range(18)]

ind_sum = [i-i for i in range(18)]
ind_cap_sum = [i-i for i in range(18)] 
com_sum= [i-i for i in range(18)]
ener_champ = [i-i for i in range(18)]
com_cap_sum = [i-i for i in range(18)]
res_sum = [i-i for i in range(18)]
res_sum_cap = [i-i for i in range(18)]
comm_sum = [i-i for i in range(18)]
comm_sum_cap = [i-i for i in range(18)]
pub_sum = [i-i for i in range(18)]
pub_sum_cap = [i-i for i in range(18)]

for i in range(length):
    temp = "gini_model_" + str(i)
    print(temp)
    t_ind = d_gini_model_correct[temp].Ind_PV_Installed
    t_comm = d_gini_model_correct[temp].Comm_PV_Installed
    ind_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Individual_solar))) 
    ind_cap_sum = list(map(add, ind_cap_sum, list(d_gini_model_correct[temp].Ind_PV_Installed))) 
    com_sum = list(map(add, com_sum, list(d_gini_model_correct[temp].Community_solar))) 
    ener_champ = list(map(add, ener_champ, list(d_gini_model_correct[temp].Energy_Champions))) 
    com_cap_sum = list(map(add, com_cap_sum, list(d_gini_model_correct[temp].Comm_PV_Installed)))
    res_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Res))) 
    res_sum_cap = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Res_PV_Size))) 
    comm_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Comm))) 
    comm_sum_cap = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Comm_PV_Size))) 
    pub_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Pub))) 
    pub_sum_cap = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Pub_PV_Size)))
    egids_total = list(map(add, ind_sum, list(d_gini_model_correct[temp].EGIDs_greater_than_one)))
    #avg_df.Individual_solar = avg_df.Individual_solar + d_gini_model[temp].Individual_solar
    #avg_df.Ind_PV_Installed = avg_df.Ind_PV_Installed + d_gini_model[temp].Ind_PV_Installed
    #avg_df.Community_solar = avg_df.Community_solar + d_gini_model[temp].Community_solar
    #avg_df.Energy_Champions = avg_df.Energy_Champions + d_gini_model[temp].Energy_Champions
    #avg_df.Comm_PV_Installed = avg_df.Comm_PV_Installed + d_gini_model[temp].Comm_PV_Installed
    #print(avg_df)
    avg_ind_cap = stats.mean(t_ind)
    rank_list_ind.append(avg_ind_cap)
    avg_comm_cap = stats.mean(t_comm)
    rank_list_comm.append(avg_comm_cap)

avg_df["Individual_solar"] = ind_sum
avg_df["Ind_PV_Installed"] = ind_cap_sum
avg_df["Community_solar"] = com_sum
avg_df["Energy_Champions"] = ener_champ
avg_df["Comm_PV_Installed"] = com_cap_sum
avg_df["Agent_Type_Res"] = res_sum
avg_df["Agent_Type_Res_PV_Size"] = res_sum_cap
avg_df["Agent_Type_Comm"] = comm_sum
avg_df["Agent_Type_Comm_PV_Size"] = comm_sum_cap
avg_df["Agent_Type_Pub"] = pub_sum
avg_df["Agent_Type_Pub_PV_Size"] = pub_sum_cap
avg_df["EGIDs_greater_than_one"] = egids_total

avg_df = avg_df/length

ranking_df["Ranks_Ind"] = rank_list_ind
ranking_df["Ranks_Comm"] = rank_list_comm

high = ranking_df.idxmax(axis = 0) 
low = ranking_df.idxmin(axis = 0)

#plotting individual capacities
high_ind_index = 'gini_model_' + str(high[0])
low_ind_index = 'gini_model_' + str(low[0])
average_line = avg_df.Ind_PV_Installed# + avg_df.Comm_PV_Installed 
high_line = d_gini_model_correct[high_ind_index].Ind_PV_Installed# + d_gini_model_correct[high_ind_index].Comm_PV_Installed
low_line = d_gini_model_correct[low_ind_index].Ind_PV_Installed# + d_gini_model_correct[low_ind_index].Comm_PV_Installed 
#historical = 2.70449/3.944*[9017.991496,10224.24023,11430.48897,12636.7377,13842.98644,15049.23518,16255.48391,17461.73265,18667.98138,19874.23012,21080.47886,22228.72759,23492.97633,24699.22506,25905.4738,27111.72254,28317.97127,29524.22001]
historical_proj = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM/Wiedikon_less_100_MWh_projections.xlsx')
historical = list(historical_proj.Wiedikon_TOTAL)

x = range(2019,2037,1)
plt.figure(0)
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']


#plt.plot(x,high_line,'hotpink',x,average_line,'gold',x,low_line,'turquoise',x,historical,'k--')
#plt.bar(x,average_line,color = 'gold')
#plt.plot(x,high_line,color = 'hotpink',linestyle = 'solid')#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
#plt.plot(x,average_line,color = 'darkkhaki',linestyle = 'solid')
#plt.plot(x,low_line,color = 'turquoise',linestyle = 'solid')
#plt.plot(x,historical,color = 'k',linestyle = 'solid')
#plt.xticks(np.arange(min(x), max(x)+2, 2.0))
#plt.fill_between(x,high_line,low_line,color = "whitesmoke")
#plt.xlabel("Year")
#plt.ylabel("Installed PV Capacity (kWp)")
#plt.legend(["Max","Average","Min","Extrapolated Historical Trend"])
#plt.grid(b = None, which = 'major', axis = 'x')
#plt.xticks(np.arange(2019, 2037, step=1))
#plt.tick_params(axis = 'x', rotation = 45)

#plt.savefig(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\Less_100MWh_716\no_ZEV\testplot.png')


'''

---------------LINE PLOTS--------------------
'''
average_line_18 = [0]
hhhh = list(average_line)
average_line_18.extend(hhhh)

high_line_18 = [0]
iiii = list(high_line)
high_line_18.extend(iiii)

low_line_18 = [0]
iiii = list(low_line)
low_line_18.extend(iiii)

historical_18 = [0]
iiii = list(historical)
historical_18.extend(iiii)
x = range(2018,2037,1)
#plt.plot(x,average_line_18,color = 'darkkhaki',linestyle = 'solid')
#high_line_18 = d_gini_model_correct[high_ind_index].Ind_PV_Installed 
#low_line_18
#historical_18

plt.plot(x,high_line_18,color = 'hotpink',linestyle = 'solid')#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.plot(x,average_line_18,color = 'darkkhaki',linestyle = 'solid')
plt.plot(x,low_line_18,color = 'turquoise',linestyle = 'solid')
plt.plot(x,historical_18,color = 'k',linestyle = 'solid')
#plt.xticks(np.arange(min(x), max(x)+2, 2.0))
plt.fill_between(x,high_line_18,low_line_18,color = "whitesmoke")
plt.xlabel("Year")
plt.ylabel("Individual PV Capacity (kWp)")
plt.legend(["Max","Average","Min","Extrapolated Historical Trend"])
plt.grid(b = None, which = 'major', axis = 'x')
plt.xticks(np.arange(2018, 2037, step=1))
plt.tick_params(axis = 'x', rotation = 45)
plt.savefig(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Retail Prices\ALL_Individual_line.png')

'''
----------bar graphs--------------
'''
plt.figure(1)
x = range(2018,2036,1)
plt.bar(x,high_line,color = 'hotpink',linestyle = 'solid',zorder = 0)#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.bar(x,average_line,color = 'darkkhaki',linestyle = 'solid',zorder = 5)
plt.bar(x,low_line,color = 'turquoise',linestyle = 'solid',zorder = 10)
plt.scatter(x,historical,color = 'k',linestyle = '-',marker = '+',zorder = 15, )
plt.xticks(np.arange(min(x), max(x)+2, 2.0))
#plt.fill_between(x,high_line,low_line,color = "whitesmoke")
plt.xlabel("Year")
plt.ylabel("Individual PV Capacity (kWp)")
plt.legend(["Extrapolated Historical Trend","Max","Average","Min"])
plt.xticks(np.arange(2018, 2036, step=1))
plt.tick_params(axis = 'x', rotation = 45)

plt.savefig(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Retail Prices\ALL_Individual_bar.png')


#%%

'''
COMMUNITY
'''

import matplotlib.pyplot as plt
import statistics as stats
import pandas as pd
from operator import add
d_gini_model_correct = d_gini_model

length = len(d_gini_model_correct)
ranking_df = pd.DataFrame(data = None, index = range(length))
rank_list_ind = []
rank_list_comm = []

avg_df = pd.DataFrame(data = None, columns = d_gini_model_correct['gini_model_0'].columns)#pd.Series(0)
avg_df["Individual_solar"] = 0
avg_df["Ind_PV_Installed"] = 0
avg_df["Community_solar"] = 0
avg_df["Comm_PV_Installed"] = 0
avg_df["Energy_Champions"] = 0
avg_df["Agent_Type_Res"] = 0
avg_df["Agent_Type_Res_PV_Size"] = 0
avg_df["Agent_Type_Comm"] = 0
avg_df["Agent_Type_Comm_PV_Size"] = 0
avg_df["Agent_Type_Pub"] = 0
avg_df["Agent_Type_Pub_PV_Size"] = 0
avg_df["EGIDs_greater_than_one"] = 0
aaa = [i-i for i in range(18)]

ind_sum = [i-i for i in range(18)]
ind_cap_sum = [i-i for i in range(18)] 
com_sum= [i-i for i in range(18)]
ener_champ = [i-i for i in range(18)]
com_cap_sum = [i-i for i in range(18)]
res_sum = [i-i for i in range(18)]
res_sum_cap = [i-i for i in range(18)]
comm_sum = [i-i for i in range(18)]
comm_sum_cap = [i-i for i in range(18)]
pub_sum = [i-i for i in range(18)]
pub_sum_cap = [i-i for i in range(18)]

for i in range(length):
    temp = "gini_model_" + str(i)
    print(temp)
    t_ind = d_gini_model_correct[temp].Ind_PV_Installed
    t_comm = d_gini_model_correct[temp].Comm_PV_Installed
    ind_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Individual_solar))) 
    ind_cap_sum = list(map(add, ind_cap_sum, list(d_gini_model_correct[temp].Ind_PV_Installed))) 
    com_sum = list(map(add, com_sum, list(d_gini_model_correct[temp].Community_solar))) 
    ener_champ = list(map(add, ener_champ, list(d_gini_model_correct[temp].Energy_Champions))) 
    com_cap_sum = list(map(add, com_cap_sum, list(d_gini_model_correct[temp].Comm_PV_Installed)))
    res_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Res))) 
    res_sum_cap = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Res_PV_Size))) 
    comm_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Comm))) 
    comm_sum_cap = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Comm_PV_Size))) 
    pub_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Pub))) 
    pub_sum_cap = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Pub_PV_Size)))
    egids_total = list(map(add, ind_sum, list(d_gini_model_correct[temp].EGIDs_greater_than_one)))
    #avg_df.Individual_solar = avg_df.Individual_solar + d_gini_model[temp].Individual_solar
    #avg_df.Ind_PV_Installed = avg_df.Ind_PV_Installed + d_gini_model[temp].Ind_PV_Installed
    #avg_df.Community_solar = avg_df.Community_solar + d_gini_model[temp].Community_solar
    #avg_df.Energy_Champions = avg_df.Energy_Champions + d_gini_model[temp].Energy_Champions
    #avg_df.Comm_PV_Installed = avg_df.Comm_PV_Installed + d_gini_model[temp].Comm_PV_Installed
    #print(avg_df)
    avg_ind_cap = stats.mean(t_ind)
    rank_list_ind.append(avg_ind_cap)
    avg_comm_cap = stats.mean(t_comm)
    rank_list_comm.append(avg_comm_cap)

avg_df["Individual_solar"] = ind_sum
avg_df["Ind_PV_Installed"] = ind_cap_sum
avg_df["Community_solar"] = com_sum
avg_df["Energy_Champions"] = ener_champ
avg_df["Comm_PV_Installed"] = com_cap_sum
avg_df["Agent_Type_Res"] = res_sum
avg_df["Agent_Type_Res_PV_Size"] = res_sum_cap
avg_df["Agent_Type_Comm"] = comm_sum
avg_df["Agent_Type_Comm_PV_Size"] = comm_sum_cap
avg_df["Agent_Type_Pub"] = pub_sum
avg_df["Agent_Type_Pub_PV_Size"] = pub_sum_cap
avg_df["EGIDs_greater_than_one"] = egids_total

avg_df = avg_df/length

ranking_df["Ranks_Ind"] = rank_list_ind
ranking_df["Ranks_Comm"] = rank_list_comm

high = ranking_df.idxmax(axis = 0) 
low = ranking_df.idxmin(axis = 0)

#plotting individual capacities
high_ind_index = 'gini_model_' + str(high[1])
low_ind_index = 'gini_model_' + str(low[1])
average_line = avg_df.Comm_PV_Installed
high_line = d_gini_model_correct[high_ind_index].Comm_PV_Installed
low_line = d_gini_model_correct[low_ind_index].Comm_PV_Installed
#historical = 2.70449/3.944*[9017.991496,10224.24023,11430.48897,12636.7377,13842.98644,15049.23518,16255.48391,17461.73265,18667.98138,19874.23012,21080.47886,22228.72759,23492.97633,24699.22506,25905.4738,27111.72254,28317.97127,29524.22001]
#historical_proj = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM/Wiedikon_less_100_MWh_projections.xlsx')
#historical = list(historical_proj.Wiedikon_less_100_kWp)

x = range(2019,2037,1)
plt.figure(0)
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']


'''
adding 2018 to the plot
---------------LINE PLOTS--------------------
'''
average_line_18 = [0]
hhhh = list(average_line)
average_line_18.extend(hhhh)

high_line_18 = [0]
iiii = list(high_line)
high_line_18.extend(iiii)

low_line_18 = [0]
iiii = list(low_line)
low_line_18.extend(iiii)

historical_18 = [0]
iiii = list(historical)
historical_18.extend(iiii)
x = range(2018,2037,1)
#plt.plot(x,average_line_18,color = 'darkkhaki',linestyle = 'solid')
#high_line_18 = d_gini_model_correct[high_ind_index].Ind_PV_Installed 
#low_line_18
#historical_18

plt.plot(x,high_line_18,color = 'hotpink',linestyle = 'solid')#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.plot(x,average_line_18,color = 'darkkhaki',linestyle = 'solid')
plt.plot(x,low_line_18,color = 'turquoise',linestyle = 'solid')
plt.plot(x,historical_18,color = 'k',linestyle = 'solid')
#plt.xticks(np.arange(min(x), max(x)+2, 2.0))
plt.fill_between(x,high_line_18,low_line_18,color = "whitesmoke")
plt.xlabel("Year")
plt.ylabel("Community PV Capacity (kWp)")
plt.legend(["Max","Average","Min","Extrapolated Historical Trend"])
plt.grid(b = None, which = 'major', axis = 'x')
plt.xticks(np.arange(2018, 2037, step=1))
plt.tick_params(axis = 'x', rotation = 45)
plt.savefig(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Retail Prices\ALL_Community_line.png')

'''
------------bar graphs--------------
'''
plt.figure(1)
x = range(2018,2036,1)
plt.bar(x,high_line,color = 'hotpink',linestyle = 'solid',zorder = 0)#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.bar(x,average_line,color = 'darkkhaki',linestyle = 'solid',zorder = 5)
plt.bar(x,low_line,color = 'turquoise',linestyle = 'solid',zorder = 10)
plt.scatter(x,historical,color = 'k',linestyle = '-',marker = '+',zorder = 15, )
plt.xticks(np.arange(min(x), max(x)+2, 2.0))
#plt.fill_between(x,high_line,low_line,color = "whitesmoke")
plt.xlabel("Year")
plt.ylabel("Community PV Capacity (kWp)")
plt.legend(["Extrapolated Historical Trend","Max","Average","Min"])
plt.xticks(np.arange(2018, 2036, step=1))
plt.tick_params(axis = 'x', rotation = 45)

plt.savefig(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Retail Prices\ALL_Community_bar.png')


#%%

'''
TOTAL
'''

import matplotlib.pyplot as plt
import statistics as stats
import pandas as pd
from operator import add
d_gini_model_correct = d_gini_model

length = len(d_gini_model_correct)
ranking_df = pd.DataFrame(data = None, index = range(length))
rank_list_ind = []
rank_list_comm = []
rank_list_total = []

avg_df = pd.DataFrame(data = None, columns = d_gini_model_correct['gini_model_0'].columns)#pd.Series(0)
avg_df["Individual_solar"] = 0
avg_df["Ind_PV_Installed"] = 0
avg_df["Community_solar"] = 0
avg_df["Comm_PV_Installed"] = 0
avg_df["Energy_Champions"] = 0
avg_df["Agent_Type_Res"] = 0
avg_df["Agent_Type_Res_PV_Size"] = 0
avg_df["Agent_Type_Comm"] = 0
avg_df["Agent_Type_Comm_PV_Size"] = 0
avg_df["Agent_Type_Pub"] = 0
avg_df["Agent_Type_Pub_PV_Size"] = 0
avg_df["EGIDs_greater_than_one"] = 0
avg_df["TOTAL_CAP"] = 0
aaa = [i-i for i in range(18)]

ind_sum = [i-i for i in range(18)]
ind_cap_sum = [i-i for i in range(18)] 
com_sum= [i-i for i in range(18)]
ener_champ = [i-i for i in range(18)]
com_cap_sum = [i-i for i in range(18)]
res_sum = [i-i for i in range(18)]
res_sum_cap = [i-i for i in range(18)]
comm_sum = [i-i for i in range(18)]
comm_sum_cap = [i-i for i in range(18)]
pub_sum = [i-i for i in range(18)]
pub_sum_cap = [i-i for i in range(18)]

for i in range(length):
    temp = "gini_model_" + str(i)
    print(temp)
    t_ind = d_gini_model_correct[temp].Ind_PV_Installed
    t_comm = d_gini_model_correct[temp].Comm_PV_Installed
    t_total = d_gini_model_correct[temp].Ind_PV_Installed + d_gini_model_correct[temp].Comm_PV_Installed
    ind_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Individual_solar))) 
    ind_cap_sum = list(map(add, ind_cap_sum, list(d_gini_model_correct[temp].Ind_PV_Installed))) 
    com_sum = list(map(add, com_sum, list(d_gini_model_correct[temp].Community_solar))) 
    ener_champ = list(map(add, ener_champ, list(d_gini_model_correct[temp].Energy_Champions))) 
    com_cap_sum = list(map(add, com_cap_sum, list(d_gini_model_correct[temp].Comm_PV_Installed)))
    res_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Res))) 
    res_sum_cap = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Res_PV_Size))) 
    comm_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Comm))) 
    comm_sum_cap = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Comm_PV_Size))) 
    pub_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Pub))) 
    pub_sum_cap = list(map(add, ind_sum, list(d_gini_model_correct[temp].Agent_Type_Pub_PV_Size)))
    egids_total = list(map(add, ind_sum, list(d_gini_model_correct[temp].EGIDs_greater_than_one)))
    #avg_df.Individual_solar = avg_df.Individual_solar + d_gini_model[temp].Individual_solar
    #avg_df.Ind_PV_Installed = avg_df.Ind_PV_Installed + d_gini_model[temp].Ind_PV_Installed
    #avg_df.Community_solar = avg_df.Community_solar + d_gini_model[temp].Community_solar
    #avg_df.Energy_Champions = avg_df.Energy_Champions + d_gini_model[temp].Energy_Champions
    #avg_df.Comm_PV_Installed = avg_df.Comm_PV_Installed + d_gini_model[temp].Comm_PV_Installed
    #print(avg_df)
    avg_ind_cap = stats.mean(t_ind)
    rank_list_ind.append(avg_ind_cap)
    avg_comm_cap = stats.mean(t_comm)
    rank_list_comm.append(avg_comm_cap)
    avg_total_cap = stats.mean(t_total)
    rank_list_total.append(avg_total_cap)

avg_df["Individual_solar"] = ind_sum
avg_df["Ind_PV_Installed"] = ind_cap_sum
avg_df["Community_solar"] = com_sum
avg_df["Energy_Champions"] = ener_champ
avg_df["Comm_PV_Installed"] = com_cap_sum
avg_df["Agent_Type_Res"] = res_sum
avg_df["Agent_Type_Res_PV_Size"] = res_sum_cap
avg_df["Agent_Type_Comm"] = comm_sum
avg_df["Agent_Type_Comm_PV_Size"] = comm_sum_cap
avg_df["Agent_Type_Pub"] = pub_sum
avg_df["Agent_Type_Pub_PV_Size"] = pub_sum_cap
avg_df["EGIDs_greater_than_one"] = egids_total
avg_df["TOTAL_CAP"] = list(map(add, ind_cap_sum, com_cap_sum))

avg_df = avg_df/length

ranking_df["Ranks_Ind"] = rank_list_ind
ranking_df["Ranks_Comm"] = rank_list_comm
ranking_df["Ranks_Total"] = rank_list_total

high = ranking_df.idxmax(axis = 0) 
low = ranking_df.idxmin(axis = 0)

#plotting individual capacities
high_ind_index = 'gini_model_' + str(high[2])
low_ind_index = 'gini_model_' + str(low[2])
average_line = avg_df.Ind_PV_Installed + avg_df.Comm_PV_Installed
high_line = d_gini_model_correct[high_ind_index].Ind_PV_Installed + d_gini_model_correct[high_ind_index].Comm_PV_Installed
low_line = d_gini_model_correct[low_ind_index].Ind_PV_Installed + d_gini_model_correct[low_ind_index].Comm_PV_Installed
#historical = 2.70449/3.944*[9017.991496,10224.24023,11430.48897,12636.7377,13842.98644,15049.23518,16255.48391,17461.73265,18667.98138,19874.23012,21080.47886,22228.72759,23492.97633,24699.22506,25905.4738,27111.72254,28317.97127,29524.22001]
#historical_proj = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM/Wiedikon_less_100_MWh_projections.xlsx')
#historical = list(historical_proj.Wiedikon_less_100_kWp)

x = range(2019,2037,1)
plt.figure(0)
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']


#plt.plot(x,high_line,'hotpink',x,average_line,'gold',x,low_line,'turquoise',x,historical,'k--')
#plt.bar(x,average_line,color = 'gold')
#plt.plot(x,high_line,color = 'hotpink',linestyle = 'solid')#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
#plt.plot(x,average_line,color = 'darkkhaki',linestyle = 'solid')
#plt.plot(x,low_line,color = 'turquoise',linestyle = 'solid')
#plt.plot(x,historical,color = 'k',linestyle = 'solid')
#plt.xticks(np.arange(min(x), max(x)+2, 2.0))
#plt.fill_between(x,high_line,low_line,color = "whitesmoke")
#plt.xlabel("Year")
#plt.ylabel("Installed PV Capacity (kWp)")
#plt.legend(["Max","Average","Min","Extrapolated Historical Trend"])
#plt.grid(b = None, which = 'major', axis = 'x')
#plt.xticks(np.arange(2019, 2037, step=1))
#plt.tick_params(axis = 'x', rotation = 45)

#plt.savefig(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\Less_100MWh_716\no_ZEV\testplot.png')


'''
TOTAL
adding 2018 to the plot
---------------LINE PLOTS--------------------
'''
average_line_18 = [0]
hhhh = list(average_line)
average_line_18.extend(hhhh)

high_line_18 = [0]
iiii = list(high_line)
high_line_18.extend(iiii)

low_line_18 = [0]
iiii = list(low_line)
low_line_18.extend(iiii)

historical_18 = [0]
iiii = list(historical)
historical_18.extend(iiii)
x = range(2018,2037,1)
#plt.plot(x,average_line_18,color = 'darkkhaki',linestyle = 'solid')
#high_line_18 = d_gini_model_correct[high_ind_index].Ind_PV_Installed 
#low_line_18
#historical_18

plt.plot(x,high_line_18,color = 'hotpink',linestyle = 'solid')#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.plot(x,average_line_18,color = 'darkkhaki',linestyle = 'solid')
plt.plot(x,low_line_18,color = 'turquoise',linestyle = 'solid')
plt.plot(x,historical_18,color = 'k',linestyle = 'solid')
#plt.xticks(np.arange(min(x), max(x)+2, 2.0))
plt.fill_between(x,high_line_18,low_line_18,color = "whitesmoke")
plt.xlabel("Year")
plt.ylabel("Total PV Capacity (kWp)")
plt.legend(["Max","Average","Min","Extrapolated Historical Trend"])
plt.grid(b = None, which = 'major', axis = 'x')
plt.xticks(np.arange(2018, 2037, step=1))
plt.tick_params(axis = 'x', rotation = 45)
plt.savefig(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Retail Prices\ALL_Total_line.png')

'''
bar graphs--------------
'''
plt.figure(1)
x = range(2018,2036,1)
plt.bar(x,high_line,color = 'hotpink',linestyle = 'solid',zorder = 0)#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.bar(x,average_line,color = 'darkkhaki',linestyle = 'solid',zorder = 5)
plt.bar(x,low_line,color = 'turquoise',linestyle = 'solid',zorder = 10)
plt.scatter(x,historical,color = 'k',linestyle = '-',marker = '+',zorder = 15, )
plt.xticks(np.arange(min(x), max(x)+2, 2.0))
#plt.fill_between(x,high_line,low_line,color = "whitesmoke")
plt.xlabel("Year")
plt.ylabel("Total PV Capacity (kWp)")
plt.legend(["Extrapolated Historical Trend","Max","Average","Min"])
plt.xticks(np.arange(2018, 2036, step=1))
plt.tick_params(axis = 'x', rotation = 45)

plt.savefig(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\Results_RECALIBRATION\ALL_1437\1437 Weights\ZEV Allowed - Normal\Retail Prices\ALL_Total_bar.png')






































#%% community
#plt.figure(1)
high_comm_index = 'gini_model_' + str(high[1])
low_comm_index = 'gini_model_' + str(low[1])
average_line = avg_df.Comm_PV_Installed
high_line = d_gini_model_correct[high_comm_index].Comm_PV_Installed
low_line = d_gini_model_correct[low_comm_index].Comm_PV_Installed
historical_proj = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM/Wiedikon_less_100_MWh_projections.xlsx')
historical = list(historical_proj.Wiedikon_less_100_kWp)
x = range(2018,2036,1)
#plt.figure(0)
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']
plt.plot(x,high_line,color = 'hotpink',linestyle = 'dashed')#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.plot(x,average_line,color = 'darkkhaki',linestyle = 'dashed')
plt.plot(x,low_line,color = 'turquoise',linestyle = 'dashed')
plt.plot(x,historical,color = 'k',linestyle = 'solid')
#plt.bar(x,average_line,color = 'gold')
plt.xticks(np.arange(min(x), max(x)+2, 2.0))
plt.fill_between(x,high_line,low_line,color = "whitesmoke")
plt.xticks(np.arange(2018, 2036, step=1))
plt.tick_params(axis = 'x', rotation = 45)

plt.xlabel("Year")
#plt.ylabel("Community Installed PV Capacity (kWp)")
plt.legend(["Max","Average","Min","Extrapolated Historical Trend"])

#%% total and separate nidividual + community
plt.figure(2)
high_ind_index_comm = 'gini_model_' + str(high[1])
low_ind_index_comm = 'gini_model_' + str(low[1])
average_line = avg_df.Ind_PV_Installed + avg_df.Comm_PV_Installed
high_line = d_gini_model_correct[high_ind_index].Ind_PV_Installed + d_gini_model_correct[high_ind_index_comm].Comm_PV_Installed
low_line = d_gini_model_correct[low_ind_index].Ind_PV_Installed + d_gini_model_correct[low_ind_index_comm].Comm_PV_Installed 
historical_proj = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM/Wiedikon_less_100_MWh_projections.xlsx')
historical = list(historical_proj.Wiedikon_less_100_kWp)
x = range(2019,2037,1)
#plt.figure(0)
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']

#plt.plot(x,average_line,'gold',x,high_line,'hotpink',x,low_line,'turquoise',x,historical,'green')

#plt.xlabel("Years -->")
#plt.ylabel("Total Installed PV Capacity (kWp)")
#plt.legend(["Average","Max","Min","Historical Projection"])
#plt.fill_between(x,high_line,low_line,color = "whitesmoke")

#plt.plot(x,high_line,'hotpink',x,average_line,'gold',x,low_line,'turquoise',x,historical,'k')
#plt.bar(x,average_line,color = 'gold')
plt.plot(x,high_line,color = 'hotpink',linestyle = 'solid')#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.plot(x,average_line,color = 'darkkhaki',linestyle = 'solid')
plt.plot(x,low_line,color = 'turquoise',linestyle = 'solid')
plt.plot(x,historical,color = 'k',linestyle = 'solid')
plt.xticks(np.arange(min(x), max(x)+2, 2.0))
plt.fill_between(x,high_line,low_line,color = "whitesmoke")
plt.xlabel("Year")
plt.ylabel("Total Installed PV Capacity (kWp)")
plt.legend(["Max","Average","Min","Extrapolated Historical Trend"])

#% separate multi EGIDs and single EGIDs to make the plots------------------------------------------------
import matplotlib.pyplot as plt
import statistics as stats
import pandas as pd
from operator import add

length = len(d_gini_model_correct)
ranking_df = pd.DataFrame(data = None, index = range(length))
rank_list_ind = []
rank_list_comm = []

avg_df = pd.DataFrame(data = None, columns = d_gini_model_correct['gini_model_0'].columns)#pd.Series(0)
avg_df["Individual_solar"] = 0
avg_df["Ind_PV_Installed"] = 0
avg_df["Community_solar"] = 0
avg_df["Comm_PV_Installed"] = 0
avg_df["Energy_Champions"] = 0
avg_df["Agent_Type_Res"] = 0
avg_df["Agent_Type_Res_PV_Size"] = 0
avg_df["Agent_Type_Comm"] = 0
avg_df["Agent_Type_Comm_PV_Size"] = 0
avg_df["Agent_Type_Pub"] = 0
avg_df["Agent_Type_Pub_PV_Size"] = 0
avg_df["EGIDs_greater_than_one"] = 0
aaa = [i-i for i in range(18)]

ind_sum = [i-i for i in range(18)]
ind_cap_sum = [i-i for i in range(18)] 
com_sum= [i-i for i in range(18)]
ener_champ = [i-i for i in range(18)]
com_cap_sum = [i-i for i in range(18)]
res_sum = [i-i for i in range(18)]
res_sum_cap = [i-i for i in range(18)]
comm_sum = [i-i for i in range(18)]
comm_sum_cap = [i-i for i in range(18)]
pub_sum = [i-i for i in range(18)]
pub_sum_cap = [i-i for i in range(18)]
egids_total_sum = [i-i for i in range(18)]
egids_total_sum_cap = [i-i for i in range(18)]

for i in range(length):
    temp = "gini_model_" + str(i)
    print(temp)
    t_ind = d_gini_model_correct[temp].Ind_PV_Installed
    t_comm = d_gini_model_correct[temp].Comm_PV_Installed
    ind_sum = list(map(add, ind_sum, list(d_gini_model_correct[temp].Individual_solar))) 
    ind_cap_sum = list(map(add, ind_cap_sum, list(d_gini_model_correct[temp].Ind_PV_Installed))) 
    com_sum = list(map(add, com_sum, list(d_gini_model_correct[temp].Community_solar))) 
    ener_champ = list(map(add, ener_champ, list(d_gini_model_correct[temp].Energy_Champions))) 
    com_cap_sum = list(map(add, com_cap_sum, list(d_gini_model_correct[temp].Comm_PV_Installed)))
    res_sum = list(map(add, res_sum, list(d_gini_model_correct[temp].Agent_Type_Res))) 
    res_sum_cap = list(map(add, res_sum_cap, list(d_gini_model_correct[temp].Agent_Type_Res_PV_Size))) 
    comm_sum = list(map(add, comm_sum, list(d_gini_model_correct[temp].Agent_Type_Comm))) 
    comm_sum_cap = list(map(add, comm_sum_cap, list(d_gini_model_correct[temp].Agent_Type_Comm_PV_Size))) 
    pub_sum = list(map(add, pub_sum, list(d_gini_model_correct[temp].Agent_Type_Pub))) 
    pub_sum_cap = list(map(add, pub_sum_cap, list(d_gini_model_correct[temp].Agent_Type_Pub_PV_Size)))
    egids_total_sum = list(map(add, egids_total_sum, list(d_gini_model_correct[temp].EGIDs_greater_than_one))) 
    egids_total_sum_cap = list(map(add, egids_total_sum_cap, list(d_gini_model_correct[temp].EGIDs_greater_than_one_SIZE)))
    
    #avg_df.Individual_solar = avg_df.Individual_solar + d_gini_model[temp].Individual_solar
    #avg_df.Ind_PV_Installed = avg_df.Ind_PV_Installed + d_gini_model[temp].Ind_PV_Installed
    #avg_df.Community_solar = avg_df.Community_solar + d_gini_model[temp].Community_solar
    #avg_df.Energy_Champions = avg_df.Energy_Champions + d_gini_model[temp].Energy_Champions
    #avg_df.Comm_PV_Installed = avg_df.Comm_PV_Installed + d_gini_model[temp].Comm_PV_Installed
    #print(avg_df)
    avg_ind_cap = stats.mean(t_ind)
    rank_list_ind.append(avg_ind_cap)
    avg_comm_cap = stats.mean(t_comm)
    rank_list_comm.append(avg_comm_cap)

avg_df["Individual_solar"] = ind_sum
avg_df["Ind_PV_Installed"] = ind_cap_sum
avg_df["Community_solar"] = com_sum
avg_df["Energy_Champions"] = ener_champ
avg_df["Comm_PV_Installed"] = com_cap_sum
avg_df["Agent_Type_Res"] = res_sum
avg_df["Agent_Type_Res_PV_Size"] = res_sum_cap
avg_df["Agent_Type_Comm"] = comm_sum
avg_df["Agent_Type_Comm_PV_Size"] = comm_sum_cap
avg_df["Agent_Type_Pub"] = pub_sum
avg_df["Agent_Type_Pub_PV_Size"] = pub_sum_cap
avg_df["EGIDs_greater_than_one"] = egids_total_sum
avg_df["EGIDs_greater_than_one_SIZE"] = egids_total_sum_cap
avg_df = avg_df/length

ranking_df["Ranks_Ind"] = rank_list_ind
ranking_df["Ranks_Comm"] = rank_list_comm

high = ranking_df.idxmax(axis = 0) 
low = ranking_df.idxmin(axis = 0)

#plotting individual capacities
high_ind_index = 'gini_model_' + str(high[0])
low_ind_index = 'gini_model_' + str(low[0])
average_line = avg_df.Ind_PV_Installed# - avg_df.EGIDs_greater_than_one_SIZE
high_line = d_gini_model_correct[high_ind_index].Ind_PV_Installed# - d_gini_model_correct[high_ind_index].EGIDs_greater_than_one_SIZE
low_line = d_gini_model_correct[low_ind_index].Ind_PV_Installed# -  d_gini_model_correct[low_ind_index].EGIDs_greater_than_one_SIZE
#historical = 2.70449/3.944*[9017.991496,10224.24023,11430.48897,12636.7377,13842.98644,15049.23518,16255.48391,17461.73265,18667.98138,19874.23012,21080.47886,22228.72759,23492.97633,24699.22506,25905.4738,27111.72254,28317.97127,29524.22001]
historical_proj = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM/Wiedikon_less_100_MWh_projections.xlsx')
historical = list(historical_proj.Wiedikon_less_100_kWp)

x = range(2019,2037,1)
#plt.figure(0)
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']

#plt.plot(x,high_line,'hotpink',x,average_line,'gold',x,low_line,'turquoise',x,historical,'k--')
#plt.bar(x,average_line,color = 'gold')
plt.plot(x,high_line,color = 'hotpink',linestyle = 'dotted')#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.plot(x,average_line,color = 'darkkhaki',linestyle = 'dotted')
plt.plot(x,low_line,color = 'turquoise',linestyle = 'dotted')
#plt.plot(x,historical,color = 'k',linestyle = 'solid')
plt.xticks(np.arange(min(x), max(x)+2, 2.0))
plt.fill_between(x,high_line,low_line,color = "whitesmoke")
plt.xlabel("Year")
plt.ylabel("Installed PV Capacity (kWp)")
#plt.legend(["Max","Average","Min","Extrapolated Historical Trend"])
#% community
#plt.figure(1)
high_comm_index = 'gini_model_' + str(high[1])
low_comm_index = 'gini_model_' + str(low[1])
average_line = avg_df.Comm_PV_Installed# + avg_df.EGIDs_greater_than_one_SIZE
high_line = d_gini_model_correct[high_comm_index].Comm_PV_Installed #+ d_gini_model_correct[high_comm_index].EGIDs_greater_than_one_SIZE
low_line = d_gini_model_correct[low_comm_index].Comm_PV_Installed #+ d_gini_model_correct[low_comm_index].EGIDs_greater_than_one_SIZE
historical_proj = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM/Wiedikon_less_100_MWh_projections.xlsx')
historical = list(historical_proj.Wiedikon_less_100_kWp)
#x = range(2019,2037,1)
#plt.figure(0)
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']
plt.plot(x,high_line,color = 'hotpink',linestyle = 'dashed')#,x,average_line,color = 'gold',linestyle = 'dashed',x,low_line,color = 'turquoise',linestyle = 'dashed',x,historical,color = 'k',linestyle = 'dashed')
plt.plot(x,average_line,color = 'darkkhaki',linestyle = 'dashed')
plt.plot(x,low_line,color = 'turquoise',linestyle = 'dashed')
#plt.plot(x,historical,color = 'k',linestyle = 'solid')
#plt.bar(x,average_line,color = 'gold')
plt.xticks(np.arange(min(x), max(x)+2, 2.0))
plt.fill_between(x,high_line,low_line,color = "whitesmoke")
plt.xlabel("Year")
#plt.ylabel("Community Installed PV Capacity (kWp)")
plt.legend(["Max","Average","Min","Extrapolated Historical Trend"])
#%% NUMBER OF INSTALLATIONS 

#plotting number of  individual installations
high_ind_index = 'gini_model_' + str(high[0])
low_ind_index = 'gini_model_' + str(low[0])
average_line = avg_df.Individual_solar
high_line = d_gini_model[high_ind_index].Individual_solar
low_line = d_gini_model[low_ind_index].Individual_solar
#historical = [9017.991496,10224.24023,11430.48897,12636.7377,13842.98644,15049.23518,16255.48391,17461.73265,18667.98138,19874.23012,21080.47886,22228.72759,23492.97633,24699.22506,25905.4738,27111.72254,28317.97127,29524.22001]
x = range(2018,2036,1)
plt.figure(0)
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']

#plt.plot(x,average_line,'gold',x,high_line,'hotpink',x,low_line,'g-')
plt.bar(x,high_line,color = 'hotpink')
plt.bar(x,average_line,color = 'gold')
plt.bar(x,low_line,color = 'lightblue')
plt.xlabel("Years -->")
plt.ylabel("Number of Individual Installations")
plt.legend(["Average","Max","Min"])

#plt.hist(average_line,high_line)

#%%
#plotting individual capacities
high_ind_index = 'gini_model_' + str(high[0])
low_ind_index = 'gini_model_' + str(low[0])
average_line = avg_df.Ind_PV_Installed
high_line = d_gini_model[high_ind_index].Ind_PV_Installed
low_line = d_gini_model[low_ind_index].Ind_PV_Installed
historical = [9017.991496,10224.24023,11430.48897,12636.7377,13842.98644,15049.23518,16255.48391,17461.73265,18667.98138,19874.23012,21080.47886,22228.72759,23492.97633,24699.22506,25905.4738,27111.72254,28317.97127,29524.22001]
x = range(2018,2036,1)
fig,ax = plt.subplots(1)

ax.set_xlabel("Years -->")
ax.set_ylabel("Individual Installed PV Capacity (kWp)")
ax.plot(x,average_line,'y-',x,high_line,'r-',x,low_line,'g-',x,historical,'c-')
plt.legend(["Average","Max","Min","Historical Projection"])
ax.tick_params(axis = 'y')

ax1 = ax.twinx()

high_ind_index_num = 'gini_model_' + str(high[0])
low_ind_index_num = 'gini_model_' + str(low[0])
average_line_num = avg_df.Individual_solar
high_line_num = d_gini_model[high_ind_index_num].Individual_solar
low_line_num = d_gini_model[low_ind_index_num].Individual_solar

color = 'tab:blue'
ax1.set_ylabel('Number of Installations', color=color)  # we already handled the x-label with ax1
ax1.plot(x, average_line_num, 'y.',x, high_line_num, 'r.',x, low_line_num, 'g.',)
ax1.tick_params(axis='y', labelcolor=color)
#ax3.legend(loc = 0,["Average","Max","Min","#Communities"])
fig.tight_layout()  # otherwise the right y-label is slightly clipped
#plt.legend(["Average","Max","Min","Historical Projection"])
plt.show()



#plotting number of  individual installations



plt.plot(x,average_line,'y-',x,high_line,'r-',x,low_line,'g-')
plt.xlabel("Years -->")
plt.ylabel("Number of Individual Installations")
plt.legend(["Average","Max","Min"])

plt.hist(average_line,high_line)

color = 'tab:red'
ax.set_xlabel("Years -->")
ax.set_ylabel("Community Installed PV Capacity (kWp)")
ax.plot(x,average_line,'y-',x,high_line,'r-',x,low_line,'g-')

#plt.legend(["Average","Max","Min","Historical Projection"])

ax2.tick_params(axis = 'y')

ax3 = ax2.twinx()

color = 'tab:blue'
ax3.set_ylabel('Number of Installations', color=color)  # we already handled the x-label with ax1
ax3.plot(x, average_inst, 'b.')
ax3.tick_params(axis='y', labelcolor=color)
#ax3.legend(loc = 0,["Average","Max","Min","#Communities"])
fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.show()

#%%
#plotting community capacities
high_comm_index = 'gini_model_' + str(high[1])
low_comm_index = 'gini_model_' + str(low[1])
average_line = avg_df.Comm_PV_Installed
average_inst = avg_df.Energy_Champions
high_line = d_gini_model[high_ind_index].Comm_PV_Installed
low_line = d_gini_model[low_ind_index].Comm_PV_Installed
historical = [9017.991496,10224.24023,11430.48897,12636.7377,13842.98644,15049.23518,16255.48391,17461.73265,18667.98138,19874.23012,21080.47886,
              22228.72759,23492.97633,24699.22506,25905.4738,27111.72254,28317.97127,29524.22001]
x = range(2018,2036,1)

fig,ax2 = plt.subplots(1)

#my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']
#plt.plot(x,average_line,'y-',x,high_line,'r-',x,low_line,'g-',x,historical,'c-')
color = 'tab:red'
ax2.set_xlabel("Years -->")
ax2.set_ylabel("Community Installed PV Capacity (kWp)")
ax2.plot(x,average_line,'y-',x,high_line,'r-',x,low_line,'g-')

#plt.legend(["Average","Max","Min","Historical Projection"])

ax2.tick_params(axis = 'y')

ax3 = ax2.twinx()

color = 'tab:blue'
ax3.set_ylabel('Number of Installations', color=color)  # we already handled the x-label with ax1
ax3.plot(x, average_inst, 'b.')
ax3.tick_params(axis='y', labelcolor=color)
#ax3.legend(loc = 0,["Average","Max","Min","#Communities"])
fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.show()








#%%
a = d_gini_model['gini_model_0'].Ind_PV_Installed
b = d_gini_model['gini_model_1'].Ind_PV_Installed
c = d_gini_model['gini_model_2'].Ind_PV_Installed
d = d_gini_model['gini_model_3'].Ind_PV_Installed
e = d_gini_model['gini_model_4'].Ind_PV_Installed
historical = [9017.991496,10224.24023,11430.48897,12636.7377,13842.98644,15049.23518,16255.48391,17461.73265,18667.98138,19874.23012,21080.47886,22228.72759,23492.97633,24699.22506,25905.4738,27111.72254,28317.97127,29524.22001]
x = range(2018,2036)
plt.figure(0)
my_colors = ['r', 'g', 'b', 'k', 'y', 'm', 'c']
for i in range(5):
    temp = "gini_model_" + str(i)
    t = d_gini_model[temp].Ind_PV_Installed
    colors = my_colors[i]
    plt.plot(x,t,colors)
    #plt.plot(x,a,'b-',x,b,'r-',x,c,'g-',x,d,'c-',x,e,'y-',x,historical)

#Installed Capacity Community PV
a_c = d_gini_model['gini_model_0'].Comm_PV_Installed
b_c = d_gini_model['gini_model_1'].Comm_PV_Installed
c_c = d_gini_model['gini_model_2'].Comm_PV_Installed
d_c = d_gini_model['gini_model_3'].Comm_PV_Installed
e_c = d_gini_model['gini_model_4'].Comm_PV_Installed

#Number of Community PV systems
a_l = d_gini_model['gini_model_0'].Energy_Champions
b_l = d_gini_model['gini_model_1'].Energy_Champions
c_l = d_gini_model['gini_model_2'].Energy_Champions
d_l = d_gini_model['gini_model_3'].Energy_Champions
e_l = d_gini_model['gini_model_4'].Energy_Champions

plt.figure(1)
plt.plot(x,a_c,'b-',x,b_c,'r-',x,c_c,'g-',x,d_c,'c-',x,e_c,'y-')
plt.xlabel("Years -->")
plt.ylabel("Community Installed PV Capacity")

plt.figure(2)
plt.plot(x,a_l,'b-',x,b_l,'r-',x,c_l,'g-',x,d_l,'c-',x,e_l,'y-')
plt.xlabel("Years -->")
plt.ylabel("Number of Community PV Systems")


plt.figure(3)
barWidth = 0.25
r1 = np.arange(len(a_l))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

plt.bar(r1,a_l,color = 'b')#b_l,c_l,d_l,e_l)
plt.bar(r2,b_l,color = 'r')#
plt.bar(r3,c_l,color = 'g')#
plt.bar(r4,d_l,color = 'c')#
plt.bar(r5,e_l,color = 'y')#
plt.xlabel("Years -->")
plt.ylabel("Number of Community PV Systems")


#plt.hist(a_l)
#plt.hist(a_l,cumulative = True)