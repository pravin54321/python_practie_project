#!/usr/bin/env python
# coding: utf-8

# In[14]:



def ispolindron(str):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
x="gog"
ans=ispolindron(x)
if (ans):
    print("yes")
else:
    print("no")


# In[26]:


x = "pra"
 
w = ""
for i in x:
    w=i+w
print(w)
if(x==w):
    print("ispolindron")
else:
    print("isNotPolindrom")


# In[ ]:





# In[ ]:




