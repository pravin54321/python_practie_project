#!/usr/bin/env python
# coding: utf-8

# In[7]:


class Student:
    """more information regarding to the  student"""
    pass
help(Student)
print(id(Student))


# In[16]:


class Test:
    def __init__(self):
        self.a=10
    def m1(self):
        self.b=20
        
t1=Test()
t2=Test()
t1.m1()
t2.x=777
print(t2.__dict__)


# In[18]:


class T:
    def __init__(self):
        self.a=10
    def m1(self):
        self.a=777
        self.b=888
t=T()
t.m1()
t.b=999
t.c=1000
print(t.__dict__)

