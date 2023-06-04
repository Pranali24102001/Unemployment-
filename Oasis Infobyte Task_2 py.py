#!/usr/bin/env python
# coding: utf-8

# Oasis Infobyte
# Data Science Internship
# Name: Yadav Pranali Tanaji
# Task 2: Unemployment Analysis Using Python

# Loading Packages And Libraries

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[4]:


data1=pd.read_csv("Unemployment_Rate_upto_11_2020.csv")
print(data1)


# In[5]:


print(data1.describe)


# In[6]:


#see if any missing value in data


# In[7]:


print(data1.isnull().sum())


# In[8]:


#rename all the columns in data sets


# In[11]:


data1.columns=("States","Date","Frequency","Estimated Unemployment Rate",
             "Estimated Employed","Estimated Labour Patricipation Rate","Region","Longitude","Latitude")
print(data1)


# In[12]:


#look at the correlation between the features of this datasets


# In[13]:


plt.style.use("seaborn-whitegrid")
plt.figure(figsize=(12,10))
sns.heatmap(data1.corr())
plt.show()


# In[14]:


#look at the estimated numbers of the employees according to the different region of india


# In[15]:


data1.columns=("States","Date","Frequency","Estimated Unemployment Rate",
             "Estimated Employed","Estimated Labour Patricipation Rate","Region","Longitude","Latitude")
plt.title("Indian Unemployment")
sns.histplot(x="Estimated Employed",hue="Region",data=data1)
plt.show()


# In[16]:


#see the unemployment rate according to the different region india


# In[17]:


plt.figure(figsize=(12,10))
plt.title("Indian Unempoyment")
sns.histplot(x="Estimated Unemployment Rate",hue="Region",data=data1)
plt.show()


# In[20]:


#create a dashboard to analyze unemployment rate of each indian state by region- use sunburst plot


# In[23]:


unemployment=data1[["States","Region","Estimated Unemployment Rate"]]
figure=px.sunburst(unemployment,path=["Region","States"],values="Estimated Unemployment Rate",width=700,height=700,color_continuous_scale="RdY1Gn",title="Unemploymet Rate in India")
figure.show()

