#!/usr/bin/env python
# coding: utf-8

# In[18]:


from collections import deque

class Node:
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
        
class avl_trees:
    
    def __init__(self):
        self.root=None
        self.temp=None
        
    def add_node(self,d):
        if self.root==None:
            self.root=Node(d,None,None)
            return
        
        self.temp=self.root
        
        while(1):
            if self.temp.data>d:
                if self.temp.left is None:
                    self.temp.left=Node(d,None,None)
                    break
                self.temp=self.temp.left

            else:
                if self.temp.right is None:
                    self.temp.right=Node(d,None,None)
                    break
                self.temp=self.temp.right
                
        self.temp=self.root
                
    
    def breadth_first_traversal(self): 
            list_of_nodes = [] 
            traversal_queue = deque([self.root]) 
            while len(traversal_queue) > 0:
                node = traversal_queue.popleft() 
                list_of_nodes.append(node.data) 
                if node.left: 
                     traversal_queue.append(node.left) 
                if node.right: 
                      traversal_queue.append(node.right) 
            return list_of_nodes 

nodes=[40,20,10,25,30,22,50]
l=[]

def optimi(nodes,l):
    if len(nodes)==0:
        return l
    nodes.sort()
    
    if len(nodes)%2==0:
        l.append(nodes[(len(nodes)//2)-1])
        l=optimi(nodes[:(len(nodes)//2)-1],l)
        l=optimi(nodes[(len(nodes)//2):],l)
    else:
        l.append(nodes[(len(nodes)//2)])
        l=optimi(nodes[:(len(nodes)//2)],l)
        l=optimi(nodes[(len(nodes)//2)+1:],l)
        
    return l

avl=avl_trees()


for i in optimi(nodes,l):
    avl.add_node(i)

print(avl.breadth_first_traversal())
             


# In[ ]:





# In[ ]:





# In[ ]:




