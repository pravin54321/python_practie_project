#!/usr/bin/env python
# coding: utf-8

# In[7]:



class P:
    def m1(self):
        print('method m1')
class C(p):
    def m2(p):
        print("method m2")
c=C()
c.m1()


# 

# In[10]:


#multiple inhiratance
class P:
    def m1(self):
        print("m1 function")
class C(p):
    def m2(self):
        print("me function")
class CC(C):
    def m3(self):
        print("m3 function")

c=CC()
c.m1()
c.m2()
c.m3()


# In[21]:


#hierachical method

class P:
    def m4(self):
        print("parent method")
class C1(P):
    def m2(self):
        print("child method")
class C2(P):
    def m3(self):
        print("sub child method")
        
c=C2()
c.m3()
c.m4()


# In[28]:


#multiple inhiratance
class P1:
    def m1(self):
        print("p1 method")
class P2:
    def m2(self):
        print("p2 method")
class C(P2,P1):
    def m3(self):
        print("child method")
c=C()
c.m1()
c.m2()
c.m3()
    


# In[34]:


#hybrid inhiritance
class A:
    def m1(self):
        print("function m1")
class B(A):
    pass
class C(A):
  pass
class D(B,C):
   pass
d=D()
d.m1()
        
    

