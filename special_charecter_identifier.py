#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re
str="pravin Shar:ad Mendhe"
str2=re.compile('[:]')
if (str2.search(str)== None):
    print("string is accepted")
else:
    print("string is not accepted")


# In[15]:


str3="pravi@n sharad: mendhe"
str3.split()
#print(str3)
s="@:"
c=0
for i in range(len(str3)):
    if str3[i] in s:
        c=c+1
print(c)
if c>0:
    print("not accepted")
else:
    print("accepted")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




