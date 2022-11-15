#!/usr/bin/env python
# coding: utf-8

# In[19]:


str="hello geeks for geeks is computer science portal" 
x=str.split(" ")
k=3
string=[]
for i in x:
    
    if len(i)>k:
        string.append(i)
print(string)        


# In[24]:


sentence = "hello geeks for geeks is computer science portal"
length = 4
x=[word for word in sentence.split()if len(word)>length]
print(x)


# In[ ]:




