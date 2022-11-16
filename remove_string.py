#!/usr/bin/env python
# coding: utf-8

# In[22]:


string="pravin"
i=4
a = string[ : i] 
b = string[i + 1: ]
print(a+b)


# In[41]:


def str(string1,i):
    for j in range(len(string1)):
        if j==i:
            string1=string1.replace(string1[i],"")
    return string1
string1="pravin"
i=4
print(str(string1,i))


# In[ ]:




