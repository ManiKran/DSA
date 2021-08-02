#!/usr/bin/env python
# coding: utf-8

# In[22]:


from collections import deque 

class Node: 
        def __init__(self, data): 
            self.data=data 
            self.right=None 
            self.left=None

n1=Node(20)  
n2=Node(50) 
n3=Node(10) 
n4=Node(9) 
n5=Node(15)  
n6=Node(55) 
n7=Node(60) 

n1.left = n3 
n1.right = n2 
n2.left=n6
n2.right=n7
n3.left=n4
n3.right=n5


def breadth_first_traversal(root): 
            list_of_nodes = [] 
            traversal_queue = deque([root]) 
            while len(traversal_queue) > 0:
                node = traversal_queue.popleft() 
                list_of_nodes.append(node.data) 
                if node.left: 
                     traversal_queue.append(node.left) 
                if node.right: 
                      traversal_queue.append(node.right) 
            return list_of_nodes 

print(breadth_first_traversal(n1))


# In[ ]:





# In[ ]:




