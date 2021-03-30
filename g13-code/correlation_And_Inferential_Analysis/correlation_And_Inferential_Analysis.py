#!/usr/bin/env python
# coding: utf-8

# In[852]:


import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
cwd = os.getcwd()


df_census = pd.read_csv(cwd+"/Preprocessing/clean_Census_Data.csv")
df_children = pd.read_csv(cwd+"/Preprocessing/clean_Children_Data.csv")
df_sc = pd.read_csv(cwd+"/Preprocessing/clean_SC_Data.csv")
df_st = pd.read_csv(cwd+"/Preprocessing/clean_ST_Data.csv")
df_women = pd.read_csv(cwd+"/Preprocessing/clean_Women_Data.csv")

census_df = pd.read_csv(cwd+"/Preprocessing/clean_Census_Data.csv")

top_SC_Districts_Population = pd.read_csv(cwd+"/Finding_Extremum/SC/Overall/Districts/top_Five_Districts_Overall_SC_Population.csv")
top_SC_States_Population = pd.read_csv(cwd+"/Finding_Extremum/SC/Overall/States/top_Five_States_Overall_SC_Population.csv")
low_SC_Districts_Population = pd.read_csv(cwd+"/Finding_Extremum/SC/Overall/Districts/low_Five_Districts_Overall_SC_Population.csv")
low_SC_States_Population = pd.read_csv(cwd+"/Finding_Extremum/SC/Overall/States/low_Five_States_Overall_SC_Population.csv")

top_ST_Districts_Population = pd.read_csv(cwd+"/Finding_Extremum/ST/Overall/Districts/top_Five_Districts_Overall_ST_Population.csv")
top_ST_States_Population = pd.read_csv(cwd+"/Finding_Extremum/ST/Overall/States/top_Five_States_Overall_ST_Population.csv")
low_ST_Districts_Population = pd.read_csv(cwd+"/Finding_Extremum/ST/Overall/Districts/low_Five_Districts_Overall_ST_Population.csv")
low_ST_States_Population = pd.read_csv(cwd+"/Finding_Extremum/ST/Overall/States/low_Five_States_Overall_ST_Population.csv")

top_Children_Districts_Population = pd.read_csv(cwd+"/Finding_Extremum/Children/Overall/Districts/top_Five_Districts_Overall_Children_Population.csv")
top_Children_States_Population = pd.read_csv(cwd+"/Finding_Extremum/Children/Overall/States/top_Five_States_Overall_Children_Population.csv")
low_Children_Districts_Population = pd.read_csv(cwd+"/Finding_Extremum/Children/Overall/Districts/low_Five_Districts_Overall_Children_Population.csv")
low_Children_States_Population = pd.read_csv(cwd+"/Finding_Extremum/Children/Overall/States/low_Five_States_Overall_Children_Population.csv")

top_Women_Districts_Population = pd.read_csv(cwd+"/Finding_Extremum/Women/Overall/Districts/top_Five_Districts_Overall_Women_Population.csv")
top_Women_States_Population = pd.read_csv(cwd+"/Finding_Extremum/Women/Overall/States/top_Five_States_Overall_Women_Population.csv")
low_Women_Districts_Population = pd.read_csv(cwd+"/Finding_Extremum/Women/Overall/Districts/low_Five_Districts_Overall_Women_Population.csv")
low_Women_States_Population = pd.read_csv(cwd+"/Finding_Extremum/Women/Overall/States/low_Five_States_Overall_Women_Population.csv")

#Contribution of subcategory
df_children_subcategory = pd.read_csv(cwd+"/Contribution_Of_Subcategory/Contribution_Children.csv")
df_sc_subcategory = pd.read_csv(cwd+"/Contribution_Of_Subcategory/Contribution_SC.csv")
df_st_subcategory = pd.read_csv(cwd+"/Contribution_Of_Subcategory/Contribution_ST.csv")
df_women_subcategory = pd.read_csv(cwd+"/Contribution_Of_Subcategory/Contribution_Women.csv")


census_dist_list = list(df_census['STATE_DISTRICT'])

children = df_children.loc[df_children['STATE_DISTRICT'].isin(census_dist_list)].copy()
sc = df_sc.loc[df_sc['STATE_DISTRICT'].isin(census_dist_list)].copy()
st = df_st.loc[df_st['STATE_DISTRICT'].isin(census_dist_list)].copy()
women = df_women.loc[df_women['STATE_DISTRICT'].isin(census_dist_list)].copy()


for col in children.columns:
    if col == 'STATE_DISTRICT' or col == 'Year' :
        continue
    children.rename({col : 'children|'+col}, axis=1, inplace=True)
for col in sc.columns:
    if col == 'STATE_DISTRICT' or col == 'Year' :
        continue
    sc.rename({col : 'sc|'+col}, axis=1, inplace=True)
for col in st.columns:
    if col == 'STATE_DISTRICT' or col == 'Year' :
        continue
    st.rename({col : 'st|'+col}, axis=1, inplace=True)
for col in women.columns:
    if col == 'STATE_DISTRICT' or col == 'Year' :
        continue
    women.rename({col : 'women|'+col}, axis=1, inplace=True)

df_merged = pd.merge(children, sc, on=['STATE_DISTRICT', 'Year'])
df_merged = pd.merge(df_merged, st, on=['STATE_DISTRICT', 'Year'])
df_merged = pd.merge(df_merged, women, on=['STATE_DISTRICT', 'Year'])
commondistricts=list(df_census['STATE_DISTRICT'].unique())
mask=df_merged['STATE_DISTRICT'].isin(commondistricts)
newdf_merged=df_merged[mask]
newdf_merged=newdf_merged.groupby(["STATE_DISTRICT"]).sum().reset_index()
newdf_merged
df_census.drop(columns=['STATE_DISTRICT'],inplace=True)
newdf_merged.drop(columns=['STATE_DISTRICT', 'Year'], inplace=True)
result = pd.concat([newdf_merged, df_census], axis=1).corr()
column1=newdf_merged.columns.tolist()
column2=df_census.columns.tolist()
corr_df=result[column2].loc[column1]
corr_df


# In[853]:


corr_df.dropna(how = 'all', inplace=True)
corr_df.dropna(axis='columns',inplace=True)


# # Inferential Analysis

# In[854]:


ls_Children = [x for x in corr_df.index if x.startswith('children')] 
ls_SC = [x for x in corr_df.index if x.startswith('sc')] 
ls_ST = [x for x in corr_df.index if x.startswith('st')] 
ls_Women = [x for x in corr_df.index if x.startswith('women')] 


# In[855]:


#df_sc_subcategory.head()
ls_SC_Inference = ['sc|'+str(i) for i in df_sc_subcategory['Types'].tolist()]
ls_ST_Inference = ['st|'+str(i) for i in df_st_subcategory['Types'].tolist()]
ls_Children_Inference = ['children|'+str(i) for i in df_children_subcategory['Types'].tolist()]
ls_Women_Inference = ['women|'+str(i) for i in df_women_subcategory['Types'].tolist()]


# # SC

# In[856]:


temp_df = corr_df.loc[ls_SC_Inference]
temp_df.drop('Age not stated', axis = 1, inplace=True)

k = 5
vals = temp_df.values
arr1 = np.argsort(-vals, axis=1)

a = temp_df.columns[arr1[:,:k]]
b = vals[np.arange(len(temp_df.index))[:,None], arr1][:,:k]

c = np.empty((vals.shape[0], 2 * k), dtype=a.dtype)
c[:,0::2] = a
c[:,1::2] = b
top_Indices = pd.DataFrame(c)
top_Indices = top_Indices.set_index([ls_SC_Inference])
top_Indices


# In[857]:


ls_New_Col = ['Murder', 'Rape', 'Kidnapping','Dacoity', 'Robbery','Arson','Hurt','POA','PCR','Other Crimes','Total Crimes']
temp_df = corr_df.loc[ls_SC]
for index in ls_SC:
    top_Indices = pd.DataFrame({n: temp_df.T[column].nlargest(4).index.tolist() for n, column in enumerate(temp_df.T)}).T
plt.subplots(figsize=(20,9))
a = top_Indices.values
b = list(set(a.ravel()))
sample = corr_df.loc[ls_SC,b]
sample.set_index([ls_New_Col], inplace=True)
sample.drop('Age not stated', axis = 1, inplace=True)

#sample.set_axis(ls_New_Col, axis=1, inplace=True)

ax = sns.heatmap(sample.T, annot=True, fmt='.2f', cmap='RdYlGn', annot_kws={'size':15})
sns.set(font_scale=1.2)
#ax.figure.tight_layout()
ax.set_title('Heatmap of Crime against SC with Census Data')
plt.tight_layout()
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_SC.eps", dpi=600)


# # SC Plots Top/Low Districts

# In[858]:


temp_Sample = pd.DataFrame(sample.loc['Total Crimes'])
temp_Sample.reset_index()
plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0.45].index.tolist()
#plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0].index.tolist()
plot_From_Census = plot_From_Census+['STATE_DISTRICT']
normalise_Columns_Census = ['Having_latrine_facility_within_the_premises_Total_Households', 'Workers', 'Literate_Education','Having_bathing_facility_Total_Households','Total_Education']
get_Columns_Census = plot_From_Census+normalise_Columns_Census


# In[859]:


#top_Population
#Districts

top_SC_Districts_Population['STATE_DISTRICT'] = top_SC_Districts_Population['States']+'_'+top_SC_Districts_Population['Districts']
state_district = list(top_SC_Districts_Population['STATE_DISTRICT'])
temp_Census = census_df[census_df['STATE_DISTRICT'].isin(state_district)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'] = (temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']/(temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']+temp_Census['Having_latrine_facility_within_the_premises_Total_Households']))*100
temp_Census['Cultivator_Workers'] = (temp_Census['Cultivator_Workers']/temp_Census['Workers'])*100
temp_Census['Below_Primary_Education'] = (temp_Census['Below_Primary_Education']/temp_Census['Literate_Education'])*100
temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households'] = (temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households']/temp_Census['Having_bathing_facility_Total_Households'])*100
temp_Census['Illiterate_Education'] = (temp_Census['Illiterate_Education']/temp_Census['Total_Education'])*100
temp_Census = temp_Census[plot_From_Census]
Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households = list(temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'])
Cultivator_Workers = list(temp_Census['Cultivator_Workers'])
Below_Primary_Education = list(temp_Census['Below_Primary_Education'])
Type_of_bathing_facility_Enclosure_without_roof_Households = list(temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households'])
Illiterate_Education = list(temp_Census['Illiterate_Education'])
index = list(temp_Census['STATE_DISTRICT'])
df = pd.DataFrame({'No latrine facility within the premises':Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households,
                  'Cultivator Workers':Cultivator_Workers,'Below Primary Education':Below_Primary_Education,
                 'Bathing facility Enclosure without roof':Type_of_bathing_facility_Enclosure_without_roof_Households,
                 'Illiterate':Illiterate_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Top Districts for Crimes against SCs', fontsize=12)
ax.set_xlabel("State-District")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Top_Districts_Population_SC.eps", dpi=600)         


# In[860]:


#top_Population
#States

census_df['STATE'] = [i.split('_')[0] for i in list(census_df['STATE_DISTRICT'])]
col_Census = list(census_df.columns)
col_Census.remove('STATE_DISTRICT')
temp_Census_df = census_df.groupby(['STATE'])[col_Census].sum()
temp_Census_df=temp_Census_df.reset_index()
plot_From_Census.remove('STATE_DISTRICT')
plot_From_Census = plot_From_Census + ['STATE']
get_Columns_Census.remove('STATE_DISTRICT')
get_Columns_Census = get_Columns_Census + ['STATE']
state = list(top_SC_States_Population['States'])
temp_Census = temp_Census_df[temp_Census_df['STATE'].isin(state)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'] = (temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']/(temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']+temp_Census['Having_latrine_facility_within_the_premises_Total_Households']))*100
temp_Census['Cultivator_Workers'] = (temp_Census['Cultivator_Workers']/temp_Census['Workers'])*100
temp_Census['Below_Primary_Education'] = (temp_Census['Below_Primary_Education']/temp_Census['Literate_Education'])*100
temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households'] = (temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households']/temp_Census['Having_bathing_facility_Total_Households'])*100
temp_Census['Illiterate_Education'] = (temp_Census['Illiterate_Education']/temp_Census['Total_Education'])*100
temp_Census = temp_Census[plot_From_Census]
Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households = list(temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'])
Cultivator_Workers = list(temp_Census['Cultivator_Workers'])
Below_Primary_Education = list(temp_Census['Below_Primary_Education'])
Type_of_bathing_facility_Enclosure_without_roof_Households = list(temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households'])
Illiterate_Education = list(temp_Census['Illiterate_Education'])
index = list(temp_Census['STATE'])
df = pd.DataFrame({'No latrine facility within the premises':Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households,
                  'Cultivator Workers':Cultivator_Workers,'Below Primary Education':Below_Primary_Education,
                 'Bathing facility Enclosure without roof':Type_of_bathing_facility_Enclosure_without_roof_Households,
                 'Illiterate':Illiterate_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Top States for Crimes against SCs', fontsize=12)
ax.set_xlabel("State")
ax.set_ylabel("Percentage")
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Top_States_Population_SC.eps", dpi=600)         


# In[861]:


temp_Sample = pd.DataFrame(sample.loc['Total Crimes'])
temp_Sample.reset_index()
plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0.45].index.tolist()
plot_From_Census = plot_From_Census+['STATE_DISTRICT']
normalise_Columns_Census = ['Having_latrine_facility_within_the_premises_Total_Households', 'Workers', 'Literate_Education','Having_bathing_facility_Total_Households','Total_Education']
get_Columns_Census = plot_From_Census+normalise_Columns_Census


#low_Population
#Districts

low_SC_Districts_Population['STATE_DISTRICT'] = low_SC_Districts_Population['States']+'_'+low_SC_Districts_Population['Districts']
state_district = list(low_SC_Districts_Population['STATE_DISTRICT'])
temp_Census = census_df[census_df['STATE_DISTRICT'].isin(state_district)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'] = (temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']/(temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']+temp_Census['Having_latrine_facility_within_the_premises_Total_Households']))*100
temp_Census['Cultivator_Workers'] = (temp_Census['Cultivator_Workers']/temp_Census['Workers'])*100
temp_Census['Below_Primary_Education'] = (temp_Census['Below_Primary_Education']/temp_Census['Literate_Education'])*100
temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households'] = (temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households']/temp_Census['Having_bathing_facility_Total_Households'])*100
temp_Census['Illiterate_Education'] = (temp_Census['Illiterate_Education']/temp_Census['Total_Education'])*100
temp_Census = temp_Census[plot_From_Census]
Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households = list(temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'])
Cultivator_Workers = list(temp_Census['Cultivator_Workers'])
Below_Primary_Education = list(temp_Census['Below_Primary_Education'])
Type_of_bathing_facility_Enclosure_without_roof_Households = list(temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households'])
Illiterate_Education = list(temp_Census['Illiterate_Education'])
index = list(temp_Census['STATE_DISTRICT'])
df = pd.DataFrame({'No latrine facility within the premises':Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households,
                  'Cultivator Workers':Cultivator_Workers,'Below Primary Education':Below_Primary_Education,
                 'Bathing facility Enclosure without roof':Type_of_bathing_facility_Enclosure_without_roof_Households,
                 'Illiterate':Illiterate_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Low Districts for Crimes against SCs', fontsize=12)
ax.set_xlabel("State-District")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Low_Districts_Population_SC.eps", dpi=600)     


# In[862]:


#low_Population
#States

census_df['STATE'] = [i.split('_')[0] for i in list(census_df['STATE_DISTRICT'])]
col_Census = list(census_df.columns)
col_Census.remove('STATE_DISTRICT')
temp_Census_df = census_df.groupby(['STATE'])[col_Census].sum()
temp_Census_df=temp_Census_df.reset_index()
plot_From_Census.remove('STATE_DISTRICT')
plot_From_Census = plot_From_Census + ['STATE']
get_Columns_Census.remove('STATE_DISTRICT')
get_Columns_Census = get_Columns_Census + ['STATE']
state = list(low_SC_States_Population['States'])
temp_Census = temp_Census_df[temp_Census_df['STATE'].isin(state)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'] = (temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']/(temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']+temp_Census['Having_latrine_facility_within_the_premises_Total_Households']))*100
temp_Census['Cultivator_Workers'] = (temp_Census['Cultivator_Workers']/temp_Census['Workers'])*100
temp_Census['Below_Primary_Education'] = (temp_Census['Below_Primary_Education']/temp_Census['Literate_Education'])*100
temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households'] = (temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households']/temp_Census['Having_bathing_facility_Total_Households'])*100
temp_Census['Illiterate_Education'] = (temp_Census['Illiterate_Education']/temp_Census['Total_Education'])*100
temp_Census = temp_Census[plot_From_Census]
Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households = list(temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households'])
Cultivator_Workers = list(temp_Census['Cultivator_Workers'])
Below_Primary_Education = list(temp_Census['Below_Primary_Education'])
Type_of_bathing_facility_Enclosure_without_roof_Households = list(temp_Census['Type_of_bathing_facility_Enclosure_without_roof_Households'])
Illiterate_Education = list(temp_Census['Illiterate_Education'])
index = list(temp_Census['STATE'])
df = pd.DataFrame({'No latrine facility within the premises':Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households,
                  'Cultivator Workers':Cultivator_Workers,'Below Primary Education':Below_Primary_Education,
                 'Bathing facility Enclosure without roof':Type_of_bathing_facility_Enclosure_without_roof_Households,
                 'Illiterate':Illiterate_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Low States for Crimes against SCs', fontsize=12)
ax.set_xlabel("State")
ax.set_ylabel("Percentage")
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Low_States_Population_SC.eps", dpi=600)    


# # ST

# In[863]:


temp_df = corr_df.loc[ls_ST_Inference]
#temp_df.dropna(inplace=True)
k = 10
vals = temp_df.values
arr1 = np.argsort(-vals, axis=1)

a = temp_df.columns[arr1[:,:k]]
b = vals[np.arange(len(temp_df.index))[:,None], arr1][:,:k]

c = np.empty((vals.shape[0], 2 * k), dtype=a.dtype)
c[:,0::2] = a
c[:,1::2] = b
top_Indices = pd.DataFrame(c)
top_Indices = top_Indices.set_index([ls_ST_Inference])
top_Indices


# In[864]:


ls_New_Col = ['Murder', 'Rape', 'Dacoity', 'Robbery','Arson','Hurt','POA','PCR','Other Crimes','Total Crimes']
temp_df = corr_df.loc[ls_ST]
for index in ls_ST:
    top_Indices = pd.DataFrame({n: temp_df.T[column].nlargest(4).index.tolist() for n, column in enumerate(temp_df.T)}).T
plt.subplots(figsize=(20,9))
a = top_Indices.values
b = list(set(a.ravel()))
sample = corr_df.loc[ls_ST,b]
sample.set_index([ls_New_Col], inplace=True)
ax.figure.tight_layout()
ax = sns.heatmap(sample.T, annot=True, fmt='.2f', cmap='RdYlGn', annot_kws={'size':15})
sns.set(font_scale=1.2)
ax.set_title('Heatmap of Crime against ST with Census Data')
plt.tight_layout()
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_ST.eps", dpi=600)


# # ST Plots Top/Low Districts

# In[865]:


temp_Sample = pd.DataFrame(sample.loc['Total Crimes'])
temp_Sample.reset_index()
plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0.30].index.tolist()
#plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0].index.tolist()
plot_From_Census = plot_From_Census+['STATE_DISTRICT']
normalise_Columns_Census = ['Population', 'Workers', 'Location_of_drinking_water_source_Within_the_premises_Households','Location_of_drinking_water_source_Near_the_premises_Households']
get_Columns_Census = plot_From_Census+normalise_Columns_Census
top_ST_Districts_Population


# In[866]:


#top_Population
#Districts

top_ST_Districts_Population['STATE_DISTRICT'] = top_ST_Districts_Population['States']+'_'+top_ST_Districts_Population['Districts']
state_district = list(top_ST_Districts_Population['STATE_DISTRICT'])
temp_Census = census_df[census_df['STATE_DISTRICT'].isin(state_district)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Female_ST'] = (temp_Census['Female_ST']/(temp_Census['ST']))*100
temp_Census['Male_ST'] = (temp_Census['Male_ST']/temp_Census['ST'])*100
temp_Census['ST'] = (temp_Census['ST']/temp_Census['Population'])*100
temp_Census['Female_Workers'] = (temp_Census['Female_Workers']/temp_Census['Workers'])*100
temp_Census['Location_of_drinking_water_source_Away_Households'] = (temp_Census['Location_of_drinking_water_source_Away_Households']/(temp_Census['Location_of_drinking_water_source_Within_the_premises_Households']+temp_Census['Location_of_drinking_water_source_Away_Households']+temp_Census['Location_of_drinking_water_source_Near_the_premises_Households']))*100
temp_Census = temp_Census[plot_From_Census]
Female_ST = list(temp_Census['Female_ST'])
ST = list(temp_Census['ST'])
Male_ST = list(temp_Census['Male_ST'])
Female_Workers = list(temp_Census['Female_Workers'])
Location_of_drinking_water_source_Away_Households = list(temp_Census['Location_of_drinking_water_source_Away_Households'])
index = list(temp_Census['STATE_DISTRICT'])
df = pd.DataFrame({'Female Population(ST)':Female_ST,
                   'Population(ST)':ST,
                   'Male Population(ST)':Male_ST,
                   'Female Workers':Female_Workers,
                   'Drinking water source away from home':Location_of_drinking_water_source_Away_Households}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Top Districts for Crimes against STs', fontsize=12)
ax.set_xlabel("State-District")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Top_Districts_Population_ST.eps", dpi=600)         


# In[867]:


#top_Population
#States

census_df['STATE'] = [i.split('_')[0] for i in list(census_df['STATE_DISTRICT'])]
col_Census = list(census_df.columns)
col_Census.remove('STATE_DISTRICT')
temp_Census_df = census_df.groupby(['STATE'])[col_Census].sum()
temp_Census_df=temp_Census_df.reset_index()
plot_From_Census.remove('STATE_DISTRICT')
plot_From_Census = plot_From_Census + ['STATE']
get_Columns_Census.remove('STATE_DISTRICT')
get_Columns_Census = get_Columns_Census + ['STATE']
state = list(top_ST_States_Population['States'])
temp_Census = temp_Census_df[temp_Census_df['STATE'].isin(state)]
temp_Census = temp_Census[get_Columns_Census]

temp_Census['Female_ST'] = (temp_Census['Female_ST']/(temp_Census['ST']))*100
temp_Census['Male_ST'] = (temp_Census['Male_ST']/temp_Census['ST'])*100
temp_Census['ST'] = (temp_Census['ST']/temp_Census['Population'])*100
temp_Census['Female_Workers'] = (temp_Census['Female_Workers']/temp_Census['Workers'])*100
temp_Census['Location_of_drinking_water_source_Away_Households'] = (temp_Census['Location_of_drinking_water_source_Away_Households']/(temp_Census['Location_of_drinking_water_source_Within_the_premises_Households']+temp_Census['Location_of_drinking_water_source_Away_Households']+temp_Census['Location_of_drinking_water_source_Near_the_premises_Households']))*100
temp_Census = temp_Census[plot_From_Census]
Female_ST = list(temp_Census['Female_ST'])
ST = list(temp_Census['ST'])
Male_ST = list(temp_Census['Male_ST'])
Female_Workers = list(temp_Census['Female_Workers'])
Location_of_drinking_water_source_Away_Households = list(temp_Census['Location_of_drinking_water_source_Away_Households'])

index = list(temp_Census['STATE'])

df = pd.DataFrame({'Female Population(ST)':Female_ST,
                   'Population(ST)':ST,
                   'Male Population(ST)':Male_ST,
                   'Female Workers':Female_Workers,
                   'Drinking water source away from home':Location_of_drinking_water_source_Away_Households}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Top States for Crimes against STs', fontsize=12)
ax.set_xlabel("State")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Top_States_Population_ST.eps", dpi=600)         


# In[868]:


#low_Population
#Districts

temp_Sample = pd.DataFrame(sample.loc['Total Crimes'])
temp_Sample.reset_index()
plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0.30].index.tolist()
#plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0].index.tolist()
plot_From_Census = plot_From_Census+['STATE_DISTRICT']
normalise_Columns_Census = ['Population', 'Workers', 'Location_of_drinking_water_source_Within_the_premises_Households','Location_of_drinking_water_source_Near_the_premises_Households']
get_Columns_Census = plot_From_Census+normalise_Columns_Census
top_ST_Districts_Population

low_ST_Districts_Population['STATE_DISTRICT'] = low_ST_Districts_Population['States']+'_'+low_ST_Districts_Population['Districts']
state_district = list(low_ST_Districts_Population['STATE_DISTRICT'])
temp_Census = census_df[census_df['STATE_DISTRICT'].isin(state_district)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Female_ST'] = (temp_Census['Female_ST']/(temp_Census['ST']))*100
temp_Census['Male_ST'] = (temp_Census['Male_ST']/temp_Census['ST'])*100
temp_Census['ST'] = (temp_Census['ST']/temp_Census['Population'])*100
temp_Census['Female_Workers'] = (temp_Census['Female_Workers']/temp_Census['Workers'])*100
temp_Census['Location_of_drinking_water_source_Away_Households'] = (temp_Census['Location_of_drinking_water_source_Away_Households']/(temp_Census['Location_of_drinking_water_source_Within_the_premises_Households']+temp_Census['Location_of_drinking_water_source_Away_Households']+temp_Census['Location_of_drinking_water_source_Near_the_premises_Households']))*100
temp_Census = temp_Census[plot_From_Census]
Female_ST = list(temp_Census['Female_ST'])
ST = list(temp_Census['ST'])
Male_ST = list(temp_Census['Male_ST'])
Female_Workers = list(temp_Census['Female_Workers'])
Location_of_drinking_water_source_Away_Households = list(temp_Census['Location_of_drinking_water_source_Away_Households'])
index = list(temp_Census['STATE_DISTRICT'])
df = pd.DataFrame({'Female Population(ST)':Female_ST,
                   'Population(ST)':ST,
                   'Male Population(ST)':Male_ST,
                   'Female Workers':Female_Workers,
                   'Drinking water source away from home':Location_of_drinking_water_source_Away_Households}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Low Districts for Crimes against STs', fontsize=12)
ax.set_xlabel("State-District")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Low_Districts_Population_ST.eps", dpi=600)         


# In[869]:


#low_Population
#States

census_df['STATE'] = [i.split('_')[0] for i in list(census_df['STATE_DISTRICT'])]
col_Census = list(census_df.columns)
col_Census.remove('STATE_DISTRICT')
temp_Census_df = census_df.groupby(['STATE'])[col_Census].sum()
temp_Census_df=temp_Census_df.reset_index()
plot_From_Census.remove('STATE_DISTRICT')
plot_From_Census = plot_From_Census + ['STATE']
get_Columns_Census.remove('STATE_DISTRICT')
get_Columns_Census = get_Columns_Census + ['STATE']
state = list(low_ST_States_Population['States'])
temp_Census = temp_Census_df[temp_Census_df['STATE'].isin(state)]
temp_Census = temp_Census[get_Columns_Census]

temp_Census['Female_ST'] = (temp_Census['Female_ST']/(temp_Census['ST']))*100
temp_Census['Male_ST'] = (temp_Census['Male_ST']/temp_Census['ST'])*100
temp_Census['ST'] = (temp_Census['ST']/temp_Census['Population'])*100
temp_Census['Female_Workers'] = (temp_Census['Female_Workers']/temp_Census['Workers'])*100
temp_Census['Location_of_drinking_water_source_Away_Households'] = (temp_Census['Location_of_drinking_water_source_Away_Households']/(temp_Census['Location_of_drinking_water_source_Within_the_premises_Households']+temp_Census['Location_of_drinking_water_source_Away_Households']+temp_Census['Location_of_drinking_water_source_Near_the_premises_Households']))*100
temp_Census = temp_Census[plot_From_Census]
Female_ST = list(temp_Census['Female_ST'])
ST = list(temp_Census['ST'])
Male_ST = list(temp_Census['Male_ST'])
Female_Workers = list(temp_Census['Female_Workers'])
Location_of_drinking_water_source_Away_Households = list(temp_Census['Location_of_drinking_water_source_Away_Households'])

index = list(temp_Census['STATE'])

df = pd.DataFrame({'Female Population(ST)':Female_ST,
                   'Population(ST)':ST,
                   'Male Population(ST)':Male_ST,
                   'Female Workers':Female_Workers,
                   'Drinking water source away from home':Location_of_drinking_water_source_Away_Households}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Low States for Crimes against STs', fontsize=12)
ax.set_xlabel("States")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Low_States_Population_ST.eps", dpi=600)         


# # Children

# In[870]:


temp_df = corr_df.loc[ls_Children_Inference]
k = 5
vals = temp_df.values
arr1 = np.argsort(-vals, axis=1)

a = temp_df.columns[arr1[:,:k]]
b = vals[np.arange(len(temp_df.index))[:,None], arr1][:,:k]

c = np.empty((vals.shape[0], 2 * k), dtype=a.dtype)
c[:,0::2] = a
c[:,1::2] = b
top_Indices = pd.DataFrame(c)
top_Indices = top_Indices.set_index([ls_Children_Inference])
top_Indices


# In[871]:


ls_New_Col = ['Murder','Rape','Kidnapping','Foeticide','Abet to Suicide','Abandon','Procure minor girls','Buying Girls P','Selling Girls P','Child Marriage','Other Crimes','Total Crimes']
temp_df = corr_df.loc[ls_Children]
for index in ls_Children:
    top_Indices = pd.DataFrame({n: temp_df.T[column].nlargest(4).index.tolist() for n, column in enumerate(temp_df.T)}).T
plt.subplots(figsize=(20,9))
a = top_Indices.values
b = list(set(a.ravel()))
sample = corr_df.loc[ls_Children,b]
sample.set_index([ls_New_Col], inplace=True)
ax.figure.tight_layout()
ax = sns.heatmap(sample.T, annot=True, fmt='.2f', cmap='RdYlGn', annot_kws={'size':15})
sns.set(font_scale=1.2)
ax.set_title('Heatmap of Crime against Children with Census Data')
plt.tight_layout()
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Children.eps", dpi=600)


# # Children Plots Top/Low Districts

# In[872]:


temp_Sample = pd.DataFrame(sample.loc['Total Crimes'])
temp_Sample.reset_index()
plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0.65].index.tolist()
#plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0].index.tolist()
plot_From_Census = plot_From_Census+['STATE_DISTRICT']
normalise_Columns_Census = ['Households', 'Literate_Education']
get_Columns_Census = plot_From_Census+normalise_Columns_Census
plot_From_Census     


# In[873]:


#top_Population
#Districts

top_Children_Districts_Population['STATE_DISTRICT'] = top_Children_Districts_Population['States']+'_'+top_Children_Districts_Population['Districts']
state_district = list(top_Children_Districts_Population['STATE_DISTRICT'])
temp_Census = census_df[census_df['STATE_DISTRICT'].isin(state_district)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Households_with_Internet'] = (temp_Census['Households_with_Internet']/(temp_Census['Households']))*100
temp_Census['LPG_or_PNG_Households'] = (temp_Census['LPG_or_PNG_Households']/temp_Census['Households'])*100
temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'] = (temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car']/temp_Census['Households'])*100
temp_Census['Households_with_Car_Jeep_Van'] = (temp_Census['Households_with_Car_Jeep_Van']/temp_Census['Households'])*100
temp_Census['Higher_Education'] = (temp_Census['Higher_Education']/(temp_Census['Literate_Education']))*100
temp_Census = temp_Census[plot_From_Census]
Households_with_Internet = list(temp_Census['Households_with_Internet'])
LPG_or_PNG_Households = list(temp_Census['LPG_or_PNG_Households'])
Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car = list(temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'])
Households_with_Car_Jeep_Van = list(temp_Census['Households_with_Car_Jeep_Van'])
Higher_Education = list(temp_Census['Higher_Education'])
index = list(temp_Census['STATE_DISTRICT'])
df = pd.DataFrame({'Households with Internet':Households_with_Internet,
                   'Households with LPG or PNG':LPG_or_PNG_Households,
                   'Households with TV, Computer, Laptop, Telephone, mobile, Scooter and Car':Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car,
                   'Households with Car, Jeep and Van':Households_with_Car_Jeep_Van,
                   'Higher Education':Higher_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Top Districts for Crimes against Children', fontsize=12)
ax.set_xlabel("State-District")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Top_Districts_Population_Children.eps", dpi=600) 


# In[874]:


#top_Population
#States

census_df['STATE'] = [i.split('_')[0] for i in list(census_df['STATE_DISTRICT'])]
col_Census = list(census_df.columns)
col_Census.remove('STATE_DISTRICT')
temp_Census_df = census_df.groupby(['STATE'])[col_Census].sum()
temp_Census_df=temp_Census_df.reset_index()
plot_From_Census.remove('STATE_DISTRICT')
plot_From_Census = plot_From_Census + ['STATE']
get_Columns_Census.remove('STATE_DISTRICT')
get_Columns_Census = get_Columns_Census + ['STATE']
state = list(top_Children_States_Population['States'])
temp_Census = temp_Census_df[temp_Census_df['STATE'].isin(state)]
temp_Census = temp_Census[get_Columns_Census]

temp_Census['Households_with_Internet'] = (temp_Census['Households_with_Internet']/(temp_Census['Households']))*100
temp_Census['LPG_or_PNG_Households'] = (temp_Census['LPG_or_PNG_Households']/temp_Census['Households'])*100
temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'] = (temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car']/temp_Census['Households'])*100
temp_Census['Households_with_Car_Jeep_Van'] = (temp_Census['Households_with_Car_Jeep_Van']/temp_Census['Households'])*100
temp_Census['Higher_Education'] = (temp_Census['Higher_Education']/(temp_Census['Literate_Education']))*100
temp_Census = temp_Census[plot_From_Census]
Households_with_Internet = list(temp_Census['Households_with_Internet'])
LPG_or_PNG_Households = list(temp_Census['LPG_or_PNG_Households'])
Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car = list(temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'])
Households_with_Car_Jeep_Van = list(temp_Census['Households_with_Car_Jeep_Van'])
Higher_Education = list(temp_Census['Higher_Education'])
index = list(temp_Census['STATE'])
df = pd.DataFrame({'Households with Internet':Households_with_Internet,
                   'Households with LPG or PNG':LPG_or_PNG_Households,
                   'Households with TV, Computer, Laptop, Telephone, mobile, Scooter and Car':Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car,
                   'Households with Car, Jeep and Van':Households_with_Car_Jeep_Van,
                   'Higher Education':Higher_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Top States for Crimes against Children', fontsize=12)
ax.set_xlabel("State")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Top_States_Population_Children.eps", dpi=600) 


# In[875]:


temp_Sample = pd.DataFrame(sample.loc['Total Crimes'])
temp_Sample.reset_index()
plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0.65].index.tolist()
#plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0].index.tolist()
plot_From_Census = plot_From_Census+['STATE_DISTRICT']
normalise_Columns_Census = ['Households', 'Literate_Education']
get_Columns_Census = plot_From_Census+normalise_Columns_Census
plot_From_Census     

#low_Population
#Districts

low_Children_Districts_Population['STATE_DISTRICT'] = low_Children_Districts_Population['States']+'_'+low_Children_Districts_Population['Districts']
state_district = list(low_Children_Districts_Population['STATE_DISTRICT'])
temp_Census = census_df[census_df['STATE_DISTRICT'].isin(state_district)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Households_with_Internet'] = (temp_Census['Households_with_Internet']/(temp_Census['Households']))*100
temp_Census['LPG_or_PNG_Households'] = (temp_Census['LPG_or_PNG_Households']/temp_Census['Households'])*100
temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'] = (temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car']/temp_Census['Households'])*100
temp_Census['Households_with_Car_Jeep_Van'] = (temp_Census['Households_with_Car_Jeep_Van']/temp_Census['Households'])*100
temp_Census['Higher_Education'] = (temp_Census['Higher_Education']/(temp_Census['Literate_Education']))*100
temp_Census = temp_Census[plot_From_Census]
Households_with_Internet = list(temp_Census['Households_with_Internet'])
LPG_or_PNG_Households = list(temp_Census['LPG_or_PNG_Households'])
Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car = list(temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'])
Households_with_Car_Jeep_Van = list(temp_Census['Households_with_Car_Jeep_Van'])
Higher_Education = list(temp_Census['Higher_Education'])
index = list(temp_Census['STATE_DISTRICT'])
df = pd.DataFrame({'Households with Internet':Households_with_Internet,
                   'Households with LPG or PNG':LPG_or_PNG_Households,
                   'Households with TV, Computer, Laplow, Telephone, mobile, Scooter and Car':Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car,
                   'Households with Car, Jeep and Van':Households_with_Car_Jeep_Van,
                   'Higher Education':Higher_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Low Districts for Crimes against Children', fontsize=12)
ax.set_xlabel("State-District")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Low_Districts_Population_Children.eps", dpi=600) 


# In[876]:


#low_Population
#States

census_df['STATE'] = [i.split('_')[0] for i in list(census_df['STATE_DISTRICT'])]
col_Census = list(census_df.columns)
col_Census.remove('STATE_DISTRICT')
temp_Census_df = census_df.groupby(['STATE'])[col_Census].sum()
temp_Census_df=temp_Census_df.reset_index()
plot_From_Census.remove('STATE_DISTRICT')
plot_From_Census = plot_From_Census + ['STATE']
get_Columns_Census.remove('STATE_DISTRICT')
get_Columns_Census = get_Columns_Census + ['STATE']
state = list(low_Children_States_Population['States'])
temp_Census = temp_Census_df[temp_Census_df['STATE'].isin(state)]
temp_Census = temp_Census[get_Columns_Census]

temp_Census['Households_with_Internet'] = (temp_Census['Households_with_Internet']/(temp_Census['Households']))*100
temp_Census['LPG_or_PNG_Households'] = (temp_Census['LPG_or_PNG_Households']/temp_Census['Households'])*100
temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'] = (temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car']/temp_Census['Households'])*100
temp_Census['Households_with_Car_Jeep_Van'] = (temp_Census['Households_with_Car_Jeep_Van']/temp_Census['Households'])*100
temp_Census['Higher_Education'] = (temp_Census['Higher_Education']/(temp_Census['Literate_Education']))*100
temp_Census = temp_Census[plot_From_Census]
Households_with_Internet = list(temp_Census['Households_with_Internet'])
LPG_or_PNG_Households = list(temp_Census['LPG_or_PNG_Households'])
Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car = list(temp_Census['Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car'])
Households_with_Car_Jeep_Van = list(temp_Census['Households_with_Car_Jeep_Van'])
Higher_Education = list(temp_Census['Higher_Education'])
index = list(temp_Census['STATE'])
df = pd.DataFrame({'Households with Internet':Households_with_Internet,
                   'Households with LPG or PNG':LPG_or_PNG_Households,
                   'Households with TV, Computer, Laptop, Telephone, mobile, Scooter and Car':Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car,
                   'Households with Car, Jeep and Van':Households_with_Car_Jeep_Van,
                   'Higher Education':Higher_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Low States for Crimes against Children', fontsize=12)
ax.set_xlabel("State")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Low_States_Population_Children.eps", dpi=600) 


# # Women 

# In[877]:


temp_df = corr_df.loc[ls_Women_Inference]
k = 5
vals = temp_df.values
arr1 = np.argsort(-vals, axis=1)

a = temp_df.columns[arr1[:,:k]]
b = vals[np.arange(len(temp_df.index))[:,None], arr1][:,:k]

c = np.empty((vals.shape[0], 2 * k), dtype=a.dtype)
c[:,0::2] = a
c[:,1::2] = b
top_Indices = pd.DataFrame(c)
top_Indices = top_Indices.set_index([ls_Women_Inference])
top_Indices


# In[878]:


ls_New_Col = ['Total Crimes', 'Rape', 'Kidnapping', 'Dowry Deaths', 'Assault', 'Insult to modesty', 'Cruelty by Family', 'Importation']
temp_df = corr_df.loc[ls_Women]
for index in ls_Women:
    top_Indices = pd.DataFrame({n: temp_df.T[column].nlargest(4).index.tolist() for n, column in enumerate(temp_df.T)}).T
plt.subplots(figsize=(20,9))
a = top_Indices.values
b = list(set(a.ravel()))
sample = corr_df.loc[ls_Women,b]
sample.set_index([ls_New_Col], inplace=True)
ax.figure.tight_layout()
ax = sns.heatmap(sample.T, annot=True, fmt='.2f', cmap='RdYlGn', annot_kws={'size':15})
sns.set(font_scale=1.2)
ax.set_title('Heatmap of Crime against Women with Census Data')
plt.tight_layout()
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Women.eps", dpi=600)


# # Women Plots Top/Low Districts

# In[879]:


temp_Sample = pd.DataFrame(sample.loc['Total Crimes'])
temp_Sample.reset_index()
plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0.745].index.tolist()
#plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0].index.tolist()
plot_From_Census = plot_From_Census+['STATE_DISTRICT']
normalise_Columns_Census = ['Households', 'Population','Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households', 'Total_Power_Parity','Literate_Education']
get_Columns_Census = plot_From_Census+normalise_Columns_Census
plot_From_Census     


# In[880]:


#top_Population
#Districts

top_Women_Districts_Population['STATE_DISTRICT'] = top_Women_Districts_Population['States']+'_'+top_Women_Districts_Population['Districts']
state_district = list(top_Women_Districts_Population['STATE_DISTRICT'])
temp_Census = census_df[census_df['STATE_DISTRICT'].isin(state_district)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Household_size_5_persons_Households'] = (temp_Census['Household_size_5_persons_Households']/(temp_Census['Households']))*100
temp_Census['Literate'] = (temp_Census['Literate']/temp_Census['Population'])*100
temp_Census['Having_latrine_facility_within_the_premises_Total_Households'] = (temp_Census['Having_latrine_facility_within_the_premises_Total_Households']/(temp_Census['Having_latrine_facility_within_the_premises_Total_Households']+temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']))*100
temp_Census['Power_Parity_Rs_45000_90000'] = (temp_Census['Power_Parity_Rs_45000_90000']/temp_Census['Total_Power_Parity'])*100
temp_Census['Higher_Education'] = (temp_Census['Higher_Education']/(temp_Census['Literate_Education']))*100
temp_Census = temp_Census[plot_From_Census]
Household_size_5_persons_Households = list(temp_Census['Household_size_5_persons_Households'])
Literate = list(temp_Census['Literate'])
Having_latrine_facility_within_the_premises_Total_Households = list(temp_Census['Having_latrine_facility_within_the_premises_Total_Households'])
Power_Parity_Rs_45000_90000 = list(temp_Census['Power_Parity_Rs_45000_90000'])
Higher_Education = list(temp_Census['Higher_Education'])
index = list(temp_Census['STATE_DISTRICT'])
df = pd.DataFrame({'Household with 5 persons':Household_size_5_persons_Households,
                   'Literate':Literate,
                   'Total Households having latrine facility within the premises':Having_latrine_facility_within_the_premises_Total_Households,
                   'Power of Parity Rs 45000 to 90000':Power_Parity_Rs_45000_90000,
                   'Higher Education':Higher_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Top Districts for Crimes against Women', fontsize=12)
ax.set_xlabel("State-District")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Top_Districts_Population_Women.eps", dpi=600) 


# In[881]:


#top_Population
#States

census_df['STATE'] = [i.split('_')[0] for i in list(census_df['STATE_DISTRICT'])]
col_Census = list(census_df.columns)
col_Census.remove('STATE_DISTRICT')
temp_Census_df = census_df.groupby(['STATE'])[col_Census].sum()
temp_Census_df=temp_Census_df.reset_index()
plot_From_Census.remove('STATE_DISTRICT')
plot_From_Census = plot_From_Census + ['STATE']
get_Columns_Census.remove('STATE_DISTRICT')
get_Columns_Census = get_Columns_Census + ['STATE']
state = list(top_Women_States_Population['States'])
temp_Census = temp_Census_df[temp_Census_df['STATE'].isin(state)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Household_size_5_persons_Households'] = (temp_Census['Household_size_5_persons_Households']/(temp_Census['Households']))*100
temp_Census['Literate'] = (temp_Census['Literate']/temp_Census['Population'])*100
temp_Census['Having_latrine_facility_within_the_premises_Total_Households'] = (temp_Census['Having_latrine_facility_within_the_premises_Total_Households']/(temp_Census['Having_latrine_facility_within_the_premises_Total_Households']+temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']))*100
temp_Census['Power_Parity_Rs_45000_90000'] = (temp_Census['Power_Parity_Rs_45000_90000']/temp_Census['Total_Power_Parity'])*100
temp_Census['Higher_Education'] = (temp_Census['Higher_Education']/(temp_Census['Literate_Education']))*100
temp_Census = temp_Census[plot_From_Census]
Household_size_5_persons_Households = list(temp_Census['Household_size_5_persons_Households'])
Literate = list(temp_Census['Literate'])
Having_latrine_facility_within_the_premises_Total_Households = list(temp_Census['Having_latrine_facility_within_the_premises_Total_Households'])
Power_Parity_Rs_45000_90000 = list(temp_Census['Power_Parity_Rs_45000_90000'])
Higher_Education = list(temp_Census['Higher_Education'])
index = list(temp_Census['STATE'])
df = pd.DataFrame({'Household with 5 persons':Household_size_5_persons_Households,
                   'Literate':Literate,
                   'Total Households having latrine facility within the premises':Having_latrine_facility_within_the_premises_Total_Households,
                   'Power of Parity Rs 45000 to 90000':Power_Parity_Rs_45000_90000,
                   'Higher Education':Higher_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Top States for Crimes against Women', fontsize=12)
ax.set_xlabel("State")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Top_States_Population_Women.eps", dpi=600) 


# In[882]:


#low_Population
#Districts

temp_Sample = pd.DataFrame(sample.loc['Total Crimes'])
temp_Sample.reset_index()
plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0.745].index.tolist()
#plot_From_Census = temp_Sample[temp_Sample['Total Crimes']>0].index.tolist()
plot_From_Census = plot_From_Census+['STATE_DISTRICT']
normalise_Columns_Census = ['Households', 'Population','Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households', 'Total_Power_Parity','Literate_Education']
get_Columns_Census = plot_From_Census+normalise_Columns_Census

low_Women_Districts_Population['STATE_DISTRICT'] = low_Women_Districts_Population['States']+'_'+low_Women_Districts_Population['Districts']
state_district = list(low_Women_Districts_Population['STATE_DISTRICT'])
temp_Census = census_df[census_df['STATE_DISTRICT'].isin(state_district)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Household_size_5_persons_Households'] = (temp_Census['Household_size_5_persons_Households']/(temp_Census['Households']))*100
temp_Census['Literate'] = (temp_Census['Literate']/temp_Census['Population'])*100
temp_Census['Having_latrine_facility_within_the_premises_Total_Households'] = (temp_Census['Having_latrine_facility_within_the_premises_Total_Households']/(temp_Census['Having_latrine_facility_within_the_premises_Total_Households']+temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']))*100
temp_Census['Power_Parity_Rs_45000_90000'] = (temp_Census['Power_Parity_Rs_45000_90000']/temp_Census['Total_Power_Parity'])*100
temp_Census['Higher_Education'] = (temp_Census['Higher_Education']/(temp_Census['Literate_Education']))*100
temp_Census = temp_Census[plot_From_Census]
Household_size_5_persons_Households = list(temp_Census['Household_size_5_persons_Households'])
Literate = list(temp_Census['Literate'])
Having_latrine_facility_within_the_premises_Total_Households = list(temp_Census['Having_latrine_facility_within_the_premises_Total_Households'])
Power_Parity_Rs_45000_90000 = list(temp_Census['Power_Parity_Rs_45000_90000'])
Higher_Education = list(temp_Census['Higher_Education'])
index = list(temp_Census['STATE_DISTRICT'])
df = pd.DataFrame({'Household with 5 persons':Household_size_5_persons_Households,
                   'Literate':Literate,
                   'Total Households having latrine facility within the premises':Having_latrine_facility_within_the_premises_Total_Households,
                   'Power of Parity Rs 45000 to 90000':Power_Parity_Rs_45000_90000,
                   'Higher Education':Higher_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Low Districts for Crimes against Women', fontsize=12)
ax.set_xlabel("State-District")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Low_Districts_Population_Women.eps", dpi=600) 


# In[883]:


#low_Population
#States

census_df['STATE'] = [i.split('_')[0] for i in list(census_df['STATE_DISTRICT'])]
col_Census = list(census_df.columns)
col_Census.remove('STATE_DISTRICT')
temp_Census_df = census_df.groupby(['STATE'])[col_Census].sum()
temp_Census_df=temp_Census_df.reset_index()
plot_From_Census.remove('STATE_DISTRICT')
plot_From_Census = plot_From_Census + ['STATE']
get_Columns_Census.remove('STATE_DISTRICT')
get_Columns_Census = get_Columns_Census + ['STATE']
state = list(low_Women_States_Population['States'])
temp_Census = temp_Census_df[temp_Census_df['STATE'].isin(state)]
temp_Census = temp_Census[get_Columns_Census]
temp_Census['Household_size_5_persons_Households'] = (temp_Census['Household_size_5_persons_Households']/(temp_Census['Households']))*100
temp_Census['Literate'] = (temp_Census['Literate']/temp_Census['Population'])*100
temp_Census['Having_latrine_facility_within_the_premises_Total_Households'] = (temp_Census['Having_latrine_facility_within_the_premises_Total_Households']/(temp_Census['Having_latrine_facility_within_the_premises_Total_Households']+temp_Census['Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households']))*100
temp_Census['Power_Parity_Rs_45000_90000'] = (temp_Census['Power_Parity_Rs_45000_90000']/temp_Census['Total_Power_Parity'])*100
temp_Census['Higher_Education'] = (temp_Census['Higher_Education']/(temp_Census['Literate_Education']))*100
temp_Census = temp_Census[plot_From_Census]
Household_size_5_persons_Households = list(temp_Census['Household_size_5_persons_Households'])
Literate = list(temp_Census['Literate'])
Having_latrine_facility_within_the_premises_Total_Households = list(temp_Census['Having_latrine_facility_within_the_premises_Total_Households'])
Power_Parity_Rs_45000_90000 = list(temp_Census['Power_Parity_Rs_45000_90000'])
Higher_Education = list(temp_Census['Higher_Education'])
index = list(temp_Census['STATE'])
df = pd.DataFrame({'Household with 5 persons':Household_size_5_persons_Households,
                   'Literate':Literate,
                   'Total Households having latrine facility within the premises':Having_latrine_facility_within_the_premises_Total_Households,
                   'Power of Parity Rs 45000 to 90000':Power_Parity_Rs_45000_90000,
                   'Higher Education':Higher_Education}, index=index)
ax = df.plot.bar(rot=0, figsize = (20,10), title='Inference for Low States for Crimes against Women', fontsize=12)
ax.set_xlabel("State")
ax.set_ylabel("Percentage")
#for p in ax.patches:
#    ax.annotate(str(p.get_height()), (p.get_x() * 1.005, p.get_height() * 1.005))
for p in ax.patches:                 
    ax.annotate(np.round(p.get_height(),decimals=2),(p.get_x()+p.get_width()/2., p.get_height()),ha='center',va='center', xytext=(0, 10),textcoords='offset points')
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Inference_Low_States_Population_Women.eps", dpi=600) 


# # Correlation

# In[884]:


result = pd.concat([newdf_merged], axis=1).corr()
column1=newdf_merged.columns.tolist()
column2=newdf_merged.columns.tolist()
corr_df_Crimes=result[column2].loc[column1]


# In[885]:


corr_df_Crimes.head()


# # # SC

# In[886]:


#ls_SC
#remove_From_SC = ['sc|Total_Crimes','sc|Other Crimes Against SCs']
#ls_SC = [i for i in ls_SC if i not in remove_From_SC]

temp_df = corr_df_Crimes.loc[ls_SC,ls_SC]
k = 5
vals = temp_df.values
arr1 = np.argsort(-vals, axis=1)

a = temp_df.columns[arr1[:,:k]]
b = vals[np.arange(len(temp_df.index))[:,None], arr1][:,:k]

c = np.empty((vals.shape[0], 2 * k), dtype=a.dtype)
c[:,0::2] = a
c[:,1::2] = b
top_Indices = pd.DataFrame(c)
top_Indices.drop([0,1],axis=1,inplace=True)
top_Indices = top_Indices.set_index([ls_SC])
top_Indices


# In[887]:


ls_New_Col = ['Murder', 'Rape', 'Kidnapping','Dacoity', 'Robbery','Arson','Hurt','POA','PCR','Other Crimes','Total Crimes']
#sns.set(rc={'figure.figsize':(11.7,11.7)})
plt.subplots(figsize=(20,9))
temp_df.set_index([ls_New_Col], inplace=True)
temp_df.set_axis(ls_New_Col, axis=1, inplace=True)
ax = sns.heatmap(temp_df, annot=True, fmt='.2f', cmap='RdYlGn', annot_kws={'size':15})
sns.set(font_scale=1.2)
ax.set_title('Crime Against Scheduled Castes', fontsize = 15)
plt.tight_layout()
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Correlation_SC.eps", dpi=600)


# In[888]:


ls_SC


# # # ST

# In[889]:


#remove_From_ST = ['st|Total_Crimes','st|Other Crimes Against STs']
#ls_ST = [i for i in ls_ST if i not in remove_From_ST]
temp_df = corr_df_Crimes.loc[ls_ST,ls_ST]
temp_df.dropna(how = 'all', inplace=True)
temp_df.dropna(axis='columns',inplace=True)
ls_ST_New = temp_df.index
k = 5
vals = temp_df.values
arr1 = np.argsort(-vals, axis=1)

a = temp_df.columns[arr1[:,:k]]
b = vals[np.arange(len(temp_df.index))[:,None], arr1][:,:k]

c = np.empty((vals.shape[0], 2 * k), dtype=a.dtype)
c[:,0::2] = a
c[:,1::2] = b
top_Indices = pd.DataFrame(c)
top_Indices.drop([0,1],axis=1,inplace=True)
top_Indices=top_Indices.set_index([ls_ST_New])
top_Indices


# In[890]:


ls_New_Col = ['Murder', 'Rape', 'Dacoity', 'Robbery','Arson','Hurt','POA','PCR','Other Crimes','Total Crimes']
#sns.set(rc={'figure.figsize':(11.7,11.7)})
plt.subplots(figsize=(20,9))
temp_df.set_index([ls_New_Col], inplace=True)
temp_df.set_axis(ls_New_Col, axis=1, inplace=True)
ax = sns.heatmap(temp_df, annot=True, fmt='.2f', cmap='RdYlGn', annot_kws={'size':15})
sns.set(font_scale=1.2)
ax.set_title('Crime Against Scheduled Tribes', fontsize = 15)
plt.tight_layout()
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Correlation_ST.eps", dpi=600)


# In[891]:


ls_ST


# # Children

# In[892]:


#remove_From_Children = ['children|Total_Crimes','children|Other Crimes']
#ls_Children = [i for i in ls_Children if i not in remove_From_Children]
temp_df = corr_df_Crimes.loc[ls_Children,ls_Children]
k = 5
vals = temp_df.values
arr1 = np.argsort(-vals, axis=1)

a = temp_df.columns[arr1[:,:k]]
b = vals[np.arange(len(temp_df.index))[:,None], arr1][:,:k]

c = np.empty((vals.shape[0], 2 * k), dtype=a.dtype)
c[:,0::2] = a
c[:,1::2] = b
top_Indices = pd.DataFrame(c)
top_Indices.drop([0,1],axis=1,inplace=True)
top_Indices=top_Indices.set_index([ls_Children])
top_Indices


# In[893]:


ls_New_Col = ['Murder','Rape','Kidnapping','Foeticide','Abet to Suicide','Abandon','Procure minor girls','Buying Girls P','Selling Girls P','Child Marriage','Other Crimes','Total Crimes']
#sns.set(rc={'figure.figsize':(11.7,11.7)})
plt.subplots(figsize=(20,9))
temp_df.set_index([ls_New_Col], inplace=True)
temp_df.set_axis(ls_New_Col, axis=1, inplace=True)
ax = sns.heatmap(temp_df, annot=True, fmt='.2f', cmap='RdYlGn', annot_kws={'size':15})
sns.set(font_scale=1.2)
ax.set_title('Crime Against Children', fontsize = 15)
plt.tight_layout()
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Correlation_Children.eps", dpi=600)


# In[894]:


ls_Children


# # Women

# In[895]:


#remove_From_Women = ['women|Total_Crimes']
#ls_Women = [i for i in ls_Women if i not in remove_From_Women]
temp_df = corr_df_Crimes.loc[ls_Women,ls_Women]
k = 5
vals = temp_df.values
arr1 = np.argsort(-vals, axis=1)

a = temp_df.columns[arr1[:,:k]]
b = vals[np.arange(len(temp_df.index))[:,None], arr1][:,:k]

c = np.empty((vals.shape[0], 2 * k), dtype=a.dtype)
c[:,0::2] = a
c[:,1::2] = b
top_Indices = pd.DataFrame(c)
top_Indices.drop([0,1],axis=1,inplace=True)
top_Indices=top_Indices.set_index([ls_Women])
top_Indices


# In[896]:


ls_New_Col = ['Total Crimes', 'Rape', 'Kidnapping', 'Dowry Deaths', 'Assault', 'Insult to modesty', 'Cruelty by Family', 'Importation']
plt.subplots(figsize=(20,9))
#sns.set(rc={'figure.figsize':(11.7,11.7)})
temp_df.set_index([ls_New_Col], inplace=True)
temp_df.set_axis(ls_New_Col, axis=1, inplace=True)
#ax.figure.tight_layout()
ax = sns.heatmap(temp_df, annot=True, fmt='.2f', cmap='RdYlGn', annot_kws={'size':15})
sns.set(font_scale=1.2)
ax.set_title('Crime Against Women', fontsize = 15)
plt.tight_layout()
ax.figure.savefig(cwd +"/correlation_And_Inferential_Analysis/Correlation_Women.eps", dpi=600)


# In[ ]:




