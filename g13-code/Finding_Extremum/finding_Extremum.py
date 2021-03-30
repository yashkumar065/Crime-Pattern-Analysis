#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
cwd = os.getcwd()

sc_Data = pd.read_csv(cwd+'/Preprocessing/clean_SC_Data.csv')
st_Data = pd.read_csv(cwd+'/Preprocessing/clean_ST_Data.csv')
children_Data = pd.read_csv(cwd+'/Preprocessing/clean_Children_Data.csv')
women_Data = pd.read_csv(cwd+'/Preprocessing/clean_Women_Data.csv')
census_Data = pd.read_csv(cwd+'/Preprocessing/clean_Census_Data.csv')
census_Data = census_Data[['STATE_DISTRICT','Population','SC','ST','Female']]


# # SC Data Extremum

# In[2]:


process_SC_Data = sc_Data[['STATE_DISTRICT','Year','Total_Crimes']]
process_Census = census_Data[['STATE_DISTRICT','SC']]
state_District_Process = set(list(process_SC_Data.STATE_DISTRICT))
state_District_Census = set(list(census_Data.STATE_DISTRICT))
drop_State_District_Process = list(state_District_Process.difference(state_District_Census))
process_Data = process_SC_Data
for dp in drop_State_District_Process:
    process_Data = process_Data[process_Data.STATE_DISTRICT!=dp]
process_Census_SC = pd.merge(process_Data, process_Census, on="STATE_DISTRICT")
process_Census_SC = process_Census_SC[process_Census_SC.SC!=0]
list_States = [i.split('_')[0] for i in list(process_Census_SC['STATE_DISTRICT'])]
process_Census_SC['STATE'] = list_States


# # # Top/Last Five Districts per year for all crimes combined[zscore considered]

# In[3]:


year = range(2001,2011)
ls_Top = []
ls_Last = []
for yr in year:
    top_States = []
    top_Districts = []
    top_Total_Crimes = []
    low_States = []
    low_Districts = []
    low_Total_Crimes = []
    process_df = process_Census_SC[process_Census_SC.Year == yr]
    process_df = process_df[process_df['Total_Crimes'] !=0]
    mean = process_df['Total_Crimes'].mean()
    stdev = process_df['Total_Crimes'].std()
    process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
    process_df['zscore'] = process_df['Crimes_Dev']/stdev
    top_Five = process_df.nlargest(5,['zscore'])
    low_Five = process_df.nsmallest(5,['zscore'])
    top_States= [i.split('_')[0] for i in list(top_Five['STATE_DISTRICT'])]
    top_Districts=[i.split('_')[1] for i in list(top_Five['STATE_DISTRICT'])]
    top_Total_Crimes=top_Five['Total_Crimes']
    low_States= [i.split('_')[0] for i in list(low_Five['STATE_DISTRICT'])]
    low_Districts= [i.split('_')[1] for i in list(low_Five['STATE_DISTRICT'])]
    low_Total_Crimes= low_Five['Total_Crimes']
    data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/SC/Per Year/Districts/top_Five_Districts_SC_Year'+str(yr)+'.csv',index=0)
    data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/SC/Per Year/Districts/low_Five_Districts_SC_Year'+str(yr)+'.csv',index=0)


# # # Top/Last Five States per year for all crimes combined[zscore considered]

# In[4]:


year = range(2001,2011)
ls_Top = []
ls_Last = []
for yr in year:
    top_States = []
    top_Total_Crimes = []
    low_States = []
    low_Total_Crimes = []
    process_df = process_Census_SC[process_Census_SC.Year == yr]
    process_df = pd.DataFrame(process_df.groupby('STATE').sum().Total_Crimes)
    process_df = process_df[process_df['Total_Crimes'] !=0]
    process_df.reset_index()
    mean = process_df['Total_Crimes'].mean()
    stdev = process_df['Total_Crimes'].std()
    process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
    process_df['zscore'] = process_df['Crimes_Dev']/stdev

    top_Five = process_df.nlargest(5,['zscore'])
    low_Five = process_df.nsmallest(5,['zscore'])
    top_Five=top_Five.reset_index()
    low_Five=low_Five.reset_index()
    top_States= [i for i in list(top_Five['STATE'])]
    top_Districts=[i for i in list(top_Five['STATE'])]
    top_Total_Crimes=top_Five['Total_Crimes']
    low_States= [i for i in list(low_Five['STATE'])]
    low_Districts= [i for i in list(low_Five['STATE'])]
    low_Total_Crimes= low_Five['Total_Crimes']
    data = {'States':top_States,'Total Crimes':top_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/SC/Per Year/States/top_Five_States_SC_Year'+str(yr)+'.csv',index=0)
    data = {'States':low_States,'Total Crimes':low_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/SC/Per Year/States/low_Five_States_SC_Year'+str(yr)+'.csv',index=0)


# # # Top/Last 5 Districts for crimes against SC for the period(2001-2010) [census state population considered]

# In[5]:


top_States = []
top_Districts = []
top_Total_Crimes = []
low_States = []
low_Districts = []
low_Total_Crimes = []
process_df = pd.DataFrame(process_Census_SC.groupby(['STATE_DISTRICT']).agg({'SC':"sum",'Total_Crimes':"sum"}))
process_df = process_df[process_df['Total_Crimes'] !=0]
process_df = process_df.reset_index()


mean = process_df['Total_Crimes'].mean()
stdev = process_df['Total_Crimes'].std()
process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
process_df['zscore'] = process_df['Crimes_Dev']/stdev
process_df['Normalised_By_Population'] = process_df['Crimes_Dev']/process_df['SC']


top_Five_Population = process_df.nlargest(5,['Normalised_By_Population'])
low_Five_Population = process_df[process_df['Normalised_By_Population']<0].nlargest(5,['Normalised_By_Population'])
#low_Five_Population = process_df.nsmallest(5,['Normalised_By_Population'])
top_Five_Zscore = process_df.nlargest(5,['zscore'])
low_Five_Zscore = process_df.nsmallest(5,['zscore'])
top_Five_Population=top_Five_Population.reset_index()
low_Five_Population=low_Five_Population.reset_index()                                       
top_Five_Zscore=top_Five_Zscore.reset_index()
low_Five_Zscore=low_Five_Zscore.reset_index()
                                       
top_States= [i.split('_')[0] for i in list(top_Five_Population['STATE_DISTRICT'])]
top_Districts= [i.split('_')[1] for i in list(top_Five_Population['STATE_DISTRICT'])]
top_Total_Crimes= top_Five_Population['Total_Crimes']
low_States= [i.split('_')[0] for i in list(low_Five_Population['STATE_DISTRICT'])]
low_Districts= [i.split('_')[1] for i in list(low_Five_Population['STATE_DISTRICT'])]
low_Total_Crimes= low_Five_Population['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/SC/Overall/Districts/top_Five_Districts_Overall_SC_Population.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/SC/Overall/Districts/low_Five_Districts_Overall_SC_Population.csv',index=0)

top_States= [i.split('_')[0] for i in list(top_Five_Zscore['STATE_DISTRICT'])]
top_Districts= [i.split('_')[1] for i in list(top_Five_Zscore['STATE_DISTRICT'])]
top_Total_Crimes= top_Five_Zscore['Total_Crimes']
low_States= [i.split('_')[0] for i in list(low_Five_Zscore['STATE_DISTRICT'])]
low_Districts= [i.split('_')[1] for i in list(low_Five_Zscore['STATE_DISTRICT'])]
low_Total_Crimes= low_Five_Zscore['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/SC/Overall/Districts/top_Five_Districts_Overall_SC_zscore.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/SC/Overall/Districts/low_Five_Districts_Overall_SC_zscore.csv',index=0)


# # # Top/Last 5 States for crimes against SC for the period(2001-2010) [census state population considered]

# In[6]:


top_States = []
top_Total_Crimes = []
low_States = []
low_Total_Crimes = []
process_df = pd.DataFrame(process_Census_SC.groupby(['STATE']).agg({'SC':"sum",'Total_Crimes':"sum"}))
process_df = process_df[process_df['Total_Crimes'] !=0]

mean = process_df['Total_Crimes'].mean()
stdev = process_df['Total_Crimes'].std()
process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
process_df['Normalised_By_Population'] = process_df['Crimes_Dev']/process_df['SC']
process_df['zscore'] = process_df['Crimes_Dev']/stdev

top_Five_Population = process_df.nlargest(5,['Normalised_By_Population'])
low_Five_Population = process_df[process_df['Normalised_By_Population']<0].nlargest(5,['Normalised_By_Population'])
top_Five_Zscore = process_df.nlargest(5,['zscore'])
low_Five_Zscore = process_df.nsmallest(5,['zscore'])
                                       
top_Five_Population=top_Five_Population.reset_index()
low_Five_Population=low_Five_Population.reset_index()                                       
top_Five_Zscore=top_Five_Zscore.reset_index()
low_Five_Zscore=low_Five_Zscore.reset_index()
                                       
top_States= [i for i in list(top_Five_Population['STATE'])]
top_Total_Crimes= top_Five_Population['Total_Crimes']
low_States= [i for i in list(low_Five_Population['STATE'])]
low_Total_Crimes= low_Five_Population['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/SC/Overall/States/top_Five_States_Overall_SC_Population.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/SC/Overall/States/low_Five_States_Overall_SC_Population.csv',index=0)

top_States= [i for i in list(top_Five_Zscore['STATE'])]
top_Total_Crimes= top_Five_Zscore['Total_Crimes']
low_States= [i for i in list(low_Five_Zscore['STATE'])]
low_Total_Crimes= low_Five_Zscore['Total_Crimes']
                                       
data = {'States':top_States,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/SC/Overall/States/top_Five_States_Overall_SC_zscore.csv',index=0)
data = {'States':low_States,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/SC/Overall/States/low_Five_States_Overall_SC_zscore.csv',index=0)


# # ST Data Extremum

# In[7]:


process_ST_Data = st_Data[['STATE_DISTRICT','Year','Total_Crimes']]
process_Census = census_Data[['STATE_DISTRICT','ST']]
state_District_Process = set(list(process_ST_Data.STATE_DISTRICT))
state_District_Census = set(list(census_Data.STATE_DISTRICT))
drop_State_District_Process = list(state_District_Process.difference(state_District_Census))
process_Data = process_ST_Data
for dp in drop_State_District_Process:
    process_Data = process_Data[process_Data.STATE_DISTRICT!=dp]
process_Census_ST = pd.merge(process_Data, process_Census, on="STATE_DISTRICT")
process_Census_ST = process_Census_ST[process_Census_ST.ST!=0]
list_States = [i.split('_')[0] for i in list(process_Census_ST['STATE_DISTRICT'])]
process_Census_ST['STATE'] = list_States


# # # Top/Last Five Districts per year for all crimes combined[zscore considered]

# In[8]:


year = range(2001,2011)
ls_Top = []
ls_Last = []
for yr in year:
    top_States = []
    top_Districts = []
    top_Total_Crimes = []
    low_States = []
    low_Districts = []
    low_Total_Crimes = []
    process_df = process_Census_ST[process_Census_ST.Year == yr]
    process_df = process_df[process_df['Total_Crimes'] !=0]
    mean = process_df['Total_Crimes'].mean()
    stdev = process_df['Total_Crimes'].std()
    process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
    process_df['zscore'] = process_df['Crimes_Dev']/stdev
    top_Five = process_df.nlargest(5,['zscore'])
    low_Five = process_df.nsmallest(5,['zscore'])
    top_States= [i.split('_')[0] for i in list(top_Five['STATE_DISTRICT'])]
    top_Districts=[i.split('_')[1] for i in list(top_Five['STATE_DISTRICT'])]
    top_Total_Crimes=top_Five['Total_Crimes']
    low_States= [i.split('_')[0] for i in list(low_Five['STATE_DISTRICT'])]
    low_Districts= [i.split('_')[1] for i in list(low_Five['STATE_DISTRICT'])]
    low_Total_Crimes= low_Five['Total_Crimes']
    data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/ST/Per Year/Districts/top_Five_Districts_ST_Year'+str(yr)+'.csv',index=0)
    data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/ST/Per Year/Districts/low_Five_Districts_ST_Year'+str(yr)+'.csv',index=0)


# # # Top/Last Five States per year for all crimes combined[zscore considered]

# In[9]:


year = range(2001,2011)
ls_Top = []
ls_Last = []
for yr in year:
    top_States = []
    top_Total_Crimes = []
    low_States = []
    low_Total_Crimes = []
    process_df = process_Census_ST[process_Census_ST.Year == yr]
    process_df = pd.DataFrame(process_df.groupby('STATE').sum().Total_Crimes)
    process_df = process_df[process_df['Total_Crimes'] !=0]
    process_df.reset_index()
    mean = process_df['Total_Crimes'].mean()
    stdev = process_df['Total_Crimes'].std()
    process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
    process_df['zscore'] = process_df['Crimes_Dev']/stdev
    top_Five = process_df.nlargest(5,['zscore'])
    low_Five = process_df.nsmallest(5,['zscore'])
    top_Five=top_Five.reset_index()
    low_Five=low_Five.reset_index()
    top_States= [i for i in list(top_Five['STATE'])]
    top_Districts=[i for i in list(top_Five['STATE'])]
    top_Total_Crimes=top_Five['Total_Crimes']
    low_States= [i for i in list(low_Five['STATE'])]
    low_Districts= [i for i in list(low_Five['STATE'])]
    low_Total_Crimes= low_Five['Total_Crimes']
    data = {'States':top_States,'Total Crimes':top_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/ST/Per Year/States/top_Five_States_ST_Year'+str(yr)+'.csv',index=0)
    data = {'States':low_States,'Total Crimes':low_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/ST/Per Year/States/low_Five_States_ST_Year'+str(yr)+'.csv',index=0)


# # # Top/Last 5 Districts for crimes against ST for the period(2001-2010) [census state population considered]

# In[10]:


top_States = []
top_Districts = []
top_Total_Crimes = []
low_States = []
low_Districts = []
low_Total_Crimes = []
process_df = pd.DataFrame(process_Census_ST.groupby(['STATE_DISTRICT']).agg({'ST':"sum",'Total_Crimes':"sum"}))
process_df = process_df[process_df['Total_Crimes'] !=0]

mean = process_df['Total_Crimes'].mean()
stdev = process_df['Total_Crimes'].std()
process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
process_df['zscore'] = process_df['Crimes_Dev']/stdev
process_df['Normalised_By_Population'] = process_df['Crimes_Dev']/process_df['ST']

top_Five_Population = process_df.nlargest(5,['Normalised_By_Population'])
low_Five_Population = process_df[process_df['Normalised_By_Population']<0].nlargest(5,['Normalised_By_Population'])
top_Five_Zscore = process_df.nlargest(5,['zscore'])
low_Five_Zscore = process_df.nsmallest(5,['zscore'])
                                       
top_Five_Population=top_Five_Population.reset_index()
low_Five_Population=low_Five_Population.reset_index()                                       
top_Five_Zscore=top_Five_Zscore.reset_index()
low_Five_Zscore=low_Five_Zscore.reset_index()
                                       
top_States= [i.split('_')[0] for i in list(top_Five_Population['STATE_DISTRICT'])]
top_Districts= [i.split('_')[1] for i in list(top_Five_Population['STATE_DISTRICT'])]
top_Total_Crimes= top_Five_Population['Total_Crimes']
low_States= [i.split('_')[0] for i in list(low_Five_Population['STATE_DISTRICT'])]
low_Districts= [i.split('_')[1] for i in list(low_Five_Population['STATE_DISTRICT'])]
low_Total_Crimes= low_Five_Population['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/ST/Overall/Districts/top_Five_Districts_Overall_ST_Population.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/ST/Overall/Districts/low_Five_Districts_Overall_ST_Population.csv',index=0)

top_States= [i.split('_')[0] for i in list(top_Five_Zscore['STATE_DISTRICT'])]
top_Districts= [i.split('_')[1] for i in list(top_Five_Zscore['STATE_DISTRICT'])]
top_Total_Crimes= top_Five_Zscore['Total_Crimes']
low_States= [i.split('_')[0] for i in list(low_Five_Zscore['STATE_DISTRICT'])]
low_Districts= [i.split('_')[1] for i in list(low_Five_Zscore['STATE_DISTRICT'])]
low_Total_Crimes= low_Five_Zscore['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/ST/Overall/Districts/top_Five_Districts_Overall_ST_zscore.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/ST/Overall/Districts/low_Five_Districts_Overall_ST_zscore.csv',index=0)


# # # Top/Last 5 States for crimes against ST for the period(2001-2010) [census state population considered]

# In[11]:


top_States = []
top_Total_Crimes = []
low_States = []
low_Total_Crimes = []
process_df = pd.DataFrame(process_Census_ST.groupby(['STATE']).agg({'ST':"sum",'Total_Crimes':"sum"}))
process_df = process_df[process_df['Total_Crimes'] !=0]

mean = process_df['Total_Crimes'].mean()
stdev = process_df['Total_Crimes'].std()
process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
process_df['Normalised_By_Population'] = process_df['Crimes_Dev']/process_df['ST']
process_df['zscore'] = process_df['Crimes_Dev']/stdev

top_Five_Population = process_df.nlargest(5,['Normalised_By_Population'])
low_Five_Population = process_df[process_df['Normalised_By_Population']<0].nlargest(5,['Normalised_By_Population'])
top_Five_Zscore = process_df.nlargest(5,['zscore'])
low_Five_Zscore = process_df.nsmallest(5,['zscore'])
                                       
top_Five_Population=top_Five_Population.reset_index()
low_Five_Population=low_Five_Population.reset_index()                                       
top_Five_Zscore=top_Five_Zscore.reset_index()
low_Five_Zscore=low_Five_Zscore.reset_index()
                                       
top_States= [i for i in list(top_Five_Population['STATE'])]
top_Total_Crimes= top_Five_Population['Total_Crimes']
low_States= [i for i in list(low_Five_Population['STATE'])]
low_Total_Crimes= low_Five_Population['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/ST/Overall/States/top_Five_States_Overall_ST_Population.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/ST/Overall/States/low_Five_States_Overall_ST_Population.csv',index=0)

top_States= [i for i in list(top_Five_Zscore['STATE'])]
top_Total_Crimes= top_Five_Zscore['Total_Crimes']
low_States= [i for i in list(low_Five_Zscore['STATE'])]
low_Total_Crimes= low_Five_Zscore['Total_Crimes']
                                       
data = {'States':top_States,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/ST/Overall/States/top_Five_States_Overall_ST_zscore.csv',index=0)
data = {'States':low_States,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/ST/Overall/States/low_Five_States_Overall_ST_zscore.csv',index=0)


# # Children Data Extremum

# In[12]:


process_Children_Data = children_Data[['STATE_DISTRICT','Year','Total_Crimes']]
process_Census = census_Data[['STATE_DISTRICT','Population']]
state_District_Process = set(list(process_Children_Data.STATE_DISTRICT))
state_District_Census = set(list(census_Data.STATE_DISTRICT))
drop_State_District_Process = list(state_District_Process.difference(state_District_Census))
process_Data = process_Children_Data
for dp in drop_State_District_Process:
    process_Data = process_Data[process_Data.STATE_DISTRICT!=dp]
process_Census_Children = pd.merge(process_Data, process_Census, on="STATE_DISTRICT")
process_Census_Children = process_Census_Children[process_Census_Children.Population!=0]
list_States = [i.split('_')[0] for i in list(process_Census_Children['STATE_DISTRICT'])]
process_Census_Children['STATE'] = list_States


# # # Top/Last Five Districts per year for all crimes combined[zscore considered]
# 

# In[13]:


year = range(2001,2011)
ls_Top = []
ls_Last = []
for yr in year:
    top_States = []
    top_Districts = []
    top_Total_Crimes = []
    low_States = []
    low_Districts = []
    low_Total_Crimes = []
    process_df = process_Census_Children[process_Census_Children.Year == yr]
    process_df = process_df[process_df['Total_Crimes'] !=0]
    mean = process_df['Total_Crimes'].mean()
    stdev = process_df['Total_Crimes'].std()
    process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
    process_df['zscore'] = process_df['Crimes_Dev']/stdev
    top_Five = process_df.nlargest(5,['zscore'])
    low_Five = process_df.nsmallest(5,['zscore'])
    top_States= [i.split('_')[0] for i in list(top_Five['STATE_DISTRICT'])]
    top_Districts=[i.split('_')[1] for i in list(top_Five['STATE_DISTRICT'])]
    top_Total_Crimes=top_Five['Total_Crimes']
    low_States= [i.split('_')[0] for i in list(low_Five['STATE_DISTRICT'])]
    low_Districts= [i.split('_')[1] for i in list(low_Five['STATE_DISTRICT'])]
    low_Total_Crimes= low_Five['Total_Crimes']
    data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/Children/Per Year/Districts/top_Five_Districts_Children_Year'+str(yr)+'.csv',index=0)
    data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/Children/Per Year/Districts/low_Five_Districts_Children_Year'+str(yr)+'.csv',index=0)


# # # Top/Last Five States per year for all crimes combined[zscore considered]
# 

# In[14]:



year = range(2001,2011)
ls_Top = []
ls_Last = []
for yr in year:
    top_States = []
    top_Total_Crimes = []
    low_States = []
    low_Total_Crimes = []
    process_df = process_Census_Children[process_Census_Children.Year == yr]
    process_df = pd.DataFrame(process_df.groupby('STATE').sum().Total_Crimes)
    process_df = process_df[process_df['Total_Crimes'] !=0]
    process_df.reset_index()
    mean = process_df['Total_Crimes'].mean()
    stdev = process_df['Total_Crimes'].std()
    process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
    process_df['zscore'] = process_df['Crimes_Dev']/stdev
    top_Five = process_df.nlargest(5,['zscore'])
    low_Five = process_df.nsmallest(5,['zscore'])
    top_Five=top_Five.reset_index()
    low_Five=low_Five.reset_index()
    top_States= [i for i in list(top_Five['STATE'])]
    top_Districts=[i for i in list(top_Five['STATE'])]
    top_Total_Crimes=top_Five['Total_Crimes']
    low_States= [i for i in list(low_Five['STATE'])]
    low_Districts= [i for i in list(low_Five['STATE'])]
    low_Total_Crimes= low_Five['Total_Crimes']
    data = {'States':top_States,'Total Crimes':top_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/Children/Per Year/States/top_Five_States_Children_Year'+str(yr)+'.csv',index=0)
    data = {'States':low_States,'Total Crimes':low_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/Children/Per Year/States/low_Five_States_Children_Year'+str(yr)+'.csv',index=0)


# # # Top/Last 5 Districts for crimes against Children for the period(2001-2010) [census state population considered]

# In[15]:


top_States = []
top_Districts = []
top_Total_Crimes = []
low_States = []
low_Districts = []
low_Total_Crimes = []
process_df = pd.DataFrame(process_Census_Children.groupby(['STATE_DISTRICT']).agg({'Population':"sum",'Total_Crimes':"sum"}))
process_df = process_df[process_df['Total_Crimes'] !=0]

mean = process_df['Total_Crimes'].mean()
stdev = process_df['Total_Crimes'].std()
process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
process_df['zscore'] = process_df['Crimes_Dev']/stdev
process_df['Normalised_By_Population'] = process_df['Crimes_Dev']/process_df['Population']

top_Five_Population = process_df.nlargest(5,['Normalised_By_Population'])
low_Five_Population = process_df[process_df['Normalised_By_Population']<0].nlargest(5,['Normalised_By_Population'])
top_Five_Zscore = process_df.nlargest(5,['zscore'])
low_Five_Zscore = process_df.nsmallest(5,['zscore'])
                                       
top_Five_Population=top_Five_Population.reset_index()
low_Five_Population=low_Five_Population.reset_index()                                       
top_Five_Zscore=top_Five_Zscore.reset_index()
low_Five_Zscore=low_Five_Zscore.reset_index()
                                       
top_States= [i.split('_')[0] for i in list(top_Five_Population['STATE_DISTRICT'])]
top_Districts= [i.split('_')[1] for i in list(top_Five_Population['STATE_DISTRICT'])]
top_Total_Crimes= top_Five_Population['Total_Crimes']
low_States= [i.split('_')[0] for i in list(low_Five_Population['STATE_DISTRICT'])]
low_Districts= [i.split('_')[1] for i in list(low_Five_Population['STATE_DISTRICT'])]
low_Total_Crimes= low_Five_Population['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Children/Overall/Districts/top_Five_Districts_Overall_Children_Population.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Children/Overall/Districts/low_Five_Districts_Overall_Children_Population.csv',index=0)

top_States= [i.split('_')[0] for i in list(top_Five_Zscore['STATE_DISTRICT'])]
top_Districts= [i.split('_')[1] for i in list(top_Five_Zscore['STATE_DISTRICT'])]
top_Total_Crimes= top_Five_Zscore['Total_Crimes']
low_States= [i.split('_')[0] for i in list(low_Five_Zscore['STATE_DISTRICT'])]
low_Districts= [i.split('_')[1] for i in list(low_Five_Zscore['STATE_DISTRICT'])]
low_Total_Crimes= low_Five_Zscore['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Children/Overall/Districts/top_Five_Districts_Overall_Children_zscore.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Children/Overall/Districts/low_Five_Districts_Overall_Children_zscore.csv',index=0)


# # # Top/Last 5 States for crimes against Children for the period(2001-2010) [census state population considered]

# In[16]:


top_States = []
top_Total_Crimes = []
low_States = []
low_Total_Crimes = []
process_df = pd.DataFrame(process_Census_Children.groupby(['STATE']).agg({'Population':"sum",'Total_Crimes':"sum"}))
process_df = process_df[process_df['Total_Crimes'] !=0]

mean = process_df['Total_Crimes'].mean()
stdev = process_df['Total_Crimes'].std()
process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
process_df['Normalised_By_Population'] = process_df['Crimes_Dev']/process_df['Population']
process_df['zscore'] = process_df['Crimes_Dev']/stdev

top_Five_Population = process_df.nlargest(5,['Normalised_By_Population'])
low_Five_Population = process_df[process_df['Normalised_By_Population']<0].nlargest(5,['Normalised_By_Population'])
top_Five_Zscore = process_df.nlargest(5,['zscore'])
low_Five_Zscore = process_df.nsmallest(5,['zscore'])
                                       
top_Five_Population=top_Five_Population.reset_index()
low_Five_Population=low_Five_Population.reset_index()                                       
top_Five_Zscore=top_Five_Zscore.reset_index()
low_Five_Zscore=low_Five_Zscore.reset_index()
                                       
top_States= [i for i in list(top_Five_Population['STATE'])]
top_Total_Crimes= top_Five_Population['Total_Crimes']
low_States= [i for i in list(low_Five_Population['STATE'])]
low_Total_Crimes= low_Five_Population['Total_Crimes']
                                       
data = {'States':top_States,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Children/Overall/States/top_Five_States_Overall_Children_Population.csv',index=0)
data = {'States':low_States,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Children/Overall/States/low_Five_States_Overall_Children_Population.csv',index=0)

top_States= [i for i in list(top_Five_Zscore['STATE'])]
top_Total_Crimes= top_Five_Zscore['Total_Crimes']
low_States= [i for i in list(low_Five_Zscore['STATE'])]
low_Total_Crimes= low_Five_Zscore['Total_Crimes']
                                       
data = {'States':top_States,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Children/Overall/States/top_Five_States_Overall_Children_zscore.csv',index=0)
data = {'States':low_States,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Children/Overall/States/low_Five_States_Overall_Children_zscore.csv',index=0)


# # Women Data Extremum

# In[18]:


process_Women_Data = women_Data[['STATE_DISTRICT','Year','Total_Crimes']]
process_Census = census_Data[['STATE_DISTRICT','Female']]
state_District_Process = set(list(process_Women_Data.STATE_DISTRICT))
state_District_Census = set(list(census_Data.STATE_DISTRICT))
drop_State_District_Process = list(state_District_Process.difference(state_District_Census))
process_Data = process_Women_Data
for dp in drop_State_District_Process:
    process_Data = process_Data[process_Data.STATE_DISTRICT!=dp]
process_Census_Women = pd.merge(process_Data, process_Census, on="STATE_DISTRICT")
process_Census_Women = process_Census_Women[process_Census_Women.Female!=0]
list_States = [i.split('_')[0] for i in list(process_Census_Women['STATE_DISTRICT'])]
process_Census_Women['STATE'] = list_States


# # # Top/Last Five Districts per year for all crimes combined[zscore considered]

# In[19]:


year = range(2001,2011)
ls_Top = []
ls_Last = []
for yr in year:
    top_States = []
    top_Districts = []
    top_Total_Crimes = []
    low_States = []
    low_Districts = []
    low_Total_Crimes = []
    process_df = process_Census_Women[process_Census_Women.Year == yr]
    process_df = process_df[process_df['Total_Crimes'] !=0]
    mean = process_df['Total_Crimes'].mean()
    stdev = process_df['Total_Crimes'].std()
    process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
    process_df['zscore'] = process_df['Crimes_Dev']/stdev
    top_Five = process_df.nlargest(5,['zscore'])
    low_Five = process_df.nsmallest(5,['zscore'])
    top_States= [i.split('_')[0] for i in list(top_Five['STATE_DISTRICT'])]
    top_Districts=[i.split('_')[1] for i in list(top_Five['STATE_DISTRICT'])]
    top_Total_Crimes=top_Five['Total_Crimes']
    low_States= [i.split('_')[0] for i in list(low_Five['STATE_DISTRICT'])]
    low_Districts= [i.split('_')[1] for i in list(low_Five['STATE_DISTRICT'])]
    low_Total_Crimes= low_Five['Total_Crimes']
    data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/Women/Per Year/Districts/top_Five_Districts_Women_Year'+str(yr)+'.csv',index=0)
    data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/Women/Per Year/Districts/low_Five_Districts_Women_Year'+str(yr)+'.csv',index=0)


# # # Top/Last Five States per year for all crimes combined[zscore considered]

# In[20]:


year = range(2001,2011)
ls_Top = []
ls_Last = []
for yr in year:
    top_States = []
    top_Total_Crimes = []
    low_States = []
    low_Total_Crimes = []
    process_df = process_Census_Women[process_Census_Women.Year == yr]
    process_df = pd.DataFrame(process_df.groupby('STATE').sum().Total_Crimes)
    process_df = process_df[process_df['Total_Crimes'] !=0]
    process_df.reset_index()
    mean = process_df['Total_Crimes'].mean()
    stdev = process_df['Total_Crimes'].std()
    process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
    process_df['zscore'] = process_df['Crimes_Dev']/stdev
    top_Five = process_df.nlargest(5,['zscore'])
    low_Five = process_df.nsmallest(5,['zscore'])
    top_Five=top_Five.reset_index()
    low_Five=low_Five.reset_index()
    top_States= [i for i in list(top_Five['STATE'])]
    top_Districts=[i for i in list(top_Five['STATE'])]
    top_Total_Crimes=top_Five['Total_Crimes']
    low_States= [i for i in list(low_Five['STATE'])]
    low_Districts= [i for i in list(low_Five['STATE'])]
    low_Total_Crimes= low_Five['Total_Crimes']
    data = {'States':top_States,'Total Crimes':top_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/Women/Per Year/States/top_Five_States_Women_Year'+str(yr)+'.csv',index=0)
    data = {'States':low_States,'Total Crimes':low_Total_Crimes}
    df= pd.DataFrame(data, columns=['States','Total Crimes'])
    df.to_csv(cwd+'/Finding_Extremum/Women/Per Year/States/low_Five_States_Women_Year'+str(yr)+'.csv',index=0)


# # # Top/Last 5 Districts for crimes against Women for the period(2001-2010) [census state population considered]

# In[21]:


top_States = []
top_Districts = []
top_Total_Crimes = []
low_States = []
low_Districts = []
low_Total_Crimes = []
process_df = pd.DataFrame(process_Census_Women.groupby(['STATE_DISTRICT']).agg({'Female':"sum",'Total_Crimes':"sum"}))
process_df = process_df[process_df['Total_Crimes'] !=0]

mean = process_df['Total_Crimes'].mean()
stdev = process_df['Total_Crimes'].std()
process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
process_df['zscore'] = process_df['Crimes_Dev']/stdev
process_df['Normalised_By_Population'] = process_df['Crimes_Dev']/process_df['Female']

top_Five_Population = process_df.nlargest(5,['Normalised_By_Population'])
low_Five_Population = process_df[process_df['Normalised_By_Population']<0].nlargest(5,['Normalised_By_Population'])
top_Five_Zscore = process_df.nlargest(5,['zscore'])
low_Five_Zscore = process_df.nsmallest(5,['zscore'])
                                       
top_Five_Population=top_Five_Population.reset_index()
low_Five_Population=low_Five_Population.reset_index()                                       
top_Five_Zscore=top_Five_Zscore.reset_index()
low_Five_Zscore=low_Five_Zscore.reset_index()
                                       
top_States= [i.split('_')[0] for i in list(top_Five_Population['STATE_DISTRICT'])]
top_Districts= [i.split('_')[1] for i in list(top_Five_Population['STATE_DISTRICT'])]
top_Total_Crimes= top_Five_Population['Total_Crimes']
low_States= [i.split('_')[0] for i in list(low_Five_Population['STATE_DISTRICT'])]
low_Districts= [i.split('_')[1] for i in list(low_Five_Population['STATE_DISTRICT'])]
low_Total_Crimes= low_Five_Population['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Women/Overall/Districts/top_Five_Districts_Overall_Women_Population.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Women/Overall/Districts/low_Five_Districts_Overall_Women_Population.csv',index=0)

top_States= [i.split('_')[0] for i in list(top_Five_Zscore['STATE_DISTRICT'])]
top_Districts= [i.split('_')[1] for i in list(top_Five_Zscore['STATE_DISTRICT'])]
top_Total_Crimes= top_Five_Zscore['Total_Crimes']
low_States= [i.split('_')[0] for i in list(low_Five_Zscore['STATE_DISTRICT'])]
low_Districts= [i.split('_')[1] for i in list(low_Five_Zscore['STATE_DISTRICT'])]
low_Total_Crimes= low_Five_Zscore['Total_Crimes']
                                       
data = {'States':top_States,'Districts':top_Districts,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Women/Overall/Districts/top_Five_Districts_Overall_Women_zscore.csv',index=0)
data = {'States':low_States,'Districts':low_Districts,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Districts','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Women/Overall/Districts/low_Five_Districts_Overall_Women_zscore.csv',index=0)


# # # Top/Last 5 States for crimes against Women for the period(2001-2010) [census state population considered]

# In[22]:


top_States = []
top_Total_Crimes = []
low_States = []
low_Total_Crimes = []
process_df = pd.DataFrame(process_Census_Women.groupby(['STATE']).agg({'Female':"sum",'Total_Crimes':"sum"}))
process_df = process_df[process_df['Total_Crimes'] !=0]

mean = process_df['Total_Crimes'].mean()
stdev = process_df['Total_Crimes'].std()
process_df['Crimes_Dev'] = process_df['Total_Crimes'] - mean
process_df['Normalised_By_Population'] = process_df['Crimes_Dev']/process_df['Female']
process_df['zscore'] = process_df['Crimes_Dev']/stdev

top_Five_Population = process_df.nlargest(5,['Normalised_By_Population'])
low_Five_Population = process_df[process_df['Normalised_By_Population']<0].nlargest(5,['Normalised_By_Population'])
top_Five_Zscore = process_df.nlargest(5,['zscore'])
low_Five_Zscore = process_df.nsmallest(5,['zscore'])
                                       
top_Five_Population=top_Five_Population.reset_index()
low_Five_Population=low_Five_Population.reset_index()                                       
top_Five_Zscore=top_Five_Zscore.reset_index()
low_Five_Zscore=low_Five_Zscore.reset_index()
                                       
top_States= [i for i in list(top_Five_Population['STATE'])]
top_Total_Crimes= top_Five_Population['Total_Crimes']
low_States= [i for i in list(low_Five_Population['STATE'])]
low_Total_Crimes= low_Five_Population['Total_Crimes']
                                       
data = {'States':top_States,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Women/Overall/States/top_Five_States_Overall_Women_Population.csv',index=0)
data = {'States':low_States,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Women/Overall/States/low_Five_States_Overall_Women_Population.csv',index=0)

top_States= [i for i in list(top_Five_Zscore['STATE'])]
top_Total_Crimes= top_Five_Zscore['Total_Crimes']
low_States= [i for i in list(low_Five_Zscore['STATE'])]
low_Total_Crimes= low_Five_Zscore['Total_Crimes']
                                       
data = {'States':top_States,'Total Crimes':top_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Women/Overall/States/top_Five_States_Overall_Women_zscore.csv',index=0)
data = {'States':low_States,'Total Crimes':low_Total_Crimes}
df= pd.DataFrame(data, columns=['States','Total Crimes'])
df.to_csv(cwd+'/Finding_Extremum/Women/Overall/States/low_Five_States_Overall_Women_zscore.csv',index=0)

