#!/usr/bin/env python
# coding: utf-8

# In[17]:


#Factor Table
factors=[]
num=int(input('Enter the Number to get the Factors:'))
for i in range(num):
    if num%(i+1)==0:
        factors.append(i+1)
    else:
        continue
print('The factors of %d are as below:\n'%num,factors)


# In[16]:


#Sequence and sort words
w=[]
n=int(input('How many words you want to input to sort them out:'))
for i in range(n):
    k=input('Enter the %d word:'%(i+1))
    w.append(k)
    continue
print('Your input is as below\n',w)
w.sort()
print('Please find as below after Alphabatically Sort\n',w)


# In[18]:


###### Even number between 1000 and 3000
num=[]
val=[]
x=int(input('How many numbers you want to enter:'))
y=1
while y<x:
    n=input('Enter the number between 1000 and 3000:')
    if int(n)>=1000 and int(n)<=3000:
        y=y+1
        val=list(n)
        k=1
        for j in range(4):
            if ((int(val[j]))%2)==0 or (int(val[j]))==0:
                k=k+1
                if k==4:
                    num.append(int(n))
                else:
                    continue
            else:
                break
    else:
        print('Your Number is not between 1000 and 3000\nPlease Try again')
        y=y-1
        continue
print('Numbers with even digits are as below\n',num)


# In[20]:


#Count of Letters and digits from input string
str1=input('Enter the string to find out count of letters and digits:')
print('Lenth of string is:',len(str1))
DIGITS=0
LETTERS=0
for i in range(len(str1)):
    if str1[i].isdigit()==True:
        DIGITS+=1
    elif str1[i].isalpha()==True:
        LETTERS+=1
    else:
        continue
print(str1)
print('DIGITS:',DIGITS)
print('LETTERS:',LETTERS)


# In[2]:


#to check palindrome number
num=input('Enter the number to check palindrome number:')
num1=list(num)
num1.reverse()
s=[str(i) for i in num1]
num1=''.join(s)
if num==num1:
    print('Number is Palindrome')
else:
    print('Nuber is not Palindrome')


# In[7]:


#Alternate way to check palindrome number
num=input('Enter the number to check palindrome number:')
print(num)
mystr=num.casefold()
print(mystr)
rev1=list(reversed(mystr))
print(rev1)


# In[23]:


#Additional to sort the string
val=input('Enter the string to sort:')
val=val.split()
val=sorted(val)
' '.join(val)

