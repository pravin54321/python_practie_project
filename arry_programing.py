#!/usr/bin/env python
# coding: utf-8

# In[5]:


arr=[1,2,3]
sum=0
for i in arr:
    sum+=i
print(sum)


# In[13]:



numbers = [1,2,3,4,5,1,4,5]
 
# start parameter is not provided
Sum = sum(numbers)
print(Sum)
 

Sum = sum(numbers, 10)
print(Sum)


# In[18]:


from functools import reduce
def sum(arr):
    sum=reduce(lambda a,b:a+b,arr)
    return(sum)
arr=[1,2,3,4,5]
print(sum(arr))


# In[ ]:




