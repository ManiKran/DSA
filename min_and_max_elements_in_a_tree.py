#!/usr/bin/env python
# coding: utf-8

# In[35]:


class Node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
class binary_tree:
    def __init__(self):
        self.root=None
        self.temp=None
        self.temp_pre=None
        self.temp_pos=None
    
    #adding nodes to the binary tree
    def add_node(self,data):
        if self.root is None:
            self.root=Node(data,None,None)
            self.temp=self.temp_pre=self.temp_pos=self.root
            return
        while self.temp is not None:
            if data<self.temp.data:
                d=self.temp
                self.temp=self.temp.left
            else:
                d=self.temp
                self.temp=self.temp.right
        self.temp=self.root
        if data<d.data:
            d.left=Node(data,None,None)
        else:
            d.right=Node(data,None,None)
    def min_element(self):
        itr=self.root
        while itr.left is not None:
            itr=itr.left
        print("min element",itr.data)
        itr=self.root
        while itr.right is not None:
            itr=itr.right
        print("max element",itr.data)
bt=binary_tree()
bt.add_node(23)
bt.add_node(34)
bt.add_node(74)
bt.add_node(32)
bt.add_node(65)
bt.add_node(72)
bt.add_node(52)
bt.add_node(43)
bt.add_node(47)
bt.add_node(83)
bt.add_node(10)
bt.min_element()


# In[ ]:





# In[ ]:




