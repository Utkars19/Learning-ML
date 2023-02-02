#!/usr/bin/env python
# coding: utf-8

# # Task 1
# 

# In[1]:


import numpy as np
arr=np.arange(1,10)


# In[2]:


for i in arr:
    print(i)


# # Searching Element

# In[3]:


n=int(input("enter the element to be searched"))                       
for i in arr:
    if i==n:
        print ("element is present")
        break
else:
    print("not found")


# # Find Largest number

# In[4]:


for i in arr:
    l=i
    for j in arr:                                                    
        if j>l:
            l=j
            break
print(l)     


# # Find Smallest Element

# In[5]:


s=arr[0]
for i in arr:                                              
    if i<s:
        s=i
print(s) 


# In[6]:


len(arr)


# # Reverse of Array

# In[7]:


for i in range(0,len(arr)):
    t=arr[0]
    for j in range(1,len(arr)-i):                     
        arr[j-1]=arr[j]
        arr[j]=t
print(arr)        


# # Reverse from kth position

# In[8]:


k=int(input("enter the k'th value"))                          
for i in range(0,k):            
    r=arr[0]                                                   
    for j in range(1,k-i):
        arr[j-1]=arr[j]
        arr[j]=r
print(arr)     


# In[ ]:




