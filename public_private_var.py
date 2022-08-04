#!/usr/bin/env python
# coding: utf-8

# In[2]:


#protected
class Test:
    _x=10
    def __init__(self):
        self._y=20
t=Test()
print(t._x)#protected access only inside class & child class it is only therotically not practicaly


# In[5]:


#private
class Test1:
    __x1=10
    def __init__(self):
        self.__y=20
t=Test1()
#print(t.__x1) #not access outside the class
print(t.__dict__)
print(t._Test1__y)# this method access outside the class


# In[8]:


#intraface
from abc import *
class Db:
    @abstractmethod
    def connect(self):pass
    @abstractmethod
    def disconnect(self):
        pass
class Oracle(Db):
    def connect(self):
        print("it connect")
    def disconnect(self):
        print("disconnect")
o=Oracle()
o.connect()
o.disconnect()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




