# -*- coding: utf-8 -*-
"""
Created on Thu May  2 21:12:56 2019

@author: iA

code to normalize the profitability indices
inputs - npv and investments of all individual buildings - separate depending on the prices (retail/wholesale)

"""

import pandas as pd
import numpy as np

#import the correct npv and inv files here! 
agents_individual_npv = pd.read_pickle('Agents_IND_wholesale_nosubsidy_NPVs_Years.pickle')
agents_individual_inv = pd.read_pickle('Agents_IND_wholesale_nosubsidy_InvestmentCosts_Years.pickle')

#import the correct agent info file here!
agents_info = pd.read_excel (r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Skeleton_Updated_No_100MWh_Restriction.xlsx')#test_agents_skeleton.xlsx') 

#%% for the case with buildings less than 100 MWh calculate prof index again as the scale needs to be changed

less_100_agents = agents_info#[agents_info['GRID_MWhyr']<=100]
#names = list(less_100_agents.index)
names = list(less_100_agents.bldg_id)
agents_less100_individual_npv = agents_individual_npv.filter(names)
agents_less100_individual_inv = agents_individual_inv.filter(names) 

profitability_index_less100 = pd.DataFrame(data = None)

profitability_index_less100 = (agents_less100_individual_npv + agents_less100_individual_inv)/agents_less100_individual_inv

#%% FINAL SCALED PROFITABILITY INDICES for less than 100 MWh buildings
 '''
 USED IN THE END FOR THE PROFITABILITY MATRIX
 segregate res, comm, public
 find max of the prof indices
 divide by that value
 cannot use scale as it scales every building within its range but we still need some comparison with other buildnigs in the system
 '''

agent_categories = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Building_Types_Segregated.xlsx')

res_agents = agent_categories.Residential.dropna().tolist()
pub_agents = agent_categories.Public.dropna().tolist()
com_agents = agent_categories.Commercial.dropna().tolist()

res_prof_index = profitability_index_less100[res_agents]
pub_prof_index = profitability_index_less100[pub_agents]
com_prof_index = profitability_index_less100[com_agents]

res_max = res_prof_index.max(axis = 0)
res_prof_index_SCALED = res_prof_index/max(res_max)

pub_max = pub_prof_index.max(axis = 0)
pub_prof_index_SCALED = pub_prof_index/max(pub_max)

comm_max = com_prof_index.max(axis = 0)
comm_prof_index_SCALED = com_prof_index/max(comm_max)

zz = pd.DataFrame(data = None)
zzzz = zz.append(res_prof_index_SCALED)
zzzzz = zzzz.append(comm_prof_index_SCALED)
zzzzzz = zzzzz.append(pub_prof_index_SCALED)

z = pd.concat([res_prof_index_SCALED,pub_prof_index_SCALED,comm_prof_index_SCALED],axis = 1)

z.to_pickle('Profitability_Index_SCALED_wholesale.pickle')
#%% case with all buildings involved (no 100 MWh restriction)

agents_individual_npv = pd.read_pickle('Agents_IND_nosubsidy_NPVs_Years.pickle')
agents_individual_inv = pd.read_pickle('Agents_IND_nosubsidy_InvestmentCosts_Years.pickle')

profitability_index = pd.DataFrame(data = None)

profitability_index = (agents_individual_npv + agents_individual_inv)/agents_individual_inv
profitability_index = profitability_index.drop(['Installation_Year'], axis = 1)



#%% FINAL SCALED PROFITABILITY INDICES
 '''
 USED IN THE END FOR THE PROFITABILITY MATRIX
 segregate res, comm, public
 find max of the prof indices
 divide by that value
 cannot use scale as it scales every building within its range but we still need some comparison with other buildnigs in the system
 '''

agent_categories = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Building_Types_Segregated.xlsx')

res_agents = agent_categories.Residential.dropna().tolist()
pub_agents = agent_categories.Public.dropna().tolist()
com_agents = agent_categories.Commercial.dropna().tolist()

res_prof_index = profitability_index[res_agents]
pub_prof_index = profitability_index[pub_agents]
com_prof_index = profitability_index[com_agents]

res_max = res_prof_index.max(axis = 0)
res_prof_index_SCALED = res_prof_index/max(res_max)

pub_max = pub_prof_index.max(axis = 0)
pub_prof_index_SCALED = pub_prof_index/max(pub_max)

comm_max = com_prof_index.max(axis = 0)
comm_prof_index_SCALED = com_prof_index/max(comm_max)

zz = pd.DataFrame(data = None)
zzzz = zz.append(res_prof_index_SCALED)
zzzzz = zzzz.append(comm_prof_index_SCALED)
zzzzzz = zzzzz.append(pub_prof_index_SCALED)

z = pd.concat([res_prof_index_SCALED,pub_prof_index_SCALED,comm_prof_index_SCALED],axis = 1)

#z.to_pickle(r"C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Codes\ABM\MasterThesis_PM\masterthesis\TPB\50_Profitability_Index_Scaled.pickle")
#%% APPROACH HERE: https://stackoverflow.com/questions/12525722/normalize-data-in-pandas

df = profitability_index
df.mean()
df.max()
df.min()
df_norm = (df - df.mean()) / (df.max() - df.min())

import statistics as stats
res_prof_index.apply(average)

#stats.mean(res_prof_index)

res_mean_list = res_prof_index.mean().tolist()
resmean = stats.mean(res_mean_list)
resmean

res_max_list = res_prof_index.max().tolist()
resmax = max(res_max_list)
resmax

res_min_list = res_prof_index.min().tolist()
resmin = min(res_min_list)
resmin
res_norm = (res_prof_index - resmean)/(resmax-resmean)

comm_mean_list = com_prof_index.mean().tolist()
commmean = stats.mean(comm_mean_list)
commmean

comm_max_list = com_prof_index.max().tolist()
commmax = max(comm_max_list)
commmax

comm_min_list = com_prof_index.min().tolist()
commmin = min(comm_min_list)
commmin
comm_norm = (com_prof_index - commmean)/(commmax-commmean)

pub_mean_list = pub_prof_index.mean().tolist()
pubmean = stats.mean(pub_mean_list)
pubmean

pub_max_list = pub_prof_index.max().tolist()
pubmax = max(pub_max_list)
pubmax

pub_min_list = pub_prof_index.min().tolist()
pubmin = min(pub_min_list)
pubmin
pub_norm = (pub_prof_index - pubmean)/(pubmax-pubmean)

all_manual_norms_together = pd.DataFrame(data = None)
all_manual_norms_together = pd.concat([res_norm,comm_norm,pub_norm],axis = 1)

#problem that there are negative values in this approach, from this link: https://stackoverflow.com/questions/12525722/normalize-data-in-pandas
#possible solution = scale this data
#done here:
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
X_train_minmax = min_max_scaler.fit_transform(X_train)
X_train_minmax

X_train_minmax = min_max_scaler.fit_transform(res_norm)
norm_scale_res = min_max_scaler.transform(res_norm)
norm_scale_res

X_train_minmax = min_max_scaler.fit_transform(pub_norm)
norm_scale_pub = min_max_scaler.transform(pub_norm)
norm_scale_pub

X_train_minmax = min_max_scaler.fit_transform(comm_norm)
norm_scale_comm = min_max_scaler.transform(comm_norm)
norm_scale_comm

norms_concat = pd.concat([res_norm,pub_norm,comm_norm],axis = 1)
X_train_minmax = min_max_scaler.fit_transform(norms_concat)
norm_scale_all = min_max_scaler.transform(norms_concat)

#problem - same as with scale - puts all numbers across a wide range of 0-1 which we do not need!!


#%%
from sklearn.preprocessing import MaxAbsScaler
X = [[ 1., -1.,  2.],[ 2.,  0.,  0.],[ 0.,  1., -1.]]
transformer = MaxAbsScaler().fit(profitability_index)
transformer
#MaxAbsScaler(copy=True)
nnnn = transformer.transform(profitability_index)

transformer = MaxAbsScaler().fit(res_norm)
res_norm_scale2 = transformer.transform(res_norm)

transformer = MaxAbsScaler().fit(pub_norm)
pub_norm_scale2 = transformer.transform(pub_norm)

transformer = MaxAbsScaler().fit(comm_norm)
comm_norm_scale2 = transformer.transform(comm_norm)

#%%


scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(norms_concat)
norms_concat_norm = scaler.transform(norms_concat)


#%%
from sklearn import preprocessing as pp

norm = pp.normalize(profitability_index)

arr = np.array([[0.,5.,10.],[15.,20.,25.],[30.,35.,40.]])
norm2 = pp.normalize(arr,norm = 'l2', axis = 0)
norm2

arr_scale = pp.scale(arr)

#%%

from sklearn import preprocessing
import numpy as np
# Get dataset
df = pd.read_csv(r'C:\Users\iA\Downloads\california_housing_train.csv')
# Normalize total_bedrooms column
x_array = np.array(profitability_index)
normalized_X = preprocessing.normalize([x_array])

#%%

from sklearn.preprocessing import MinMaxScaler 

norm3 = mms.transform([1,2,3,4,5])

#%%
series = [1,2,3,4,5,6,7,8,9]
values = series
values = values.reshape((len(values), 1))
# train the normalization
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
print('Min: %f, Max: %f' % (scaler.data_min_, scaler.data_max_))
# normalize the dataset and print the first 5 rows
normalized = scaler.transform(values)
for i in range(5):
	print(normalized[i])
# inverse transform and print the first 5 rows
inversed = scaler.inverse_transform(normalized)
for i in range(5):
	print(inversed[i])
    
    #%%

X_train = np.array([[ 1., -1.,  2.],
                    [ 2.,  0.,  0.],
                    [ 0.,  1., -1.]])

min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
X_train_minmax = min_max_scaler.fit_transform(X_train)
X_train_minmax

norm_scale = min_max_scaler.transform(profitability_index)
norm_scale

#%%

from sklearn.preprocessing import MaxAbsScaler
X = [[ 1., -1.,  2.],[ 2.,  0.,  0.],[ 0.,  1., -1.]]
transformer = MaxAbsScaler().fit(profitability_index)
transformer
#MaxAbsScaler(copy=True)
nnnn = transformer.transform(profitability_index)
#array([[ 0.5, -1. ,  1. ],[ 1. ,  0. ,  0. ],[ 0. ,  1. , -0.5]])