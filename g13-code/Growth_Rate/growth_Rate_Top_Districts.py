#!/usr/bin/env python
# coding: utf-8

# # SC 

# # District Growth Rate

# In[1]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os
cwd = os.getcwd()

sc_data = pd.read_csv(cwd+"/Preprocessing/clean_SC_Data.csv")
prevelant_df = pd.DataFrame()
prevelant_df["STATE_DISTRICT"] = sc_data["STATE_DISTRICT"].unique()
for year in range(2001,2011):
  district_df = sc_data[sc_data["Year"]== year]
  prevelant_df[str(year)] = district_df.Total_Crimes.to_list()
prevelant_df = prevelant_df.loc[(prevelant_df.iloc[:,1:].sum(axis=1)!=0)]
for year in range(2002,2011):
  prevelant_df[str(year-1)+'-'+str(year)] = (prevelant_df[str(year)]-prevelant_df[str(year-1)])/prevelant_df[str(year-1)]*100

top_districts = ['RAJASTHAN_BHARATPUR','MADHYA PRADESH_UJJAIN', 'MADHYA PRADESH_GUNA', 'MADHYA PRADESH_DEWAS','RAJASTHAN_DHOLPUR']
prevelant_df = prevelant_df[prevelant_df.STATE_DISTRICT.isin(top_districts)]
prevelant_df.replace([np.inf, -np.inf], np.nan, inplace=True)
prevelant_df.fillna(0, inplace=True)
prevelant_df_growth = prevelant_df[['STATE_DISTRICT',"2001-2002","2002-2003","2003-2004","2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010"]]
prevelant_df_crimes = prevelant_df[['STATE_DISTRICT',"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]]

#######################Plotting ###########################################

t_df = prevelant_df_crimes.set_index('STATE_DISTRICT').transpose()
prevelant_df_growth = prevelant_df_growth.set_index('STATE_DISTRICT').transpose()
X = t_df.index.to_list()
X = t_df.index.to_list()
for ele in top_districts:
  crimes = t_df[ele].to_list()
  rate = prevelant_df_growth[ele].to_list()
  rate = [round(i,2) for i in rate]
  rate.insert(0,0)
  fig = go.Figure()  # create a figure object 
  fig.add_trace(
      go.Scatter(x = X, y=crimes, 
               text= [str(i) for i in rate],
               mode = 'lines+text+markers',
               textposition = 'top right',
               name= ele, # legend name
               showlegend=True, # legend name can be hidden from legend
        )
      )

  fig.update_layout(title_text="SC Crime Growth Rate", # plot title
                  legend_orientation="h", # h:horizontal, v
                  xaxis_title="Years",
                  yaxis_title="Crimes",
                  )
  fig.write_image(cwd+'/Growth_Rate/SC/Top_Districts_'+str(ele)+'.eps', width = 1000, height = 500)
  #fig.show()
  


# # States Growth Rate

# In[2]:


def state(string):
  string1 = string.split("_")[0]
  return string1
def district(string):
  string1 = string.split("_")[1]
  return string1
  
sc_data = pd.read_csv(cwd+"/Preprocessing/clean_SC_Data.csv")
sc_data['STATE'] = sc_data["STATE_DISTRICT"].apply(state)
sc_data['DISTRICT'] = sc_data["STATE_DISTRICT"].apply(district)
sc_data = pd.DataFrame(sc_data.groupby(['STATE', 'Year']).agg({'Total_Crimes':"sum"}).reset_index())

prevelant_df = pd.DataFrame()
prevelant_df["STATE"] = sc_data["STATE"].unique()
for year in range(2001,2011):
  district_df = sc_data[sc_data["Year"]== year]
  prevelant_df[str(year)] = district_df.Total_Crimes.to_list()
  
for year in range(2002,2011):
  prevelant_df[str(year-1)+'-'+str(year)] = (prevelant_df[str(year)]-prevelant_df[str(year-1)])/prevelant_df[str(year-1)]*100
  
top_states = ['MADHYA PRADESH','RAJASTHAN', 'ANDHRA PRADESH', 'UTTAR PRADESH','BIHAR']
prevelant_df = prevelant_df[prevelant_df.STATE.isin(top_states)]
prevelant_df.replace([np.inf, -np.inf], np.nan, inplace=True)
prevelant_df.fillna(0, inplace=True)
prevelant_df_growth = prevelant_df[['STATE',"2001-2002","2002-2003","2003-2004","2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010"]]
prevelant_df_crimes = prevelant_df[['STATE',"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]]

#######################Plotting ###########################################
t_df = prevelant_df_crimes.set_index('STATE').transpose()
prevelant_df_growth = prevelant_df_growth.set_index('STATE').transpose()

X = t_df.index.to_list()
##############################################################
for ele in top_states:
  crimes = t_df[ele].to_list()
  rate = prevelant_df_growth[ele].to_list()
  rate = [round(i,2) for i in rate]
  rate.insert(0,0)
  fig = go.Figure()  # create a figure object 
  fig.add_trace(
      go.Scatter(x = X, y=crimes, 
               text= [str(i) for i in rate],
               mode = 'lines+text+markers',
               textposition = 'top right',
               name= ele, # legend name
               showlegend=True, # legend name can be hidden from legend
        )
      )

  fig.update_layout(title_text="SC Crime Growth Rate", # plot title
                  legend_orientation="h", # h:horizontal, v
                  xaxis_title="Years",
                  yaxis_title="Crimes",
                  )
  fig.write_image(cwd+'/Growth_Rate/SC/Top_States_'+str(ele)+'.eps', width = 1000, height = 500)
  #fig.show()


# # ST

# # Districts Growth Rate

# In[3]:


sc_data = pd.read_csv(cwd+"/Preprocessing/clean_ST_Data.csv")

prevelant_df = pd.DataFrame()
prevelant_df["STATE_DISTRICT"] = sc_data["STATE_DISTRICT"].unique()
for year in range(2001,2011):
  district_df = sc_data[sc_data["Year"]== year]
  prevelant_df[str(year)] = district_df.Total_Crimes.to_list()
prevelant_df = prevelant_df.loc[(prevelant_df.iloc[:,1:].sum(axis=1)!=0)]
for year in range(2002,2011):
  prevelant_df[str(year-1)+'-'+str(year)] = (prevelant_df[str(year)]-prevelant_df[str(year-1)])/prevelant_df[str(year-1)]*100

top_districts = ['MADHYA PRADESH_GWALIOR','RAJASTHAN_BHARATPUR', 'RAJASTHAN_TONK', 'RAJASTHAN_SIKAR', 'ANDHRA PRADESH_KARIMNAGAR']
prevelant_df = prevelant_df[prevelant_df.STATE_DISTRICT.isin(top_districts)]
prevelant_df.replace([np.inf, -np.inf], np.nan, inplace=True)
prevelant_df.fillna(0, inplace=True)
prevelant_df_growth = prevelant_df[['STATE_DISTRICT',"2001-2002","2002-2003","2003-2004","2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010"]]
prevelant_df_crimes = prevelant_df[['STATE_DISTRICT',"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]]

#######################Plotting ###########################################

t_df = prevelant_df_crimes.set_index('STATE_DISTRICT').transpose()
prevelant_df_growth = prevelant_df_growth.set_index('STATE_DISTRICT').transpose()
X = t_df.index.to_list()
X = t_df.index.to_list()
for ele in top_districts:
  crimes = t_df[ele].to_list()
  rate = prevelant_df_growth[ele].to_list()
  rate = [round(i,2) for i in rate]
  rate.insert(0,0)
  fig = go.Figure()  # create a figure object 
  fig.add_trace(
      go.Scatter(x = X, y=crimes, 
               text= [str(i) for i in rate],
               mode = 'lines+text+markers',
               textposition = 'top right',
               name= ele, # legend name
               showlegend=True, # legend name can be hidden from legend
        )
      )

  fig.update_layout(title_text="ST Crime Growth Rate", # plot title
                  legend_orientation="h", # h:horizontal, v
                  xaxis_title="Years",
                  yaxis_title="Crimes",
                  )
  fig.write_image(cwd+'/Growth_Rate/ST/Top_Districts_'+str(ele)+'.eps', width = 1000, height = 500)
  #fig.show()


# # States Growth Rate

# In[4]:


def state(string):
  string1 = string.split("_")[0]
  return string1
def district(string):
  string1 = string.split("_")[1]
  return string1
  
sc_data = pd.read_csv(cwd+"/Preprocessing/clean_ST_Data.csv")
sc_data['STATE'] = sc_data["STATE_DISTRICT"].apply(state)
sc_data['DISTRICT'] = sc_data["STATE_DISTRICT"].apply(district)
sc_data = pd.DataFrame(sc_data.groupby(['STATE', 'Year']).agg({'Total_Crimes':"sum"}).reset_index())

prevelant_df = pd.DataFrame()
prevelant_df["STATE"] = sc_data["STATE"].unique()
for year in range(2001,2011):
  district_df = sc_data[sc_data["Year"]== year]
  prevelant_df[str(year)] = district_df.Total_Crimes.to_list()
  
for year in range(2002,2011):
  prevelant_df[str(year-1)+'-'+str(year)] = (prevelant_df[str(year)]-prevelant_df[str(year-1)])/prevelant_df[str(year-1)]*100
  
top_states = ['RAJASTHAN', 'MADHYA PRADESH','ANDHRA PRADESH', 'CHHATTISGARH','ODISHA']
prevelant_df = prevelant_df[prevelant_df.STATE.isin(top_states)]
prevelant_df.replace([np.inf, -np.inf], np.nan, inplace=True)
prevelant_df.fillna(0, inplace=True)
prevelant_df_growth = prevelant_df[['STATE',"2001-2002","2002-2003","2003-2004","2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010"]]
prevelant_df_crimes = prevelant_df[['STATE',"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]]

#######################Plotting ###########################################
t_df = prevelant_df_crimes.set_index('STATE').transpose()
prevelant_df_growth = prevelant_df_growth.set_index('STATE').transpose()

X = t_df.index.to_list()
##############################################################
for ele in top_states:
  crimes = t_df[ele].to_list()
  rate = prevelant_df_growth[ele].to_list()
  rate = [round(i,2) for i in rate]
  rate.insert(0,0)
  fig = go.Figure()  # create a figure object 
  fig.add_trace(
      go.Scatter(x = X, y=crimes, 
               text= [str(i) for i in rate],
               mode = 'lines+text+markers',
               textposition = 'top right',
               name= ele, # legend name
               showlegend=True, # legend name can be hidden from legend
        )
      )

  fig.update_layout(title_text="ST Crime Growth Rate", # plot title
                  legend_orientation="h", # h:horizontal, v
                  xaxis_title="Years",
                  yaxis_title="Crimes",
                  )
  fig.write_image(cwd+'/Growth_Rate/ST/Top_States_'+str(ele)+'.eps', width = 1000, height = 500)
  #fig.show()


# # Children

# # Districts Growth Data

# In[5]:


sc_data = pd.read_csv(cwd+"/Preprocessing/clean_Children_Data.csv")
prevelant_df = pd.DataFrame()
prevelant_df["STATE_DISTRICT"] = sc_data["STATE_DISTRICT"].unique()
for year in range(2001,2011):
  district_df = sc_data[sc_data["Year"]== year]
  prevelant_df[str(year)] = district_df.Total_Crimes.to_list()
prevelant_df = prevelant_df.loc[(prevelant_df.iloc[:,1:].sum(axis=1)!=0)]
for year in range(2002,2011):
  prevelant_df[str(year-1)+'-'+str(year)] = (prevelant_df[str(year)]-prevelant_df[str(year-1)])/prevelant_df[str(year-1)]*100

top_districts = ['DELHI_DELHI','MADHYA PRADESH_INDORE', 'MADHYA PRADESH_KHANDWA', 'MADHYA PRADESH_BETUL','MADHYA PRADESH_RAJGARH']
prevelant_df = prevelant_df[prevelant_df.STATE_DISTRICT.isin(top_districts)]
prevelant_df.replace([np.inf, -np.inf], np.nan, inplace=True)
prevelant_df.fillna(0, inplace=True)
prevelant_df_growth = prevelant_df[['STATE_DISTRICT',"2001-2002","2002-2003","2003-2004","2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010"]]
prevelant_df_crimes = prevelant_df[['STATE_DISTRICT',"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]]

#######################Plotting ###########################################

t_df = prevelant_df_crimes.set_index('STATE_DISTRICT').transpose()
prevelant_df_growth = prevelant_df_growth.set_index('STATE_DISTRICT').transpose()
X = t_df.index.to_list()
X = t_df.index.to_list()
for ele in top_districts:
  crimes = t_df[ele].to_list()
  rate = prevelant_df_growth[ele].to_list()
  rate = [round(i,2) for i in rate]
  rate.insert(0,0)
  fig = go.Figure()  # create a figure object 
  fig.add_trace(
      go.Scatter(x = X, y=crimes, 
               text= [str(i) for i in rate],
               mode = 'lines+text+markers',
               textposition = 'top right',
               name= ele, # legend name
               showlegend=True, # legend name can be hidden from legend
        )
      )

  fig.update_layout(title_text="Children Crime Growth Rate", # plot title
                  legend_orientation="h", # h:horizontal, v
                  xaxis_title="Years",
                  yaxis_title="Crimes",
                  )
  fig.write_image(cwd+'/Growth_Rate/Children/Top_Districts_'+str(ele)+'.eps', width = 1000, height = 500)

  #fig.show()


# # States Growth Rate

# In[6]:


def state(string):
  string1 = string.split("_")[0]
  return string1
def district(string):
  string1 = string.split("_")[1]
  return string1
  
sc_data = pd.read_csv(cwd+"/Preprocessing/clean_Children_Data.csv")
sc_data['STATE'] = sc_data["STATE_DISTRICT"].apply(state)
sc_data['DISTRICT'] = sc_data["STATE_DISTRICT"].apply(district)
sc_data = pd.DataFrame(sc_data.groupby(['STATE', 'Year']).agg({'Total_Crimes':"sum"}).reset_index())

prevelant_df = pd.DataFrame()
prevelant_df["STATE"] = sc_data["STATE"].unique()
for year in range(2001,2011):
  district_df = sc_data[sc_data["Year"]== year]
  prevelant_df[str(year)] = district_df.Total_Crimes.to_list()
  
for year in range(2002,2011):
  prevelant_df[str(year-1)+'-'+str(year)] = (prevelant_df[str(year)]-prevelant_df[str(year-1)])/prevelant_df[str(year-1)]*100
  
top_states = ['DELHI', 'MADHYA PRADESH', 'CHHATTISGARH', 'MAHARASHTRA', 'UTTAR PRADESH']
prevelant_df = prevelant_df[prevelant_df.STATE.isin(top_states)]
prevelant_df.replace([np.inf, -np.inf], np.nan, inplace=True)
prevelant_df.fillna(0, inplace=True)
prevelant_df_growth = prevelant_df[['STATE',"2001-2002","2002-2003","2003-2004","2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010"]]
prevelant_df_crimes = prevelant_df[['STATE',"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]]

#######################Plotting ###########################################
t_df = prevelant_df_crimes.set_index('STATE').transpose()
prevelant_df_growth = prevelant_df_growth.set_index('STATE').transpose()

X = t_df.index.to_list()
##############################################################
for ele in top_states:
  crimes = t_df[ele].to_list()
  rate = prevelant_df_growth[ele].to_list()
  rate = [round(i,2) for i in rate]
  rate.insert(0,0)
  fig = go.Figure()  # create a figure object 
  fig.add_trace(
      go.Scatter(x = X, y=crimes, 
               text= [str(i) for i in rate],
               mode = 'lines+text+markers',
               textposition = 'top right',
               name= ele, # legend name
               showlegend=True, # legend name can be hidden from legend
        )
      )

  fig.update_layout(title_text="Children Crime Growth Rate", # plot title
                  legend_orientation="h", # h:horizontal, v
                  xaxis_title="Years",
                  yaxis_title="Crimes",
                  )
  fig.write_image(cwd+'/Growth_Rate/Children/Top_States_'+str(ele)+'.eps', width = 1000, height = 500)

  #fig.show()


# # Women

# # Districts Growth Rate

# In[7]:


sc_data = pd.read_csv(cwd+"/Preprocessing/clean_Women_Data.csv")

prevelant_df = pd.DataFrame()
prevelant_df["STATE_DISTRICT"] = sc_data["STATE_DISTRICT"].unique()
for year in range(2001,2011):
  district_df = sc_data[sc_data["Year"]== year]
  prevelant_df[str(year)] = district_df.Total_Crimes.to_list()
prevelant_df = prevelant_df.loc[(prevelant_df.iloc[:,1:].sum(axis=1)!=0)]
for year in range(2002,2011):
  prevelant_df[str(year-1)+'-'+str(year)] = (prevelant_df[str(year)]-prevelant_df[str(year-1)])/prevelant_df[str(year-1)]*100

top_districts = ['DELHI_DELHI','ANDHRA PRADESH_HYDERABAD CITY', 'RAJASTHAN_CHITTORGARH', 'ANDHRA PRADESH_KARIMNAGAR','RAJASTHAN_KOTA']
prevelant_df = prevelant_df[prevelant_df.STATE_DISTRICT.isin(top_districts)]
prevelant_df.replace([np.inf, -np.inf], np.nan, inplace=True)
prevelant_df.fillna(0, inplace=True)
prevelant_df_growth = prevelant_df[['STATE_DISTRICT',"2001-2002","2002-2003","2003-2004","2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010"]]
prevelant_df_crimes = prevelant_df[['STATE_DISTRICT',"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]]

#######################Plotting ###########################################

t_df = prevelant_df_crimes.set_index('STATE_DISTRICT').transpose()
prevelant_df_growth = prevelant_df_growth.set_index('STATE_DISTRICT').transpose()
X = t_df.index.to_list()
X = t_df.index.to_list()
for ele in top_districts:
  crimes = t_df[ele].to_list()
  rate = prevelant_df_growth[ele].to_list()
  rate = [round(i,2) for i in rate]
  rate.insert(0,0)
  fig = go.Figure()  # create a figure object 
  fig.add_trace(
      go.Scatter(x = X, y=crimes, 
               text= [str(i) for i in rate],
               mode = 'lines+text+markers',
               textposition = 'top right',
               name= ele, # legend name
               showlegend=True, # legend name can be hidden from legend
        )
      )

  fig.update_layout(title_text="Women Crime Growth Rate", # plot title
                  legend_orientation="h", # h:horizontal, v
                  xaxis_title="Years",
                  yaxis_title="Crimes",
                  )
  fig.write_image(cwd+'/Growth_Rate/Women/Top_Districts_'+str(ele)+'.eps', width = 1000, height = 500)

  #fig.show()


# # States Growth Rate

# In[8]:


def state(string):
  string1 = string.split("_")[0]
  return string1
def district(string):
  string1 = string.split("_")[1]
  return string1
  
sc_data = pd.read_csv(cwd+"/Preprocessing/clean_Women_Data.csv")
sc_data['STATE'] = sc_data["STATE_DISTRICT"].apply(state)
sc_data['DISTRICT'] = sc_data["STATE_DISTRICT"].apply(district)
sc_data = pd.DataFrame(sc_data.groupby(['STATE', 'Year']).agg({'Total_Crimes':"sum"}).reset_index())

prevelant_df = pd.DataFrame()
prevelant_df["STATE"] = sc_data["STATE"].unique()
for year in range(2001,2011):
  district_df = sc_data[sc_data["Year"]== year]
  prevelant_df[str(year)] = district_df.Total_Crimes.to_list()
  
for year in range(2002,2011):
  prevelant_df[str(year-1)+'-'+str(year)] = (prevelant_df[str(year)]-prevelant_df[str(year-1)])/prevelant_df[str(year-1)]*100
  
top_states = ['DELHI', 'ANDHRA PRADESH', 'MADHYA PRADESH', 'RAJASTHAN', 'WEST BENGAL']
prevelant_df = prevelant_df[prevelant_df.STATE.isin(top_states)]
prevelant_df.replace([np.inf, -np.inf], np.nan, inplace=True)
prevelant_df.fillna(0, inplace=True)
prevelant_df_growth = prevelant_df[['STATE',"2001-2002","2002-2003","2003-2004","2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010"]]
prevelant_df_crimes = prevelant_df[['STATE',"2001","2002","2003","2004","2005","2006","2007","2008","2009","2010"]]

#######################Plotting ###########################################
t_df = prevelant_df_crimes.set_index('STATE').transpose()
prevelant_df_growth = prevelant_df_growth.set_index('STATE').transpose()

X = t_df.index.to_list()
##############################################################
for ele in top_states:
  crimes = t_df[ele].to_list()
  rate = prevelant_df_growth[ele].to_list()
  rate = [round(i,2) for i in rate]
  rate.insert(0,0)
  fig = go.Figure()  # create a figure object 
  fig.add_trace(
      go.Scatter(x = X, y=crimes, 
               text= [str(i) for i in rate],
               mode = 'lines+text+markers',
               textposition = 'top right',
               name= ele, # legend name
               showlegend=True, # legend name can be hidden from legend
        )
      )

  fig.update_layout(title_text="Women Crime Growth Rate", # plot title
                  legend_orientation="h", # h:horizontal, v
                  xaxis_title="Years",
                  yaxis_title="Crimes",
                  )
  fig.write_image(cwd+'/Growth_Rate/Women/Top_States_'+str(ele)+'.eps', width = 1000, height = 500)

  #fig.show()


# In[ ]:




