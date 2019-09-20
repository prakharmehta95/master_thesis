# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:23:43 2019

@author: iA
"""
#%%
import os
import pandas as pd
os.chdir(r'C:\Users\iA\Documents\CEA_Wiedikon\17SEP_CEAresults\sample_1650\baseline\outputs\data\demand')
a = os.listdir()
df = pd.DataFrame(data = None)
df['name'] = ""
df['name'] = a
df.to_csv(r'C:\Users\iA\Desktop\folder\namesall.csv')
