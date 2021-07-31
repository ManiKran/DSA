#!/usr/bin/env python
# coding: utf-8

# In[50]:


class Queue:
    def __init__(self):
        self.items=[]
        self.size=0
    def enqueue(self,data):
        self.items.insert(0,data)
        self.size+=1
        return self.items
    def dequeue(self):
        self.items.pop()
        self.size-=1
        return self.items
q=Queue()


# In[ ]:




