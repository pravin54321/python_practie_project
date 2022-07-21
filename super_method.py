#!/usr/bin/env python
# coding: utf-8

# # super  method

# In[18]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
        print(self.age)
    
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display(self):    
        super().display()
        print(self.rollno)
        print(self.marks)

s=Student("durga",10,12,101)
s.display()


# In[21]:


class P:
    a=10
    def __init__(self):
            self.b=20
    def m1(self):
        print("instance method")
    @classmethod
    def m2(cls):
        print("class method")
    @staticmethod
    def m3():
        print("static method")
class C(P):
    a=888
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
c=C()        


# In[27]:


class A:
    def m1(self):
        print("class A")
class B(A):
    def m1(self):
        print("class B")
class C(B):
    def m1(self):
        print("class c")
class D(C):
    pass
class E(D):
    def m1(self):
        super(B,self).m1()
e=E() 
e.m1()
        


# In[34]:


class P:
    a=10
    def __init__(self):
      self.b=20
class C(P):
    def m1(self):
        print(self.b)
        
        
c=C()
c.m1()


# In[37]:


class E:
    a=10
    def __init__(self):
        self.b=20
class P(E):
    def m1(self):
        print(self.b)
        self.b=888
       
        print(self.b)
        super().__init__()
        print(self.b)
a=P()
a.m1()

