#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
    def __init__(self,data,nxt,prev):
        self.data=data
        self.next=nxt
        self.prev=prev
class circular_linked_list:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_at_begining(self,data):
        if self.head is None:
            self.head=Node(data,None,None)
            self.tail=Node(data,None,None)
            return
        if self.head.next is None:
            self.head=Node(data,self.tail,None)
            self.tail.next=self.head
            return
        self.head=Node(data,self.head,None)
        self.tail.next=self.head
    def insert_at_end(self,data):
        #if self.head is None:
            #self.head=Node(data,None)
        #itr=self.head
        #while itr.next:
            #itr=itr.next
        #itr.next=Node(data,None)
        self.tail.next=Node(data,self.head,None)
        self.tail=self.tail.next
    def insert_in_between(self,data,n):
        if self.head is None:
            self.head=Node(data,None,None)
        itr=self.head
        while itr.data!=n:
            itr=itr.next
        itr.next=Node(data,itr.next,None)
    def delete(self,n):
        if self.head.data==n:
            self.head=self.head.next
            self.tail.next=self.head
            return
        itr=self.head
        while itr.next.data!=n:
            itr=itr.next
        d=itr.next
        if itr.next.next:
            itr.next=itr.next.next
            d.next=None
        else:
            self.tail=itr
            itr.next=self.head 
    def Print(self):
        if self.head is None:
            print("linked list is empty")
            return
        s=""
        c=0
        itr=self.head
        while itr and c<15:
            s+=str(itr.data)+'->'
            itr=itr.next
            c+=1
        print(s)


# In[ ]:




