#!/usr/bin/env python
# coding: utf-8

# In[8]:


str="pravin sharad mendhe"
s=str.split(' ')
repl_word={'pravin':'sir','sharad':'thank','mendhe':'lakhandur'}
res=set()
for idx,ele in enumerate(s):
    if ele in repl_word:
        if ele in res:
            s[idx] = repl_word[ele]
        else:
            res.add(ele)
    res = ' '.join(s)
    print(res)


# In[ ]:




