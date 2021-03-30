#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import os
cwd = os.getcwd()

########################## SC DATA ################################
sc_data = pd.read_csv(cwd+"/Preprocessing/clean_SC_Data.csv")
district_data = sc_data.copy()
district_data.drop('STATE_DISTRICT', axis =1, inplace= True)
district_data.drop('Year', axis =1, inplace= True)
district_data = pd.DataFrame(district_data.sum(axis = 0))
district_data.reset_index(inplace= True)
district_data.rename(columns={'index': 'Types', 0 : 'Crimes' }, inplace= True)
total_crimes = int(district_data[district_data.Types == 'Total_Crimes']['Crimes'])
district_data['%Contribution']= district_data['Crimes']/total_crimes*100
district_data = district_data.nlargest(7, '%Contribution')
district_data.to_csv(cwd+'/Contribution_Of_Subcategory/Contribution_SC.csv', index= 0)

###################################### WOMEN DATA ##########################
women_data = pd.read_csv(cwd+"/Preprocessing/clean_Women_Data.csv")
district_data = women_data.copy()
district_data.drop('STATE_DISTRICT', axis =1, inplace= True)
district_data.drop('Year', axis =1, inplace= True)
district_data = pd.DataFrame(district_data.sum(axis = 0))
district_data.reset_index(inplace= True)
district_data.rename(columns={'index': 'Types', 0 : 'Crimes' }, inplace= True)
total_crimes = int(district_data[district_data.Types == 'Total_Crimes']['Crimes'])
district_data['%Contribution']= district_data['Crimes']/total_crimes*100
district_data = district_data.nlargest(7, '%Contribution')
district_data.to_csv(cwd+'/Contribution_Of_Subcategory/Contribution_Women.csv', index= 0)

####################################### ST DATA ###############################
st_data = pd.read_csv(cwd+"/Preprocessing/clean_ST_Data.csv")
district_data = st_data.copy()
district_data.drop('STATE_DISTRICT', axis =1, inplace= True)
district_data.drop('Year', axis =1, inplace= True)
district_data = pd.DataFrame(district_data.sum(axis = 0))
district_data.reset_index(inplace= True)
district_data.rename(columns={'index': 'Types', 0 : 'Crimes' }, inplace= True)
total_crimes = int(district_data[district_data.Types == 'Total_Crimes']['Crimes'])
district_data['%Contribution']= district_data['Crimes']/total_crimes*100
district_data = district_data.nlargest(7, '%Contribution')
district_data.to_csv(cwd+'/Contribution_Of_Subcategory/Contribution_ST.csv', index= 0)

#################################### CHILDREN DATA ###########################
children_data = pd.read_csv(cwd+"/Preprocessing/clean_Children_Data.csv")
district_data = children_data.copy()
district_data.drop('STATE_DISTRICT', axis =1, inplace= True)
district_data.drop('Year', axis =1, inplace= True)
district_data = pd.DataFrame(district_data.sum(axis = 0))
district_data.reset_index(inplace= True)
district_data.rename(columns={'index': 'Types', 0 : 'Crimes' }, inplace= True)
total_crimes = int(district_data[district_data.Types == 'Total_Crimes']['Crimes'])
district_data['%Contribution']= district_data['Crimes']/total_crimes*100
district_data = district_data.nlargest(7, '%Contribution')
district_data.to_csv(cwd+'/Contribution_Of_Subcategory/Contribution_Children.csv', index= 0)


# # Plots

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

############# Plotting ####################
sc_data = pd.read_csv(cwd+"/Preprocessing/clean_SC_Data.csv")
district_data = sc_data.copy()
district_data.drop('STATE_DISTRICT', axis =1, inplace= True)
district_data.drop('Year', axis =1, inplace= True)
district_data = pd.DataFrame(district_data.sum(axis = 0))
district_data.reset_index(inplace= True)
district_data.rename(columns={'index': 'Types', 0 : 'Crimes' }, inplace= True)
total_crimes = int(district_data[district_data.Types == 'Total_Crimes']['Crimes'])
district_data['%Contribution']= district_data['Crimes']/total_crimes*100
district_data = district_data[district_data.Types != 'Total_Crimes']
x = ['Murder', 'Rape', 'Kidnapping','Dacoity', 'Robbery','Arson','Hurt','POA','PCR','Other Crimes']
y = district_data['%Contribution'].tolist()
plt.figure(figsize=(10,10))
plt.bar(x, y, label='SC Sub Category Contribution', width = .5)
plt.xlabel('Sub Category Crimes',fontsize=14)
plt.ylabel('Percentage Contribution',fontsize=14)
#plt.xticks(x, rotation = 90, )
plt.legend(loc='upper left')
plt.savefig(cwd+"/Contribution_Of_Subcategory/SC_subcategory.eps", format='eps', dpi=300)

############# Plotting ####################
women_data = pd.read_csv(cwd+"/Preprocessing/clean_Women_Data.csv")
district_data = women_data.copy()
district_data.drop('STATE_DISTRICT', axis =1, inplace= True)
district_data.drop('Year', axis =1, inplace= True)
district_data = pd.DataFrame(district_data.sum(axis = 0))
district_data.reset_index(inplace= True)
district_data.rename(columns={'index': 'Types', 0 : 'Crimes' }, inplace= True)
total_crimes = int(district_data[district_data.Types == 'Total_Crimes']['Crimes'])
district_data['%Contribution']= district_data['Crimes']/total_crimes*100
district_data = district_data[district_data.Types != 'Total_Crimes']

x = ['Rape','Kidnapping','Dowry Deaths','Assault','Insult','Cruelty(Relatives)','Importation']
y = district_data['%Contribution'].tolist()
plt.figure(figsize=(10,10))
plt.bar(x, y, label='Women Sub Category Contribution', width = .5)
plt.xlabel('Sub Category Crimes',fontsize=14)
plt.ylabel('Percentage Contribution',fontsize=14)
#plt.xticks(x, rotation = 90, )
plt.legend(loc = 'upper left')
plt.savefig(cwd+"/Contribution_Of_Subcategory/Women_subcategory.eps", format='eps', dpi=300)

############# Plotting ####################
st_data = pd.read_csv(cwd+"/Preprocessing/clean_ST_Data.csv")
district_data = st_data.copy()
district_data.drop('STATE_DISTRICT', axis =1, inplace= True)
district_data.drop('Year', axis =1, inplace= True)
district_data = pd.DataFrame(district_data.sum(axis = 0))
district_data.reset_index(inplace= True)
district_data.rename(columns={'index': 'Types', 0 : 'Crimes' }, inplace= True)
total_crimes = int(district_data[district_data.Types == 'Total_Crimes']['Crimes'])
district_data['%Contribution']= district_data['Crimes']/total_crimes*100
district_data = district_data[district_data.Types != 'Total_Crimes']
#x = district_data.Types.tolist()
x = ['Murder', 'Rape', 'Kidnapping','Dacoity', 'Robbery','Arson','Hurt','POA','PCR','Other Crimes']
y = district_data['%Contribution'].tolist()
plt.figure(figsize=(10,10))
plt.bar(x, y, label='ST Sub Category Contribution', width = .5)
plt.xlabel('Sub Category Crimes',fontsize=14)
plt.ylabel('Percentage Contribution',fontsize=14)
#plt.xticks(x, rotation = 90, )
plt.legend(loc = 'upper left')
plt.savefig(cwd+"/Contribution_Of_Subcategory/ST_subcategory.eps", format='eps', dpi=300)

############# Plotting ####################
# Abetment of suicide-->suicide
# Procuration of minor girls --> PMG
# Buying of girls for prostitution---> BGP
# Selling of girls for prostitution --> SGP
# Prohibition of child marriage act--> PCMA
children_data = pd.read_csv(cwd+"/Preprocessing/clean_Children_Data.csv")
district_data = children_data.copy()
district_data.drop('STATE_DISTRICT', axis =1, inplace= True)
district_data.drop('Year', axis =1, inplace= True)
district_data = pd.DataFrame(district_data.sum(axis = 0))
district_data.reset_index(inplace= True)
district_data.rename(columns={'index': 'Types', 0 : 'Crimes' }, inplace= True)
total_crimes = int(district_data[district_data.Types == 'Total_Crimes']['Crimes'])
district_data['%Contribution']= district_data['Crimes']/total_crimes*100
district_data = district_data[district_data.Types != 'Total_Crimes']
x = district_data.Types.tolist()
x = ['Murder','Rape','Kidnapping','Foeticide','Suicide','Abandonment','PMG','BGP','SGP','PCMA','Other Crimes']
y = district_data['%Contribution'].tolist()
plt.figure(figsize=(11,11))
plt.bar(x, y, label='Children Sub Category Contribution', width = .4)
plt.xlabel('Sub Category Crimes',fontsize=14)
plt.ylabel('Percentage Contribution',fontsize=14)
#plt.xticks(x, rotation = 90, )
plt.legend(loc = 'upper left')
plt.savefig(cwd+"/Contribution_Of_Subcategory/Children_subcategory.eps", format='eps', dpi=300)


# In[ ]:




