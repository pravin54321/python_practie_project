#!/usr/bin/env python
# coding: utf-8

# In[26]:


arr=[10,20,5,50,40]
l=len(arr)
i=0
x=[]
temp=0
for i in range(0,l):
    for j in range(i+1,l):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp

print(arr)    


# In[ ]:




