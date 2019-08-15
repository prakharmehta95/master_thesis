# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:47:40 2019

@author: iA
"""

import pandas as pd

#community_info = pd.read_pickle('Duplicate_Combinations_TOP4_All_Info.pickle')
community_info = pd.read_csv(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\Duplicate_Combinations_TOP4_All_Info.csv')
community_info.to_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\Duplicate_Combinations_All_Info.xlsx')

#%%make IDs for the different communities

#community_info = pd.read_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\Duplicate_Combinations_TOP4_All_Info.xlsx')

#list_unique_names = [327,	596,	241,	214,	683,	875,	334,	176,	26,	144,	28,	440,	846,	1052,	1049,	589,	177,	1056,	621,	805,	368,	182,	174,	245,	187,	178,	19,	12,	249,	394,	215,	167,	351,	195,	224,	286,	221,	172,	361,	380,	362,	372,	958,	889,	942,	864,	277,	363,	343,	344,	356,	240,	269,	389,	382,	384,	398,	349,	385,	281,	976,	658,	371,	657,	345,	346,	370,	670,	932,	1047,	997,	365,	612,	598,	663,	985,	669,	1077,	667,	946,	614,	809,	891,	807,	748,	463,	500,	499,	330,	386,	325,	324,	329,	21,	38,	155,	156,	154,	153,	223,	1073,	611,	1060,	855,	347,	975,	962,	803,]
list_unique_names = [12,19,21,23,24,25,26,27,28,38,41,42,43,109,144,153,154,155,156,165,166,167,172,174,176,177,178,182,187,195,198,204,214,215,221,223,224,238,239,240,241,245,249,253,259,261,265,266,269,271,277,281,282,286,320,324,325,326,327,329,330,333,334,343,344,345,346,347,349,350,351,356,357,360,361,362,363,365,368,369,370,371,372,377,379,380,382,384,385,386,389,390,394,396,398,
                     417,432,434,435,436,440,441,442,443,444,445,446,448,451,453,456,462,463,474,477,499,500,549,550,551,553,562,569,576,577,585,589,596,598,610,611,612,614,618,621,627,628,634,657,658,663,664,667,668,	669,	670,	681,	683,	691,	697,	713,	715,	747,	748,	776,	779,	780,	781,	795,	796,	803,	805,	806,	807,	809,	841,	842,	844,	846,	854,	855,	858,	859,	862,	864,	875,	883,	886,	889,	891,	906,	928,	932,	933,	942,	946,	954,	957,	958,	961,	962,	973,	975,	976,	984,	985,	997,	1026,	1030,	1042,	1043,	1045,	1047,	1049,	1052,	1056,	1058,	1060,	1073,	1077]



list_unique_names.sort()

name_list = []
for j in list_unique_names:
    c = 0
    for i in community_info.Plot_ID.tolist():
        if i == j:
            c = c + 1
            name = "P" + str(j) + "_C_" + str(c)
            name_list.append(name)
    print(c)

community_info["Comm_ID"] = ""
community_info["Comm_ID"] =  name_list

community_info.to_pickle('Duplicate_Combinations_TOP4_All_Info_commIDs.pickle')
community_info.to_excel(r'C:\Users\iA\OneDrive - ETHZ\Thesis\PM\Data_Prep_ABM\Subplots_Communities\1436 Buildings\Duplicate_Combinations_TOP4_All_Info_commIDs.xlsx')
