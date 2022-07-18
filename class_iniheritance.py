#!/usr/bin/env python
# coding: utf-8

# In[15]:


class person:
    def __init__(self ,name,age):
        self.name=name
        self.age=age
    def eat(self):
            print("brani")
class Emplyee(person):
            def __init__(self,name,age,eno,esal):
                super().__init__(name,age)
                self.eno=eno
                self.esal=esal
            def work(self):
                print("pyton codin")
            def enpinfo(self):
                print(self.name)
                print(self.age)
                print(self.eno)
                print(self.esal)
                
                
            
e=Emplyee("durga",32,877,1000)
e.eat()
e.work()
e.enpinfo()


                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                


# In[ ]:




