#!/usr/bin/env python
# coding: utf-8

# In[15]:


def max_area(l):
    i=0
    j=len(l)-1
    max=0
    while i<j:
        area=min(l[i],l[j])*(j-i)
        if area>max:
            max=area
        if l[i]<=l[j]:
            i+=1
        else:
            j-=1
            
    return max

l=[1,8,6,2,5,4,8,3,7]
max_area(l)


# In[3]:





# In[ ]:




