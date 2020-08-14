#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(path)
df


# In[3]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
"drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
"num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
"peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
df


# In[4]:


df.head(5)
df.tail(5)


# In[5]:


df = df.replace("?", np.nan)
df.dropna(subset=["price"], axis=0, inplace = True)
df.head()


# In[6]:


missing_data = df.isnull()
missing_data.head(5)


# In[8]:


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")


# In[9]:


mean_stroke = df["stroke"].astype("float").mean(axis=0)
print(mean_stroke)
df["stroke"].replace(np.nan, mean_stroke)


# In[10]:


df.dtypes


# In[11]:


df["price"] = df["price"].astype(float)
df.dtypes


# In[20]:


df.to_csv("used_car.csv", index=False)

