#!/usr/bin/env python
# coding: utf-8

# In[7]:


a="pravin sharad mendhe bit"
b="pravin sharad mendhe lakhandur"
x=a.split()
print(x)
y=b.split()
print(y)
uncommomn=[]
for i in x:
    if i not in y:
        uncommomn.append(i)
for j in y:
    if j not in x:
        uncommomn.append(j)
print(uncommomn)        


# In[13]:


A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
count={}
for word in A.split():
    x=count[word]=count.get(word,0)+1
    print(x)
for word in B.split():
    e=count[word]=count.get(word,0)+1
    print(e)
z= [word for word in count if count[word] == 1]
print(z)
    


# In[ ]:





# In[ ]:





# In[ ]:




