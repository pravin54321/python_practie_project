#!/usr/bin/env python
# coding: utf-8

# In[4]:


num =int(input("Enter Number"))
fact=1
for num in range(1,num+1):
    fact=fact*num
    num-=1
print(fact)    


# In[15]:


def fact(n):
    
    if n<0:
        return 0
    elif n==1 or n==0:
        return 1
    else:
        facts=1
        while n>0:
            facts=facts*n
            n=n-1
        return facts
print(fact(6))        


# In[ ]:





# In[ ]:





# In[13]:


n=5
facts=1
while n>0:
            facts=facts*n
            n=n-1
print(facts)            
           


# In[21]:


for i in range(6,0,-1):
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




