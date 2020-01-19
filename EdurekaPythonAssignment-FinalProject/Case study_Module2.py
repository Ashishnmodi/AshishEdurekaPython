#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1
d ={"john":40, "peter":45}
print(list(d.keys()))


# In[ ]:


#2
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))


# In[38]:


#3
q='$'
r='#'
s='@'
u=input('Welcome to out Website\nYou are a New User so please register\nEnter the Username:')
while True:    
    print('Your Password should contain atleast\n1 Uppercase letter(A-Z)\n1 Lowercase letter(a-z)\n1 Numeric digit(0-9)\n1 Charater from(@#$)')
    p=input('Enter the password:')
    if len(p)>=6 and len(p)<=12:
        if p.lower()!=p and p.upper()!=p:
            if q in list(p) or r in list(p) or s in list(p):
                b=list(p)
                c=[i for i in b if i in ['1','2','3','4','5','6','7','8','9','0']]
                d=''.join(c)
                if d.isnumeric()==True:
                    print('Password is Valid & Accepted as per policy\nThank you for registering with us')
                    break
                else:
                    print('Password is not following the Criteria\nPlease try again')
                    continue
            else:
                print('Password is not following the Criteria\nPlease try again')
                continue
        else:
            print('Password is not following the Criteria\nPlease try again')
            continue
    else:
        print('Password is not following the Criteria\nPlease try again')
        continue
print('Good Bye\nHave a Wonderful time ahead')


# In[70]:


#4
l=[4,7,3,2,5,9]
for elem in l:
    print('Element: %s and Index: %s' %(elem,l.index(elem)))
    #print('Index:',l.index(elem))
print('Thank you')


# In[74]:


#5
s=input('Enter the Input String:')
l=list(s)
k=[]
for i in range(0,len(s),2):
    k.append(l[i])
n=''.join(k)
print('Please find the New String with Even Number charaters as below\n',n)


# In[76]:


#6
s=input('Enter the Input String:')
n=s[::-1]
print('Reverse String is as below\n',n)


# In[83]:


#7
s=input('Enter the Input String:')
l=list(s)
for elem in l:
    i=l.count(elem)
    print('%s,%s'%(elem,i)) 


# In[84]:


#8
l1=[1,3,6,78,35,55]
l2=[12,24,35,24,88,120,155]
s1=set(l1)
s2=set(l2)
s3=s1&s2
l3=list(s3)
print(l3)


# In[87]:


#9
l1=[12,24,35,24,88,120,155,88,120,155]
s1=set(l1)
l1=sorted(list(s1))
print(l1)


# In[88]:


#10
l=[12,24,35,24,88,120,155]
n=[i for i in l if i!=24]
print(n)


# In[90]:


#11
l=[12,24,35,70,88,120,155]
n=[i for i in l if i!=l[0] and i!=l[4] and i!=l[5]]
print(n)


# In[93]:


#12
l=[12,24,35,70,88,120,155]
n=[i for i in l if i%5!=0 or i%7!=0]
print(n)


# In[109]:


#13
l=[]
n1=0
import random
while n1<5:
    n=random.randint(1,1001)
    if n%5==0 and n%7==0:
        l.append(n)
        n1+=1
    else:
        continue
print(l)    


# In[113]:


#14
n=int(input('Enter the number:'))
n1=0
for i in range(1,n+1):
    n1=n1+(i/(i+1))
print('%.2f'%n1)


# In[128]:


#Case Study II
import base64
i=3
while i>0:
    n=input('Enter the 12 character alphanumeric Reference Id:')
    if n.isalnum()==True and len(n)==12:
        encrypt=base64.b64encode(n.encode())
        print('Your Ref Id is encrypted as below\n:',encrypt)
        hint=input('Enter the hint:')
        ans=input('Thank you for trust on us, we stored your key securely\nif you want to see your Reference Id then press Y else press N:')
        if ans=='Y':
            hcheck=input('Enter the hint for verification:')
            if hcheck==hint:
                print('Your Entered Reference Id is:',n)
                break
            else:
                print('Sorry!!You hint is not matching\nGood bye!!')
                break
        else:
            print('Thanks for visiting our website,Good Bye!!')
            break
    else:
        print('Sorry you have not followed the policy\nTry again\n you left with %d chance'%(i-1))
        i=i-1
        continue
print('Thank you and Have a wonderful time ahead!!')
        
        

