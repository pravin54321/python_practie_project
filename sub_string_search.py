#!/usr/bin/env python
# coding: utf-8

# In[2]:


mystring="pravin sharad mendhe"
if "kas" in mystring:
    print("its present")
else:
    print("its not present")


# In[6]:


str="pravin sharad mendhe"
s=str.split()
print(s)
if "vipin"in s:
    print("its present")
else:
    print("its not present")


# In[12]:


str1="pravin sharad mendhe"
s1="vipin"
print(str1.find(s1))
def substring(str1,s1):
    if (str1.find(s1))==-1:
        print("its not present")
    else:
        print("its  present")
print(substring(str1,s1))


# In[18]:


str2="pravin sharad mendhe"
s2="pravin"
def ispresent(str2,s2):
    if (str.count(s2))>0:
        print("its present")
    else:
        print("not present")
print(ispresent(str2,s2))        


# In[27]:


str3="pravin sharad mendhe"
s3="rahul"
start=0
end=1000
print(str3.index(s3,start,end))


# In[30]:


a = ['Geeks-13', 'for-56', 'Geeks-78', 'xyz-46']
for i in a:
   if i.__contains__("for-56"):
    print(f"yes! {i} is conatining")


# In[ ]:





# In[ ]:





# In[ ]:




