#!/usr/bin/env python
# coding: utf-8

# In[48]:


def greedy(l,a,lst):
    for i in reversed(sorted(l)):
        if i<a:
            for j in range(a//i):
                lst.append(i)
            a=a%i
            return greedy(l,a,lst)
        elif i>a:
            pass
        else:
            lst.append(i)
            return lst
    return lst

l=[4, 7, 6, 9, 2, 1]
a=80
greedy(l,a,[])

