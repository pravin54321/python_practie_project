#!/usr/bin/env python
# coding: utf-8

# In[8]:


from abc import *
class P(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
class C(P):
    def m1(self):
        print("m1 implimentation")
    def m3(self):
        print("m3 is simpale class")
class E(C):
    def m2(self):
        print("implimentation of m2 class")
    
c=E()
c.m1()
c.m3()
c.m3()


# In[25]:


# duck philosophy
class A:
    def m1(self):
        print("class A")
    
        
class B:
    def m1(self):
        print("class B")
class C:
    def m1(self):
        print("class c")       
class D:
    def m1(self):
        print("class A")  
def f(obj):
    obj.m1
l=[A(),B(),C(),D()]
for obj in l:pass
 #print(f(A()))
f(A())


# In[ ]:




