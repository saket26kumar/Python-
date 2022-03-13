#!/usr/bin/env python
# coding: utf-8

# In[1]:


element={"hydrogen":1,"helium":2,"carbon":6,"oxygen":8}
element.items()


# In[2]:


element["helium"]


# In[3]:


element["lithium"]=3
element


# In[4]:


print("carbon" in element)


# In[5]:


element.keys()


# In[6]:


element.values()


# In[7]:


n=7
if(n%2==0):
    print("even")
else:
    print("odd")


# In[8]:


n=7
if(n%2==0):
    print("number" + str(n) + "is even")
else:
    print("number " +str(n)+ " is odd")      ##strn(n) is typecasting. to convert number into string


# In[9]:


for i in range(0,11):
    print(i)


# In[10]:


cities=["delhi","patna","kolkata","bangalore","ranchi"]
for city in cities:
    print(city)

print("end")


# In[11]:


cities=["delhi","patna","kolkata","bangalore","ranchi"]
capitalized_cities=[]

for city in cities:
    capitalized_cities.append(city.title()) 
print(capitalized_cities)                  ## here i took capitalized city as empty list using the help of for loop 
                                                   ## added with the cities and again used for loop to store in cap_city     
## for new paragraph
for cap_city in capitalized_cities:
    print(cap_city)


# In[12]:


for cap_city in capitalized_cities:
    print(cap_city)


# In[13]:


cities=["delhi","patna","kolkata","bangalore","ranchi"]
d_cities=[1,2]
cities.append(d_cities)
print(cities)


# # iteration of dictionaries with for loop
# 
# 

# In[14]:


element={"hydrogen":1,"helium":2,"carbon":6,"oxygen":8,"lithium":3}
element
element.keys()
element.values()


# In[15]:


for key in element:
    print(key)


# In[16]:


for key,value in element.items():
    print("name : {} & atomic_number : {}" .format(key,value))


# 
# # while loop

# In[24]:


card_deck= [4,11,8,5,13,2,6,10]
hand= []
while sum(hand)<17:
    hand.append(card_deck.pop())
for card in hand:
    print(card)


# In[25]:


card_deck= [4,11,8,5,13,2,6,10]
hand= []
while sum(hand)<17:
    hand.append(card_deck.pop())
    print(hand)


# In[26]:


fruits=["orange","strawberry","apple"]
foods=["apple","apple","burger","toast"]
fruit_count=0
for food in foods:
    if food not in fruits:
        print("not a fruit")
        continue
    fruit_count+=1
    print("found a fruit!!")
print("total fruits :", fruit_count)


# 
# # functions in python

# In[29]:


def hello():
    print("hello")
hello()
hello()


# In[31]:


def shapeAI():
    for i in range(0,10):
        print("saket")
shapeAI()


# In[33]:


def shapeAI(name):
    for i in range(0,10):
        print(name)
shapeAI("kumar")


# In[37]:


def add(a,b):
    print(a+b)
add(6,8)


# In[39]:


def divide(a,b):
    print(a/b)
divide(16,8)                 #by positioniwse
divide(a=16,b=2)             #by namewise          we can do in both way to call a function


# In[40]:


def add(a,b):
    return a+b
sum=add(5,6)
print(sum)


# In[47]:


def fun(a,b):
   
    sum=a+b
    diff=a-b
    return sum,diff
sum,diff= fun(10,5)

print(sum)
print(diff)


# In[48]:


def simple_interest(p,r,t):
    return (p*r*t/100)
simple_interest(100,5,5)


# In[51]:


# WAP to create the factorial of a number

factorial(n)=n*factorial(n-1)
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
factorial(n)


# In[56]:


#factorial(n)=n*factorial(n-1)
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
factorial(4)


# In[ ]:




