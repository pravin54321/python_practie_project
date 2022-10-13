#!/usr/bin/env python
# coding: utf-8

# In[13]:


def max_value(n,arr):
    x=arr[0]
    for i in range(1,n):
        if arr[i]>x:
            x=arr[i]
        
    return x
arr= [10,20,30,40,50,400,55,72,34]
n=len(arr)
arr.sort()
print(arr)


# In[14]:


def mota_number(arr,n):
    arr.sort()
    return arr[n-1]
arr= [10,20,30,40,50,400,55,72,34]
n=len(arr)
print(mota_number(arr,n))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


arr= [10,20,30,40,50,400,55,72,34]
print(arr.sort())


# In[ ]:





# In[ ]:





# In[ ]:




