#!/usr/bin/env python
# coding: utf-8

# In[33]:


graph=dict()

graph_nodes=['A','B','C','D','E','F','G','H','S']

graph['A']=['B','S']
graph['B']=[]
graph['C']=['D','E','F','S']
graph['D']=[]
graph['E']=['C','H']
graph['F']=['C','G']
graph['G']=['F','H','S']
graph['H']=['E','G']
graph['S']=['A','C','G']


adjacency_matrix=[[0 for i in range(len(graph_nodes))]for j in range(len(graph_nodes))]
    
for i in graph:
    for j in graph[i]:
        adjacency_matrix[graph_nodes.index(i)][graph_nodes.index(j)]=1


class Node:
    
    def __init__(self,data,nxt):
        self.data=data
        self.next=nxt
class stack:
        
    def __init__(self):
        self.top=None
        
    def push(self,data):
        
        if self.top==None:
            self.top=Node(data,None)
            return
        
        self.top=Node(data,self.top)
        return 
    
    def pop(self):
        
        if self.top==None:
            return None
    
        x=self.top.data
        self.top=self.top.next
        return x
    
    def peek(self):
        
        if self.top==None:
            return None
        
        return self.top.data
    
    def Print(self):
        
        if self.top.data==None:
            print("stack is empty")
        
        itr=self.top
        s=''
        while itr!=None:
            s=s+str(itr.data)+'->'
            itr=itr.next
            
        print(s)
        
visited=['A']
st=[]

for i in visited:
    for j in graph[i]:
        if j not in visited:
            st.append(j)
            #print(st)
    if st[-1] not in visited:
        visited.append(st.pop())
    else:
        st.pop()
    
for i in reversed(st):
    if i not in visited:
        visited.append(i)

print(visited)


# In[ ]:





# In[ ]:




