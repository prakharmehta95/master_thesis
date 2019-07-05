All pickle files and excel data files specefic to Model B
1437 agents
100 MWh restriction to adopt individually or to form communites is lifted. But only a maximum of 4 neighbour members allowed in a ZEV (hence the TOP4 used in the names of the files)

Two scenarios - RETAIL and WHOLESALE prices 
wherever "wholesale" is included in the name, that is for the wholesale prices scenario. All other data remains the same.

Individual PV System Information:
	Agents_IND_nosubsidy_InvestmentCosts_Years	- investment costs of installing PV, inclusive of all system and installation costs, smart meter costs. Changes according to the year installed
	Agents_IND_nosubsidy_NPVs_Years				- NPV of the individual PV systems. Changes according to the year installed (2018-2035).
	Agents_IND_wholesale_nosubsidy_NPVs_Years	- NPV of the individual PV systems with WHOLESALE prices. Changes according to the year installed (2018-2035)
	Agents_IND_nosubsidy_SCR_Years				- SCRs of the individual PV systems, for 25 years (installed whenever, lasts for 25 years). As a degradation factor of 0.6%/year is taken, the SCR increases every year as the PV production decreases

Community PV System Information:
	Duplicate_Combinations_TOP4_All_Info_commIDs				- Information on all possible combinations of community formations - Bldgs, bldg types, Area, PV sizes, Share of bldgs in community, EGIDs, Occupants, Demand_Yearly, PV Subsidy, ID
	
	Duplicate_Combos_TOP4_nosubsidy_Agents_NPVs_Years			- NPVs of all community combinations
	Duplicate_Combos_TOP4_wholesale_nosubsidy_Agents_NPVs_Years	- NPVs of all community combinations with WHOLESALE prices
	Duplicate_Combos_TOP4_nosubsidy_Agents_SCRs					- SCRs of all community combinations
	
Agent Information:
	Profitability_Index_Scaled				- Profitability Index values for all the agents, calculated for each year they might adopt between 2018 - 2035 and scaled between 0-1. Profitability Index increases from 2018 to 2029 as PV prices keep going down. But in 2030, the investment subsidy is halted and hence the Profitability Index goes down. 
	
	Profitability_Index_SCALED_wholesale	- Profitability Index values for all the agents in the WHOLESALE prices scenario
	
	Skeleton_Updated_No_100MWh_Restriction.xlsx				- Contains information of all agents - ID, ID with type, Plot ID, Building Type, Building Type Category, No. of EGIDs, No. of occupants, no. of Smart Meters, Yearly Demand MWh, Roof Areas, PV Size, PV Size Category (small/large), PV Subsidy, Part of Community Yes or No, Minergie Bldg Yes or No

	subplots_CLEAN_100MWh_TOP4.xlsx								- Each building and it's possible ZEV members (other buildings it can form a ZEV with)
	
	