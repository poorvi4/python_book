
# coding: utf-8

# In[5]:


#basic practice for if,elif, and else statements.Same as MATLAB.
mylist=[1,2,3,4,5,6,7]

for x in mylist:
#check for evens and odds
    if x%2==0:
        print(f'{x} is an even number')
    else:
        print(f'{x} is an odd number')


# In[8]:


#counting function that displays c
c=0
list1=[1,2,3,4,5,3,3,3,5,7,8,3,5,4,2,3,4,5]
for x in list1:
    if x==3:
        c=c+1
print(c)
        


# In[19]:


#sum of numbers in list
sum_list=[1,2,3,4,5,6,7,8,9]

c=0

for x in sum_list:
    c=c+x

print(c)

print(' ')

#See what happens when we include 'print()' inside of our for-loop when we don't indent

c=0

for x in sum_list:
    c=c+x
    print(c)

#we see the sum for each iteration
    


# In[17]:


#tuple iterations and unpackings

tup=(1,2,3)

for x in tup:
    print(x)
    
print(' ')

#Now lets unpack a tuple

mylist=[(1,2,3),(4,5,6),(7,8,9)]

#let tuple be denoted as (a,b)

for (a,b,c) in mylist:
    print (a)
    print(b)
    print(c)
#we duplicated the structure of an item and then "unpacked" them...don't necessarily need the ()


# In[32]:


# when iterating thru a dictionary we only iterate thru the keys as shown below:

d={'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
    
#we have to call the items...d.items() returns back [(...,...),(...,...)(...,...)] format which we can then use tuple unpacking
for item in d.items():
    print(item)

#now we can use same tuple unpacking
for key,value in d.items:
    print(value)

        

