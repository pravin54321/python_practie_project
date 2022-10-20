#!/usr/bin/env python
# coding: utf-8

# In[14]:


#lambada_function
x=lambda a:a+10
print(x(5))


# In[16]:


y=lambda a,b:a+b
print(y(10,5))


# In[19]:


z=lambda a,b,c:a+b+c
print(z(5,5,5))


# In[22]:


def myfunc(n):
    return lambda a:a*n
x=myfunc(2)
print(x(22))


# In[ ]:





# In[ ]:





# In[ ]:




