#!/usr/bin/env python
# coding: utf-8

# #Case Study I

# In[3]:


#1
import numpy as np
arr=np.loadtxt('SalaryGender.csv',skiprows=1,delimiter=',')
arr_salary=arr[:,0:1]
arr_gender=arr[:,1:2]
arr_age=arr[:,2:3]
arr_phd=arr[:,3:4]
#print(arr_salary)
#print(arr_gender)
#print(arr_age)
#print(arr_phd)


# In[4]:


#2
import numpy as np
arr=np.loadtxt('SalaryGender.csv',skiprows=1,delimiter=',')
len(arr)
arr_gender=arr[:,1:2]
arr_phd=arr[:,3:4]
m=0
f=0
for i in range(len(arr)):
    if arr_gender[i]==1 and arr_phd[i]==1:
        m+=1
    elif arr_gender[i]==0 and arr_phd[i]==1:
        f+=1
    else:
        continue            
print("The number of men with a PhD:",m)
print("The number of women with a PhD:",f)


# In[5]:


#3
import pandas as pd
df=pd.read_csv('SalaryGender.csv')
#storing Age and Phd in dataframe df1
df1=df.drop(['Salary','Gender'],axis=1)
ser_phd=df1['PhD']
df2=df1.drop([i for i in range(len(df1)) if ser_phd[i]==0],axis=0)
print("Dataframe with PhD:\n",df2)


# In[6]:


#4
import pandas as pd
df=pd.read_csv('SalaryGender.csv')
ser_phd=df['PhD']
df2=df1.drop([i for i in range(len(df)) if ser_phd[i]==0],axis=0)
print("Total number of people with PhD:\n",len(df2))


# In[7]:


#5
import numpy as np
arr=np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
max_val=arr.max()
arr=list(arr)
arr.sort(reverse=False)
elem=[]

for i in range(max_val+1):
    elem.append(arr.count(i))
print("Element count is as below:\n",elem)
    
#arr=[arr.count(arr[i]) for i in range(len(arr))]
#arr.remove(a)


# In[8]:


#6
import numpy as np
arr1=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print("Input Array is:\n",arr1)
def arraytolist(arr):
    lst=list(arr)
    for k in range(len(lst)):
        lst[k]=list(lst[k])
    return lst
def listtoarray(lst):
    arr=np.array(lst)
    for k in range(len(arr)):
        arr[k]=np.array(arr[k])
    return arr
l1 = arraytolist(arr1)
l2 = arraytolist(arr1)
l3=[]
for i in range(len(l1)):
    for j in range(len(l1[i])):
        elem=l1[i][j]
        if elem > 5:
            l3.append(elem)
        else:
            continue
    s1= set(l1[i]) ^ set(l3)
    l1[i]=list(s1)
    l3=[]
    continue
count=l1.count([])
for i in range(count):
    l1.remove([])
arr1=listtoarray(l1)
print("Final Output after filter values more than 5:\n",arr1)


# In[9]:


#7
arr=np.arange(1,6,1,dtype='float32')
arr_nan=np.insert(arr,[0,2],np.nan)
print("Array is created as below:\n",arr_nan)
arr_wonan=arr.astype(float)
print("Array after filtering 'nan':\n",arr_wonan)


# In[10]:


#8
import numpy as np
arr_1d=np.arange(100)
arr_2d=arr_1d.reshape(10,10)
print("Maximum Number from 2D Array:\n",np.max(arr_2d))
print("Minimum Number from 2D Array:\n",np.min(arr_2d))


# In[11]:


#9
import numpy as np
ran=np.random.random(30)
ran_mean=ran.mean()
print("Mean of Vector with 30 random values: %.2f "%ran_mean)


# In[12]:


#10
import numpy as np
arr=np.arange(0,11)
for i in range(11):
    if arr[i] > 3 and arr[i] < 9:
        arr[i]*=-1
    else:
        continue
print("Requested Output is as below:\n",arr)


# In[13]:


#11
import numpy as np
arr=[]
for i in range(9):
    rand=np.random.randint(100)
    arr.append(rand)
arr=np.array(arr)
ran_2d=arr.reshape(3,3)
print(ran_2d)
ran_sorted=np.sort(ran_2d,axis=0)
print(ran_sorted)


# In[14]:


#12
import numpy as np
lst=np.arange(2*3*4*5)
arr_1d=np.array(lst)
arr_4d=arr_1d.reshape(2,3,4,5)
print("Below one is 4D array\n",arr_4d)
nw_arr=np.sum(arr_4d,axis=(2,3))
print("Sum of last two axis is as below\n",nw_arr)


# In[15]:


#13
import numpy as np
arr=[]
for i in range(16):
    rand=np.random.randint(100)
    arr.append(rand)
arr=np.array(arr)
ran_2d=arr.reshape(4,4)
print("The given 2D array is as below\n",ran_2d)
x,y=eval(input("Enter the row numbers to be swapped for given (4,4) array:\n"))
ran_2d[[x,y]]=ran_2d[[y,x]]
print("The requested output is as below:\n",ran_2d)


# In[16]:


#14
import numpy as np
#arr=np.zeros((2,2))
arr=np.random.random((5,5))
print("The given Random Array is as below:\n",arr)
mat=np.matrix(arr)
mat_rank=np.linalg.matrix_rank(mat)
print("Matrix Rank for given matrix is as below\n",mat_rank)


# In[17]:


#15
#Phase-I
import pandas as pd
data_sch=pd.read_csv("middle_tn_schools.csv")
data_sch.describe()
data_sch


# In[23]:


#15
#Phase-II
#isolating by reduced_lunch
data_r1=data_sch.drop('reduced_lunch',axis=1)
#group by school rating
grouped_data=data_r1.groupby('school_rating')
for sch_rating, sch_val in grouped_data:
    print("School Rating:",sch_rating)
    print("Data by school rating:\n")
    print(sch_val)
    print("#"*90)
grouped_data.describe()


# In[19]:


#15
#Phase-III
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("middle_tn_schools.csv")
column_list=['reduced_lunch','school_rating']
df[column_list].corr()


# In[20]:


#15
#Phase-IV
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("middle_tn_schools.csv")
rlunch=df['reduced_lunch']
srating=df['school_rating']
tstudent=df['size']
p_rlunch=(rlunch/tstudent)*100
plt.scatter(rlunch,srating)
plt.xlabel('Percentage of reduced lunch')
plt.ylabel("school's rating")
plt.title('rlunch vs srating')
plt.show()


# In[21]:


#15
#Phase-V
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data=pd.read_csv("middle_tn_schools.csv")
sns.pairplot(data,diag_kind="kde", markers="+",plot_kws=dict(s=50, edgecolor="b", linewidth=1),diag_kws=dict(shade=True))
plt.savefig('pairplot.png')


# #Case Study II

# In[22]:


import pandas as pd
#reading all 3 csv
ph_data=pd.read_csv("PhysicsScoreTerm1.csv")
ma_data=pd.read_csv("MathScoreTerm1.csv")
ds_data=pd.read_csv("DSScoreTerm1.csv")
##Dropping the Name data as part of security
ph_conf=ph_data.drop(['Name'],axis=1)
ma_conf=ma_data.drop(['Name'],axis=1)
ds_conf=ds_data.drop(['Name'],axis=1)
#Replacing missing score data with average of the class
ph_conf['Score']=ph_conf['Score'].fillna(int(ph_conf['Score'].mean()))
ma_conf['Score']=ma_conf['Score'].fillna(int(ma_conf['Score'].mean()))
ds_conf['Score']=ds_conf['Score'].fillna(int(ds_conf['Score'].mean()))
#Merging all three score data frames
merge_data=pd.concat([ph_conf,ma_conf,ds_conf],sort=False)
#Replacing Ethinicity as per below substitute
#White American ==> 3
#European American ==> 1
#Hispanic ==> 2
#African American ==> 0
merge_data['Ethinicity']=merge_data['Ethinicity'].replace('African American',0)
merge_data['Ethinicity']=merge_data['Ethinicity'].replace('European American',1)
merge_data['Ethinicity']=merge_data['Ethinicity'].replace('Hispanic',2)
merge_data['Ethinicity']=merge_data['Ethinicity'].replace('White American',3)
#Replacing Sex M with 1 and F with 2
merge_data['Sex']=merge_data['Sex'].replace('M',1)
merge_data['Sex']=merge_data['Sex'].replace('F',2)
merge_data.to_csv('ScoreFinal.csv',index=False)
merge_data


# In[ ]:




