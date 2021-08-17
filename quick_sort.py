#!/usr/bin/env python
# coding: utf-8

# In[92]:


l=['52','81','62','1','51','14','32','28','44','59','9','19','65','74','15']
s=''
def quick_sort(l,s):
    if l==[]:
        return
    if sorted(l)==l:
        s=s+','.join(l)+','
        return s
    p=0
    lp=1
    rp=len(l)-1
    while rp>=lp:
        while int(l[lp])<int(l[p]) and lp<len(l)-1:
            lp+=1
        while int(l[rp])>int(l[p]):
            rp=rp-1
        if lp<rp:
            swap(l,l[lp],l[rp])
        elif rp==p:
            s=s+''.join(l[p])+','
            s=quick_sort(l[(p+1):],s)
        elif lp==rp:
            if sorted(l)==l:
                s=s+','.join(l)+','
                return s
            else:
                swap(l,l[p],l[rp])
                s=quick_sort(l[:rp],s)
                s=s+''.join(l[rp])+','
                return s
        else:
            if sorted(l)==l:
                s=s+','.join(l)+','
                return s
            swap(l,l[p],l[rp])
            s=quick_sort(l[:rp],s)
            s=s+''.join(l[rp])+','
            s=quick_sort(l[rp+1:],s)
    return s

def swap(k,a,b):
    x=k.index(a)
    y=k.index(b)
    if x>y:
        k.pop(x)
        k.pop(y)
        k.insert(x,a)
        l.insert(y,b)
    else:
        k.pop(y)
        k.pop(x)
        k.insert(x,b)
        k.insert(y,a)
    return k
quick_sort(l,s)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




