#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=4
b=5
maximum=max(a,b)
print(maximum)


# In[5]:


def mximum(a,b):
    if a>=b:
        return a
    else:
        return b
print(mximum(9,5))    


# In[8]:


a=15
b=8
print(a if a>=b else b)


# In[13]:


#lambada
a=10
b=4
m=lambda a,b : a if a>=b else b
print(m(a,b))


# In[16]:


a=10
b=5
x=[a if a>=b else b]
print(x)


# In[ ]:





# In[ ]:





# In[ ]:




