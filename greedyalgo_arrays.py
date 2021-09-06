#!/usr/bin/env python
# coding: utf-8

# In[1]:


#max_prod_subset
def max_prod_subset(l):
    if len(l)==1:
        return l[0]
    count_zero=0
    count_neg=0
    min_pos=float('inf')
    max_neg=float('-inf')
    prod=1
    
    for i in range(len(l)):
        if l[i]==0:
            count_zero+=1
            continue
        elif l[i]<0:
            count_neg+=1
            max_neg=max(max_neg,l[i])
            
        prod=prod*l[i]
        
    if count_zero==len(l):
        return 0
    elif count_neg==len(l):
        return max_neg
    elif (count_neg&1)==1:
        if (count_neg == 1 and count_zero > 0 and
            count_zero + count_neg == n):
            return 0
        return int(prod/max_neg)
    return prod

l=[1,2,-3,-4,-5,6]
max_prod_subset(l)


# In[2]:


# min produt subset of an array
def minProductSubset(a, n):
    if (n == 1):
        return a[0]
    
    max_neg = float('-inf')
    min_pos = float('inf')
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range(0, n):
 
        if (a[i] == 0):
            count_zero = count_zero + 1
            continue
        if (a[i] < 0):
            count_neg = count_neg + 1
            max_neg = max(max_neg, a[i])
        if (a[i] > 0):
            min_pos = min(min_pos, a[i])
 
        prod = prod * a[i]
 
    if (count_zero == n or (count_neg == 0
                            and count_zero > 0)):
        return 0
    if (count_neg == 0):
        return min_pos
 
    if ((count_neg & 1) == 0 and
            count_neg != 0):
 
        prod = int(prod / max_neg)
 
    return prod

a = [-1, -1, -2, 4, 3]
n = len(a)
print(minProductSubset(a, n))


# In[3]:


# max sum of an array
def max_sum_of_array(l,k):
    l.sort()
    for i in range(len(l)):
        if k and l[i]<0:
            k-=1
            l[i]*=-1
            continue
        break
    if k==0 or k%2==0:
        return sum(l)
    elif i!=0 and abs(l[i])>=abs(l[i-1]):
        i-=1
    l[i]*=-1
    return sum(l)
        
l=[-10, -9, -8, 5, 6]

k=4
max_sum_of_array(l,k)


# In[4]:


#Maximize the sum of arr[i]*i
def Maximize(a, n): 
        a.sort()
        s=0
        for i in range(len(a)):
            s+=a[i]*i
        return s
    
N = 20
arr =[6, 6, 8, 19, 8, 10, 19, 14, 20, 18, 5, 11, 20, 6, 10, 7, 15, 8, 8, 9]
Maximize(arr, N)


# In[5]:


#Maximum sum of increasing order elements from n arrays
M = 4

def maximumSum(a, n):
 
    prev = max(max(a))
    print(prev)
    Sum = prev
    for i in range(n - 2, -1, -1):
 
        max_smaller = -10**9
        for j in range(M - 1, -1, -1):
            if (a[i][j] < prev and
                a[i][j] > max_smaller):
                max_smaller = a[i][j]
 
        if (max_smaller == -10**9):
            return 0
 
        prev = max_smaller
        Sum += max_smaller
 
    return Sum

arr = [[1, 7, 3, 4],
       [4, 2, 5, 1],
       [9, 5, 1, 8]]
n = len(arr)
print(maximumSum(arr, n))


# In[6]:


# maximum sum of absolute difference of any permutation of the given array.
def max_sum(l):
    l.sort()
    lst=[]
    n=len(l)
    sum=0
    i=0
    j=n-1
    while i<j:
        lst.append(l[i])
        lst.append(l[j])
        i+=1
        j-=1 
    if n%2!=0:
        lst.append(l[n//2])
    i=0
    j=1
    while j<=n-1:
        sum+=abs(lst[i]-lst[j])
        i+=1
        j+=1
    sum+=abs(lst[j-1]-lst[0])
    return sum
l=[1,2,4,8]
max_sum(l)


# In[7]:


# Maximum height pyramid from the given array of objects
# works only if all elements in an array are positive
def max_height(l):
    n=len(l)
    i=1
    j=2
    while i*j<=n*2:
        i+=1
        j+=1
    return i-1
l=[10,20,30,50,60,70]

max_height(l)


# In[8]:


# Partition into two subarrays of lengths k and (N – k) such that the difference of sums is maximum
def max_difference(l,k):
    l.sort()
    return abs(sum(l[:k])-sum(l[k:]))
               
l=[1,1,1,1,1,1,1,1,1,1,1,1,1]
k=3
max_difference(l,k)


# In[9]:


l=[]
l2=[]
import random
for i in range(5):
    l.append(random.randint(-10,10))
    l2.append(random.randint(-10,10))
print(l)
print(l2)


# In[10]:


# Minimum sum of product of two arrays
def product(l):
    return l[0]*l[1]

def min_sum(a,b,k):
    mini=float('inf')
    c=0
    d={}
    sum=0
    for i in range(len(a)):
        if b[i]<0:
            if (a[i]+(k*2))*b[i]<mini:
                if mini!=float('inf'):
                    sum+=product(d[max(d)])
                mini=(a[i]+(k*2))*b[i]
                d[c]=[a[i],b[i]]
                c+=1
            elif (a[i]+(k*2))*b[i]==mini:
                if product(d[max(d)])<(a[i]*b[i]):
                    sum+=product(d[max(d)])
                    d[c]=[a[i],b[i]]
                else:
                    sum+=(a[i]*b[i])
            else:
                sum+=(a[i]*b[i])
        else:
            if (a[i]-(k*2))*b[i]<mini:
                if mini!=float('inf'):
                    sum+=product(d[max(d)])
                mini=(a[i]-(k*2))*b[i]
                d[c]=[a[i],b[i]]
                c+=1
            elif (a[i]-(k*2))*b[i]==mini:
                if product(d[max(d)])<(a[i]*b[i]):
                    sum+=product(d[max(d)])
                    d[c]=[a[i],b[i]]
                else:
                    sum+=(a[i]*b[i])
            else:
                sum+=(a[i]*b[i])
        
    return sum+mini

a=[1,2,-3]
b=[-2,3,-5]
k=5
min_sum(a,b,k)
        


# In[11]:


# Minimum sum by choosing minimum of pairs from array
def minSum(A):
 
    min_val = min(A);
 
    return min_val * (len(A)-1)

A = [7, 2, 3, 4, 5, 6]
print (minSum(A))


# In[12]:


# Minimum sum of absolute difference of pairs of two arrays
def min_sum(a,b):
    a.sort()
    b.sort()
    sum=0
    for i in range(len(a)-1,-1,-1):
        sum+=abs(a[i]-b[i])
    return sum
    
a = [4,1,8,7]
b = [2,3,6,5]
min_sum(a,b)


# In[13]:


# Minimum operations to make GCD of array a multiple of k
def min_operations(l,k):
    sum=0
    for i in l:
        if i%k>k//2+1:
            sum+=k-(i%k)
        else:
            sum+=i%k
    return sum
l=[4,9,6]
k=5
min_operations(l,k)


# In[14]:


# Minimum sum of two numbers formed from digits of an array
def min_sum(l):
    l.sort()
    s1=''
    s2=''
    c=0
    for i in l:
        if c%2==0:
            s1+=str(i)
        else:
            s2+=str(i)
        c+=1
    return int(s1)+int(s2)

l=[5,3,0,7,4]
min_sum(l)


# In[15]:


# Minimum increment/decrement to make array non-Increasing
def min_incre_decre(l):
    l.reverse()
    c=0
    for i in range(len(l)):
        try:
            if l[i]<=l[i+1]:
                pass
            else:
                c+=l[i]-l[i+1]
                l[i]=l[i+1]
        except:
            pass
    return c

l=[3,1,2,1]
min_incre_decre(l)
            


# In[16]:


# Making elements of two arrays same with minimum increment/decrement
def making_ele(a,b):
    a.sort()
    b.sort()
    sum=0
    for i in range(len(a)):
        sum+=abs(a[i]-b[i])
    return sum

a = [ 3, 1, 1 ]
b = [ 1, 1, 2 ] 
making_ele(a,b)


# In[17]:


# Minimize sum of product of two arrays with permutation allowed
def min_value(a,b):
    a.sort()
    b.sort(reverse=True)
    sum=0
    for i in range(len(a)):
        sum+=a[i]*b[i]
    return sum

a=[3,1,1]
b=[6,5,4]
min_value(a,b)


# In[18]:


# Sorting array with reverse around middle
def sorting_array(l):
    a=[]
    a=a+l
    l.sort()
    for i in range(len(a)):
        if l[i]!=a[i] and l[i]!=a[-(i+1)]:
            return 'NO'
    return 'YES'

l=[1, 6, 3, 4, 5, 7, 2]
sorting_array(l)


# In[19]:


# Sum of Areas of Rectangles possible for an array
def product(a):
    return a[0]*a[1]
def maxi_sum(l):
    l.sort(reverse=True)
    print(l)
    fin=[]
    lst=[]
    for i in range(0,len(l)-1,2):
        if l[i]==l[i+1]:
            lst.append(l[i])
        else:
            if l[i]-1==l[i+1]:
                lst.append(l[i+1])
            else:
                pass
        if len(lst)==2:
            fin.append(product(lst))
            lst=[]
        else:
            pass
    
    return sum(fin)

l=[3, 4, 5, 6]
maxi_sum(l)


# In[20]:


# Array element moved by k using single moves
def ele_moved(l,k):
    while(1):
        if max(l[1:k+1])<l[0]:
            return l[0]
        else:
            for i in l[1:k+1]:
                if l[0]>i:
                    l.remove(i)
                    l.append(i)
                else:
                    x=l.pop(0)
                    l.append(x)
                    break
                
    return 'not possible'

l=[3, 1, 2]
k=2
ele_moved(l,k)


# In[21]:


# Find if k bookings possible with given arrival and departure times
def areBookingsPossible(A, B, K):
        A.sort()
        B.sort()
        for i in range(len(A)):
            if i+K < len(A) and A[i+K] < B[i] :
                return "No"
        return "Yes"
    
arrival = [1,2,5,3,8,6] 
departure = [5,4,7,8,9,10]  
K = 3
print (areBookingsPossible(arrival,departure,K))


# In[22]:


# Lexicographically smallest array after at-most K consecutive swaps
def Lexicographically_smallest(l,k):
    
    i=0
    
    while k!=0:
        
        if sorted(l)==l:
            return l
        
        x=l[i:i+k+1].index(min(l[i:i+k+1]))
        
        if l[i]!=l[i:i+k+1][x]:
            
            l.insert(i,l.pop(i+x))
            i+=1
            k-=x
            
        else:
            
            i+=1
            
    return l        

l=[5, 7, 6, 3, 8, 1]
k=3
Lexicographically_smallest(l,k)

