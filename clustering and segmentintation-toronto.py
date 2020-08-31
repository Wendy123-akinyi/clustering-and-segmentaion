#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df=pd.read_html('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M')
df


# In[11]:


type(df)


# In[15]:


new_df=pd.DataFrame(df)
new_df


# In[22]:


new_df.replace('Not assigned:Neighborhood',inplace=True)


# In[23]:


new_df.dropna(inplace=True)


# In[25]:


new_df.head()


# In[27]:


new_df.shape


# In[ ]:




