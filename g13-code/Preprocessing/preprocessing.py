#!/usr/bin/env python
# coding: utf-8

# In[156]:


import pandas as pd
import os
cwd = os.getcwd()

sc_Data = pd.read_csv(cwd+'/Input_Files/02_01_District_wise_crimes_committed_against_SC_2001_2012.csv')
st_Data = pd.read_csv(cwd+'/Input_Files/02_District_wise_crimes_committed_against_ST_2001_2012.csv')
children_Data = pd.read_csv(cwd+'/Input_Files/03_District_wise_crimes_committed_against_children_2001_2012.csv')
women_Data = pd.read_csv(cwd+'/Input_Files/42_District_wise_crimes_committed_against_women_2001_2012.csv')
census_Data = pd.read_csv(cwd+'/Input_Files/india-districts-census-2011.csv')
#census_Filtered_Data = census_Data[['State name','District name','Population','Female','SC','ST']]
census_Filtered_Data = census_Data
census_Filtered_Data['District name'] = census_Filtered_Data['District name'].str.upper()


# # District Data(SC)
# 
# #Completed:Paschim Midnapur and Purab Midnapur to be combined together as Midnapur and rows of corresponding years to be added(2002 onwards)
# #CompletedState : KERALA and Distt. : TRIVANDRUM COMMR. and TRIVANDRUM RURAL to be combined together as TRIVANDRUM and rows of corresponding years to be added(2003 onwards)
# #CompletedState : KERALA and Distt. : KOZHIKODE COMMR. and KOZHIKODE RURAL to be combined together as KOZHIKODE and rows of corresponding years to be added(2003 onwards)
# #CompletedState : KERALA and Distt. : ERNAKULAM COMMR. and ERNAKULAM RURAL to be combined together as ERNAKULAM and rows of corresponding years to be added(2003 onwards)
# #CompletedState : ARUNACHAL PRADESH and Distt. : UPPER DIBANG VALLEY and DIBANG VALLEY to be combined together as DIBANG VALLEY and rows of corresponding years to be added(2003 onwards)
# 
# #CompletedState : ANDHRA PRADESH and Distt. : CYBERABAD enter with 0 in all columns for year 2001 and 2002
# #CompletedState : MADHYA PRADESH and Distt. : ASHOK NAGAR enter with 0 in all columns for year 2001 and 2002
# #CompletedState : MADHYA PRADESH and Distt. : ANUPPUR enter with 0 in all columns for year 2001 and 2002
# #CompletedState : CHHATTISGARH and Distt. : NARAYANPUR enter with 0 in all columns for year 2001 and 2002
# #CompletedState : MADHYA PRADESH and Distt. : BURHANPUR enter with 0 in all columns for year 2001 and 2002
# #CompletedState : ARUNACHAL PRADESH and Distt. : K/KUMEY enter with 0 in all columns for year 2001 and 2002
# #Completed:State : Tamil Nadu Distt: Ariyalur enter 0s to every row for year 2001 to 2011
# #CompletesState : West Bengal and Distt. : Kharagpur G.R.P. enter with 0 in all columns for year 2001
# #CompletedState : Chhattisgarh and Distt. : Kabirdham enter with 0 in all columns for year 2001
# #CompletedState : JAMMU & KASHMIR and Distt. : HANDWARA enter with 0 in all columns for year 2001
# #CompletedState : ASSAM Distt : N.C. HILLS change to N.C.HILLS in 2001
# #CompletedState : JHARKHAND and Distt. : GUMALA to GUMLA in 2001
# #CompletedState : Haryana Distt : HISAR change to HISSAR in 2001
# #CompletedState : Haryana Distt : MAHENDERGARH change to MAHENDRAGARH in 2001 
# #completed4 to 3 {'TAMIL NADU_KRISHNAGIRI'(1 - 3 enter 0), 
# #'PUNJAB_FEROZPUR'(handled)}
# #completed4 to 5 {'TAMIL NADU_CHENGAI'(5 onwards enter 0), 
# #completed'TAMIL NADU_VILLUPURAM'(5 entry missing enter 0)}
# #completed3 to 4 {'PUNJAB_FEROZEPUR'(change to FEROZPUR)}
# #completed5 to 4 {'HARYANA_MEWAT'(1 -4 enter 0), 
# #'TAMIL NADU_VILUPPURAM'(handled), 
# #completed'CHHATTISGARH_SURAJPUR'(1-4 enter 0), 
# #completed'ASSAM_UDALGURI'(1-4 enter 0), 
# #completed'ASSAM_BASKA'(1 - 4 enter 0), 
# #completed'ASSAM_CHIRANG'(1 - 4 enter 0)}
# #completed5 to 6 {'RAJASTHAN_KOTA'(2006 to 2010 Kota city and Kota rural combine), 
# #completed'TAMIL NADU_VILUPPURAM'(5 enter 0), 
# #completed'WEST BENGAL_HOWRAH CITY'(HOWRAH, HOWRAH CITY, HOWRAH G.R.P. combine), 
# #completed'MAHARASHTRA_MUMBAI'-{MUMBAI COMMR., MUMBAI RLY., NAVI MUMBAI}, 
# #completed'ANDHRA PRADESH_VIJAYAWADA'(Vijayawada city to Vijayawada for year 2006 to 2010)}
# #'JAMMU & KASHMIR_BORDER', 'MANIPUR_IMPHAL(EAST)', 'MANIPUR_IMPHAL(WEST)', 'RAJASTHAN_JAIPUR', 'RAJASTHAN_JODHPUR', 
# #completed6 to 5 {'ANDHRA PRADESH_VIJAYAWADA CITY', 
# #completed'JAMMU & KASHMIR_BORDER DISTRICT'(Border District to Border 2006 and 2007,
# #completedand add 0s to all entries 2008 onwards), 
# #completed'TAMIL NADU_VILLUPURAM'(2005 entry missing enter 0),
# #completed'RAJASTHAN_KOTA CITY', 'RAJASTHAN_KOTA RURAL', 
# #completed'MANIPUR_IMPHAL WEST'(Convert Imphal (West)to Imphal West till 2005), 
# #completed'MANIPUR_IMPHAL EAST'(Convert Imphal (East)to Imphal East till 2005),
# #completed'MAHARASHTRA_MUMBAI COMMR.',  
# #completed'PUNJAB_SAS NGR'(1-5 enter 0), 
# #completed'HARYANA_PALWAL'(1 - 5 enter 0), 
# #completed'RAJASTHAN_JAIPUR SOUTH','RAJASTHAN_JAIPUR NORTH','RAJASTHAN_JAIPUR RURAL', 'RAJASTHAN_JAIPUR EAST'() Convert all three to Jaipur 2006 - 2010}
# #completed'RAJASTHAN_JODHPUR CITY', 'RAJASTHAN_JODHPUR RURAL'(Convert to Jodhpur 2006 to 2010 G.R.P. Jodhpur to Jodhpur(2010))
# #completed6 to 7 {'PUNJAB_MAJITHA'(enter 0 for 6 and post)}
# #completed7 to 6 {'JHARKHAND_KHUNTI'(enter 0 fr 1 -6), 
# #completed'JHARKHAND_RAMGARH'(1-6 enter 0), 
# #completed'PUNJAB_AMRITSAR RURAL, CP AMRITSAR'(combine to make Amritsar), 
# #completeed'NAGALAND_LONGLENG'(1-6 enter 0)}
# 
# #7 to 8 {'JAMMU & KASHMIR_BORDER DISTRICT', 'CHHATTISGARH_DANTEWARA', 'PUNJAB_JAGRAON', 'PUNJAB_NAWAN SHAHR', 
# #'KERALA_CBCID'}
# 
# #8 to 7 {'JAMMU & KASHMIR_SHOPIAN', 'ODISHA_DCP BBSR', 'KARNATAKA_CBPURA', 'MADHYA PRADESH_SINGRAULI', 
# #'TAMIL NADU_CHENNAISUBURBAN', 'UTTAR PRADESH_KANSHIRAM NAGAR', 'JAMMU & KASHMIR_KISHTWAR', 'MANIPUR_CID', 'GUJARAT_TAPI',
# #'PUNJAB_LUDHIANA RURAL', 'CHHATTISGARH_DANTEWADA', 'KARNATAKA_RAMANAGAR', 'MADHYA PRADESH_ALIRAJPUR', 
# #'RAJASTHAN_PRATAPGARH', 'JAMMU & KASHMIR_BANDIPORA', 'ODISHA_DCP CTC', 'PUNJAB_SBS NAGAR', 'JAMMU & KASHMIR_SAMBA'}
# 
# #completed9 to 8 {'JAMMU & KASHMIR_RAILWAYS KMR'(change to RAILWAYS), 
# #completed'HIMACHAL PRADESH_BADDIPOLICEDIST'(1 - 8 enter 0), 
# #completed'ARUNACHAL PRADESH_ANJAW'(1-8 enter 0), 
# #completed'TAMIL NADU_TIRUPPUR'(1 - 8 enter 0), 
# #completed'HIMACHAL PRADESH_CID'(1-7 enter 0)}
# 
# #completed9 to 10 {'RAJASTHAN_G.R.P.'(10 enter 0), 
# #completed'PUNJAB_AMRITSAR'(completed), 
# #completed'JAMMU & KASHMIR_RAILWAYS KMR'(handled), 
# #completed'PUNJAB_LUDHIANA'(LUDHIANA RURAL and CP LUDHIANA combine), 
# #completed'JAMMU & KASHMIR_CRIME SRINAGAR'(10 enter 0), 
# #completed'PUNJAB_JALANDHAR'(CP JALANDHAR and JALANDHAR RURAL combine), 
# #completed'UTTAR PRADESH_KANPUR DEHAT'(KANPUR NAGAR and KANPUR DEHAT combine to make KANPUR)}
# 
# #completed10 to 9 {'UTTAR PRADESH_CSM NAGAR'(1-9 enter 0), 
# #completed'ANDHRA PRADESH_GUNTUR URBAN'(GUNTUR URBAN change to GUNTUR), 
# #'PUNJAB_CP LUDHIANA'(handled), 
# #'PUNJAB_CP JALANDHAR'(handled), 
# #'PUNJAB_JALANDHAR RURAL'(handled), 
# #'JAMMU & KASHMIR_RAILWAYSKMR'(handled), 
# #completed'ARUNACHAL PRADESH_RURAL'(1-9 enter 0), 
# #completed'TRIPURA_G.R.P.'(1-9 enter 0), 
# #completed'RAJASTHAN_G.R.P. AJMER'(1-9 enter 0), 
# #completed'ANDHRA PRADESH_TIRUPATHI URBAN'(1-9 enter 0), 
# #completed'JAMMU & KASHMIR_C.B.KASHMIR'(1-9 enter 0), 
# #completed'UTTAR PRADESH_RAMABAI NAGAR'(1-9 enter 0),
# #completed'RAJASTHAN_G.R.P. JODHPUR'(1-9 enter 0), 
# #completed'ANDHRA PRADESH_WARANGAL URBAN'(1-9 enter 0), 
# #completed'ANDHRA PRADESH_RAJAHMUNDRY'(1-9 enter 0), 
# #completed'KARNATAKA_YADGIRI'(1-9 enter 0), 
# #completed'PUNJAB_CP AMRITSAR'(handled), 
# #completed'JAMMU & KASHMIR_SOPORE'(1-9 enter 0), 
# #completed'GUJARAT_CID CRIME'(1-9 enter 0)}

# In[157]:


sc_Data = sc_Data[sc_Data.Year<2011]
sc_Col = list(sc_Data.columns)
sc_Col.remove('STATE/UT')
sc_Col.remove('DISTRICT')
sc_Col.remove('Year')
sc_Data = sc_Data[sc_Data['DISTRICT'] != 'TOTAL']
#sum of all the crimes as Total Crimes
sc_Data['Total_Crimes'] = sc_Data.iloc[:,3:].sum(axis=1)

district_Data = sc_Data
################  UP-->>CSM NAGAR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','CSM NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    #print(data_To_Add)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ARUNACHAL PRADESH-->>RURAL ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','RURAL'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TRIPURA-->>G.R.P. ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TRIPURA'),('DISTRICT','G.R.P.'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  RAJASTHAN-->>G.R.P. AJMER ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','G.R.P. AJMER'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  JAMMU & KASHMIR-->>C.B.KASHMIR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','C.B.KASHMIR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  UTTAR PRADESH-->>RAMABAI NAGAR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','RAMABAI NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  RAJASTHAN-->>G.R.P. JODHPUR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','G.R.P. JODHPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ANDHRA PRADESH-->>WARANGAL URBAN ##############################'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','WARANGAL URBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  ANDHRA PRADESH-->>'RAJAHMUNDRY' ##############################'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','RAJAHMUNDRY'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  KARNATAKA-->>YADGIRI ##############################'KARNATAKA'.upper(),'DISTRICT':'YADGIRI'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','YADGIRI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  JAMMU & KASHMIR-->>SOPORE ##############################'.upper(),'DISTRICT':'SOPORE'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SOPORE'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  GUJARAT-->>CID CRIME ##############################'.upper(),'DISTRICT':'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','GUJARAT'),('DISTRICT','CID CRIME'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HIMACHAL PRADESH-->>CID ##############################'HIMACHAL PRADESH'.upper(),'DISTRICT':'CID'
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HIMACHAL PRADESH'),('DISTRICT','CID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  TAMIL NADU-->>TIRUPPUR ##############################'.upper(),'DISTRICT':''
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','TIRUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  ARUNACHAL PRADESH-->>ANJAW ##############################'.upper(),'DISTRICT':''
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','ANJAW'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HIMACHAL PRADESH-->>CID ##############################
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','TIRUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

 ################  HIMACHAL PRADESH-->>BADDIPOLICEDIST ############################## HIMACHAL PRADESH'.upper(),'DISTRICT':'
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HIMACHAL PRADESH'),('DISTRICT','BADDIPOLICEDIST'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
######################################################################################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','TIRUPATHI URBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  NAGALAND-->>LONGLENG ##############################'.upper(),'DISTRICT':''
for year in range(2001,2007):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','NAGALAND'),('DISTRICT','LONGLENG'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  JHARKHAND-->>RAMGARH ##############################''.upper(),'DISTRICT':''
for year in range(2001,2007):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JHARKHAND'),('DISTRICT','RAMGARH'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  JHARKHAND-->>KHUNTI ##############################JHARKHAND'.upper(),'DISTRICT':'
for year in range(2001,2007):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JHARKHAND'),('DISTRICT','KHUNTI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  PUNJAB-->>MAJITHA ##############################
for year in range(2006,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','MAJITHA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>CHENGAI ##############################' '.upper(),'DISTRICT':'
for year in range(2005,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','CHENGAI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  HARYANA-->>MEWAT ##############################'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HARYANA'),('DISTRICT','MEWAT'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  CHHATTISGARH-->>SURAJPUR ##############################''.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','SURAJPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>UDALGURI ##############################'''.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','UDALGURI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>BASKA ##############################'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','BASKA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>CHIRANG ##############################'ASSAM'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','CHIRANG'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  PUNJAB-->>SAS NGR ##############################' '.upper(),'DISTRICT':''
for year in range(2001,2006):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','SAS NGR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HARYANA-->>PALWAL ##############################'''.upper(),'DISTRICT':''
for year in range(2001,2006):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HARYANA'),('DISTRICT','PALWAL'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>Ariyalur ##############################' Tamil Nadu'.upper(),'DISTRICT':''
for year in range(2001,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','ARIYALUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>KRISHNAGIRI ##############################' 
for year in range(2001,2004):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','KRISHNAGIRI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
##################################################################################
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','BORDER'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','CYBERABAD'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ASHOK NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ANUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################','DISTRICT':''
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','NARAYANPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','BURHANPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### PRADESH','DISTRICT':'
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','K/KUMEY'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### ''.upper(),'DISTRICT':'
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','JAGRAON'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### 
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','NAWAN SHAHR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
######################################################################################### '.upper(),'DISTRICT':'
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KERALA'),('DISTRICT','CBCID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
############### JAMMU & KASHMIR_SHOPIAN--> add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SHOPIAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_BANDIPORA- add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','BANDIPORA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_KISHTWAR--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','KISHTWAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_SAMBA- add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SAMBA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  ODISHA_DCP BBSR--> add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ODISHA'),('DISTRICT','DCP BBSR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  ODISHA_DCP CTC---> add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ODISHA'),('DISTRICT','DCP CTC'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  KARNATAKA_CBPURA--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','CBPURA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  MADHYA PRADESH_SINGRAULI-->add zero rows 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','SINGRAULI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
#  MADHYA PRADESH_ALIRAJPUR--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ALIRAJPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  TAMIL NADU_CHENNAISUBURBAN---> add zero rows for 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','CHENNAISUBURBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  UTTAR PRADESH_KANSHIRAM NAGAR-->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','KANSHIRAM NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  MANIPUR_CID--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MANIPUR'),('DISTRICT','CID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  GUJARAT_TAPI-->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','GUJARAT'),('DISTRICT','TAPI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  PUNJAB_SBS NAGAR--->  add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','SBS NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  KARNATAKA_RAMANAGAR-->add zero rows from 2001 to 2007


for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','RAMANAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  RAJASTHAN_PRATAPGARH--->add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','PRATAPGARH'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

###########################################
data_To_Add = {'STATE/UT':'JAMMU & KASHMIR', 'DISTRICT': 'CRIME SRINAGAR', 'Year': 2010,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against SCs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
data_To_Add = {'STATE/UT':'RAJASTHAN', 'DISTRICT': 'G.R.P.', 'Year': 2010,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against SCs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
####################################################
############################################################################
data_To_Add = {'STATE/UT':'West Bengal'.upper(), 'DISTRICT': 'Kharagpur G.R.P.'.upper(), 'Year': 2001,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against SCs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
#######################################################################
data_To_Add = {'STATE/UT':'Chhattisgarh'.upper(), 'DISTRICT': 'Kabirdham'.upper(), 'Year': 2001,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against SCs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
#######################################################################
data_To_Add = {'STATE/UT':'JAMMU & KASHMIR'.upper(), 'DISTRICT': 'HANDWARA', 'Year': 2001,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against SCs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
################################################################################################
data_To_Add = {'STATE/UT':'ASSAM', 'DISTRICT': 'N.C. HILLS', 'Year': 2001,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against SCs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
################################################################################################
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'N.C. HILLS'.upper()), 'DISTRICT'] = 'N.C.HILLS'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'GUMALA'.upper()), 'DISTRICT'] = 'GUMLA'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'MAHENDERGARH'.upper()), 'DISTRICT'] = 'MAHENDRAGARH'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'HISAR'.upper()), 'DISTRICT'] = 'HISSAR'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2002) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2003) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2006) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2007) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2008) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2009) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2010) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2006) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2007) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2008) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2009) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2010) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH CITY'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH G.R.P.'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'MUMBAI COMMR.'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'MUMBAI RLY.'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'NAVI MUMBAI'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'Vijayawada city'.upper()), 'DISTRICT'] = 'VIJAYAWADA'
district_Data.loc[(district_Data['DISTRICT'] == 'VIJAYAWADA RLY.'.upper()), 'DISTRICT'] = 'VIJAYAWADA'
district_Data.loc[(district_Data['DISTRICT'] == 'BORDER DISTRICT'.upper()), 'DISTRICT'] = 'Border'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'Imphal(West)'.upper()), 'DISTRICT'] = 'Imphal West'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'Imphal(East)'.upper()), 'DISTRICT'] = 'Imphal East'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR SOUTH'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR NORTH'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR RURAL'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR EAST'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JODHPUR CITY'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JODHPUR RURAL'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'G.R.P. Jodhpur'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'VILUPPURAM'.upper()), 'DISTRICT'] = 'VILLUPURAM'
district_Data.loc[(district_Data['DISTRICT'] == 'CP AMRITSAR'.upper()), 'DISTRICT'] = 'AMRITSAR'
district_Data.loc[(district_Data['DISTRICT'] == 'AMRITSAR RURAL'.upper()), 'DISTRICT'] = 'AMRITSAR'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYS KMR'.upper()), 'DISTRICT'] = 'RAILWAYS'
district_Data.loc[(district_Data['DISTRICT'] == 'CP LUDHIANA'.upper()), 'DISTRICT'] = 'LUDHIANA'
district_Data.loc[(district_Data['DISTRICT'] == 'LUDHIANA RURAL'.upper()), 'DISTRICT'] = 'LUDHIANA'
district_Data.loc[(district_Data['DISTRICT'] == 'JALANDHAR RURAL'.upper()), 'DISTRICT'] = 'JALANDHAR'
district_Data.loc[(district_Data['DISTRICT'] == 'CP JALANDHAR'.upper()), 'DISTRICT'] = 'JALANDHAR'
district_Data.loc[(district_Data['DISTRICT'] == 'KANPUR DEHAT'.upper()), 'DISTRICT'] = 'KANPUR'
district_Data.loc[(district_Data['DISTRICT'] == 'KANPUR NAGAR'.upper()), 'DISTRICT'] = 'KANPUR'
district_Data.loc[(district_Data['DISTRICT'] == 'GUNTUR URBAN'.upper()), 'DISTRICT'] = 'GUNTUR'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYS KMR'.upper()), 'DISTRICT'] = 'RAILWAYS'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYSKMR'.upper()), 'DISTRICT'] = 'RAILWAYS'

#  CHHATTISGARH_DANTEWARA---> DANTEWADA from 2001 to 2007
for i in range(2001,2008):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'DANTEWARA'.upper()), 'DISTRICT'] = 'DANTEWADA'


for i in range(2002,2011):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'Paschim Midnapur'.upper()), 'DISTRICT'] = 'MIDNAPUR'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'Purab Midnapur'.upper()), 'DISTRICT'] = 'MIDNAPUR'
    
for i in range(2003,2011):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'TRIVANDRUM COMMR.'.upper()), 'DISTRICT'] = 'TRIVANDRUM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'TRIVANDRUM RURAL'.upper()), 'DISTRICT'] = 'TRIVANDRUM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'KOZHIKODE COMMR.'.upper()), 'DISTRICT'] = 'KOZHIKODE'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'KOZHIKODE RURAL'.upper()), 'DISTRICT'] = 'KOZHIKODE'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'ERNAKULAM COMMR.'.upper()), 'DISTRICT'] = 'ERNAKULAM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'ERNAKULAM RURAL'.upper()), 'DISTRICT'] = 'ERNAKULAM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'UPPER DIBANG VALLEY'.upper()), 'DISTRICT'] = 'DIBANG VALLEY'

district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AMRAVATI COMMR.'.upper()), 'DISTRICT'] = 'AMRAVATI'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AMRAVATI RURAL'.upper()), 'DISTRICT'] = 'AMRAVATI'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AURANGABAD COMMR.'.upper()), 'DISTRICT'] = 'AURANGABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AURANGABAD RURAL'.upper()), 'DISTRICT'] = 'AURANGABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR COMMR.'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR RLY.'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR RURAL'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NASIK COMMR.'.upper()), 'DISTRICT'] = 'NASHIK'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NASIK RURAL'.upper()), 'DISTRICT'] = 'NASHIK'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE COMMR.'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE RLY.'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE RURAL'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'SOLAPUR COMMR.'.upper()), 'DISTRICT'] = 'SOLAPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'SOLAPUR RURAL'.upper()), 'DISTRICT'] = 'SOLAPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'THANE COMMR.'.upper()), 'DISTRICT'] = 'THANE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'THANE RURAL'.upper()), 'DISTRICT'] = 'THANE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'COIMBATORE RURAL'.upper()), 'DISTRICT'] = 'COIMBATORE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'COIMBATORE URBAN'.upper()), 'DISTRICT'] = 'COIMBATORE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'MADURAI URBAN'.upper()), 'DISTRICT'] = 'MADURAI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'MADURAI RURAL'.upper()), 'DISTRICT'] = 'MADURAI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'SALEM URBAN'.upper()), 'DISTRICT'] = 'SALEM'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY RLY.'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY RURAL'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY URBAN'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'THIRUNELVELI URBAN'.upper()), 'DISTRICT'] = 'TIRUNELVELI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'THIRUNELVELI RURAL'.upper()), 'DISTRICT'] = 'TIRUNELVELI'
district_Data.loc[(district_Data['STATE/UT'] == 'JHARKHAND') & (district_Data['DISTRICT'] == 'JAMSHEDPUR RLY.'.upper()), 'DISTRICT'] = 'PURBI SINGHBHUM'
district_Data.loc[(district_Data['STATE/UT'] == 'JHARKHAND') & (district_Data['DISTRICT'] == 'JAMSHEDPUR'.upper()), 'DISTRICT'] = 'PURBI SINGHBHUM'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'BANGALORE COMMR.'.upper()), 'DISTRICT'] = 'BANGALORE'
#district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'BANGALORE RURAL'.upper()), 'DISTRICT'] = 'BANGALORE'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'DHARWAD COMMR.'.upper()), 'DISTRICT'] = 'DHARWAD'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'DHARWAD COMMR.'.upper()), 'DISTRICT'] = 'DHARWAD'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'MYSORE COMMR.'.upper()), 'DISTRICT'] = 'MYSORE'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'MYSORE RURAL'.upper()), 'DISTRICT'] = 'MYSORE'
district_Data.loc[(district_Data['STATE/UT'] == 'BIHAR') & (district_Data['DISTRICT'] == 'BAGAHA'.upper()), 'DISTRICT'] = 'PASHCHIM CHAMPARAN'
district_Data.loc[(district_Data['STATE/UT'] == 'BIHAR') & (district_Data['DISTRICT'] == 'BETTIAH'.upper()), 'DISTRICT'] = 'PASHCHIM CHAMPARAN'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'SURAT COMMR.'.upper()), 'DISTRICT'] = 'SURAT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'SURAT RURAL'.upper()), 'DISTRICT'] = 'SURAT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'RAJKOT COMMR.'.upper()), 'DISTRICT'] = 'RAJKOT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'RAJKOT RURAL'.upper()), 'DISTRICT'] = 'RAJKOT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'AHMEDABAD COMMR.'.upper()), 'DISTRICT'] = 'AHMADABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'AHMEDABAD RURAL'.upper()), 'DISTRICT'] = 'AHMADABAD'
#district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'BANAS KANTHA'.upper()), 'DISTRICT'] = 'PALANPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'VADODARA COMMR.'.upper()), 'DISTRICT'] = 'VADODARA'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'VADODARA RURAL'.upper()), 'DISTRICT'] = 'VADODARA'
district_Data.loc[(district_Data['STATE/UT'] == 'ANDHRA PRADESH') & (district_Data['DISTRICT'] == 'CYBERABAD'.upper()), 'DISTRICT'] = 'RANGAREDDY'
district_Data.loc[(district_Data['STATE/UT'] == 'ANDHRA PRADESH') & (district_Data['DISTRICT'] == 'RANGA REDDY'.upper()), 'DISTRICT'] = 'RANGAREDDY'


UTs = ['A & N ISLANDS','CHANDIGARH', 'D & N HAVELI', 'DAMAN & DIU', 'DELHI', 'LAKSHADWEEP', 'PUDUCHERRY']
district_Data['STATE_DISTRICT'] = district_Data['STATE/UT']+'_'+district_Data['DISTRICT']
for i in list(district_Data['STATE/UT']):
    if i in UTs:
        district_Data.loc[district_Data['STATE/UT'] == i, 'STATE_DISTRICT'] = district_Data['STATE/UT']+'_'+district_Data['STATE/UT']
district_Data.head(15)
#district_Data = pd.DataFrame(district_Data.groupby(['STATE/UT','DISTRICT','Year']).agg({'Total_Crimes':"sum"}).reset_index())
district_Data = pd.DataFrame(district_Data.groupby(['STATE_DISTRICT','Year']).agg({'Murder':"sum",'Rape':"sum",'Kidnapping and Abduction':"sum",'Dacoity':"sum",'Robbery':"sum",'Arson':"sum",'Hurt':"sum",'Prevention of atrocities (POA) Act':"sum",'Protection of Civil Rights (PCR) Act':"sum",'Other Crimes Against SCs':"sum"}).reset_index())
district_Data['Total_Crimes'] = district_Data.iloc[:,2:].sum(axis=1)
sc_Data = district_Data


# In[159]:


sc_Data.to_csv(cwd+'/Preprocessing/clean_SC_Data.csv',index = 0)


# # District Data(ST) 

# In[160]:


st_Data = st_Data[st_Data.Year<2011]
sc_Col = list(st_Data.columns)
sc_Col.remove('STATE/UT')
sc_Col.remove('DISTRICT')
sc_Col.remove('Year')
st_Data = st_Data[st_Data['DISTRICT'] != 'TOTAL']
#sum of all the crimes as Total Crimes
st_Data['Total_Crimes'] = st_Data.iloc[:,3:].sum(axis=1)

district_Data = st_Data
################  UP-->>CSM NAGAR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','CSM NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    #print(data_To_Add)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ARUNACHAL PRADESH-->>RURAL ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','RURAL'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TRIPURA-->>G.R.P. ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TRIPURA'),('DISTRICT','G.R.P.'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  RAJASTHAN-->>G.R.P. AJMER ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','G.R.P. AJMER'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  JAMMU & KASHMIR-->>C.B.KASHMIR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','C.B.KASHMIR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  UTTAR PRADESH-->>RAMABAI NAGAR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','RAMABAI NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  RAJASTHAN-->>G.R.P. JODHPUR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','G.R.P. JODHPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ANDHRA PRADESH-->>WARANGAL URBAN ##############################'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','WARANGAL URBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  ANDHRA PRADESH-->>'RAJAHMUNDRY' ##############################'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','RAJAHMUNDRY'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  KARNATAKA-->>YADGIRI ##############################'KARNATAKA'.upper(),'DISTRICT':'YADGIRI'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','YADGIRI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  JAMMU & KASHMIR-->>SOPORE ##############################'.upper(),'DISTRICT':'SOPORE'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SOPORE'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  GUJARAT-->>CID CRIME ##############################'.upper(),'DISTRICT':'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','GUJARAT'),('DISTRICT','CID CRIME'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HIMACHAL PRADESH-->>CID ##############################'HIMACHAL PRADESH'.upper(),'DISTRICT':'CID'
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HIMACHAL PRADESH'),('DISTRICT','CID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  TAMIL NADU-->>TIRUPPUR ##############################'.upper(),'DISTRICT':''
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','TIRUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  ARUNACHAL PRADESH-->>ANJAW ##############################'.upper(),'DISTRICT':''
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','ANJAW'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HIMACHAL PRADESH-->>CID ##############################
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','TIRUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

 ################  HIMACHAL PRADESH-->>BADDIPOLICEDIST ############################## HIMACHAL PRADESH'.upper(),'DISTRICT':'
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HIMACHAL PRADESH'),('DISTRICT','BADDIPOLICEDIST'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
######################################################################################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','TIRUPATHI URBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  NAGALAND-->>LONGLENG ##############################'.upper(),'DISTRICT':''
for year in range(2001,2007):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','NAGALAND'),('DISTRICT','LONGLENG'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  JHARKHAND-->>RAMGARH ##############################''.upper(),'DISTRICT':''
for year in range(2001,2007):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JHARKHAND'),('DISTRICT','RAMGARH'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  JHARKHAND-->>KHUNTI ##############################JHARKHAND'.upper(),'DISTRICT':'
for year in range(2001,2007):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JHARKHAND'),('DISTRICT','KHUNTI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  PUNJAB-->>MAJITHA ##############################
for year in range(2006,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','MAJITHA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>CHENGAI ##############################' '.upper(),'DISTRICT':'
for year in range(2005,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','CHENGAI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  HARYANA-->>MEWAT ##############################'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HARYANA'),('DISTRICT','MEWAT'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  CHHATTISGARH-->>SURAJPUR ##############################''.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','SURAJPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>UDALGURI ##############################'''.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','UDALGURI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>BASKA ##############################'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','BASKA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>CHIRANG ##############################'ASSAM'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','CHIRANG'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  PUNJAB-->>SAS NGR ##############################' '.upper(),'DISTRICT':''
for year in range(2001,2006):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','SAS NGR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HARYANA-->>PALWAL ##############################'''.upper(),'DISTRICT':''
for year in range(2001,2006):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HARYANA'),('DISTRICT','PALWAL'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>Ariyalur ##############################' Tamil Nadu'.upper(),'DISTRICT':''
for year in range(2001,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','ARIYALUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>KRISHNAGIRI ##############################' 
for year in range(2001,2004):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','KRISHNAGIRI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
##################################################################################
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','BORDER'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','CYBERABAD'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ASHOK NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ANUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################','DISTRICT':''
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','NARAYANPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','BURHANPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### PRADESH','DISTRICT':'
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','K/KUMEY'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### ''.upper(),'DISTRICT':'
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','JAGRAON'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### 
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','NAWAN SHAHR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
######################################################################################### '.upper(),'DISTRICT':'
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KERALA'),('DISTRICT','CBCID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
############### JAMMU & KASHMIR_SHOPIAN--> add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SHOPIAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_BANDIPORA- add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','BANDIPORA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_KISHTWAR--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','KISHTWAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_SAMBA- add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SAMBA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  ODISHA_DCP BBSR--> add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ODISHA'),('DISTRICT','DCP BBSR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  ODISHA_DCP CTC---> add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ODISHA'),('DISTRICT','DCP CTC'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  KARNATAKA_CBPURA--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','CBPURA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  MADHYA PRADESH_SINGRAULI-->add zero rows 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','SINGRAULI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
#  MADHYA PRADESH_ALIRAJPUR--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ALIRAJPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  TAMIL NADU_CHENNAISUBURBAN---> add zero rows for 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','CHENNAISUBURBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  UTTAR PRADESH_KANSHIRAM NAGAR-->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','KANSHIRAM NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  MANIPUR_CID--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MANIPUR'),('DISTRICT','CID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  GUJARAT_TAPI-->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','GUJARAT'),('DISTRICT','TAPI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  PUNJAB_SBS NAGAR--->  add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','SBS NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  KARNATAKA_RAMANAGAR-->add zero rows from 2001 to 2007


for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','RAMANAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  RAJASTHAN_PRATAPGARH--->add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','PRATAPGARH'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

###########################################
data_To_Add = {'STATE/UT':'JAMMU & KASHMIR', 'DISTRICT': 'CRIME SRINAGAR', 'Year': 2010,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against STs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
data_To_Add = {'STATE/UT':'RAJASTHAN', 'DISTRICT': 'G.R.P.', 'Year': 2010,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against STs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
####################################################
############################################################################
data_To_Add = {'STATE/UT':'West Bengal'.upper(), 'DISTRICT': 'Kharagpur G.R.P.'.upper(), 'Year': 2001,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against STs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
#######################################################################
data_To_Add = {'STATE/UT':'Chhattisgarh'.upper(), 'DISTRICT': 'Kabirdham'.upper(), 'Year': 2001,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against STs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
#######################################################################
data_To_Add = {'STATE/UT':'JAMMU & KASHMIR'.upper(), 'DISTRICT': 'HANDWARA', 'Year': 2001,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against STs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
################################################################################################
data_To_Add = {'STATE/UT':'ASSAM', 'DISTRICT': 'N.C. HILLS', 'Year': 2001,'Total_Crimes': 0,'Murder': 0, 'Rape': 0, 'Kidnapping and Abduction': 0, 'Dacoity': 0, 'Robbery': 0, 'Arson': 0, 'Hurt': 0, 'Prevention of atrocities (POA) Act': 0, 'Protection of Civil Rights (PCR) Act': 0, 'Other Crimes Against STs': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
################################################################################################
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'N.C. HILLS'.upper()), 'DISTRICT'] = 'N.C.HILLS'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'GUMALA'.upper()), 'DISTRICT'] = 'GUMLA'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'MAHENDERGARH'.upper()), 'DISTRICT'] = 'MAHENDRAGARH'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'HISAR'.upper()), 'DISTRICT'] = 'HISSAR'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2002) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2003) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2006) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2007) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2008) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2009) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2010) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2006) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2007) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2008) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2009) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2010) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH CITY'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH G.R.P.'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'MUMBAI COMMR.'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'MUMBAI RLY.'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'NAVI MUMBAI'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'Vijayawada city'.upper()), 'DISTRICT'] = 'VIJAYAWADA'
district_Data.loc[(district_Data['DISTRICT'] == 'VIJAYAWADA RLY.'.upper()), 'DISTRICT'] = 'VIJAYAWADA'
district_Data.loc[(district_Data['DISTRICT'] == 'BORDER DISTRICT'.upper()), 'DISTRICT'] = 'Border'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'Imphal(West)'.upper()), 'DISTRICT'] = 'Imphal West'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'Imphal(East)'.upper()), 'DISTRICT'] = 'Imphal East'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR SOUTH'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR NORTH'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR RURAL'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR EAST'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JODHPUR CITY'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JODHPUR RURAL'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'G.R.P. Jodhpur'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'VILUPPURAM'.upper()), 'DISTRICT'] = 'VILLUPURAM'
district_Data.loc[(district_Data['DISTRICT'] == 'CP AMRITSAR'.upper()), 'DISTRICT'] = 'AMRITSAR'
district_Data.loc[(district_Data['DISTRICT'] == 'AMRITSAR RURAL'.upper()), 'DISTRICT'] = 'AMRITSAR'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYS KMR'.upper()), 'DISTRICT'] = 'RAILWAYS'
district_Data.loc[(district_Data['DISTRICT'] == 'CP LUDHIANA'.upper()), 'DISTRICT'] = 'LUDHIANA'
district_Data.loc[(district_Data['DISTRICT'] == 'LUDHIANA RURAL'.upper()), 'DISTRICT'] = 'LUDHIANA'
district_Data.loc[(district_Data['DISTRICT'] == 'JALANDHAR RURAL'.upper()), 'DISTRICT'] = 'JALANDHAR'
district_Data.loc[(district_Data['DISTRICT'] == 'CP JALANDHAR'.upper()), 'DISTRICT'] = 'JALANDHAR'
district_Data.loc[(district_Data['DISTRICT'] == 'KANPUR DEHAT'.upper()), 'DISTRICT'] = 'KANPUR'
district_Data.loc[(district_Data['DISTRICT'] == 'KANPUR NAGAR'.upper()), 'DISTRICT'] = 'KANPUR'
district_Data.loc[(district_Data['DISTRICT'] == 'GUNTUR URBAN'.upper()), 'DISTRICT'] = 'GUNTUR'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYS KMR'.upper()), 'DISTRICT'] = 'RAILWAYS'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYSKMR'.upper()), 'DISTRICT'] = 'RAILWAYS'

#  CHHATTISGARH_DANTEWARA---> DANTEWADA from 2001 to 2007
for i in range(2001,2008):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'DANTEWARA'.upper()), 'DISTRICT'] = 'DANTEWADA'


for i in range(2002,2011):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'Paschim Midnapur'.upper()), 'DISTRICT'] = 'MIDNAPUR'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'Purab Midnapur'.upper()), 'DISTRICT'] = 'MIDNAPUR'
    
for i in range(2003,2011):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'TRIVANDRUM COMMR.'.upper()), 'DISTRICT'] = 'TRIVANDRUM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'TRIVANDRUM RURAL'.upper()), 'DISTRICT'] = 'TRIVANDRUM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'KOZHIKODE COMMR.'.upper()), 'DISTRICT'] = 'KOZHIKODE'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'KOZHIKODE RURAL'.upper()), 'DISTRICT'] = 'KOZHIKODE'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'ERNAKULAM COMMR.'.upper()), 'DISTRICT'] = 'ERNAKULAM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'ERNAKULAM RURAL'.upper()), 'DISTRICT'] = 'ERNAKULAM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'UPPER DIBANG VALLEY'.upper()), 'DISTRICT'] = 'DIBANG VALLEY'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AMRAVATI COMMR.'.upper()), 'DISTRICT'] = 'AMRAVATI'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AMRAVATI RURAL'.upper()), 'DISTRICT'] = 'AMRAVATI'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AURANGABAD COMMR.'.upper()), 'DISTRICT'] = 'AURANGABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AURANGABAD RURAL'.upper()), 'DISTRICT'] = 'AURANGABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR COMMR.'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR RLY.'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR RURAL'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NASIK COMMR.'.upper()), 'DISTRICT'] = 'NASHIK'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NASIK RURAL'.upper()), 'DISTRICT'] = 'NASHIK'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE COMMR.'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE RLY.'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE RURAL'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'SOLAPUR COMMR.'.upper()), 'DISTRICT'] = 'SOLAPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'SOLAPUR RURAL'.upper()), 'DISTRICT'] = 'SOLAPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'THANE COMMR.'.upper()), 'DISTRICT'] = 'THANE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'THANE RURAL'.upper()), 'DISTRICT'] = 'THANE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'COIMBATORE RURAL'.upper()), 'DISTRICT'] = 'COIMBATORE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'COIMBATORE URBAN'.upper()), 'DISTRICT'] = 'COIMBATORE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'MADURAI URBAN'.upper()), 'DISTRICT'] = 'MADURAI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'MADURAI RURAL'.upper()), 'DISTRICT'] = 'MADURAI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'SALEM URBAN'.upper()), 'DISTRICT'] = 'SALEM'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY RLY.'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY RURAL'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY URBAN'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'THIRUNELVELI URBAN'.upper()), 'DISTRICT'] = 'TIRUNELVELI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'THIRUNELVELI RURAL'.upper()), 'DISTRICT'] = 'TIRUNELVELI'
district_Data.loc[(district_Data['STATE/UT'] == 'JHARKHAND') & (district_Data['DISTRICT'] == 'JAMSHEDPUR RLY.'.upper()), 'DISTRICT'] = 'PURBI SINGHBHUM'
district_Data.loc[(district_Data['STATE/UT'] == 'JHARKHAND') & (district_Data['DISTRICT'] == 'JAMSHEDPUR'.upper()), 'DISTRICT'] = 'PURBI SINGHBHUM'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'BANGALORE COMMR.'.upper()), 'DISTRICT'] = 'BANGALORE'
#district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'BANGALORE RURAL'.upper()), 'DISTRICT'] = 'BANGALORE'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'DHARWAD COMMR.'.upper()), 'DISTRICT'] = 'DHARWAD'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'DHARWAD COMMR.'.upper()), 'DISTRICT'] = 'DHARWAD'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'MYSORE COMMR.'.upper()), 'DISTRICT'] = 'MYSORE'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'MYSORE RURAL'.upper()), 'DISTRICT'] = 'MYSORE'
district_Data.loc[(district_Data['STATE/UT'] == 'BIHAR') & (district_Data['DISTRICT'] == 'BAGAHA'.upper()), 'DISTRICT'] = 'PASHCHIM CHAMPARAN'
district_Data.loc[(district_Data['STATE/UT'] == 'BIHAR') & (district_Data['DISTRICT'] == 'BETTIAH'.upper()), 'DISTRICT'] = 'PASHCHIM CHAMPARAN'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'SURAT COMMR.'.upper()), 'DISTRICT'] = 'SURAT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'SURAT RURAL'.upper()), 'DISTRICT'] = 'SURAT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'RAJKOT COMMR.'.upper()), 'DISTRICT'] = 'RAJKOT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'RAJKOT RURAL'.upper()), 'DISTRICT'] = 'RAJKOT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'AHMEDABAD COMMR.'.upper()), 'DISTRICT'] = 'AHMADABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'AHMEDABAD RURAL'.upper()), 'DISTRICT'] = 'AHMADABAD'
#district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'BANAS KANTHA'.upper()), 'DISTRICT'] = 'PALANPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'VADODARA COMMR.'.upper()), 'DISTRICT'] = 'VADODARA'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'VADODARA RURAL'.upper()), 'DISTRICT'] = 'VADODARA'
district_Data.loc[(district_Data['STATE/UT'] == 'ANDHRA PRADESH') & (district_Data['DISTRICT'] == 'CYBERABAD'.upper()), 'DISTRICT'] = 'RANGAREDDY'
district_Data.loc[(district_Data['STATE/UT'] == 'ANDHRA PRADESH') & (district_Data['DISTRICT'] == 'RANGA REDDY'.upper()), 'DISTRICT'] = 'RANGAREDDY'


UTs = ['A & N ISLANDS','CHANDIGARH', 'D & N HAVELI', 'DAMAN & DIU', 'DELHI', 'LAKSHADWEEP', 'PUDUCHERRY']
district_Data['STATE_DISTRICT'] = district_Data['STATE/UT']+'_'+district_Data['DISTRICT']
for i in list(district_Data['STATE/UT']):
    if i in UTs:
        district_Data.loc[district_Data['STATE/UT'] == i, 'STATE_DISTRICT'] = district_Data['STATE/UT']+'_'+district_Data['STATE/UT']
district_Data.head(15)
#district_Data = pd.DataFrame(district_Data.groupby(['STATE/UT','DISTRICT','Year']).agg({'Total_Crimes':"sum"}).reset_index())
district_Data = pd.DataFrame(district_Data.groupby(['STATE_DISTRICT','Year']).agg({'Murder':"sum",'Rape':"sum",'Kidnapping and Abduction':"sum",'Dacoity':"sum",'Robbery':"sum",'Arson':"sum",'Hurt':"sum",'Prevention of atrocities (POA) Act':"sum",'Protection of Civil Rights (PCR) Act':"sum",'Other Crimes Against STs':"sum"}).reset_index())
district_Data['Total_Crimes'] = district_Data.iloc[:,2:].sum(axis=1)
st_Data = district_Data


# In[162]:


st_Data.to_csv(cwd+'/Preprocessing/clean_ST_Data.csv',index = 0)


# # District Data(Children) 

# In[163]:


children_Data = children_Data[children_Data.Year<2011]
children_Data = children_Data[children_Data['DISTRICT'] != 'TOTAL']
#children_Data['Total_Crimes'] = children_Data.iloc[:,3:].sum(axis=1)
children_Data['Total_Crimes'] = children_Data['Total']
children_Data = children_Data.drop('Total', axis=1)
sc_Col = list(children_Data.columns)
sc_Col.remove('STATE/UT')
sc_Col.remove('DISTRICT')
sc_Col.remove('Year')
#sum of all the crimes as Total Crimes

district_Data = children_Data
district_Data.loc[(district_Data['DISTRICT'] == 'GARI HILLS EAST'.upper()), 'DISTRICT'] = 'GARO HILLS EAST'
district_Data.loc[(district_Data['DISTRICT'] == 'BADWANI'.upper()), 'DISTRICT'] = 'BARWANI'
district_Data.loc[(district_Data['DISTRICT'] == 'KANCHEEPURAM'.upper()), 'DISTRICT'] = 'KANCHIPURAM'
district_Data.loc[(district_Data['DISTRICT'] == 'AMBEDKARNAGAR'.upper()), 'DISTRICT'] = 'AMBEDKAR NAGAR'
district_Data.loc[(district_Data['DISTRICT'] == 'BIJAPUR'.upper()) & (district_Data['STATE/UT'] == 'CHHATTISGARH'.upper()), 'DISTRICT'] = 'BIZAPUR'
district_Data.loc[(district_Data['DISTRICT'] == 'SURGUJA'.upper()), 'DISTRICT'] = 'SARGUJA'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYSJMU'.upper()), 'DISTRICT'] = 'RAILWAYS'

################  UP-->>CSM NAGAR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','CSM NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    #print(data_To_Add)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ARUNACHAL PRADESH-->>RURAL ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','RURAL'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TRIPURA-->>G.R.P. ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TRIPURA'),('DISTRICT','G.R.P.'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  RAJASTHAN-->>G.R.P. AJMER ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','G.R.P. AJMER'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  JAMMU & KASHMIR-->>C.B.KASHMIR ##############################
for year in range(2001,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','C.B.KASHMIR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  UTTAR PRADESH-->>RAMABAI NAGAR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','RAMABAI NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  RAJASTHAN-->>G.R.P. JODHPUR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','G.R.P. JODHPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ANDHRA PRADESH-->>WARANGAL URBAN ##############################'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','WARANGAL URBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  ANDHRA PRADESH-->>'RAJAHMUNDRY' ##############################'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','RAJAHMUNDRY'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  KARNATAKA-->>YADGIRI ##############################'KARNATAKA'.upper(),'DISTRICT':'YADGIRI'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','YADGIRI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  JAMMU & KASHMIR-->>SOPORE ##############################'.upper(),'DISTRICT':'SOPORE'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SOPORE'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  GUJARAT-->>CID CRIME ##############################'.upper(),'DISTRICT':'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','GUJARAT'),('DISTRICT','CID CRIME'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HIMACHAL PRADESH-->>CID ##############################'HIMACHAL PRADESH'.upper(),'DISTRICT':'CID'
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HIMACHAL PRADESH'),('DISTRICT','CID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  TAMIL NADU-->>TIRUPPUR ##############################'.upper(),'DISTRICT':''
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','TIRUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  ARUNACHAL PRADESH-->>ANJAW ##############################'.upper(),'DISTRICT':''
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','ANJAW'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HIMACHAL PRADESH-->>CID ##############################
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','TIRUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

 ################  HIMACHAL PRADESH-->>BADDIPOLICEDIST ############################## HIMACHAL PRADESH'.upper(),'DISTRICT':'
for year in range(2001,2009):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HIMACHAL PRADESH'),('DISTRICT','BADDIPOLICEDIST'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
######################################################################################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','TIRUPATHI URBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  NAGALAND-->>LONGLENG ##############################'.upper(),'DISTRICT':''
for year in range(2001,2007):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','NAGALAND'),('DISTRICT','LONGLENG'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  JHARKHAND-->>RAMGARH ##############################''.upper(),'DISTRICT':''
for year in range(2001,2007):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JHARKHAND'),('DISTRICT','RAMGARH'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  JHARKHAND-->>KHUNTI ##############################JHARKHAND'.upper(),'DISTRICT':'
for year in range(2001,2007):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JHARKHAND'),('DISTRICT','KHUNTI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  PUNJAB-->>MAJITHA ##############################
for year in range(2006,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','MAJITHA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>CHENGAI ##############################' '.upper(),'DISTRICT':'
for year in range(2005,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','CHENGAI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  HARYANA-->>MEWAT ##############################'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HARYANA'),('DISTRICT','MEWAT'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  CHHATTISGARH-->>SURAJPUR ##############################''.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','SURAJPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>UDALGURI ##############################'''.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','UDALGURI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>BASKA ##############################'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','BASKA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>CHIRANG ##############################'ASSAM'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','CHIRANG'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  PUNJAB-->>SAS NGR ##############################' '.upper(),'DISTRICT':''
for year in range(2001,2006):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','SAS NGR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HARYANA-->>PALWAL ##############################'''.upper(),'DISTRICT':''
for year in range(2001,2006):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','HARYANA'),('DISTRICT','PALWAL'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>Ariyalur ##############################' Tamil Nadu'.upper(),'DISTRICT':''
for year in range(2001,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','ARIYALUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>KRISHNAGIRI ##############################' 
for year in range(2001,2004):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','KRISHNAGIRI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
##################################################################################
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','BORDER'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','CYBERABAD'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ASHOK NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ANUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################','DISTRICT':''
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','NARAYANPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','BURHANPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### PRADESH','DISTRICT':'
for year in range(2001,2003):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','K/KUMEY'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### ''.upper(),'DISTRICT':'
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','JAGRAON'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### 
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','NAWAN SHAHR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
######################################################################################### '.upper(),'DISTRICT':'
for year in range(2008,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KERALA'),('DISTRICT','CBCID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
############### JAMMU & KASHMIR_SHOPIAN--> add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SHOPIAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_BANDIPORA- add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','BANDIPORA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_KISHTWAR--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','KISHTWAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_SAMBA- add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SAMBA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  ODISHA_DCP BBSR--> add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ODISHA'),('DISTRICT','DCP BBSR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  ODISHA_DCP CTC---> add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','ODISHA'),('DISTRICT','DCP CTC'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  KARNATAKA_CBPURA--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','CBPURA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  MADHYA PRADESH_SINGRAULI-->add zero rows 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','SINGRAULI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
#  MADHYA PRADESH_ALIRAJPUR--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ALIRAJPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  TAMIL NADU_CHENNAISUBURBAN---> add zero rows for 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','CHENNAISUBURBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  UTTAR PRADESH_KANSHIRAM NAGAR-->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','KANSHIRAM NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  MANIPUR_CID--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','MANIPUR'),('DISTRICT','CID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  GUJARAT_TAPI-->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','GUJARAT'),('DISTRICT','TAPI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  PUNJAB_SBS NAGAR--->  add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','SBS NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  KARNATAKA_RAMANAGAR-->add zero rows from 2001 to 2007


for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','RAMANAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  RAJASTHAN_PRATAPGARH--->add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','PRATAPGARH'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
    
#  CHHATTISGARH_KAWARDHA--->add zero rows from 2002 to 2010
for year in range(2002,2011):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','KAWARDHA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
    
#  JAMMU & KASHMIR_CRIME KASHMIR--->add zero rows from 2001 to 2009
for year in range(2001,2010):
    data_To_Add = {k:0 for k in sc_Col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','CRIME KASHMIR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

###########################################
data_To_Add = {'STATE/UT':'JAMMU & KASHMIR', 'DISTRICT': 'CRIME SRINAGAR', 'Year': 2010, 'Murder':0, 'Rape':0, 'Kidnapping and Abduction':0, 'Foeticide':0, 'Abetment of suicide':0,'Exposure and abandonment':0, 'Procuration of minor girls':0,'Buying of girls for prostitution':0, 'Selling of girls for prostitution':0,'Prohibition of child marriage act':0, 'Other Crimes':0, 'Total_Crimes':0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
data_To_Add = {'STATE/UT':'RAJASTHAN', 'DISTRICT': 'G.R.P.', 'Year': 2010,'Murder':0, 'Rape':0, 'Kidnapping and Abduction':0, 'Foeticide':0, 'Abetment of suicide':0,'Exposure and abandonment':0, 'Procuration of minor girls':0,'Buying of girls for prostitution':0, 'Selling of girls for prostitution':0,'Prohibition of child marriage act':0, 'Other Crimes':0, 'Total_Crimes':0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
####################################################
############################################################################
data_To_Add = {'STATE/UT':'West Bengal'.upper(), 'DISTRICT': 'Kharagpur G.R.P.'.upper(), 'Year': 2001,'Murder':0, 'Rape':0, 'Kidnapping and Abduction':0, 'Foeticide':0, 'Abetment of suicide':0,'Exposure and abandonment':0, 'Procuration of minor girls':0,'Buying of girls for prostitution':0, 'Selling of girls for prostitution':0,'Prohibition of child marriage act':0, 'Other Crimes':0, 'Total_Crimes':0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
#######################################################################
data_To_Add = {'STATE/UT':'Chhattisgarh'.upper(), 'DISTRICT': 'Kabirdham'.upper(), 'Year': 2001,'Murder':0, 'Rape':0, 'Kidnapping and Abduction':0, 'Foeticide':0, 'Abetment of suicide':0,'Exposure and abandonment':0, 'Procuration of minor girls':0,'Buying of girls for prostitution':0, 'Selling of girls for prostitution':0,'Prohibition of child marriage act':0, 'Other Crimes':0, 'Total_Crimes':0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
#######################################################################
data_To_Add = {'STATE/UT':'JAMMU & KASHMIR'.upper(), 'DISTRICT': 'HANDWARA', 'Year': 2001,'Murder':0, 'Rape':0, 'Kidnapping and Abduction':0, 'Foeticide':0, 'Abetment of suicide':0,'Exposure and abandonment':0, 'Procuration of minor girls':0,'Buying of girls for prostitution':0, 'Selling of girls for prostitution':0,'Prohibition of child marriage act':0, 'Other Crimes':0, 'Total_Crimes':0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
################################################################################################
data_To_Add = {'STATE/UT':'ASSAM', 'DISTRICT': 'N.C. HILLS', 'Year': 2001,'Murder':0, 'Rape':0, 'Kidnapping and Abduction':0, 'Foeticide':0, 'Abetment of suicide':0,'Exposure and abandonment':0, 'Procuration of minor girls':0,'Buying of girls for prostitution':0, 'Selling of girls for prostitution':0,'Prohibition of child marriage act':0, 'Other Crimes':0, 'Total_Crimes':0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
################################################################################################
data_To_Add = {'STATE/UT':'BIHAR', 'DISTRICT': 'NAWADAH', 'Year': 2003,'Murder':0, 'Rape':0, 'Kidnapping and Abduction':0, 'Foeticide':0, 'Abetment of suicide':0,'Exposure and abandonment':0, 'Procuration of minor girls':0,'Buying of girls for prostitution':0, 'Selling of girls for prostitution':0,'Prohibition of child marriage act':0, 'Other Crimes':0, 'Total_Crimes':0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
################################################################################################
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'N.C. HILLS'.upper()), 'DISTRICT'] = 'N.C.HILLS'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'GUMALA'.upper()), 'DISTRICT'] = 'GUMLA'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'MAHENDERGARH'.upper()), 'DISTRICT'] = 'MAHENDRAGARH'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'HISAR'.upper()), 'DISTRICT'] = 'HISSAR'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2002) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2003) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2006) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2007) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2008) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2009) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2010) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2006) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2007) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2008) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2009) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2010) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH CITY'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH G.R.P.'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'MUMBAI COMMR.'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'MUMBAI RLY.'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'NAVI MUMBAI'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'Vijayawada city'.upper()), 'DISTRICT'] = 'VIJAYAWADA'
district_Data.loc[(district_Data['DISTRICT'] == 'VIJAYAWADA RLY.'.upper()), 'DISTRICT'] = 'VIJAYAWADA'
district_Data.loc[(district_Data['DISTRICT'] == 'BORDER DISTRICT'.upper()), 'DISTRICT'] = 'Border'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'Imphal(West)'.upper()), 'DISTRICT'] = 'Imphal West'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'Imphal(East)'.upper()), 'DISTRICT'] = 'Imphal East'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR SOUTH'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR NORTH'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR RURAL'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR EAST'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JODHPUR CITY'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JODHPUR RURAL'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'G.R.P. Jodhpur'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'VILUPPURAM'.upper()), 'DISTRICT'] = 'VILLUPURAM'
district_Data.loc[(district_Data['DISTRICT'] == 'CP AMRITSAR'.upper()), 'DISTRICT'] = 'AMRITSAR'
district_Data.loc[(district_Data['DISTRICT'] == 'AMRITSAR RURAL'.upper()), 'DISTRICT'] = 'AMRITSAR'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYS KMR'.upper()), 'DISTRICT'] = 'RAILWAYS'
district_Data.loc[(district_Data['DISTRICT'] == 'CP LUDHIANA'.upper()), 'DISTRICT'] = 'LUDHIANA'
district_Data.loc[(district_Data['DISTRICT'] == 'LUDHIANA RURAL'.upper()), 'DISTRICT'] = 'LUDHIANA'
district_Data.loc[(district_Data['DISTRICT'] == 'JALANDHAR RURAL'.upper()), 'DISTRICT'] = 'JALANDHAR'
district_Data.loc[(district_Data['DISTRICT'] == 'CP JALANDHAR'.upper()), 'DISTRICT'] = 'JALANDHAR'
district_Data.loc[(district_Data['DISTRICT'] == 'KANPUR DEHAT'.upper()), 'DISTRICT'] = 'KANPUR'
district_Data.loc[(district_Data['DISTRICT'] == 'KANPUR NAGAR'.upper()), 'DISTRICT'] = 'KANPUR'
district_Data.loc[(district_Data['DISTRICT'] == 'GUNTUR URBAN'.upper()), 'DISTRICT'] = 'GUNTUR'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYS KMR'.upper()), 'DISTRICT'] = 'RAILWAYS'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYSKMR'.upper()), 'DISTRICT'] = 'RAILWAYS'

#  CHHATTISGARH_DANTEWARA---> DANTEWADA from 2001 to 2007
for i in range(2001,2008):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'DANTEWARA'.upper()), 'DISTRICT'] = 'DANTEWADA'


for i in range(2002,2011):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'Paschim Midnapur'.upper()), 'DISTRICT'] = 'MIDNAPUR'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'Purab Midnapur'.upper()), 'DISTRICT'] = 'MIDNAPUR'
    
for i in range(2003,2011):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'TRIVANDRUM COMMR.'.upper()), 'DISTRICT'] = 'TRIVANDRUM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'TRIVANDRUM RURAL'.upper()), 'DISTRICT'] = 'TRIVANDRUM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'KOZHIKODE COMMR.'.upper()), 'DISTRICT'] = 'KOZHIKODE'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'KOZHIKODE RURAL'.upper()), 'DISTRICT'] = 'KOZHIKODE'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'ERNAKULAM COMMR.'.upper()), 'DISTRICT'] = 'ERNAKULAM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'ERNAKULAM RURAL'.upper()), 'DISTRICT'] = 'ERNAKULAM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'UPPER DIBANG VALLEY'.upper()), 'DISTRICT'] = 'DIBANG VALLEY'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AMRAVATI COMMR.'.upper()), 'DISTRICT'] = 'AMRAVATI'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AMRAVATI RURAL'.upper()), 'DISTRICT'] = 'AMRAVATI'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AURANGABAD COMMR.'.upper()), 'DISTRICT'] = 'AURANGABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AURANGABAD RURAL'.upper()), 'DISTRICT'] = 'AURANGABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR COMMR.'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR RLY.'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR RURAL'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NASIK COMMR.'.upper()), 'DISTRICT'] = 'NASHIK'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NASIK RURAL'.upper()), 'DISTRICT'] = 'NASHIK'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE COMMR.'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE RLY.'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE RURAL'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'SOLAPUR COMMR.'.upper()), 'DISTRICT'] = 'SOLAPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'SOLAPUR RURAL'.upper()), 'DISTRICT'] = 'SOLAPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'THANE COMMR.'.upper()), 'DISTRICT'] = 'THANE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'THANE RURAL'.upper()), 'DISTRICT'] = 'THANE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'COIMBATORE RURAL'.upper()), 'DISTRICT'] = 'COIMBATORE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'COIMBATORE URBAN'.upper()), 'DISTRICT'] = 'COIMBATORE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'MADURAI URBAN'.upper()), 'DISTRICT'] = 'MADURAI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'MADURAI RURAL'.upper()), 'DISTRICT'] = 'MADURAI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'SALEM URBAN'.upper()), 'DISTRICT'] = 'SALEM'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY RLY.'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY RURAL'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY URBAN'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'THIRUNELVELI URBAN'.upper()), 'DISTRICT'] = 'TIRUNELVELI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'THIRUNELVELI RURAL'.upper()), 'DISTRICT'] = 'TIRUNELVELI'
district_Data.loc[(district_Data['STATE/UT'] == 'JHARKHAND') & (district_Data['DISTRICT'] == 'JAMSHEDPUR RLY.'.upper()), 'DISTRICT'] = 'PURBI SINGHBHUM'
district_Data.loc[(district_Data['STATE/UT'] == 'JHARKHAND') & (district_Data['DISTRICT'] == 'JAMSHEDPUR'.upper()), 'DISTRICT'] = 'PURBI SINGHBHUM'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'BANGALORE COMMR.'.upper()), 'DISTRICT'] = 'BANGALORE'
#district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'BANGALORE RURAL'.upper()), 'DISTRICT'] = 'BANGALORE'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'DHARWAD COMMR.'.upper()), 'DISTRICT'] = 'DHARWAD'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'DHARWAD COMMR.'.upper()), 'DISTRICT'] = 'DHARWAD'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'MYSORE COMMR.'.upper()), 'DISTRICT'] = 'MYSORE'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'MYSORE RURAL'.upper()), 'DISTRICT'] = 'MYSORE'
district_Data.loc[(district_Data['STATE/UT'] == 'BIHAR') & (district_Data['DISTRICT'] == 'BAGAHA'.upper()), 'DISTRICT'] = 'PASHCHIM CHAMPARAN'
district_Data.loc[(district_Data['STATE/UT'] == 'BIHAR') & (district_Data['DISTRICT'] == 'BETTIAH'.upper()), 'DISTRICT'] = 'PASHCHIM CHAMPARAN'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'SURAT COMMR.'.upper()), 'DISTRICT'] = 'SURAT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'SURAT RURAL'.upper()), 'DISTRICT'] = 'SURAT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'RAJKOT COMMR.'.upper()), 'DISTRICT'] = 'RAJKOT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'RAJKOT RURAL'.upper()), 'DISTRICT'] = 'RAJKOT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'AHMEDABAD COMMR.'.upper()), 'DISTRICT'] = 'AHMADABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'AHMEDABAD RURAL'.upper()), 'DISTRICT'] = 'AHMADABAD'
#district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'BANAS KANTHA'.upper()), 'DISTRICT'] = 'PALANPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'VADODARA COMMR.'.upper()), 'DISTRICT'] = 'VADODARA'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'VADODARA RURAL'.upper()), 'DISTRICT'] = 'VADODARA'
district_Data.loc[(district_Data['STATE/UT'] == 'ANDHRA PRADESH') & (district_Data['DISTRICT'] == 'CYBERABAD'.upper()), 'DISTRICT'] = 'RANGAREDDY'
district_Data.loc[(district_Data['STATE/UT'] == 'ANDHRA PRADESH') & (district_Data['DISTRICT'] == 'RANGA REDDY'.upper()), 'DISTRICT'] = 'RANGAREDDY'


UTs = ['A & N ISLANDS','CHANDIGARH', 'D & N HAVELI', 'DAMAN & DIU', 'DELHI', 'LAKSHADWEEP', 'PUDUCHERRY']
district_Data['STATE_DISTRICT'] = district_Data['STATE/UT']+'_'+district_Data['DISTRICT']
for i in list(district_Data['STATE/UT']):
    if i in UTs:
        district_Data.loc[district_Data['STATE/UT'] == i, 'STATE_DISTRICT'] = district_Data['STATE/UT']+'_'+district_Data['STATE/UT']
district_Data.head(15)
#district_Data = pd.DataFrame(district_Data.groupby(['STATE/UT','DISTRICT','Year']).agg({'Total_Crimes':"sum"}).reset_index())
district_Data = pd.DataFrame(district_Data.groupby(['STATE_DISTRICT','Year']).agg({'Murder':"sum", 'Rape':"sum", 'Kidnapping and Abduction':"sum", 'Foeticide':"sum", 'Abetment of suicide':"sum",'Exposure and abandonment':"sum", 'Procuration of minor girls':"sum",'Buying of girls for prostitution':"sum", 'Selling of girls for prostitution':"sum",'Prohibition of child marriage act':"sum", 'Other Crimes':"sum"}).reset_index())
district_Data['Total_Crimes'] = district_Data.iloc[:,2:].sum(axis=1)
children_Data = district_Data


# In[164]:


children_Data.to_csv(cwd+'/Preprocessing/clean_Children_Data.csv',index = 0)


# # District Data(Women)

# In[165]:


women_Data = women_Data[women_Data.Year<2011]
women_Data_col = list(women_Data.columns)
women_Data_col.remove('STATE/UT')
women_Data_col.remove('DISTRICT')
women_Data_col.remove('Year')
women_Data = women_Data[women_Data['DISTRICT'] != 'TOTAL']
#sum of all the crimes as Total Crimes
women_Data['Total_Crimes'] = women_Data.iloc[:,3:].sum(axis=1)
district_Data = women_Data

################  UP-->>CSM NAGAR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','CSM NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    #print(data_To_Add)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ARUNACHAL PRADESH-->>RURAL ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','RURAL'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TRIPURA-->>G.R.P. ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','TRIPURA'),('DISTRICT','G.R.P.'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  RAJASTHAN-->>G.R.P. AJMER ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','G.R.P. AJMER'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  JAMMU & KASHMIR-->>C.B.KASHMIR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','C.B.KASHMIR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  UTTAR PRADESH-->>RAMABAI NAGAR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','RAMABAI NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  RAJASTHAN-->>G.R.P. JODHPUR ##############################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','G.R.P. JODHPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ANDHRA PRADESH-->>WARANGAL URBAN ##############################'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','WARANGAL URBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  ANDHRA PRADESH-->>'RAJAHMUNDRY' ##############################'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','RAJAHMUNDRY'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  KARNATAKA-->>YADGIRI ##############################'KARNATAKA'.upper(),'DISTRICT':'YADGIRI'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','YADGIRI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  JAMMU & KASHMIR-->>SOPORE ##############################'.upper(),'DISTRICT':'SOPORE'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SOPORE'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  GUJARAT-->>CID CRIME ##############################'.upper(),'DISTRICT':'
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','GUJARAT'),('DISTRICT','CID CRIME'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HIMACHAL PRADESH-->>CID ##############################'HIMACHAL PRADESH'.upper(),'DISTRICT':'CID'
for year in range(2001,2009):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','HIMACHAL PRADESH'),('DISTRICT','CID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  TAMIL NADU-->>TIRUPPUR ##############################'.upper(),'DISTRICT':''
for year in range(2001,2009):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','TIRUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  ARUNACHAL PRADESH-->>ANJAW ##############################'.upper(),'DISTRICT':''
for year in range(2001,2009):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','ANJAW'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HIMACHAL PRADESH-->>CID ##############################
for year in range(2001,2009):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','TIRUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

 ################  HIMACHAL PRADESH-->>BADDIPOLICEDIST ############################## HIMACHAL PRADESH'.upper(),'DISTRICT':'
for year in range(2001,2009):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','HIMACHAL PRADESH'),('DISTRICT','BADDIPOLICEDIST'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
######################################################################################
for year in range(2001,2010):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','TIRUPATHI URBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  NAGALAND-->>LONGLENG ##############################'.upper(),'DISTRICT':''
for year in range(2001,2007):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','NAGALAND'),('DISTRICT','LONGLENG'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  JHARKHAND-->>RAMGARH ##############################''.upper(),'DISTRICT':''
for year in range(2001,2007):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','JHARKHAND'),('DISTRICT','RAMGARH'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
 ################  JHARKHAND-->>KHUNTI ##############################JHARKHAND'.upper(),'DISTRICT':'
for year in range(2001,2007):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','JHARKHAND'),('DISTRICT','KHUNTI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  PUNJAB-->>MAJITHA ##############################
for year in range(2006,2011):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','MAJITHA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>CHENGAI ##############################' '.upper(),'DISTRICT':'
for year in range(2005,2011):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','CHENGAI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  HARYANA-->>MEWAT ##############################'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','HARYANA'),('DISTRICT','MEWAT'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  CHHATTISGARH-->>SURAJPUR ##############################''.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','SURAJPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>UDALGURI ##############################'''.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','UDALGURI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>BASKA ##############################'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','BASKA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  ASSAM-->>CHIRANG ##############################'ASSAM'.upper(),'DISTRICT':''
for year in range(2001,2005):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ASSAM'),('DISTRICT','CHIRANG'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  PUNJAB-->>SAS NGR ##############################' '.upper(),'DISTRICT':''
for year in range(2001,2006):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','SAS NGR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
################  HARYANA-->>PALWAL ##############################'''.upper(),'DISTRICT':''
for year in range(2001,2006):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','HARYANA'),('DISTRICT','PALWAL'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>Ariyalur ##############################' Tamil Nadu'.upper(),'DISTRICT':''
for year in range(2001,2011):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','ARIYALUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

################  TAMIL NADU-->>KRISHNAGIRI ##############################' 
for year in range(2001,2004):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','KRISHNAGIRI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
##################################################################################
for year in range(2008,2011):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','BORDER'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ANDHRA PRADESH'),('DISTRICT','CYBERABAD'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ASHOK NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ANUPPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################','DISTRICT':''
for year in range(2001,2003):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','NARAYANPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#########################################################################################
for year in range(2001,2003):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','BURHANPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### PRADESH','DISTRICT':'
for year in range(2001,2003):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ARUNACHAL PRADESH'),('DISTRICT','K/KUMEY'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### ''.upper(),'DISTRICT':'
for year in range(2008,2011):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','JAGRAON'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

######################################################################################### 
for year in range(2008,2011):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','NAWAN SHAHR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
######################################################################################### '.upper(),'DISTRICT':'
for year in range(2008,2011):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','KERALA'),('DISTRICT','CBCID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
############### JAMMU & KASHMIR_SHOPIAN--> add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SHOPIAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_BANDIPORA- add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','BANDIPORA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_KISHTWAR--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','KISHTWAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  JAMMU & KASHMIR_SAMBA- add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','JAMMU & KASHMIR'),('DISTRICT','SAMBA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  ODISHA_DCP BBSR--> add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ODISHA'),('DISTRICT','DCP BBSR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  ODISHA_DCP CTC---> add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','ODISHA'),('DISTRICT','DCP CTC'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  KARNATAKA_CBPURA--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','CBPURA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  MADHYA PRADESH_SINGRAULI-->add zero rows 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','SINGRAULI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)
#  MADHYA PRADESH_ALIRAJPUR--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','MADHYA PRADESH'),('DISTRICT','ALIRAJPUR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  TAMIL NADU_CHENNAISUBURBAN---> add zero rows for 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','TAMIL NADU'),('DISTRICT','CHENNAISUBURBAN'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  UTTAR PRADESH_KANSHIRAM NAGAR-->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','UTTAR PRADESH'),('DISTRICT','KANSHIRAM NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  MANIPUR_CID--->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','MANIPUR'),('DISTRICT','CID'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  GUJARAT_TAPI-->add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','GUJARAT'),('DISTRICT','TAPI'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  PUNJAB_SBS NAGAR--->  add zero rows from 2001 to 2007

for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','PUNJAB'),('DISTRICT','SBS NAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  KARNATAKA_RAMANAGAR-->add zero rows from 2001 to 2007


for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','KARNATAKA'),('DISTRICT','RAMANAGAR'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

#  RAJASTHAN_PRATAPGARH--->add zero rows from 2001 to 2007
for year in range(2001,2008):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','RAJASTHAN'),('DISTRICT','PRATAPGARH'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

###########################################

data_To_Add = {'STATE/UT':'JAMMU & KASHMIR', 'DISTRICT': 'CRIME SRINAGAR', 'Year': 2010,'Rape': 0, 'Kidnapping and Abduction': 0, 'Dowry Deaths': 0, 'Assault on women with intent to outrage her modesty': 0, 'Insult to modesty of Women': 0, 'Cruelty by Husband or his Relatives': 0, 'Importation of Girls': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
data_To_Add = {'STATE/UT':'RAJASTHAN', 'DISTRICT': 'G.R.P.', 'Year': 2010,'Rape': 0, 'Kidnapping and Abduction': 0, 'Dowry Deaths': 0, 'Assault on women with intent to outrage her modesty': 0, 'Insult to modesty of Women': 0, 'Cruelty by Husband or his Relatives': 0, 'Importation of Girls': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
####################################################
############################################################################
data_To_Add = {'STATE/UT':'West Bengal'.upper(), 'DISTRICT': 'Kharagpur G.R.P.'.upper(), 'Year': 2001,'Rape': 0, 'Kidnapping and Abduction': 0, 'Dowry Deaths': 0, 'Assault on women with intent to outrage her modesty': 0, 'Insult to modesty of Women': 0, 'Cruelty by Husband or his Relatives': 0, 'Importation of Girls': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
#######################################################################
data_To_Add = {'STATE/UT':'Chhattisgarh'.upper(), 'DISTRICT': 'Kabirdham'.upper(), 'Year': 2001,'Rape': 0, 'Kidnapping and Abduction': 0, 'Dowry Deaths': 0, 'Assault on women with intent to outrage her modesty': 0, 'Insult to modesty of Women': 0, 'Cruelty by Husband or his Relatives': 0, 'Importation of Girls': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
#######################################################################
data_To_Add = {'STATE/UT':'JAMMU & KASHMIR'.upper(), 'DISTRICT': 'HANDWARA', 'Year': 2001,'Rape': 0, 'Kidnapping and Abduction': 0, 'Dowry Deaths': 0, 'Assault on women with intent to outrage her modesty': 0, 'Insult to modesty of Women': 0, 'Cruelty by Husband or his Relatives': 0, 'Importation of Girls': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
################################################################################################
data_To_Add = {'STATE/UT':'ASSAM', 'DISTRICT': 'N.C. HILLS', 'Year': 2001,'Rape': 0, 'Kidnapping and Abduction': 0, 'Dowry Deaths': 0, 'Assault on women with intent to outrage her modesty': 0, 'Insult to modesty of Women': 0, 'Cruelty by Husband or his Relatives': 0, 'Importation of Girls': 0}
district_Data = district_Data.append(data_To_Add, ignore_index=True)
################################################################################################
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'N.C. HILLS'.upper()), 'DISTRICT'] = 'N.C.HILLS'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'GUMALA'.upper()), 'DISTRICT'] = 'GUMLA'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'MAHENDERGARH'.upper()), 'DISTRICT'] = 'MAHENDRAGARH'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'HISAR'.upper()), 'DISTRICT'] = 'HISSAR'
district_Data.loc[(district_Data['Year'] == 2001) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2002) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2003) & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['Year'] == 2006) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2007) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2008) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2009) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2010) & (district_Data['DISTRICT'] == 'Kota city'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2006) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2007) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2008) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2009) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['Year'] == 2010) & (district_Data['DISTRICT'] == 'Kota rural'.upper()), 'DISTRICT'] = 'KOTA'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH CITY'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'HOWRAH G.R.P.'.upper()), 'DISTRICT'] = 'HOWRAH'
district_Data.loc[(district_Data['DISTRICT'] == 'MUMBAI COMMR.'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'MUMBAI RLY.'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'NAVI MUMBAI'.upper()), 'DISTRICT'] = 'MUMBAI'
district_Data.loc[(district_Data['DISTRICT'] == 'Vijayawada city'.upper()), 'DISTRICT'] = 'VIJAYAWADA'
district_Data.loc[(district_Data['DISTRICT'] == 'VIJAYAWADA RLY.'.upper()), 'DISTRICT'] = 'VIJAYAWADA'
district_Data.loc[(district_Data['DISTRICT'] == 'BORDER DISTRICT'.upper()), 'DISTRICT'] = 'Border'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'Imphal(West)'.upper()), 'DISTRICT'] = 'Imphal West'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'Imphal(East)'.upper()), 'DISTRICT'] = 'Imphal East'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR SOUTH'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR NORTH'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR RURAL'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JAIPUR EAST'.upper()), 'DISTRICT'] = 'Jaipur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JODHPUR CITY'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'JODHPUR RURAL'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'G.R.P. Jodhpur'.upper()), 'DISTRICT'] = 'Jodhpur'.upper()
district_Data.loc[(district_Data['DISTRICT'] == 'VILUPPURAM'.upper()), 'DISTRICT'] = 'VILLUPURAM'
district_Data.loc[(district_Data['DISTRICT'] == 'CP AMRITSAR'.upper()), 'DISTRICT'] = 'AMRITSAR'
district_Data.loc[(district_Data['DISTRICT'] == 'AMRITSAR RURAL'.upper()), 'DISTRICT'] = 'AMRITSAR'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYS KMR'.upper()), 'DISTRICT'] = 'RAILWAYS'
district_Data.loc[(district_Data['DISTRICT'] == 'CP LUDHIANA'.upper()), 'DISTRICT'] = 'LUDHIANA'
district_Data.loc[(district_Data['DISTRICT'] == 'LUDHIANA RURAL'.upper()), 'DISTRICT'] = 'LUDHIANA'
district_Data.loc[(district_Data['DISTRICT'] == 'JALANDHAR RURAL'.upper()), 'DISTRICT'] = 'JALANDHAR'
district_Data.loc[(district_Data['DISTRICT'] == 'CP JALANDHAR'.upper()), 'DISTRICT'] = 'JALANDHAR'
district_Data.loc[(district_Data['DISTRICT'] == 'KANPUR DEHAT'.upper()), 'DISTRICT'] = 'KANPUR'
district_Data.loc[(district_Data['DISTRICT'] == 'KANPUR NAGAR'.upper()), 'DISTRICT'] = 'KANPUR'
district_Data.loc[(district_Data['DISTRICT'] == 'GUNTUR URBAN'.upper()), 'DISTRICT'] = 'GUNTUR'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYS KMR'.upper()), 'DISTRICT'] = 'RAILWAYS'
district_Data.loc[(district_Data['DISTRICT'] == 'RAILWAYSKMR'.upper()), 'DISTRICT'] = 'RAILWAYS'
##########################Only for Women data ############################
district_Data.loc[(district_Data['STATE/UT'] == 'PUNJAB') & (district_Data['DISTRICT'] == 'FEROZEPUR'.upper()), 'DISTRICT'] = 'FEROZPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'CHHATTISGARH') & (district_Data['DISTRICT'] == 'DANTEWARA'.upper()), 'DISTRICT'] = 'DANTEWADA'
district_Data.loc[(district_Data['STATE/UT'] == 'JAMMU & KASHMIR') & (district_Data['DISTRICT'] == 'CRIME KASHMIR'.upper()), 'DISTRICT'] = 'C.B.KASHMIR'
############################Only for Women Data################################

#  CHHATTISGARH_KAWARDHA--->add zero rows from 2002 to 2010
for year in range(2002,2011):
    data_To_Add = {k:0 for k in women_Data_col}
    new_pairs = [('STATE/UT','CHHATTISGARH'),('DISTRICT','KAWARDHA'),('Total_Crimes', 0)]
    new_pairs.append(('Year', year))
    data_To_Add.update(new_pairs)
    district_Data= district_Data.append(data_To_Add, ignore_index= True)

###################  CHHATTISGARH_DANTEWARA---> DANTEWADA from 2001 to 2007
for i in range(2001,2008):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'DANTEWARA'.upper()), 'DISTRICT'] = 'DANTEWADA'


for i in range(2002,2011):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'Paschim Midnapur'.upper()), 'DISTRICT'] = 'MIDNAPUR'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'Purab Midnapur'.upper()), 'DISTRICT'] = 'MIDNAPUR'

for i in range(2003,2011):
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'TRIVANDRUM COMMR.'.upper()), 'DISTRICT'] = 'TRIVANDRUM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'TRIVANDRUM RURAL'.upper()), 'DISTRICT'] = 'TRIVANDRUM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'KOZHIKODE COMMR.'.upper()), 'DISTRICT'] = 'KOZHIKODE'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'KOZHIKODE RURAL'.upper()), 'DISTRICT'] = 'KOZHIKODE'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'ERNAKULAM COMMR.'.upper()), 'DISTRICT'] = 'ERNAKULAM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'ERNAKULAM RURAL'.upper()), 'DISTRICT'] = 'ERNAKULAM'
    district_Data.loc[(district_Data['Year'] == i) & (district_Data['DISTRICT'] == 'UPPER DIBANG VALLEY'.upper()), 'DISTRICT'] = 'DIBANG VALLEY'

district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AMRAVATI COMMR.'.upper()), 'DISTRICT'] = 'AMRAVATI'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AMRAVATI RURAL'.upper()), 'DISTRICT'] = 'AMRAVATI'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AURANGABAD COMMR.'.upper()), 'DISTRICT'] = 'AURANGABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'AURANGABAD RURAL'.upper()), 'DISTRICT'] = 'AURANGABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR COMMR.'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR RLY.'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NAGPUR RURAL'.upper()), 'DISTRICT'] = 'NAGPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NASIK COMMR.'.upper()), 'DISTRICT'] = 'NASHIK'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'NASIK RURAL'.upper()), 'DISTRICT'] = 'NASHIK'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE COMMR.'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE RLY.'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'PUNE RURAL'.upper()), 'DISTRICT'] = 'PUNE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'SOLAPUR COMMR.'.upper()), 'DISTRICT'] = 'SOLAPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'SOLAPUR RURAL'.upper()), 'DISTRICT'] = 'SOLAPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'THANE COMMR.'.upper()), 'DISTRICT'] = 'THANE'
district_Data.loc[(district_Data['STATE/UT'] == 'MAHARASHTRA') & (district_Data['DISTRICT'] == 'THANE RURAL'.upper()), 'DISTRICT'] = 'THANE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'COIMBATORE RURAL'.upper()), 'DISTRICT'] = 'COIMBATORE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'COIMBATORE URBAN'.upper()), 'DISTRICT'] = 'COIMBATORE'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'MADURAI URBAN'.upper()), 'DISTRICT'] = 'MADURAI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'MADURAI RURAL'.upper()), 'DISTRICT'] = 'MADURAI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'SALEM URBAN'.upper()), 'DISTRICT'] = 'SALEM'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY RLY.'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY RURAL'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'TRICHY URBAN'.upper()), 'DISTRICT'] = 'TIRUCHIRAPPALLI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'THIRUNELVELI URBAN'.upper()), 'DISTRICT'] = 'TIRUNELVELI'
district_Data.loc[(district_Data['STATE/UT'] == 'TAMIL NADU') & (district_Data['DISTRICT'] == 'THIRUNELVELI RURAL'.upper()), 'DISTRICT'] = 'TIRUNELVELI'
district_Data.loc[(district_Data['STATE/UT'] == 'JHARKHAND') & (district_Data['DISTRICT'] == 'JAMSHEDPUR RLY.'.upper()), 'DISTRICT'] = 'PURBI SINGHBHUM'
district_Data.loc[(district_Data['STATE/UT'] == 'JHARKHAND') & (district_Data['DISTRICT'] == 'JAMSHEDPUR'.upper()), 'DISTRICT'] = 'PURBI SINGHBHUM'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'BANGALORE COMMR.'.upper()), 'DISTRICT'] = 'BANGALORE'
#district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'BANGALORE RURAL'.upper()), 'DISTRICT'] = 'BANGALORE'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'DHARWAD COMMR.'.upper()), 'DISTRICT'] = 'DHARWAD'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'DHARWAD COMMR.'.upper()), 'DISTRICT'] = 'DHARWAD'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'MYSORE COMMR.'.upper()), 'DISTRICT'] = 'MYSORE'
district_Data.loc[(district_Data['STATE/UT'] == 'KARNATAKA') & (district_Data['DISTRICT'] == 'MYSORE RURAL'.upper()), 'DISTRICT'] = 'MYSORE'
district_Data.loc[(district_Data['STATE/UT'] == 'BIHAR') & (district_Data['DISTRICT'] == 'BAGAHA'.upper()), 'DISTRICT'] = 'PASHCHIM CHAMPARAN'
district_Data.loc[(district_Data['STATE/UT'] == 'BIHAR') & (district_Data['DISTRICT'] == 'BETTIAH'.upper()), 'DISTRICT'] = 'PASHCHIM CHAMPARAN'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'SURAT COMMR.'.upper()), 'DISTRICT'] = 'SURAT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'SURAT RURAL'.upper()), 'DISTRICT'] = 'SURAT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'RAJKOT COMMR.'.upper()), 'DISTRICT'] = 'RAJKOT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'RAJKOT RURAL'.upper()), 'DISTRICT'] = 'RAJKOT'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'AHMEDABAD COMMR.'.upper()), 'DISTRICT'] = 'AHMADABAD'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'AHMEDABAD RURAL'.upper()), 'DISTRICT'] = 'AHMADABAD'
#district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'BANAS KANTHA'.upper()), 'DISTRICT'] = 'PALANPUR'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'VADODARA COMMR.'.upper()), 'DISTRICT'] = 'VADODARA'
district_Data.loc[(district_Data['STATE/UT'] == 'GUJARAT') & (district_Data['DISTRICT'] == 'VADODARA RURAL'.upper()), 'DISTRICT'] = 'VADODARA'
district_Data.loc[(district_Data['STATE/UT'] == 'ANDHRA PRADESH') & (district_Data['DISTRICT'] == 'CYBERABAD'.upper()), 'DISTRICT'] = 'RANGAREDDY'
district_Data.loc[(district_Data['STATE/UT'] == 'ANDHRA PRADESH') & (district_Data['DISTRICT'] == 'RANGA REDDY'.upper()), 'DISTRICT'] = 'RANGAREDDY'


UTs = ['A & N ISLANDS','CHANDIGARH', 'D & N HAVELI', 'DAMAN & DIU', 'DELHI', 'LAKSHADWEEP', 'PUDUCHERRY']
district_Data['STATE_DISTRICT'] = district_Data['STATE/UT']+'_'+district_Data['DISTRICT']
for i in list(district_Data['STATE/UT']):
    if i in UTs:
        district_Data.loc[district_Data['STATE/UT'] == i, 'STATE_DISTRICT'] = district_Data['STATE/UT']+'_'+district_Data['STATE/UT']
#district_Data = pd.DataFrame(district_Data.groupby(['STATE/UT','DISTRICT','Year']).agg({'Total_Crimes':"sum"}).reset_index())
district_Data = pd.DataFrame(district_Data.groupby(['STATE_DISTRICT','Year']).agg({'Total_Crimes':"sum",'Rape':"sum",'Kidnapping and Abduction':"sum",'Dowry Deaths':"sum",'Assault on women with intent to outrage her modesty':"sum",'Insult to modesty of Women':"sum",'Cruelty by Husband or his Relatives':"sum",'Importation of Girls':"sum"}).reset_index())
women_Data = district_Data


# In[166]:


women_Data.to_csv(cwd+'/Preprocessing/clean_Women_Data.csv',index = 0)


# # Census Data

# In[103]:


#census_Data.head()
##Census - SC :
# {'PONDICHERRY', change to PUDUCHERRY
#  'ANDAMAN AND NICOBAR ISLANDS', change to A & N ISLANDS 
#  'DADRA AND NAGAR HAVELI', change t0 D & N HAVELI
#  'JAMMU AND KASHMIR', change to JAMMU & KASHMIR
#  'NCT OF DELHI', change to DELHI combine groupby DELHI 
#  'ORISSA', change to Odisha
#  'DAMAN AND DIU'} change to DAMAN & DIU

# {'JAMMU & KASHMIR_BADGAM', change to BUDGAM
#  'JAMMU & KASHMIR_BANDIPORE', change to BANDIPORA
#  'JAMMU & KASHMIR_BARAMULA', change to BARAMULLA
#  'JAMMU & KASHMIR_LEH(LADAKH)', change to LEH
#  'JAMMU & KASHMIR_PUNCH', change to POONCH
#  'JAMMU & KASHMIR_SHUPIYAN', change to SHOPIAN
#  'ODISHA_ANUGUL', change to ANGUL
#  'ODISHA_BALANGIR', change to BOLANGIR
#  'ODISHA_BALESHWAR', change to BALASORE
#  'ODISHA_BARGARH', change to BARAGARH
#  'ODISHA_BAUDH', change to BOUDH
#  'ODISHA_DEBAGARH', change to DEOGARH
#  'ODISHA_JAGATSINGHAPUR', change to JAGATSINGHPUR
#  'ODISHA_JAJAPUR', change to JAJPUR
#  'ODISHA_KENDUJHAR', change to KEONJHAR
#  'ODISHA_KHORDHA', change to KHURDA
#  'ODISHA_MALKANGIRI', change to MALKANGIR
#  'ODISHA_NABARANGAPUR', change to NOWRANGPUR
#  'ODISHA_SUBARNAPUR'} change to SONEPUR

#dict_oStatename_nStatename = {'PONDICHERRY':'PUDUCHERRY', 'ANDAMAN AND NICOBAR ISLANDS':'A & N ISLANDS', 
#'DADRA AND NAGAR HAVELI':'D & N HAVELI', 'JAMMU AND KASHMIR':'JAMMU & KASHMIR','NCT OF DELHI':'DELHI',
#'ORISSA':'Odisha'.upper(), 'DAMAN AND DIU':'DAMAN & DIU'}
#census_Filtered_Data['State name']=census_Filtered_Data['State name'].map(dict_oStatename_nStatename)


# In[167]:


#census_Filtered_Data['STATE_DISTRICT'] = census_Filtered_Data['State name'] +'_'+census_Filtered_Data['District name']
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'PONDICHERRY'.upper()), 'State name'] = 'PUDUCHERRY'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ANDAMAN AND NICOBAR ISLANDS'.upper()), 'State name'] = 'A & N ISLANDS'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'DADRA AND NAGAR HAVELI'.upper()), 'State name'] = 'D & N HAVELI'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JAMMU AND KASHMIR'.upper()), 'State name'] = 'JAMMU & KASHMIR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'NCT OF DELHI'.upper()), 'State name'] = 'DELHI'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'DAMAN AND DIU'.upper()), 'State name'] = 'DAMAN & DIU'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ORISSA'.upper()), 'State name'] = 'Odisha'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JAMMU & KASHMIR'.upper())&(census_Filtered_Data['District name'] == 'BADGAM'.upper()), 'District name'] = 'BUDGAM'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JAMMU & KASHMIR'.upper())&(census_Filtered_Data['District name'] == 'BANDIPORE'.upper()), 'District name'] = 'BANDIPORA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JAMMU & KASHMIR'.upper())&(census_Filtered_Data['District name'] == 'BARAMULA'.upper()), 'District name'] = 'BARAMULLA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JAMMU & KASHMIR'.upper())&(census_Filtered_Data['District name'] == 'LEH(LADAKH)'.upper()), 'District name'] = 'LEH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JAMMU & KASHMIR'.upper())&(census_Filtered_Data['District name'] == 'PUNCH'.upper()), 'District name'] = 'POONCH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JAMMU & KASHMIR'.upper())&(census_Filtered_Data['District name'] == 'SHUPIYAN'.upper()), 'District name'] = 'SHOPIAN'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'ANUGUL'.upper()), 'District name'] = 'ANGUL'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'BALANGIR'.upper()), 'District name'] = 'BOLANGIR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'BALESHWAR'.upper()), 'District name'] = 'BALASORE'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'BARGARH'.upper()), 'District name'] = 'BARAGARH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'BAUDH'.upper()), 'District name'] = 'BOUDH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'DEBAGARH'.upper()), 'District name'] = 'DEOGARH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'JAGATSINGHAPUR'.upper()), 'District name'] = 'JAGATSINGHPUR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'JAJAPUR'.upper()), 'District name'] = 'JAJPUR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'KENDUJHAR'.upper()), 'District name'] = 'KEONJHAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'KHORDHA'.upper()), 'District name'] = 'KHURDA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'MALKANGIRI'.upper()), 'District name'] = 'MALKANGIR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'NABARANGAPUR'.upper()), 'District name'] = 'NOWRANGPUR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ODISHA'.upper())&(census_Filtered_Data['District name'] == 'SUBARNAPUR'.upper()), 'District name'] = 'SONEPUR'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ANDHRA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'HYDERABAD'.upper()), 'District name'] = 'HYDERABAD CITY'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ANDHRA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'MAHBUBNAGAR'.upper()), 'District name'] = 'MAHABOOBNAGAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ANDHRA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'PRAKASAM'.upper()), 'District name'] = 'PRAKASHAM'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ANDHRA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'SRI POTTI SRIRAMULU NELLORE'.upper()), 'District name'] = 'NELLORE'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ANDHRA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'Y.S.R.'.upper()), 'District name'] = 'CUDDAPAH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ARUNACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'EAST KAMENG'.upper()), 'District name'] = 'KAMENG EAST'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ARUNACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'EAST SIANG'.upper()), 'District name'] = 'SIANG EAST'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ARUNACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'KURUNG KUMEY'.upper()), 'District name'] = 'K/KUMEY'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ARUNACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'LOWER DIBANG VALLEY'.upper()), 'District name'] = 'DIBANG VALLEY'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ARUNACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'LOWER SUBANSIRI'.upper()), 'District name'] = 'SUBANSIRI LOWER'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ARUNACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'UPPER SIANG'.upper()), 'District name'] = 'SIANG UPPER'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ARUNACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'UPPER SUBANSIRI'.upper()), 'District name'] = 'SUBANSIRI UPPER'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ARUNACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'WEST KAMENG'.upper()), 'District name'] = 'KAMENG WEST'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ARUNACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'WEST SIANG'.upper()), 'District name'] = 'SIANG WEST'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ASSAM'.upper())&(census_Filtered_Data['District name'] == 'BAKSA'.upper()), 'District name'] = 'BASKA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ASSAM'.upper())&(census_Filtered_Data['District name'] == 'KAMRUP METROPOLITAN'.upper()), 'District name'] = 'KAMRUP'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'ASSAM'.upper())&(census_Filtered_Data['District name'] == 'SIVASAGAR'.upper()), 'District name'] = 'SIBSAGAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'BIHAR'.upper())&(census_Filtered_Data['District name'] == 'KAIMUR (BHABUA)'.upper()), 'District name'] = 'BHABHUA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'BIHAR'.upper())&(census_Filtered_Data['District name'] == 'NAWADA'.upper()), 'District name'] = 'NAWADAH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'BIHAR'.upper())&(census_Filtered_Data['District name'] == 'PURBA CHAMPARAN'.upper()), 'District name'] = 'MOTIHARI'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'BIHAR'.upper())&(census_Filtered_Data['District name'] == 'PURNIA'.upper()), 'District name'] = 'PURNEA'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'CHHATTISGARH'.upper())&(census_Filtered_Data['District name'] == 'BASTAR'.upper()), 'District name'] = 'JAGDALPUR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'CHHATTISGARH'.upper())&(census_Filtered_Data['District name'] == 'BIJAPUR'.upper()), 'District name'] = 'BIZAPUR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'CHHATTISGARH'.upper())&(census_Filtered_Data['District name'] == 'DAKSHIN BASTAR DANTEWADA'.upper()), 'District name'] = 'DANTEWADA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'CHHATTISGARH'.upper())&(census_Filtered_Data['District name'] == 'JANJGIR - CHAMPA'.upper()), 'District name'] = 'JANJGIR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'CHHATTISGARH'.upper())&(census_Filtered_Data['District name'] == 'KABEERDHAM'.upper()), 'District name'] = 'KABIRDHAM'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'CHHATTISGARH'.upper())&(census_Filtered_Data['District name'] == 'SURGUJA'.upper()), 'District name'] = 'SARGUJA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'CHHATTISGARH'.upper())&(census_Filtered_Data['District name'] == 'UTTAR BASTAR KANKER'.upper()), 'District name'] = 'KANKER'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'GUJARAT'.upper())&(census_Filtered_Data['District name'] == 'DOHAD'.upper()), 'District name'] = 'DAHOD'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'GUJARAT'.upper())&(census_Filtered_Data['District name'] == 'KACHCHH'.upper()), 'District name'] = 'KUTCH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'GUJARAT'.upper())&(census_Filtered_Data['District name'] == 'KHEDA'.upper()), 'District name'] = 'KHEDA NORTH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'GUJARAT'.upper())&(census_Filtered_Data['District name'] == 'MAHESANA'.upper()), 'District name'] = 'MEHSANA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'GUJARAT'.upper())&(census_Filtered_Data['District name'] == 'PANCH MAHALS'.upper()), 'District name'] = 'PANCHMAHAL'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'GUJARAT'.upper())&(census_Filtered_Data['District name'] == 'SABAR KANTHA'.upper()), 'District name'] = 'HIMATNAGAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'GUJARAT'.upper())&(census_Filtered_Data['District name'] == 'THE DANGS'.upper()), 'District name'] = 'AHWA-DANG'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'GUJARAT'.upper())&(census_Filtered_Data['District name'] == 'BANAS KANTHA'.upper()), 'District name'] = 'Palanpur'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'HARYANA'.upper())&(census_Filtered_Data['District name'] == 'HISAR'.upper()), 'District name'] = 'HISSAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'HIMACHAL PRADESH'.upper())&(census_Filtered_Data['District name'] == 'LAHUL AND SPITI'.upper()), 'District name'] = 'LAHAUL-SPITI'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JHARKHAND'.upper())&(census_Filtered_Data['District name'] == 'KODARMA'.upper()), 'District name'] = 'KODERMA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JHARKHAND'.upper())&(census_Filtered_Data['District name'] == 'LOHARDAGA'.upper()), 'District name'] = 'LOHARDAGGA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JHARKHAND'.upper())&(census_Filtered_Data['District name'] == 'PASHCHIMI SINGHBHUM'.upper()), 'District name'] = 'CHAIBASA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JHARKHAND'.upper())&(census_Filtered_Data['District name'] == 'SAHIBGANJ'.upper()), 'District name'] = 'SAHEBGANJ'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'JHARKHAND'.upper())&(census_Filtered_Data['District name'] == 'SARAIKELA-KHARSAWAN'.upper()), 'District name'] = 'SARAIKELA'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KARNATAKA'.upper())&(census_Filtered_Data['District name'] == 'CHAMARAJANAGAR'.upper()), 'District name'] = 'CHAMARAJNAGAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KARNATAKA'.upper())&(census_Filtered_Data['District name'] == 'CHIKKABALLAPURA'.upper()), 'District name'] = 'KOLAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KARNATAKA'.upper())&(census_Filtered_Data['District name'] == 'CHIKMAGALUR'.upper()), 'District name'] = 'CHICKMAGALUR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KARNATAKA'.upper())&(census_Filtered_Data['District name'] == 'DAKSHINA KANNADA'.upper()), 'District name'] = 'DAKSHIN KANNADA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KARNATAKA'.upper())&(census_Filtered_Data['District name'] == 'RAMANAGARA'.upper()), 'District name'] = 'RAMANAGAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KARNATAKA'.upper())&(census_Filtered_Data['District name'] == 'UTTARA KANNADA'.upper()), 'District name'] = 'UTTAR KANNADA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KARNATAKA'.upper())&(census_Filtered_Data['District name'] == 'YADGIR'.upper()), 'District name'] = 'YADGIRI'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KERALA'.upper())&(census_Filtered_Data['District name'] == 'ALAPPUZHA'.upper()), 'District name'] = 'ALAPUZHA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KERALA'.upper())&(census_Filtered_Data['District name'] == 'KASARAGOD'.upper()), 'District name'] = 'KASARGOD'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KERALA'.upper())&(census_Filtered_Data['District name'] == 'THIRUVANANTHAPURAM'.upper()), 'District name'] = 'TRIVANDRUM'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'KERALA'.upper())&(census_Filtered_Data['District name'] == 'WAYANAD'.upper()), 'District name'] = 'WAYANADU'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MADHYA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'ASHOKNAGAR'.upper()), 'District name'] = 'ASHOK NAGAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MADHYA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'DATIA'.upper()), 'District name'] = 'DATIYA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MADHYA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'KHANDWA (EAST NIMAR)'.upper()), 'District name'] = 'KHANDWA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MADHYA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'KHARGONE (WEST NIMAR)'.upper()), 'District name'] = 'KHARGON'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MADHYA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'NARSIMHAPUR'.upper()), 'District name'] = 'NARSINGHPUR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MADHYA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'SEHORE'.upper()), 'District name'] = 'SIHORE'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MADHYA PRADESH'.upper())&(census_Filtered_Data['District name'] == 'UMARIA'.upper()), 'District name'] = 'UMARIYA'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MAHARASHTRA'.upper())&(census_Filtered_Data['District name'] == 'AHMADNAGAR'.upper()), 'District name'] = 'AHMEDNAGAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MAHARASHTRA'.upper())&(census_Filtered_Data['District name'] == 'BID'.upper()), 'District name'] = 'BEED'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MAHARASHTRA'.upper())&(census_Filtered_Data['District name'] == 'BULDANA'.upper()), 'District name'] = 'BULDHANA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MAHARASHTRA'.upper())&(census_Filtered_Data['District name'] == 'GONDIYA'.upper()), 'District name'] = 'GONDIA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MAHARASHTRA'.upper())&(census_Filtered_Data['District name'] == 'MUMBAI SUBURBAN'.upper()), 'District name'] = 'MUMBAI'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MAHARASHTRA'.upper())&(census_Filtered_Data['District name'] == 'RAIGARH'.upper()), 'District name'] = 'RAIGAD'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MEGHALAYA'.upper())&(census_Filtered_Data['District name'] == 'EAST GARO HILLS'.upper()), 'District name'] = 'GARO HILLS EAST'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MEGHALAYA'.upper())&(census_Filtered_Data['District name'] == 'EAST KHASI HILLS'.upper()), 'District name'] = 'KHASI HILLS EAST'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MEGHALAYA'.upper())&(census_Filtered_Data['District name'] == 'RIBHOI'.upper()), 'District name'] = 'RI-BHOI'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MEGHALAYA'.upper())&(census_Filtered_Data['District name'] == 'SOUTH GARO HILLS'.upper()), 'District name'] = 'GARO HILLS SOUTH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MEGHALAYA'.upper())&(census_Filtered_Data['District name'] == 'WEST GARO HILLS'.upper()), 'District name'] = 'GARO HILLS WEST'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'MEGHALAYA'.upper())&(census_Filtered_Data['District name'] == 'WEST KHASI HILLS'.upper()), 'District name'] = 'KHASI HILLS WEST'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'PUNJAB'.upper())&(census_Filtered_Data['District name'] == 'BATHINDA'.upper()), 'District name'] = 'BHATINDA'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'PUNJAB'.upper())&(census_Filtered_Data['District name'] == 'FIROZPUR'.upper()), 'District name'] = 'FEROZPUR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'PUNJAB'.upper())&(census_Filtered_Data['District name'] == 'RUPNAGAR'.upper()), 'District name'] = 'ROPAR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'PUNJAB'.upper())&(census_Filtered_Data['District name'] == 'SAHIBZADA AJIT SINGH NAGAR'.upper()), 'District name'] = 'SAS NGR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'PUNJAB'.upper())&(census_Filtered_Data['District name'] == 'SHAHID BHAGAT SINGH NAGAR'.upper()), 'District name'] = 'SBS NAGAR'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'RAJASTHAN'.upper())&(census_Filtered_Data['District name'] == 'CHITTAURGARH'.upper()), 'District name'] = 'CHITTORGARH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'RAJASTHAN'.upper())&(census_Filtered_Data['District name'] == 'DHAULPUR'.upper()), 'District name'] = 'DHOLPUR'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'RAJASTHAN'.upper())&(census_Filtered_Data['District name'] == 'JALOR'.upper()), 'District name'] = 'JALORE'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'RAJASTHAN'.upper())&(census_Filtered_Data['District name'] == 'JHUNJHUNUN'.upper()), 'District name'] = 'JHUNJHUNU'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'SIKKIM'.upper())&(census_Filtered_Data['District name'] == 'EAST DISTRICT'.upper()), 'District name'] = 'EAST'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'SIKKIM'.upper())&(census_Filtered_Data['District name'] == 'NORTH  DISTRICT'.upper()), 'District name'] = 'NORTH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'SIKKIM'.upper())&(census_Filtered_Data['District name'] == 'SOUTH DISTRICT'.upper()), 'District name'] = 'SOUTH'.upper()
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'SIKKIM'.upper())&(census_Filtered_Data['District name'] == 'WEST DISTRICT'.upper()), 'District name'] = 'WEST'.upper()

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TAMIL NADU')&(census_Filtered_Data['District name'] == 'KANCHEEPURAM'), 'District name'] = 'KANCHIPURAM'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TAMIL NADU')&(census_Filtered_Data['District name'] == 'KANNIYAKUMARI'), 'District name'] = 'KANYAKUMARI'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TAMIL NADU')&(census_Filtered_Data['District name'] == 'PUDUKKOTTAI'), 'District name'] = 'PUDUKOTTAI'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TAMIL NADU')&(census_Filtered_Data['District name'] == 'RAMANATHAPURAM'), 'District name'] = 'RAMNATHAPURAM'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TAMIL NADU')&(census_Filtered_Data['District name'] == 'SIVAGANGA'), 'District name'] = 'SIVAGANGAI'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TAMIL NADU')&(census_Filtered_Data['District name'] == 'THE NILGIRIS'), 'District name'] = 'NILGIRIS'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TAMIL NADU')&(census_Filtered_Data['District name'] == 'THOOTHUKKUDI'), 'District name'] = 'THOOTHUGUDI'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TAMIL NADU')&(census_Filtered_Data['District name'] == 'TIRUVANNAMALAI'), 'District name'] = 'THIRUVANNAMALAI'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TAMIL NADU')&(census_Filtered_Data['District name'] == 'VILUPPURAM'), 'District name'] = 'VILLUPURAM'

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TRIPURA')&(census_Filtered_Data['District name'] == 'NORTH TRIPURA'), 'District name'] = 'NORTH'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TRIPURA')&(census_Filtered_Data['District name'] == 'SOUTH TRIPURA'), 'District name'] = 'SOUTH'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'TRIPURA')&(census_Filtered_Data['District name'] == 'WEST TRIPURA'), 'District name'] = 'WEST'

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'BARA BANKI'), 'District name'] = 'BARABANKI'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'BUDAUN'), 'District name'] = 'BADAUN'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'BULANDSHAHR'), 'District name'] = 'BULANDSHAHAR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'CHANDAULI'), 'District name'] = 'CHANDOLI'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'CHITRAKOOT'), 'District name'] = 'CHITRAKOOT DHAM'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'FARRUKHABAD'), 'District name'] = 'FATEHGARH'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'GAUTAM BUDDHA NAGAR'), 'District name'] = 'GAUTAMBUDH NAGAR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'JYOTIBA PHULE NAGAR'), 'District name'] = 'J.P.NAGAR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'KANPUR DEHAT'), 'District name'] = 'KANPUR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'KANPUR NAGAR'), 'District name'] = 'KANPUR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'KHERI'), 'District name'] = 'KHIRI'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'KUSHINAGAR'), 'District name'] = 'KUSHI NAGAR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'MAHAMAYA NAGAR'), 'District name'] = 'HATHRAS'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'MAHRAJGANJ'), 'District name'] = 'MAHARAJGANJ'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'RAE BARELI'), 'District name'] = 'RAIBAREILLY'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'SANT KABIR NAGAR'), 'District name'] = 'SANT KABIRNAGAR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'SANT RAVIDAS NAGAR (BHADOHI)'), 'District name'] = 'ST.RAVIDASNAGAR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTAR PRADESH')&(census_Filtered_Data['District name'] == 'SIDDHARTHNAGAR'), 'District name'] = 'SIDHARTHNAGAR'

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTARAKHAND')&(census_Filtered_Data['District name'] == 'GARHWAL'), 'District name'] = 'PAURI GARHWAL'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTARAKHAND')&(census_Filtered_Data['District name'] == 'HARDWAR'), 'District name'] = 'HARIDWAR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTARAKHAND')&(census_Filtered_Data['District name'] == 'RUDRAPRAYAG'), 'District name'] = 'RUDRA PRAYAG'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'UTTARAKHAND')&(census_Filtered_Data['District name'] == 'UDHAM SINGH NAGAR'), 'District name'] = 'UDHAMSINGH NAGAR'

census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'BARDDHAMAN'), 'District name'] = 'BURDWAN'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'DARJILING'), 'District name'] = 'DARJEELING'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'HAORA'), 'District name'] = 'HOWRAH'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'HUGLI'), 'District name'] = 'HOOGHLY'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'KOCH BIHAR'), 'District name'] = 'COOCHBEHAR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'MALDAH'), 'District name'] = 'MALDA'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'NORTH TWENTY FOUR PARGANAS'), 'District name'] = '24 PARGANAS NORTH'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'PASCHIM MEDINIPUR'), 'District name'] = 'MIDNAPUR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'PURBA MEDINIPUR'), 'District name'] = 'MIDNAPUR'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'PURULIYA'), 'District name'] = 'PURULIA'
census_Filtered_Data.loc[(census_Filtered_Data['State name'] == 'WEST BENGAL')&(census_Filtered_Data['District name'] == 'SOUTH TWENTY FOUR PARGANAS'), 'District name'] = '24 PARGANAS SOUTH'

#census_Filtered_Data = census_Filtered_Data[(census_Filtered_Data['State name'] != 'ASSAM') & (census_Filtered_Data['District name'] != 'DIMA HASAO')]
census_Filtered_Data.drop(index=314, inplace=True)
census_Filtered_Data.reset_index()
census_Filtered_Data['STATE_DISTRICT'] = census_Filtered_Data['State name']+'_'+census_Filtered_Data['District name']
UTs = ['A & N ISLANDS','CHANDIGARH', 'D & N HAVELI', 'DAMAN & DIU', 'DELHI', 'LAKSHADWEEP', 'PUDUCHERRY']
for i in list(census_Filtered_Data['State name']):
    if i in UTs:
        census_Filtered_Data.loc[census_Filtered_Data['State name'] == i, 'STATE_DISTRICT'] = census_Filtered_Data['State name']+'_'+census_Filtered_Data['State name']
ls_dict = {}
ls = list(census_Filtered_Data.columns)
ls.remove('District code')
ls.remove('State name')
ls.remove('District name') 
ls.remove('STATE_DISTRICT')
for ele in ls:
    ls_dict[ele] = "sum"
census_Filtered_Data = pd.DataFrame(census_Filtered_Data.groupby(['STATE_DISTRICT']).agg(ls_dict).reset_index())


# In[168]:


census_Filtered_Data.to_csv(cwd+'/Preprocessing/clean_Census_Data.csv', index=0)


# In[48]:


#  'SIKKIM_EAST DISTRICT',--->> EAST
#  'SIKKIM_NORTH  DISTRICT',-->> NORTH
#  'SIKKIM_SOUTH DISTRICT',--->> SOUTH
#  'SIKKIM_WEST DISTRICT',---->> WEST 
#  'RAJASTHAN_CHITTAURGARH',---> CHITTORGARH
#  'RAJASTHAN_DHAULPUR',----> DHOLPUR
#  'RAJASTHAN_JALOR',----> JALORE
#  'RAJASTHAN_JHUNJHUNUN',--->> JHUNJHUNU
#  'PUNJAB_BATHINDA',--->> BHATINDA in census
#  'PUNJAB_FIROZPUR',---->> FEROZPUR in census
#  'PUNJAB_RUPNAGAR',-----> ROPAR in census
#  'PUNJAB_SAHIBZADA AJIT SINGH NAGAR',---> SAS NGR in census
#  'PUNJAB_SHAHID BHAGAT SINGH NAGAR', SBS NAGAR in census
#  'MAHARASHTRA_AHMADNAGAR',----->> AHMEDNAGAR
#  'MAHARASHTRA_BID',--->> BEED
#  'MAHARASHTRA_BULDANA',--->> BULDHANA
#  'MAHARASHTRA_GONDIYA', --->> GONDIA
#  'MAHARASHTRA_MUMBAI SUBURBAN', ---->> MUMBAI --67
#  'MAHARASHTRA_RAIGARH',--->> RAIGAD
#  'MEGHALAYA_EAST GARO HILLS',---->> GARO HILLS EAST
#  'MEGHALAYA_EAST KHASI HILLS',------>>> KHASI HILLS EAST
#  'MEGHALAYA_RIBHOI',----->> RI-BHOI
#  'MEGHALAYA_SOUTH GARO HILLS', --->> GARO HILLS SOUTH
#  'MEGHALAYA_WEST GARO HILLS', -->> GARO HILLS WEST
#  'MEGHALAYA_WEST KHASI HILLS', --->> KHASI HILLS WEST
#  'MADHYA PRADESH_ASHOKNAGAR'--->> ASHOK NAGAR
#  'MADHYA PRADESH_DATIA', ---> DATIYA
#  'MADHYA PRADESH_KHANDWA (EAST NIMAR)', --->>> KHANDWA
#  'MADHYA PRADESH_KHARGONE (WEST NIMAR)', --->> KHARGON
#  'MADHYA PRADESH_NARSIMHAPUR',--->> NARSINGHPUR
#  'MADHYA PRADESH_SEHORE',---->> SIHORE
#  'MADHYA PRADESH_UMARIA',---->> UMARIYA
#  'KERALA_ALAPPUZHA', change in census ALAPPUZHA to ALAPUZHA
#  'KERALA_KASARAGOD', change in census KASARAGOD to KASARGOD
#  'KERALA_THIRUVANANTHAPURAM', change in census THIRUVANANTHAPURAM to TRIVANDRUM
#  'KERALA_WAYANAD', change in census WAYANAD to WAYANADU
#  'KARNATAKA_CHAMARAJANAGAR', change in census CHAMARAJANAGAR to CHAMARAJNAGAR
#  'KARNATAKA_CHIKKABALLAPURA', change in census CHIKKABALLAPURA to KOLAR
#  'KARNATAKA_CHIKMAGALUR', change in census CHIKMAGALUR to CHICKMAGALUR
#  'KARNATAKA_DAKSHINA KANNADA', change in census DAKSHINA KANNADA to DAKSHIN KANNADA
#  'KARNATAKA_RAMANAGARA', change in census RAMANAGARA to RAMANAGAR
#  'KARNATAKA_UTTARA KANNADA', change in census UTTARA KANNADA to UTTAR KANNADA
#  'KARNATAKA_YADGIR', change in  census YADGIR to YADGIRI
#  'HARYANA_HISAR', change in census HISAR to HISSAR
#  'HIMACHAL PRADESH_LAHUL AND SPITI', change in census LAHUL AND SPITI to LAHAUL-SPITI
#  'JHARKHAND_KODARMA', change in census KODARMA to KODERMA
#  'JHARKHAND_LOHARDAGA', change in census LOHARDAGA to LOHARDAGGA
#  'JHARKHAND_PASHCHIMI SINGHBHUM', change in census PASHCHIMI SINGHBHUM to CHAIBASA
#  'JHARKHAND_SAHIBGANJ', change in census SAHIBGANJ to SAHEBGANJ
#  'JHARKHAND_SARAIKELA-KHARSAWAN', change in census SARAIKELA-KHARSAWAN to SARAIKELA
#  'GUJARAT_DOHAD', change in census DOHAD to DAHOD
#  'GUJARAT_KACHCHH', change in census KACHCHH to KUTCH
#  'GUJARAT_KHEDA', change in census KHEDA to KHEDA NORTH
#  'GUJARAT_MAHESANA', change in census MAHESANA to MEHSANA
#  'GUJARAT_PANCH MAHALS', change in census PANCH MAHALS to PANCHMAHAL
#  'GUJARAT_SABAR KANTHA', change in census SABAR KANTHA to HIMATNAGAR
#  'GUJARAT_THE DANGS', change in census THE DANGS to AHWA-DANG
#  'CHHATTISGARH_BASTAR', change in census BASTAR to JAGDALPUR
#  'CHHATTISGARH_BIJAPUR', change in census BIJAPUR to BIZAPUR
#  'CHHATTISGARH_DAKSHIN BASTAR DANTEWADA', change in census DAKSHIN BASTAR DANTEWADA to DANTEWADA
#  'CHHATTISGARH_JANJGIR - CHAMPA', change in census JANJGIR - CHAMPA to JANJGIR
#  'CHHATTISGARH_KABEERDHAM', change in census KABEERDHAM to KABIRDHAM
#  'CHHATTISGARH_SURGUJA', change in census SURGUJA to SARGUJA
#  'CHHATTISGARH_UTTAR BASTAR KANKER', change in census UTTAR BASTAR KANKER to KANKER
#  'ASSAM_BAKSA', change in census to BAKSA to BASKA
#  'ASSAM_KAMRUP METROPOLITAN', change in census KAMRUP METROPOLITAN to KAMRUP
#  'ASSAM_SIVASAGAR', change in census SIVASAGAR to SIBSAGAR
#  'BIHAR_KAIMUR (BHABUA)', change in census KAIMUR (BHABUA) to BHABHUA
#  'BIHAR_NAWADA', change in census NAWADA to NAWADAH
#  'BIHAR_PURBA CHAMPARAN', change in census PURBA CHAMPARAN to MOTIHARI
#  'BIHAR_PURNIA', change census PURNIA to PURNEA
#  'ARUNACHAL PRADESH_EAST KAMENG', change in census EAST KAMENG to KAMENG EAST
#  'ARUNACHAL PRADESH_EAST SIANG', change in census EAST SIANG to SIANG EAST
#  'ARUNACHAL PRADESH_KURUNG KUMEY', change in census KURUNG KUMEY to K/KUMEY
#  'ARUNACHAL PRADESH_LOWER DIBANG VALLEY', change in census LOWER DIBANG VALLEY to DIBANG VALLEY
#  'ARUNACHAL PRADESH_LOWER SUBANSIRI', change in census LOWER SUBANSIRI to SUBANSIRI LOWER
#  'ARUNACHAL PRADESH_UPPER SIANG', change in census UPPER SIANG to SIANG UPPER
#  'ARUNACHAL PRADESH_UPPER SUBANSIRI', change in census UPPER SUBANSIRI to SUBANSIRI UPPER
#  'ARUNACHAL PRADESH_WEST KAMENG', change in census WEST KAMENG to KAMENG WEST
#  'ARUNACHAL PRADESH_WEST SIANG', change in census to WEST SIANG to SIANG WEST
#  'ANDHRA PRADESH_HYDERABAD', change in Census HYDERABAD to HYDERABAD CITY
#  'ANDHRA PRADESH_MAHBUBNAGAR', change in Census MAHBUBNAGAR to MAHABOOBNAGAR
#  'ANDHRA PRADESH_PRAKASAM', change in Census PRAKASAM to PRAKASHAM
#  'ANDHRA PRADESH_SRI POTTI SRIRAMULU NELLORE', change in census SRI POTTI SRIRAMULU NELLORE to NELLORE
#  'ANDHRA PRADESH_Y.S.R.', change in census Y.S.R. to CUDDAPAH



#####################Do Till Here!########################################
#  'TAMIL NADU_KANCHEEPURAM',--> KANCHIPURAM
#  'TAMIL NADU_KANNIYAKUMARI',---> KANYAKUMARI
#  'TAMIL NADU_PUDUKKOTTAI',--->> PUDUKOTTAI
#  'TAMIL NADU_RAMANATHAPURAM',----> RAMNATHAPURAM
#  'TAMIL NADU_SIVAGANGA', ---->> SIVAGANGAI
#  'TAMIL NADU_THE NILGIRIS',--->> NILGIRIS
#  'TAMIL NADU_THOOTHUKKUDI',---> THOOTHUGUDI
#  'TAMIL NADU_TIRUVANNAMALAI',-->> THIRUVANNAMALAI
#  'TAMIL NADU_VILUPPURAM',-->> VILLUPURAM
#  'TRIPURA_NORTH TRIPURA',-->> NORTH
#  'TRIPURA_SOUTH TRIPURA',--->> SOUTH
#  'TRIPURA_WEST TRIPURA',---> WEST
#  'UTTAR PRADESH_BARA BANKI',-->> BARABANKI
#  'UTTAR PRADESH_BUDAUN',--->> BADAUN
#  'UTTAR PRADESH_BULANDSHAHR',----> BULANDSHAHAR
#  'UTTAR PRADESH_CHANDAULI',-----> CHANDOLI
#  'UTTAR PRADESH_CHITRAKOOT',---->>  CHITRAKOOT DHAM
#  'UTTAR PRADESH_FARRUKHABAD',----->> FATEHGARH
#  'UTTAR PRADESH_GAUTAM BUDDHA NAGAR',--->> GAUTAMBUDH NAGAR
#  'UTTAR PRADESH_JYOTIBA PHULE NAGAR',--->> J.P.NAGAR
#  'UTTAR PRADESH_KANPUR DEHAT',---->> KANPUR
#  'UTTAR PRADESH_KANPUR NAGAR',---->> KANPUR
#  'UTTAR PRADESH_KHERI',---->> KHIRI
#  'UTTAR PRADESH_KUSHINAGAR',--->> KUSHI NAGAR
#  'UTTAR PRADESH_MAHAMAYA NAGAR',---->> HATHRAS
#  'UTTAR PRADESH_MAHRAJGANJ',--->> MAHARAJGANJ
#  'UTTAR PRADESH_RAE BARELI',--->> BAREILLY
#  'UTTAR PRADESH_SANT KABIR NAGAR',---->> SANT KABIRNAGAR
#  'UTTAR PRADESH_SANT RAVIDAS NAGAR (BHADOHI)', --->> ST.RAVIDASNAGAR
#  'UTTAR PRADESH_SIDDHARTHNAGAR',---->> SIDHARTHNAGAR
#  'UTTARAKHAND_GARHWAL',---->> PAURI GARHWAL
#  'UTTARAKHAND_HARDWAR', ---->> HARIDWAR
#  'UTTARAKHAND_RUDRAPRAYAG',----->> RUDRA PRAYAG
#  'UTTARAKHAND_UDHAM SINGH NAGAR',----->> UDHAMSINGH NAGAR
#  'WEST BENGAL_BARDDHAMAN',--->> BURDWAN
#  'WEST BENGAL_DARJILING',--->> DARJEELING
#  'WEST BENGAL_HAORA',--->> HOWRAH
#  'WEST BENGAL_HUGLI',---->> HOOGHLY
#  'WEST BENGAL_KOCH BIHAR', ---> COOCHBEHAR
#  'WEST BENGAL_MALDAH',---> MALDA
#  'WEST BENGAL_NORTH TWENTY FOUR PARGANAS', ---> 24 PARGANAS NORTH
#  'WEST BENGAL_PASCHIM MEDINIPUR',----> MIDNAPUR
#  'WEST BENGAL_PURBA MEDINIPUR',----->> MIDNAPUR
#  'WEST BENGAL_PURULIYA',-----> PURULIA
#  'WEST BENGAL_SOUTH TWENTY FOUR PARGANAS' -->> 24 PARGANAS SOUTH
##################Not Present#####################
#  'ASSAM_DIMA HASAO', 
##################################################
# GUJARAT_BANAS KANTHA change to Palanpur in census


# In[49]:


# 'ANDHRA PRADESH_CUDDAPAH',
#  'ANDHRA PRADESH_CYBERABAD',
#  'ANDHRA PRADESH_GUNTAKAL RLY.',
#  'ANDHRA PRADESH_HYDERABAD CITY',
#  'ANDHRA PRADESH_MAHABOOBNAGAR',
#  'ANDHRA PRADESH_NELLORE',
#  'ANDHRA PRADESH_PRAKASHAM',
#  'ANDHRA PRADESH_RAJAHMUNDRY',
#  'ANDHRA PRADESH_RANGA REDDY',
#  'ANDHRA PRADESH_SECUNDERABAD RLY.',
#  'ANDHRA PRADESH_TIRUPATHI URBAN',
#  'ANDHRA PRADESH_VIJAYAWADA',
#  'ANDHRA PRADESH_VISAKHA RURAL',
#  'ANDHRA PRADESH_WARANGAL URBAN',
#  'ARUNACHAL PRADESH_K/KUMEY',
#  'ARUNACHAL PRADESH_KAMENG EAST',
#  'ARUNACHAL PRADESH_KAMENG WEST',
#  'ARUNACHAL PRADESH_RURAL',
#  'ARUNACHAL PRADESH_SIANG EAST',
#  'ARUNACHAL PRADESH_SIANG UPPER',
#  'ARUNACHAL PRADESH_SIANG WEST',
#  'ARUNACHAL PRADESH_SUBANSIRI LOWER',
#  'ARUNACHAL PRADESH_SUBANSIRI UPPER',
#  'ASSAM_BASKA',
#  'ASSAM_C.I.D.',
#  'ASSAM_G.R.P.',
#  'ASSAM_GUWAHATI CITY',
#  'ASSAM_N.C.HILLS',
#  'ASSAM_R.P.O.',
#  'ASSAM_SIBSAGAR',
#  'BIHAR_BAGAHA',
#  'BIHAR_BETTIAH',
#  'BIHAR_BHABHUA',
#  'BIHAR_JAMALPUR RLY.',
#  'BIHAR_KATIHAR RLY.',
#  'BIHAR_MOTIHARI',
#  'BIHAR_MUZAFFARPUR RLY.',
#  'BIHAR_NAUGACHIA',
#  'BIHAR_NAWADAH',
#  'BIHAR_PATNA RLY.',
#  'BIHAR_PURNEA',
#  'CHHATTISGARH_BALRAMPUR',
#  'CHHATTISGARH_BIZAPUR',
#  'CHHATTISGARH_DANTEWADA',
#  'CHHATTISGARH_GRP RAIPUR',
#  'CHHATTISGARH_JAGDALPUR',
#  'CHHATTISGARH_JANJGIR',
#  'CHHATTISGARH_KABIRDHAM',
#  'CHHATTISGARH_KANKER',
#  'CHHATTISGARH_SARGUJA',
#  'CHHATTISGARH_SURAJPUR',
#  'GUJARAT_AHMEDABAD COMMR.',
#  'GUJARAT_AHMEDABAD RURAL',
#  'GUJARAT_AHWA-DANG',
#  'GUJARAT_CID CRIME',
#  'GUJARAT_DAHOD',
#  'GUJARAT_HIMATNAGAR',
#  'GUJARAT_KHEDA NORTH',
#  'GUJARAT_KUTCH',
#  'GUJARAT_MEHSANA',
#  'GUJARAT_PALANPUR',
#  'GUJARAT_PANCHMAHAL',
#  'GUJARAT_RAJKOT COMMR.',
#  'GUJARAT_RAJKOT RURAL',
#  'GUJARAT_SURAT COMMR.',
#  'GUJARAT_SURAT RURAL',
#  'GUJARAT_VADODARA COMMR.',
#  'GUJARAT_VADODARA RURAL',
#  'GUJARAT_W.RLY',
#  'HARYANA_GRP',
#  'HARYANA_HISSAR',
#  'HIMACHAL PRADESH_BADDIPOLICEDIST',
#  'HIMACHAL PRADESH_CID',
#  'HIMACHAL PRADESH_G.R.P.',
#  'HIMACHAL PRADESH_LAHAUL-SPITI',
#  'JAMMU & KASHMIR_AWANTIPORA',
#  'JAMMU & KASHMIR_BORDER',
#  'JAMMU & KASHMIR_C.B.KASHMIR',
#  'JAMMU & KASHMIR_CRIME JAMMU',
#  'JAMMU & KASHMIR_CRIME SRINAGAR',
#  'JAMMU & KASHMIR_HANDWARA',
#  'JAMMU & KASHMIR_RAILWAYS',
#  'JAMMU & KASHMIR_SOPORE',
#  'JHARKHAND_CHAIBASA',
#  'JHARKHAND_DHANBAD RLY.',
#  'JHARKHAND_JAMSHEDPUR',
#  'JHARKHAND_JAMSHEDPUR RLY.',
#  'JHARKHAND_KODERMA',
#  'JHARKHAND_LOHARDAGGA',
#  'JHARKHAND_SAHEBGANJ',
#  'JHARKHAND_SARAIKELA',
#  'KARNATAKA_BANGALORE COMMR.',
#  'KARNATAKA_CBPURA',
#  'KARNATAKA_CHAMARAJNAGAR',
#  'KARNATAKA_CHICKMAGALUR',
#  'KARNATAKA_DAKSHIN KANNADA',
#  'KARNATAKA_DHARWAD COMMR.',
#  'KARNATAKA_DHARWAD RURAL',
#  'KARNATAKA_K.G.F.',
#  'KARNATAKA_MYSORE COMMR.',
#  'KARNATAKA_MYSORE RURAL',
#  'KARNATAKA_RAILWAYS',
#  'KARNATAKA_RAMANAGAR',
#  'KARNATAKA_UTTAR KANNADA',
#  'KARNATAKA_YADGIRI',
#  'KERALA_ALAPUZHA',
#  'KERALA_CBCID',
#  'KERALA_KASARGOD',
#  'KERALA_RAILWAYS',
#  'KERALA_TRIVANDRUM',
#  'KERALA_WAYANADU',
#  'MADHYA PRADESH_ASHOK NAGAR',
#  'MADHYA PRADESH_BHOPAL RLY.',
#  'MADHYA PRADESH_DATIYA',
#  'MADHYA PRADESH_INDORE RLY.',
#  'MADHYA PRADESH_JABALPUR RLY.',
#  'MADHYA PRADESH_KHANDWA',
#  'MADHYA PRADESH_KHARGON',
#  'MADHYA PRADESH_NARSINGHPUR',
#  'MADHYA PRADESH_SIHORE',
#  'MADHYA PRADESH_UMARIYA',
#  'MAHARASHTRA_AHMEDNAGAR',
#  'MAHARASHTRA_AMRAVATI COMMR.',
#  'MAHARASHTRA_AMRAVATI RURAL',
#  'MAHARASHTRA_AURANGABAD COMMR.',
#  'MAHARASHTRA_AURANGABAD RURAL',
#  'MAHARASHTRA_BEED',
#  'MAHARASHTRA_BULDHANA',
#  'MAHARASHTRA_GONDIA',
#  'MAHARASHTRA_NAGPUR COMMR.',
#  'MAHARASHTRA_NAGPUR RLY.',
#  'MAHARASHTRA_NAGPUR RURAL',
#  'MAHARASHTRA_NASIK COMMR.',
#  'MAHARASHTRA_NASIK RURAL',
#  'MAHARASHTRA_PUNE COMMR.',
#  'MAHARASHTRA_PUNE RLY.',
#  'MAHARASHTRA_PUNE RURAL',
#  'MAHARASHTRA_RAIGAD',
#  'MAHARASHTRA_SOLAPUR COMMR.',
#  'MAHARASHTRA_SOLAPUR RURAL',
#  'MAHARASHTRA_THANE COMMR.',
#  'MAHARASHTRA_THANE RURAL',
#  'MANIPUR_CID',
#  'MEGHALAYA_GARO HILLS EAST',
#  'MEGHALAYA_GARO HILLS SOUTH',
#  'MEGHALAYA_GARO HILLS WEST',
#  'MEGHALAYA_KHASI HILLS EAST',
#  'MEGHALAYA_KHASI HILLS WEST',
#  'MEGHALAYA_RI-BHOI',

