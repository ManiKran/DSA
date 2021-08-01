#!/usr/bin/env python
# coding: utf-8

# In[18]:


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
            
    #inorder traversal in a binary tree        
    def inorder(self):
        itr=self.temp
        while itr is not None:
            if itr.left:
                self.temp=itr.left
                self.inorder()
            print(itr.data)
            if itr.right:
                self.temp=itr.right
                self.inorder()
            return
    
    #preorder traversal in a binary tree    
    def preorder(self):
        itr=self.temp_pre
        while itr is not None:
            print(itr.data)
            if itr.left:
                self.temp_pre=itr.left
                self.preorder()
            if itr.right:
                self.temp_pre=itr.right
                self.preorder()
            return
        
    #postorder traversal in a binary tree
    def postorder(self):
        itr=self.temp_pos
        while itr is not None:
            if itr.left:
                self.temp_pos=itr.left
                self.postorder()
            if itr.right:
                self.temp_pos=itr.right
                self.postorder()
            print(itr.data)
            return
    
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
print("Inorder")
bt.inorder()
print("preorder")
bt.preorder()
print("postorder()")
bt.postorder()


# In[ ]:





# In[ ]:




