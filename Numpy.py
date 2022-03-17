#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import numpy as np


# In[2]:


x=np.random.rand(100)
x


# In[3]:


x1=np.zeros((3,4))
print(x1)                  #this value in float


# In[4]:


x1=np.zeros((3,4),dtype=np.int64)
print(x1)                               #this value in integer


# In[5]:


x1=np.ones((3,4),dtype=np.int64)
print(x1) 


# In[6]:


x1=np.full((3,4), 5,dtype=np.int64)
print(x1) 


# In[7]:


x1=np.full((3,4),5)
print(x1)                   #in full function array will be in integer form only


# In[8]:


x1=np.identity(5)
x1


# In[9]:


x1=np.identity(3)
x1


# In[10]:


x=np.diag([10,20,30,40])
x


# In[11]:


x=np.arange(15)
x


# In[12]:


x=np.arange(1,5)
x


# In[13]:


x=np.linspace(1,20,3)
x


# In[25]:


x=np.linspace(1,20,3, endpoint=False)
x


# In[21]:


x=np.arange(20)
np.reshape(x,(5,4))    #it willconvert into matrix of given range 1-19


# In[27]:


x=np.linspace(0,50,10,endpoint=False).reshape(5,2)
x


# In[29]:


x=np.linspace(0,50,10,endpoint=False)
np.reshape(x,(5,2))


# In[32]:


x=np.random.rand(3,3)
x


# In[33]:


x=np.random.randint(3,9 , size=(3,2))
x


# In[37]:


x=np.random.randint(3,12 , size=(3,2))
x


# In[40]:


x=np.random.normal(2, 0.5 , size=(3,2))
x


# In[41]:


x=np.array([[1,2,3],[4,5,6],[7,8,9]])
x


# In[44]:


x[2,1]


# In[53]:


x=np.array([[1,2,3],[4,5,6],[7,8,9]])
x[1,1]=6
x


# In[55]:


x=np.array([1,2,3,4,5,6,7,8,9])

np.delete(x,2)
np.delete(x,(3,7))


# In[59]:


y=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.delete(y,2,axis=0)
np.delete(y,(1,2),axis=0)
np.delete(y,(1,2),axis=1)


# In[60]:


x=np.arange(30).reshape(5,6)
x


# In[61]:


x[x>20]


# In[65]:


x=np.arange(30).reshape(5,6)
np.sort(x,axis=0)


# In[ ]:


x=np.arange(30).reshape(5,6)
x

