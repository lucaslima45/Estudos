#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import pandas
dados = pandas.read_csv('C:/Users/datas/Downloads/arquivooo/athlete_events.csv')


# In[3]:


dados.head()


# In[6]:


masculinos = dados.loc[dados['Sex']=='M']
altura = masculinos['Height']
peso = masculinos['Weight']
plt.scatter(altura,peso)


# In[ ]:




