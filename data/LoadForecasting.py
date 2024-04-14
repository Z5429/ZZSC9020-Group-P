#!/usr/bin/env python
# coding: utf-8

# In[93]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import datetime


# In[94]:


def load_demand_data():
    return pd.read_csv(Path("C:/Users/User/Documents/UNSW_Data Science 7446/ZZSC9020 Data Science Capstone Project/Data/Total Demand/totaldemand_nsw.csv"))


# In[95]:


totalDemand = load_demand_data()


# In[96]:


totalDemand.head()


# In[97]:


totalDemand.describe()


# In[98]:


totalDemand.shape


# In[99]:


def load_temperature_data():
    return pd.read_csv(Path("C:/Users/User/Documents/UNSW_Data Science 7446/ZZSC9020 Data Science Capstone Project/Data/Temperature/temperature_nsw.csv"))


# In[100]:


temperature = load_temperature_data()


# In[101]:


temperature.head()


# In[102]:


temperature.describe()


# In[103]:


temperature.shape


# In[104]:


dem_temp = pd.merge(temperature, totalDemand, on = 'DATETIME', how='outer')


# In[105]:


dem_temp.head()


# In[106]:


dem_temp.describe()


# In[107]:


dem_temp_inner = pd.merge(temperature, totalDemand, on = 'DATETIME')


# In[108]:


dem_temp_inner.describe()


# In[109]:


dem_temp_inner.head()


# In[110]:


dem_temp_inner.hist(bins=50, figsize=(20, 15))
plt.show()


# In[111]:


#sns.color_palette("Set2")
sns.scatterplot(data=dem_temp_inner, x="TEMPERATURE", y="TOTALDEMAND",  palette="pastel")
#sns.color_palette("Set2")
plt.show()


# In[112]:


def load_forecast_data():
    return pd.read_csv(Path("C:/Users/User/Documents/UNSW_Data Science 7446/ZZSC9020 Data Science Capstone Project/Data/Forecast Demand/forecastdemand_sa.csv"))


# In[113]:


forecastDemand = load_forecast_data()


# In[114]:


forecastDemand.shape


# In[115]:


forecastDemand.head()


# In[116]:


forecastDemand = forecastDemand[forecastDemand['REGIONID'] == 'SA1']


# In[117]:


forecastDemand.shape


# In[118]:


forecastDemand.head()


# In[119]:


forecastDemand['REGIONID'] == 'SA1'


# In[120]:


forecastDemand.dtypes


# In[121]:


forecastDemand['REGIONID'] == 'NSW1'


# In[122]:


dem_temp_inner['DATETIME'] = pd.to_datetime(dem_temp_inner['DATETIME'])


# In[123]:


dem_temp_inner.dtypes


# In[168]:


dem_temp_inner['day'] = dem_temp_inner['DATETIME'].dt.day
dem_temp_inner['month'] = dem_temp_inner['DATETIME'].dt.month
dem_temp_inner['year'] = dem_temp_inner['DATETIME'].dt.year
dem_temp_inner['hour'] = dem_temp_inner['DATETIME'].dt.hour
dem_temp_inner['date'] = dem_temp_inner['DATETIME'].dt.date
dem_temp_inner['weekday'] = dem_temp_inner['DATETIME'].dt.weekday
dem_temp_inner['day_name'] = dem_temp_inner['DATETIME'].dt.day_name()
#dem_temp_inner['date + hour'] = str(dem_temp_inner['DATETIME'].dt.date) + str(dem_temp_inner['DATETIME'].dt.hour)


# In[169]:


dem_temp_inner.head()


# In[170]:


grouped_hour = dem_temp_inner.groupby('hour')


# In[171]:


grouped_hour.head()


# In[172]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.date])["TEMPERATURE", "TOTALDEMAND"].mean()


# In[173]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.date])["TEMPERATURE"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[174]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.date])["TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[175]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.date])["TEMPERATURE", "TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[176]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TEMPERATURE"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[177]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[178]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.month])["TEMPERATURE"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[179]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.month])["TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[180]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TEMPERATURE", "TOTALDEMAND"].mean()


# In[181]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TEMPERATURE", "TOTALDEMAND"].median()


# In[182]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.year])["TEMPERATURE", "TOTALDEMAND"].count()


# In[183]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.month])["TEMPERATURE", "TOTALDEMAND"].count()


# In[184]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day])["TEMPERATURE", "TOTALDEMAND"].count()


# In[185]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day_name()])["TEMPERATURE", "TOTALDEMAND"].count()


# In[188]:


dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day_name()])["TEMPERATURE", "TOTALDEMAND"].mean()


# In[189]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day_name()])["TOTALDEMAND"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[190]:


fig, axs = plt.subplots(figsize=(12, 4))

dem_temp_inner.groupby([dem_temp_inner["DATETIME"].dt.day_name()])["TEMPERATURE"].mean().plot(
    kind='line', rot=0, ax=axs
)


# In[ ]:




