#!/usr/bin/env python
# coding: utf-8

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[21]:


data=pd.read_csv('headbrain.csv')
print(data.shape)
data.head()


# In[22]:


X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values


# In[23]:


mean_x=np.mean(X)
mean_y=np.mean(Y)
max_x=np.max(X)+100
min_x=np.min(X)-100
l=len(X)
print(mean_x)
print(mean_y)
print(l)


# In[24]:


numer=0
denom=0
for i in range(l):
    numer+=(X[i]-mean_x)*(Y[i]-mean_y)
    denom+=(X[i]-mean_x)**2
    b1=numer/denom
    b0=mean_y-(b1*mean_x)
print(b1)
print(b0)


# In[25]:


x=np.linspace(min_x,max_x,1000)
y=b0+b1*x


# In[27]:


plt.plot(x,y,color='red',label='Regression Line')
plt.scatter(X,Y,color='black',label='Scatter plot')
plt.xlabel('Head and Brain')
plt.ylabel('Brain Weight')
plt.legend()
plt.show()


# In[29]:


ss_tot = 0
ss_res = 0
for i in range(l):
    y_pred = b0 + b1 * X[i]
    ss_tot += (Y[i] - mean_y) ** 2
    ss_res += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_res/ss_tot)
print("R2 Score")
print(r2)


# In[ ]:




