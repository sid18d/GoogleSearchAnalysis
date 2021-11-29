#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Google search analysis with Python.


# In[10]:


import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()              

# Loading necessary libraries


# In[14]:



trends.build_payload(kw_list=["Artificial Intelligence"])      # Preparing Keywords to get the data for
data = trends.interest_by_region()                             # Returns data for where the keyword is most searched
data = data.sort_values(by="Artificial Intelligence", ascending=False)
data = data.head(10)
print(data)                                                    # Loading the data 


# In[15]:


data.reset_index().plot(x="geoName", y="Artificial Intelligence", 
                        figsize=(20,15), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()                                                      # visualizing the data


# In[16]:


data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Artificial Intelligence'])
data = data.interest_over_time()                                      # Returns historical, indexed data
fig, ax = plt.subplots(figsize=(20, 15))
data['Artificial Intelligence'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Artificial Intelligence', fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()


# In[ ]:




