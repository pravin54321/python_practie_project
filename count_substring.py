#!/usr/bin/env python
# coding: utf-8

# In[7]:


str="pravin sharad mendhe pravin"
s=str.split("pravin")
str2=str.count("pravin")
res = {key: str.count(key) for key in str.split()}
  
print((res),str2)


# In[11]:


from collections import Counter
  
str3="pravin sharad mendhe"

res = Counter(str3.split())
print(res)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




