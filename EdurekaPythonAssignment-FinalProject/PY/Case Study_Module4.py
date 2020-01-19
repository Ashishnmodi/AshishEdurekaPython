#!/usr/bin/env python
# coding: utf-8

# #Case Study-I

# In[12]:


#1
from math import fsum,sqrt
#Function to calculate position
def calc_pos(args):
    global or_po
    print("Current Movement:",args)
    pos=sqrt(((args[0]-or_po[0])**2)+((args[1]-or_po[1])**2))
    cu_pos=((args[0]+or_po[0]),(args[1]+or_po[1]))
    or_po=cu_pos
    print("Robot current posotion after movement: %s and steps moved: %.2f"%(cu_pos,pos))
or_po=(0,0)
for i in range(4,0,-1):
    dir,step=input("Enter the Robot Direction(U-Up,D-Down,R-Right,L-Left) and Movement Steps(0-9)\n")
    step=int(step)
    if dir=='U':
        seq=(0,step)
        calc_pos(seq)
    elif dir=='D':
        seq=(0,(0-step))
        calc_pos(seq)
    elif dir=='R':
        seq=(step,0)
        calc_pos(seq)
    elif dir=='L':
        seq=((0-step),0)
        calc_pos(seq)
    else:
        print("Enter the correct letter, you have %s chance left"%(i-1))
        continue
print("Thank you and have a wonderful time ahead!!")


# In[14]:


#2
x=["My name is Ashish, age is 25 and number is 7788991234"]
import re
for elem in x:
    match_obj=re.search('\d+',elem)
    if match_obj:
        print("Matched object is:",match_obj.group())
    else:
        print("No data matched")


# In[15]:


#3
import time
c_time=time.ctime()
hr=int(time.strftime("%H"))
if hr>18 or hr<6:
        print("It is a Night and current time is:",c_time)
else:
    print("It is a Day and current time is:",c_time)


# In[16]:


#4
import math
# approximate radius of earth in km
R = 6373.0

lat1 = math.radians(52.2296756)
lon1 = math.radians(21.0122287)
lat2 = math.radians(52.406374)
lon2 = math.radians(16.9251681)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = (math.sin(dlat / 2)**2) + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon / 2)**2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

distance = R * c

print("Result:", distance)
print("Should be:", 278.546, "km")


# In[1]:


#5
def ChooseOption():
    "Function to choose ATM Options"
    global balance
    global pin
    print("1.Cash Withdraw\n2.Cash Credit\n3.Change Pin")
    opt=eval(input("Kindly choose above Options for further banking:"))
    if opt==1:
        debit=eval(input("Enter the amount to withdraw:"))
        if debit<=balance:
            balance=balance-debit
            print("Thank you for using ATM of My Bank\nYour Current Balance after this transaction is:",balance)
            answer()
        else:
            print("Entered amount is more than the current balance\nPlease try again")
            answer()
    elif opt==2:
        credit=eval(input("Enter the amount to credit:"))
        balance=balance+credit
        print("Thank you for using ATM of My Bank\nYour Current Balance after this transaction is:",balance)
        answer()
    elif opt==3:
        np1=eval(input("Please enter new Pin with 4 digits:"))
        pin=np1
        print("Thank you for using ATM of My Bank\nYour pin has been changed successfully:")
        answer()
    else:
        print("Sorry you choose wrong option\nPlease try again")
        answer()
      
"""      
def Bal(ibal=45000):
    "Function to update the Balance"
    balance=ibal
    return balance
def Upin(ipin=1234):
    "Function to update Pin"
    pin=ipin
    return pin
"""
def atm():
    "Function to proceed based on Pin"
    for i in range(3,0,-1):
        p1=eval(input("Enter the 4 digit pin:"))
        if p1==pin:
            ChooseOption()
            break
        else:
            i-=1
            print("Sorry you entered wrong Pin")
            print("You left with %d chance"%i)
            if i==0:
                print("Thank you for using My Bank ATM")
                break
            else:
                print("Try again")
                continue
def answer():
    "Function to ask user to continue or stop using ATM services"
    ans=input("Press 'Y' to continue 'N' to exit:")
    if ans=='Y' or ans=='y':
        atm()
    else:
        print("Thank you and have a nice time!!")
    
balance=45000
pin=1234
print("Welcome to My Bank ATM")
atm()


# In[2]:


#6
for i in range(2000,3201,1):
    if i%7==0 and i%5!=0:
        print(i,end=',')
    else:
        continue
print(end='\b') #backspace key to remove last comma


# In[3]:


#7
def fact(num):
    global f
    if num==0 or num==1:
        f=1
        return f
    else:
        f=num * fact(num-1)
        return f
num=int(input("Enter the Number you want to calculate Factorial:"))
f=1
fact(num)
print("Factorial of %d is %d"%(num,f))


# In[4]:


#8
from math import sqrt
def func(elem):
    p=elem*100/30
    q=sqrt(p)
    print("%d"%q,end=',')
args=eval(input("Enter the values in comma seperated format:"))
for elem in args:
    func(elem)
print("\b")


# In[5]:


#9
def array(x,y):
    row=[]
    col=[]
    for i in range(x):
        for j in range(y):
            k=i*j
            col.append(k)
        row.append(col)
        col=[]
    return row
x,y=eval(input("Enter raw(i) and column(j) values to generate 2D array:"))
array(x,y)


# In[6]:


#10
import re
def sorting(data):
    data1=data.split(',')
    data1=sorted(data1,reverse=False)
    for elem in data1:
        print(elem,end=',')
data=input("Enter the words in comma separated way to sort them out:")
sorting(data)
print('\b')


# In[7]:


#11
lines=[]
print("Enter the sequence of lines:\n")
while True:
    line=input()
    if line:
        lines.append(line)
    else:
        break
lwstr='\n'.join(lines)
print(lwstr.upper())


# In[162]:


#12
def WordSort():
    l1=[]
    w=input("Enter the words separed by whitespace:\n")
    l1=w.split(' ')
    s1=set(sorted(l1,reverse=False))
    s1=list(s1)
    s1=sorted(s1,reverse=False)
    s2=' '.join(s1)
    print("Output String after sorting is:\n",s2)
WordSort()    


# In[12]:


#13
def BinDivby5():
    while True:
        str1=input("Enter Comma separated 4 digit Binary Number:\n")
        str2=str1.split(',')
        str3=''.join(str2)
        if str3.isdigit():
            import re
            match_obj=re.search('[0-1]+',str3)
            if match_obj:
                print("You Entered Correct Data")
                break
            else:
                print("You have not entered Binary Data\nTry again later")
                continue
        else:
            print("You have not entered Binary Data\nTry again")
            continue
    print("Below are the entered numbers which are divisible by 5")
    for elem in str2:
        if int(elem,2)%5==0:
            print(elem,end=',')
    print('\b')
BinDivby5()


# In[21]:


#14
def LetterCount():
    str1=input("Enter the String to calculate Upper and Lower case letter:\n")
    import re
    match_obj1=re.findall('[A-Z]',str1)
    u_count=len(match_obj1)
    print("UPPER CASE ",u_count)
    match_obj2=re.findall('[a-z]',str1)
    l_count=len(match_obj2)
    print("UPPER CASE ",l_count)
LetterCount()


# In[34]:


#15
a=[1,2]
b=[1,2.777,4.55,2.99]
#Sum is standard library function
#It gives output as integer if all iterables are integers
c=sum(a)
print("C",c)
#fSum is math library function
#It gives output as float always
from math import fsum
d=fsum(a)
print("D",d)


# #Case Study II

# In[1]:


def maxage():
    import csv
    fo=open('bank-data.csv')
    reader=csv.reader(fo)
    next(reader) #skipping header
    age_max=max((int(row[0])) for row in reader)
    fo.close()
    return age_max

def minage():
    import csv
    fo=open('bank-data.csv')
    reader=csv.reader(fo)
    next(reader) #skipping header
    age_min=min((int(row[0])) for row in reader)
    fo.close()
    return age_min

def UniqueProfession():
    import csv
    with open('bank-data.csv') as fo:
        reader=csv.reader(fo)
        next(reader) #skipping header
        u_prof=[row[1] for row in reader]
        u_prof=set(u_prof)
        u_prof=list(u_prof)
    return u_prof

def selfexit():
    try:
        import sys
        sys.exit()
    except SystemExit:
        print("Thank you and have a wonderful time ahead")

def ans():
    global i
    while True:
        ans=input("Press 'Y' to continue, 'END' to end the session:\n")
        if ans=='Y':
            UserEligibility()
            break
        elif ans=='END' or ans=='end':
            i=0
            break
        else:
            print("Choose Correct option:\n")
            continue
    selfexit()
    
def UserEligibility():
    global i
    i=1
    while i>0:
        age=eval(input("Enter the age:\n"))
        prof=input("Enter the profession:\n")
        if age<=maxage() and age>=minage():
            if prof.casefold() in UniqueProfession():
                print("User is eligible for %s Profession:"%prof)
                i=i-1
                print("Value of i:",i)
                ans()
            else:
                print("User is not eligible for %s Profession:"%prof)
                i=i-1
                print("Value of i:",i)
                ans()
        else:
            print("User is not eligible for %s Profession:"%prof)
            i=i-1
            print("Value of i:",i)
            ans()

#one time call the function
#global i
i=1
for elem in range(1):
    if i>0:
        UserEligibility()
    else:
        break


# #CaseStudy III

# In[43]:


#Customer.py
class Customer:
 title = ""
 fname = ""
 lname = ""
 isblacklisted = 0;
 def __init__(self):
  self.title = ""
 def __str__(self):
  return "Title:" + self.title + " First Name:" + self.fname + " Last Name:" +self.lname + " Blacklisted:" + self.isblacklisted
 def setIsblacklisted(self,isblacklisted):
  self.isblacklisted = isblacklisted
 def isblacklisted(self):
  return self.isblacklisted
 def setTitle(self,title):
  self.title = title
 def getTitle(self):
  return self.title
 def setFname(self,fname):
  self.fname = fname
 def getFname(self):
  return self.fname
 def setLname(self,lname):
  self.lname = lname
 def getLname(self):
  return self.lname

#defining functions:
# define exception for BlackListed Customer
class CustomerNotAllowed(Exception):
 def __init__(self, value):
    self.value = value
 def __str__(self):
    return repr(self.value)

# function to process the data and return Customer object
def createCustomerObject(custdata):
 # Extract title
    customer = Customer()


    match = re.search('([A-Za-z]+)\.', custdata) # Usage of regular Expression
    title = ""
    if( match is not None):
        title = match.group()
        customer.setTitle(title.strip())
    data = (custdata.replace(title,'')).split(',',2) # Removed the title from name
    customer.setLname(data[0].strip())
    customer.setFname(data[1].strip())
    customer.setIsblacklisted(data[2])
    return customer
# function to create order if user is not blacklisted else throw exception
def createOrder(customer,productname):
    if customer.isblacklisted == "1":
        #print("Raising Customer Exception")
        raise CustomerNotAllowed("Customer is Black Listed:" + customer.__str__())
    else:
        print(" Order created successfully for:" + customer.__str__())
### End of Function #####################

### Start of the flow ############
# Read the file
from Customer import Customer
import re
customer_file = open('FairDealCustomerData.csv','r')
customerlist = [] # list defined to store Customer Objects
for data in customer_file:
    customerlist.append(createCustomerObject(data.rstrip('\n')))
customer_file.close()
print ("No . of customers read from file:",len(customerlist))
# Create order for all customers , except blacklisted ones
for i in range(len(customerlist)):
    try:
        createOrder(customerlist[i]," LEDTV")
    except CustomerNotAllowed as cne:
        print(" Exception Customer NotAllowed handled message", cne)
print ("End of Program")


# In[ ]:




