#!/usr/bin/env python
# coding: utf-8

# #Case Study I

# In[45]:


#1
import numpy as np
import pandas as pd
df=pd.read_csv("HollywoodMovies.csv")
d1=df[df['Story'] == 'Quest']
d2=df[df['Story'] == 'quest']
data=pd.concat([d1,d2],sort=False)
data=data[['Movie','Story','AudienceScore']]
max_val=data['AudienceScore'].max()
for row in data.itertuples():
    if row.AudienceScore == float(max_val):
        mo=row.Movie
        break
    else:
        continue
print("The Highest rated movie in Quest Story Type is %s with %s Score"%(mo,max_val))


# In[61]:


#2
import numpy as np
import pandas as pd
df=pd.read_csv("HollywoodMovies.csv")
d1=df[['Movie','Genre']]
val=d1['Genre'].value_counts()
data=pd.DataFrame(val)
max_val=data['Genre'].max()
for col_val in data['Genre'].iteritems():
    if col_val[-1] == int(max_val):
        ge=col_val[0]
        break
    else:
        continue
print("The genre with greatest no. of movies is %s with %s movies release"%(ge,max_val))


# In[69]:


#3
import numpy as np
import pandas as pd
df=pd.read_csv("HollywoodMovies.csv")
data=df.sort_values(by='Budget',ascending=False).head()
print("5 Highest Budget Movies:")
print(data[['Movie','Budget']])


# In[81]:


#4
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("HollywoodMovies.csv")
#d1=df[['RottenTomatoes','Profitability','Movies']]
plt.scatter(df['RottenTomatoes'],df['Profitability'],c=df['RottenTomatoes'])
plt.xlabel("Rotten Tomatoes Rating",size=20)
plt.ylabel("Net Profitability",size=20)
plt.ylim(0,3000)
plt.title("Public Acceptance Vs Collection",size=30)
plt.show()


# In[82]:


#5
#5.1
import matplotlib.pyplot as plt
import pandas as pd
data={'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
     'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
     'age': [42, 52, 36, 24, 73],
     'preTestScore': [4, 24, 31, ".", "."],
     'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df=pd.DataFrame(data)
df


# In[84]:


#5.2
df.to_csv("example.csv",index=False)


# In[85]:


#5.3
data=pd.read_csv("example.csv")
data


# In[90]:


#5.4
data=pd.read_csv("example.csv",skiprows=1, header=None)
data


# In[96]:


#5.5
data=pd.read_csv("example.csv",index_col=(0,1))
data


# In[113]:


#5.6
data=pd.read_csv("example.csv") #blank will be replaced by True
data.isnull()


# In[122]:


#5.7
data=pd.read_csv("example.csv",skiprows=[1,2,3])
data


# In[124]:


#5.8
data=pd.read_csv("example.csv",thousands=',')
data


# In[130]:


#6.1
import pandas as pd
data=['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat']
s1=pd.Series(data)
print("Elements in Lower Case are as below:\n",s1.str.lower())
print("Elements in Upper Case are as below:\n",s1.str.upper())
print("Length of all Elements are as below:\n",s1.str.len())


# In[153]:


#6.2
import pandas as pd
data=[' Atul', 'John ', ' jack ', 'Sam']
s1=pd.Series(data)
#s1.str.strip()
print("Elements with Left & Right strip:\n",s1.str.strip())
print("Elements with Left strip:\n",s1.str.lstrip())
print("Elements with Right strip:\n",s1.str.rstrip())


# In[140]:


#6.2
import pandas as pd
data=[' Atul', 'John ', ' jack ', 'Sam']
s1=pd.Series(data)
s1.str.strip()


# In[208]:


#6.3(a & b)
import pandas as pd
import numpy as np
data=['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture']
#data=['India_is_big', 'Population_is_huge', 'Has_diverse_culture']
s1=pd.Series(data)
s1.fillna(0,inplace=True)
for i in range(len(s1)):
    if s1[i] != 0:
        s1[i]=s1[i].split('_')
    else:
        continue
#Accessing elements of list
for i in range(len(s1)):
    if s1[i] != 0:
        for j in range(len(s1[i])):
            print(s1[i][j])
    else:
        continue


# In[207]:


#6.3(c)
import pandas as pd
import numpy as np
data=['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture']
s1=pd.Series(data)
s1.str.split(pat='_', expand=True)


# In[218]:


#6.4
import pandas as pd
data=['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat']
s1=pd.Series(data)
s1=s1.str.replace(pat='X$',repl='XX-XX')
s1.replace(to_replace=['X','dog'],value='XX-XX',inplace=True)
s1


# In[234]:


#6.5
import pandas as pd
data=['12', '-$10', '$10,000']
s1=pd.Series(data)
s1=s1.replace('\$','',regex=True)
s1


# In[240]:


#6.6
import pandas as pd
import numpy as np
data=['india 1998', 'big country', np.nan]
s1=pd.Series(data)
for i in range(len(s1)):
    if s1.str.islower()[i] == True:
        s1[i]=s1[i][::-1]
    else:
        continue
s1


# In[248]:


#6.7
import pandas as pd
data=['1', '2', '1a', '2b', '2003c']
s1=pd.Series(data)
for i in range(len(s1)):
    if s1.str.isalnum()[i] == True:
        print('true')
    else:
        print('false')


# In[253]:


#6.8
import pandas as pd
data=['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c']
s1=pd.Series(data)
for i in range(len(s1)):
    if s1.str.contains(pat='A')[i] == True:
        print("Element %s : true"%i)
    else:
        continue


# In[256]:


#6.9
import pandas as pd
data=['d', 'a|b', np.nan, 'a|c']
s1=pd.Series(data)
for i in range(len(s1)):
    if s1.str.contains(pat='[a-c]',regex=True)[i] == True:
        print("Element %s : 1"%i)
    else:
        print("Element %s : 0"%i)


# In[264]:


#6.10
import pandas as pd
d1={'key': ['One', 'Two'], 'ltable': [1, 2]}
d2={'key': ['One', 'Two'], 'rtable': [4, 5]}
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
pd.merge(df1,df2,on='key')


# #CaseStudy II

# In[275]:


#1
import pandas as pd
df=pd.read_csv("Salaries.csv")
sal_2011=df[df['Year']==2011]
sal_2014=df[df['Year']==2014]
s2011=sal_2011['TotalPayBenefits'].sum()
s2014=sal_2014['TotalPayBenefits'].sum()
cost_inc=s2014-s2011
print("Total Cost Increased from 2011 to 2014 is:",cost_inc)


# In[327]:


#2
import pandas as pd
df=pd.read_csv("Salaries.csv")
sal_2014=df[df['Year']==2014]
data=sal_2014[['JobTitle','TotalPayBenefits']]
data_14=pd.DataFrame(data.groupby('JobTitle').TotalPayBenefits.mean())
max_val=data_14['TotalPayBenefits'].max()
min_val=data_14['TotalPayBenefits'].min()
for col_val in data_14['TotalPayBenefits'].iteritems():
    if col_val[-1]==float(max_val):
        jt_max=col_val[0]
    elif col_val[-1]==float(min_val):
        jt_min=col_val[0]
    else:
        continue
print("Job Title %s in Year 2014 has highest mean salary of %.2f"%(jt_max,max_val))
print("Job Title %s in Year 2014 has lowest mean salary of %.2f"%(jt_min,min_val))


# In[325]:


#3
import pandas as pd
df=pd.read_csv("Salaries.csv")
sal_2014=df[df['Year']==2014]
amount=sal_2014['OvertimePay'].sum()
print("The money which could be save in 2014 by stopping Overtime pay is %s"%amount)
#2011
sal_2014=df[df['Year']==2011]
ot=sal_2011['OvertimePay'].sum()
tp=sal_2011['TotalPayBenefits'].sum()
per=(ot/tp)*100
print("In year 2011 OverTimePay was %.2f percentage of TotalPayBenefits"%per)


# In[317]:


#4
import pandas as pd
df=pd.read_csv("Salaries.csv")
sal_2014=df[df['Year']==2014].sort_values(by='TotalPayBenefits',ascending=False)
data1=sal_2014.head()
data2=sal_2014.tail()
data1=data1[['JobTitle','TotalPayBenefits']]
data2=data2[['JobTitle','TotalPayBenefits']]
costosfo_top=data1['TotalPayBenefits'].sum()
costosfo_last=data2['TotalPayBenefits'].sum()
print("Top 5 common job in Year 2014 are as below & the cost to SFO is %s :\n"%costosfo_top,data1)
print("Last 5 common job in Year 2014 are as below & the cost to SFO is %s :\n"%costosfo_last,data2)


# In[323]:


#5
import pandas as pd
df=pd.read_csv("Salaries.csv")
#2014
sal_2014=df[df['Year']==2014]
data=sal_2014[['EmployeeName','TotalPayBenefits']]
data_14=pd.DataFrame(data.groupby('EmployeeName').TotalPayBenefits.max())
max_val_14=data_14['TotalPayBenefits'].max()
for col_val in data_14['TotalPayBenefits'].iteritems():
    if col_val[-1]==float(max_val_14):
        emp_14=col_val[0]
        break
    else:
        continue
print("Top earning employee in Year 2014 is %s with earning of %s"%(emp_14,max_val_14))
#2013
sal_2013=df[df['Year']==2013]
data=sal_2013[['EmployeeName','TotalPayBenefits']]
data_13=pd.DataFrame(data.groupby('EmployeeName').TotalPayBenefits.max())
max_val_13=data_13['TotalPayBenefits'].max()
for col_val in data_13['TotalPayBenefits'].iteritems():
    if col_val[-1]==float(max_val_13):
        emp_13=col_val[0]
        break
    else:
        continue
print("Top earning employee in Year 2013 is %s with earning of %s"%(emp_13,max_val_13))
#2012
sal_2012=df[df['Year']==2012]
data=sal_2012[['EmployeeName','TotalPayBenefits']]
data_12=pd.DataFrame(data.groupby('EmployeeName').TotalPayBenefits.max())
max_val_12=data_12['TotalPayBenefits'].max()
for col_val in data_12['TotalPayBenefits'].iteritems():
    if col_val[-1]==float(max_val_12):
        emp_12=col_val[0]
        break
    else:
        continue
print("Top earning employee in Year 2012 is %s with earning of %s"%(emp_12,max_val_12))
#2011
sal_2011=df[df['Year']==2011]
data=sal_2011[['EmployeeName','TotalPayBenefits']]
data_11=pd.DataFrame(data.groupby('EmployeeName').TotalPayBenefits.max())
max_val_11=data_11['TotalPayBenefits'].max()
for col_val in data_11['TotalPayBenefits'].iteritems():
    if col_val[-1]==float(max_val_11):
        emp_11=col_val[0]
        break
    else:
        continue
print("Top earning employee in Year 2011 is %s with earning of %s"%(emp_11,max_val_11))

