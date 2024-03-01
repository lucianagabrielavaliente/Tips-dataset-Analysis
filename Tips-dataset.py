#!/usr/bin/env python
# coding: utf-8

# In[81]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


tips = sns.load_dataset("tips")
tips.head()


# In[21]:


sns.displot(tips["total_bill"], bins=40)


# In[29]:


sns.set_theme(style="ticks")
sns.jointplot(x="total_bill",y="tip", data=tips, kind="scatter")


# In[30]:


sns.barplot(x="sex",y="total_bill",data=tips)


# In[33]:


sns.set_theme(style="ticks", palette="pastel")
sns.boxplot(x="day",y="tip",data=tips)


# In[80]:


day = tips.groupby("day")
day.describe()[["total_bill"]]


# In[48]:


day = tips.groupby("day")
day.count()[["smoker"]]


# In[ ]:




