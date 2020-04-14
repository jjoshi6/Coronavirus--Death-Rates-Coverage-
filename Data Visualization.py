#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

#get_ipython().run_line_magic('matplotlib', 'inline')


# In[84]:


data = pd.read_csv("data.csv")


# In[85]:


sns.catplot(x="Country, Other", y="Total Cases", data=data, kind="bar" )


# In[86]:


data


# In[185]:


data['New Cases'].fillna('0', inplace=True)
data.fillna(0, inplace=True)


# In[186]:


data


# In[105]:


new_data=data.head(10)


# In[106]:


new_data


# In[127]:


sns.catplot(x="Country, Other", y="Total Cases", data=new_data, kind="bar" )
sns.catplot(x="Total Cases", y="Country, Other", data=new_data, kind="bar" )


# In[188]:


data1=data.drop(data.index[[0]])
data1


# In[198]:


new_data=data1.head(10)
new_data


# In[202]:


sns.set(style="dark")
sns.catplot(x="Country, Other", y="Total Cases", data=new_data, kind="bar", height=11, aspect=1 )
sns.catplot(x="Country, Other", y="Active Cases" ,data=new_data, kind="bar",height=8, aspect=3)
sns.catplot(x="Country, Other", y="Total Recovered" ,data=new_data, kind="bar",height=8, aspect=3)


# In[199]:


f, ax = plt.subplots(figsize=(25, 6))


sns.set_color_codes("pastel")
sns.barplot(x="Country, Other", y="Total Cases", data=new_data,
            label="Total", color="black")

# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="Country, Other", y="Active Cases", data=new_data, label="Active", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="deaths")
sns.despine(left=True, bottom=True)


# In[203]:


f, ax = plt.subplots(figsize=(25, 6))


sns.set_color_codes("pastel")
sns.barplot(x="Country, Other", y="Total Cases", data=new_data,
            label="Total", color="black")

# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="Country, Other", y="Active Cases", data=new_data, label="Active", color="b")

sns.set_color_codes("muted")
sns.barplot(x="Country, Other", y="Total Recovered", data=new_data, label="Recovery", color="pink")

# Add a legend and informative axis label
ax.legend(loc="lower right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="deaths")
sns.despine(left=True, bottom=True)

plt.show(block=True)

# In[ ]:




