#!/usr/bin/env python
# coding: utf-8

# In[11]:


from nsepython import *   
print(indices)


# In[10]:


import requests
import json
import pandas as pd
import nsepython


# In[31]:


with open ('selected.txt',"r") as f:
    selected_sc = f.readlines()
    selected_sc = [x.replace('\n', '') for x in selected_sc]
    portfolio = {x.split(',')[0]: float(x.split(',')[1]) for x in selected_sc}


# In[32]:


positions = nsefetch('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')
df = pd.DataFrame(positions['data'])


# In[54]:


df = df[df['symbol'].isin(portfolio.keys())][['symbol', 'lastPrice']]
df['bought_price'] = df['symbol'].map(portfolio)
df['diff_price'] = (df['lastPrice'].astype(float) - df['bought_price'].astype(float))
df['percentage_changes'] = (df['bought_price'].astype(float) - df['diff_price'].astype(float))/10
# Format the percentages changes to display 2 decimal places
df['percentage_changes'] = df['percentage_changes'].apply(
                                lambda x: '{0:.2f}%'.format(x))
df.to_csv('result.csv', index=False)


# In[ ]:




