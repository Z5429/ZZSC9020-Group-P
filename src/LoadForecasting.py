#!/usr/bin/env python
# coding: utf-8

# In[5]:


#conda install -c conda-forge ydata-profiling


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import datetime
from ydata_profiling import ProfileReport


# In[3]:


def load_demand_data():
    return pd.read_csv(Path("C:/Users/User/Documents/UNSW_Data Science 7446/ZZSC9020 Data Science Capstone Project/Data/Total Demand/totaldemand_nsw.csv"))


# In[4]:


totalDemand = load_demand_data()


# In[5]:


totalDemand.head()


# In[6]:


totalDemand.describe()


# In[7]:


totalDemand.shape


# In[8]:


def load_temperature_data():
    return pd.read_csv(Path("C:/Users/User/Documents/UNSW_Data Science 7446/ZZSC9020 Data Science Capstone Project/Data/Temperature/temperature_nsw.csv"))


# In[9]:


temperature = load_temperature_data()


# In[10]:


temperature.head()


# In[11]:


temperature.describe()


# In[12]:


temperature.shape


# In[13]:


dem_temp = pd.merge(temperature, totalDemand, on = 'DATETIME', how='outer')


# In[14]:


dem_temp.head()


# In[15]:


dem_temp.describe()


# In[16]:


dem_temp_inner = pd.merge(temperature, totalDemand, on = 'DATETIME')


# In[17]:


dem_temp_inner.describe()


# In[18]:


dem_temp_inner.head()


# In[19]:


dem_temp_inner.hist(bins=50, figsize=(20, 15))
plt.show()


# In[20]:


#sns.color_palette("Set2")
sns.scatterplot(data=dem_temp_inner, x="TEMPERATURE", y="TOTALDEMAND",  palette="pastel")
#sns.color_palette("Set2")
plt.show()


# In[21]:


def load_forecast_data():
    return pd.read_csv(Path("C:/Users/User/Documents/UNSW_Data Science 7446/ZZSC9020 Data Science Capstone Project/Data/Forecast Demand/forecastdemand_sa.csv"))


# In[22]:


forecastDemand = load_forecast_data()


# In[23]:


forecastDemand.shape


# In[24]:


forecastDemand.head()


# In[25]:


forecastDemand = forecastDemand[forecastDemand['REGIONID'] == 'SA1']


# In[26]:


forecastDemand.shape


# In[27]:


forecastDemand.head()


# In[28]:


forecastDemand['REGIONID'] == 'SA1'


# In[29]:


forecastDemand.dtypes


# In[30]:


forecastDemand['REGIONID'] == 'NSW1'


# In[31]:


dem_temp_inner['DATETIME'] = pd.to_datetime(dem_temp_inner['DATETIME'])


# In[32]:


dem_temp_inner.dtypes


# In[33]:


dem_temp_inner['day'] = dem_temp_inner['DATETIME'].dt.day
dem_temp_inner['month'] = dem_temp_inner['DATETIME'].dt.month
dem_temp_inner['year'] = dem_temp_inner['DATETIME'].dt.year
dem_temp_inner['hour'] = dem_temp_inner['DATETIME'].dt.hour
dem_temp_inner['date'] = dem_temp_inner['DATETIME'].dt.date
dem_temp_inner['weekday'] = dem_temp_inner['DATETIME'].dt.weekday
dem_temp_inner['day_name'] = dem_temp_inner['DATETIME'].dt.day_name()
#dem_temp_inner['date + hour'] = str(dem_temp_inner['DATETIME'].dt.date) + str(dem_temp_inner['DATETIME'].dt.hour)


# In[34]:


dem_temp_inner.head()


# In[35]:


grouped_hour = dem_temp_inner.groupby('hour')


# In[36]:


grouped_hour.head()


# In[37]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.date])["TEMPERATURE", "TOTALDEMAND"].mean()


# In[38]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.date])["TEMPERATURE"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[39]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.date])["TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[40]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.date])["TEMPERATURE", "TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[41]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TEMPERATURE"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[42]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[43]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.month])["TEMPERATURE"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[44]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.month])["TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[45]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TEMPERATURE", "TOTALDEMAND"].mean()


# In[46]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TEMPERATURE", "TOTALDEMAND"].median()


# In[47]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TEMPERATURE", "TOTALDEMAND"].count()


# In[48]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.month])["TEMPERATURE", "TOTALDEMAND"].count()


# In[49]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day])["TEMPERATURE", "TOTALDEMAND"].count()


# In[50]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day_name()])["TEMPERATURE", "TOTALDEMAND"].count()


# In[51]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day_name()])["TEMPERATURE", "TOTALDEMAND"].mean()


# In[52]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day_name()])["TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[53]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day_name()])["TEMPERATURE"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[54]:


dem_temp_inner.groupby(['year', 'month'])["TEMPERATURE", "TOTALDEMAND"].mean()


# In[55]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby(['year', 'month'])["TEMPERATURE"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[56]:


dem_temp_inner.groupby(['year', 'month'])["TEMPERATURE", "TOTALDEMAND"].count()


# In[57]:


profile = ProfileReport(dem_temp_inner, title="Pandas Profiling Report")


# In[58]:


profile


# In[59]:


dem_temp_inner.groupby(['year','month'])["TEMPERATURE", "TOTALDEMAND"].mean()


# In[60]:


dem_temp_inner.groupby(['year','month'])["TEMPERATURE"].min()


# In[61]:


dem_temp_inner.groupby(['year','month'])["TEMPERATURE"].max()


# In[63]:


temp_dem =dem_temp_inner.groupby(['year', 'month'])["TEMPERATURE", "TOTALDEMAND"].mean()


# In[65]:


temp_dem.to_csv('C:/Users/User/Documents/UNSW_Data Science 7446/ZZSC9020 Data Science Capstone Project/Data/temp_dem.csv', index=False)


# In[ ]:









