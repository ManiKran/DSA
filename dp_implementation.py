#!/usr/bin/env python
# coding: utf-8

# In[1]:


def dyna_fib(n, lookup): 
        if n <= 2: 
            l[n] = 1 
        if l[n] is None: 
            l[n] = dyna_fib(n-1, l) + dyna_fib(n-2, l) 
        return l[n] 

n=10
l=[None]*1000
dyna_fib(n, l)
print(l[1:n+1])


# In[2]:


def fib_tab(n): 
        l = [1, 1] 
        for i in range(2, n): 
            l.append(l[i-1] + l[i-2]) 
        return l[-1] 
n=10
fib_tab(n)


# In[ ]:




