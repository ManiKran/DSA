#!/usr/bin/env python
# coding: utf-8

# In[44]:


class Node:
    def __init__(self,data,nxt):
        self.data=data
        self.next=nxt
class stack:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,data):
        if self.top is None:
            self.top=Node(data,None)
            self.size+=1
            return
        self.top=Node(data,self.top)
        self.size+=1
    def pop(self):
        self.top=self.top.next
        self.size-=1
    def peek(self):
        return self.top.data
    def Print(self):
        if self.top is None:
            print("stack is empty")
            return
        s=""
        itr=self.top
        while itr:
            s+=str(itr.data)+','
            itr=itr.next
        print(s)
        print(self.size)
statement=input()
def check_brac(statement):
    st=stack()
    for i in statement:
        if i in ('{','(','['):
            st.push(i)
        if i in ('}',')',']'):
            last=st.peek()
            st.pop()
            if last=='{' and i=='}':
                pass
            elif last=='(' and i==')':
                pass
            elif last=='[' and i==']':
                pass
            else:
                return False
    if st.size>0:
        return False
    else:
        return True
print(check_brac(statement))


# In[ ]:




