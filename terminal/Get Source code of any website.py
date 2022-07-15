#!/usr/bin/env python
# coding: utf-8

# In[8]:


## the library used

import urllib.request as urw


# In[50]:


## goal.com is the name of the website

website = input('Enter the name of the website:  ')


source = str(ur.urlopen('https://'+website).read())


# In[55]:


## papa.csv will save the source of the file


file = 'papa.csv'
with open (file,'w') as f:
    f.write(source)

