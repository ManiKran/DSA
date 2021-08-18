#!/usr/bin/env python
# coding: utf-8

# In[16]:


s=12
def quick_sort(l,s):
    if sorted(l)==l:
        return l[s-1]
    p=0
    lp=1
    rp=len(l)-1
    while rp>=lp:
        while int(l[lp])<int(l[p]) and lp<len(l)-1:
            lp+=1
        while int(l[rp])>int(l[p]):
            rp=rp-1
        if lp<rp:
            l[lp],l[rp]=l[rp],l[lp]
        elif rp==p:
            s=s-1
            f=quick_sort(l[(p+1):],s)
        elif lp==rp:
            if sorted(l)==l:
                return l[s-1]
            else:
                l[p],l[rp]=l[rp],l[p]
                if s<rp+1:
                    f=quick_sort(l[:rp],s)
                elif s==rp+1:
                    return l[rp]
                else:
                    s=s-rp-1
                    f=quick_sort(l[rp+1:],s)
        else:
            if sorted(l)==l:
                return l[s-1]
            l[p],l[rp]=l[rp],l[p]
            if s<rp+1:
                f=quick_sort(l[:rp],s)
            elif s==rp+1:
                return l[rp]
            else:
                s=s-rp-1
                f=quick_sort(l[rp+1:],s)
    return f

l=[52,81,62,1,51,14,32,28,44,59,9,19,65,74,15]
quick_sort(l,s)


# In[ ]:




