#!/usr/bin/env python
# coding: utf-8

# #Case Study I

# In[121]:


#1
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Hurricanes.csv")
plt.bar(df['Year'],df['Hurricanes'])
plt.xlabel('Year')
plt.ylabel('Hurricanes Count')
plt.title('Hurricanes Plot')
plt.show()


# In[122]:


#1
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("CityTemps.csv")
plt.hist(df['San Francisco'],range=(-20,40),histtype='barstacked')
plt.xlabel('Temperature')
plt.ylabel('Count')
plt.title('San Francisco Plot')
plt.show()

plt.hist(df['Moscow'],range=(-20,40),histtype='barstacked')
plt.xlabel('Temperature')
plt.ylabel('Count')
plt.title('Moscow Plot')
plt.show()


# In[126]:


#3
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("Cars2015.csv")
val=df['Make'].value_counts()
data=pd.DataFrame(val)
plt.figure(figsize=(9,9))
plt.pie(x=data['Make'],labels=data.index,autopct='%d%%')
plt.show()
max_val=data['Make'].max()
for col_val in data['Make'].iteritems():
    if col_val[-1]==int(max_val):
        mk=col_val[0]
        break
    else:
        continue
print("The largest Model Manufacturer is %s with %s Models"%(mk,max_val))


# In[127]:


#4
#Phase1-Reading data from clipboard
df=pd.read_clipboard(sep=',')
df.to_csv("exercise4.csv",index=False)


# In[128]:


#Phase2-Describe the data on unit price
df1=pd.read_csv("exercise4.csv")
df1['unit price'].describe()


# In[129]:


#Phase3-filter the data
df2=df1[['name','net_price','date']]
grouped_obj=df2.groupby('name')
for grp_name,grp_val in grouped_obj:
    print("Group Name",grp_name)
    print("Group Value")
    print(grp_val)


# In[130]:


#Phase4-Plotting graph
import matplotlib.pyplot as plt
df3=df2[['name','net_price']]
df4=pd.DataFrame(df3.groupby('name').net_price.sum())
plt.figure(figsize=(9,9))
plt.xlabel('Customer Name',size=20)
plt.ylabel('Total Sales',size=20)
plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large')
plt.title('Customer Total Sale Data',size=20)
plt.plot(df4.index,df4['net_price'])
plt.show()


# In[131]:


#5
#5.1
import matplotlib.pyplot as plt
import pandas as pd
X = [1,2,3,4]
Y = [20, 21, 20.5, 20.8]
plt.plot(X,Y)
plt.show()


# In[132]:


#5.2
import matplotlib.pyplot as plt
import pandas as pd
X = [1,2,3,4]
Y = [20, 21, 20.5, 20.8]
plt.plot(X,Y,color='red', linestyle='dashdot', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.grid()
plt.show()


# In[133]:


#5.3
import matplotlib.pyplot as plt
import pandas as pd
X = [1,2,3,4]
Y = [20, 21, 20.5, 20.8]
plt.plot(X,Y,color='red', linestyle='dashdot', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.axis([0,5,19,22])
plt.grid()
plt.show()


# In[134]:


#5.4
import matplotlib.pyplot as plt
import pandas as pd
X = [1,2,3,4]
Y = [20, 21, 20.5, 20.8]
plt.plot(X,Y,color='red', linestyle='dashdot', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.axis([0,5,19,22])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Simple Plot")
plt.grid()
plt.show()


# In[135]:


#5.5
import matplotlib.pyplot as plt
import pandas as pd
X = [1,2,3,4]
Y = [20, 21, 20.5, 20.8]
plt.plot(X,Y,color='red', linestyle='dashdot', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.axis([0,5,19,22])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Simple Plot")
y_error = [0.12, 0.13, 0.2, 0.1]
plt.errorbar(X,Y,yerr=y_error)
plt.grid()
plt.show()


# In[136]:


#5.6
import matplotlib.pyplot as plt
import pandas as pd
X = [1,2,3,4]
Y = [20, 21, 20.5, 20.8]
plt.plot(X,Y,color='red', linestyle='dashdot', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.axis([0,5,19,22])
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Simple Plot")
y_error = [0.12, 0.13, 0.2, 0.1]
plt.errorbar(X,Y,yerr=y_error)
plt.grid()
plt.figure(figsize=(4,5),dpi=100)
plt.show()


# In[137]:


#5.7
import matplotlib.pyplot as plt
import pandas as pd
X = [1,2,3,4]
Y = [20, 21, 20.5, 20.8]
plt.plot(X,Y,color='red', linestyle='dashdot', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.axis([0,5,19,22])
plt.xlabel("X-Axis",size=14)
plt.ylabel("Y-Axis",size=14)
plt.title("Simple Plot",size=14)
y_error = [0.12, 0.13, 0.2, 0.1]
plt.errorbar(X,Y,yerr=y_error)
plt.grid()
plt.figure(figsize=(4,5),dpi=100)
plt.show()


# In[138]:


#5.8
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x = np.random.randn(10,5)
x = x.ravel()
y = np.random.randn(5,10)
y = y.ravel()
plt.scatter(x,y)
plt.show()


# In[139]:


#5.9
import matplotlib.pyplot as plt
import pandas as pd
data={'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
'female': [0, 1, 1, 0, 1],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, 2, 3],
'postTestScore': [25, 94, 57, 62, 70]}
df=pd.DataFrame(data)
df
plt.scatter(df['preTestScore'],df['postTestScore'],s=df['age'])
plt.show()


# In[140]:


#5.10
import matplotlib.pyplot as plt
import pandas as pd
data={'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
'female': [0, 1, 1, 0, 1],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, 2, 3],
'postTestScore': [25, 94, 57, 62, 70]}
df=pd.DataFrame(data)
df
plt.scatter(df['preTestScore'],df['postTestScore'],s=300,c=df['female'])
plt.show()


# #Case Study II

# In[141]:


#1
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("BigMartSalesData.csv")
data=df[df['Year']==2011]
data=data[['Amount','Month']]
data_11=pd.DataFrame(data.groupby('Month').Amount.sum())
plt.plot(data_11.index,data_11['Amount'],color='red', linestyle='dashdot', linewidth = 3,marker='o', markerfacecolor='blue', markersize=12)
plt.xlabel("Month",size=14)
plt.ylabel("Total Sales Amount",size=14)
plt.title("Total Sales of Year-2011",size=14)
plt.show()
min_val=data_11['Amount'].min()
for col_val in data_11['Amount'].iteritems():
    if col_val[-1]==float(min_val):
        mth=col_val[0]
        break
    else:
        continue
print("The lowest sales month is %s with %.2f Total Sales Value"%(mth,min_val))


# In[150]:


#2
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("BigMartSalesData.csv")
data=df[df['Year']==2011]
data=data[['Amount','Month']]
data_11=pd.DataFrame(data.groupby('Month').Amount.sum())
plt.bar(data_11.index,data_11['Amount'],color='blue', linestyle='dashdot', linewidth = 3)
plt.xlabel("Month",size=14)
plt.ylabel("Total Sales Amount",size=14)
plt.title("Total Sales of Year-2011",size=14)
plt.show()


# In[152]:


#3
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("BigMartSalesData.csv")
data=df[df['Year']==2011]
data=data[['Amount','Country']]
data_co=pd.DataFrame(data.groupby('Country').Amount.sum())
plt.figure(figsize=(7,7),dpi=50)
plt.pie(data_co['Amount'],labels=data_co.index,autopct='%d%%',shadow=True,startangle=90)
plt.title("Total Sales of Year-2011",size=14)
plt.show()
max_val=data_co['Amount'].max()
for col_val in data_co['Amount'].iteritems():
    if col_val[-1]==float(max_val):
        con=col_val[0]
        break
    else:
        continue
print("The Highest sales Country is %s with %.2f Total Sales Value"%(con,max_val))


# In[155]:


#4
#Option1
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("BigMartSalesData.csv")
#data=df[df['Year']==2011]
data=df[['Amount','Quantity']]
data_co=pd.DataFrame(data.groupby('Amount').Quantity.sum())
#plt.figure(figsize=(7,7),dpi=50)
plt.scatter(data['Amount'],data['Quantity'],c='red')
plt.xlabel("Quantity",size=14)
plt.ylabel("Total Sales Amount",size=14)
plt.title("Invoice Amount Concentration",size=14)
plt.show()


# In[156]:


#4
#Option2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("BigMartSalesData.csv")
amount_less_than_16000 = df[df['Amount'] < 16000]['Amount']
sns.boxplot(y=amount_less_than_16000)
plt.title("Invoice Amount Concentration",size=14)
plt.show()
amount_less_than_16000.describe()

