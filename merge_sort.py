#!/usr/bin/env python
# coding: utf-8

# In[18]:


def merge_sort(l):
    k=len(l)//2
    if len(l)==1:
        return l
    else:
        a=merge_sort(l[:k])
        b=merge_sort(l[k:])
    return merge(a,b)

def merge(a,b):
    lst=[]
    i=0
    j=0
    while len(lst)<len(a)+len(b) and i<len(a) and j<len(b):
        if a[i]>b[j]:
            lst.append(b[j])
            j+=1
        elif a[i]<b[j]:
            lst.append(a[i])
            i+=1
    if i>=len(a):
        lst=lst+b[j:]
    elif j>=len(a):
        lst=lst+a[i:]
    return lst

l=[29,23,72,49,57,39,94,38,47,30,62]
merge_sort(l)

