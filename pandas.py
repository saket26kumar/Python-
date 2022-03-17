#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


x=pd.Series(data=[12,3,"yes"], index=["orange","apple","yellow"])   
x


# In[3]:


data={"integer":[1,2,3,4],"float":[1.1,2.2,3.3,4.4]}   #two list together
df=pd.DataFrame(data,index=[0,1,2,3])
df


# In[4]:


data1={"integer":[1,2,3,4]}
data2={"float":[1.1,2.2,3.3,4.4]}
df=pd.DataFrame(data1)
df


# In[5]:


data1={"integer":[1,2,3,4]}
data2={"float":[1.1,2.2,3.3,4.4]}
df=pd.DataFrame(data1,index=["a","b","c","d"])
df


# In[6]:


data1=[1,2,3,4]
data2=[1.1,2.2,3.3,4.4]
df=pd.DataFrame(list(zip(data1,data2)),columns=["integer","float"],index=["A","B","C","D"])   #two sepoerate list with ZIP fn
df


# In[7]:


#two lists are given but first created dict then converted into dataframe
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
dict = {'name': nme, 'degree': deg, 'score': scr} 
df = pd.DataFrame(dict)
df 


# In[8]:


fruit_A={"apple":23,"orange":34,"banana":43,"pineapple":12}
fruit_B={"papaya":56,"lichi":54,"apple":78,"banana":87}
df=pd.DataFrame([fruit_A,fruit_B], index=["A","B"])
df


# In[9]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits)
df


# In[10]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits)
df
df.items #get all values


# In[11]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits)
df.columns #get columns names


# In[12]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits)
df.shape #get row & column


# In[13]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits)
df.ndim #get dimensions


# In[14]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits)
df["apple"]


# In[15]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits)
df["apple"][0]


# # LOC fn

# In[16]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits)
df.loc[[0]]


# In[17]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits)
df.loc[:,["banana"]]    #loc with column use :, but for row simple .low & use [[ ]]


# In[18]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits,index=["f1","f2"])
df.loc[["f1"]]


# In[19]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits,index=["f1","f2"])
df


# In[20]:


fruits=[{"apple":23,"orange":34,"banana":43},{"pineapple":12,"papaya":56,"lichi":54,"apple":78,"banana":87}]
df=pd.DataFrame(fruits,index=["f1","f2"])
asp=df.loc[["f1","f2"],["banana","orange"]]
asp


# In[21]:


data = pd.DataFrame({
    'age' :     [ 10, 22, 13, 21, 12, 11, 17],
    'section' : [ 'A', 'B', 'C', 'B', 'B', 'A', 'A'],
    'city' :    [ 'Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'gender' :  [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'favourite_color' : [ 'red', np.NAN, 'yellow', np.NAN, 'black', 'green', 'red']})
data


# In[22]:


data.loc[data.age==10]     #using loc apllying the condition


# In[23]:


data.loc[1:3]


# In[24]:


data.loc[1:3, "section":"gender"]    #using loc slicing row & column both


# In[ ]:




