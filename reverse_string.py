#!/usr/bin/env python
# coding: utf-8

# In[13]:


str="pravin sharad mendhe"
x=str.split()[::-1]
print(x)
l=[]
for i in x:
    print(i)
    l.append(i)
print(" ".join(l))    
print(l)    


# In[16]:


words="pravin mendhe"
for i in range(len(words)-1, -1, -1):
    print(words[i])


# In[18]:


str ="pravin"
new_str=""
for i in range(len(str)):
    if i!=2:
        new_str=new_str+str[i]
print(new_str)        
        


# In[ ]:





# In[ ]:




