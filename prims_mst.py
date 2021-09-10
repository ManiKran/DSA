#!/usr/bin/env python
# coding: utf-8

# In[22]:


graph=dict()
vertices=['A','B','C','D','E','F','G','H','I']
graph['A']=[['B',4],['H',8]]
graph['B']=[['A',4],['C',8],['H',11]]
graph['C']=[['B',8],['D',7],['F',4],['I',2]]
graph['D']=[['C',7],['E',9],['F',14]]
graph['E']=[['D',9],['F',10]]
graph['F']=[['C',4],['D',14],['E',10],['G',2]]
graph['G']=[['I',6],['F',2],['H',1]]
graph['H']=[['A',8],['B',11],['G',1],['I',7]]
graph['I']=[['C',2],['G',6],['H',7]]

def prims_mst():
    l=[]
    mini=float('inf')
    sum=0
    lst=[]
    for i in vertices:
        for j in graph[i]:
            if j[1]<mini:
                mini=j[1]
                l.clear()
                lst.clear()
                lst.append(i)
                lst.append(j[0])
                l.append([i,j[0]])
    sum+=mini
    
    while len(l)<len(vertices)-1:
        mini=float('inf')
        for i in lst:
            for k in graph[i]:
                if i in lst and k[0] in lst:
                    pass
                else:
                    if [i,k[0]] not in l and [k[0],i] not in l:
                        if k[1]<mini:
                            mini=k[1]
                            if len(l)>len(lst)-1:
                                l.pop()
                            l.append([i,k[0]])
        if l[-1][0] not in lst:
            if l[-1][1] not in lst:
                lst.append(l[-1][0])
                lst.append(l[-1][1])
            else:
                lst.append(l[-1][0])
        else:
            if l[-1][1] not in lst:
                lst.append(l[-1][1])
                
        sum+=mini
    print(sum)
    
prims_mst()


# In[ ]:





# In[ ]:




