#!/usr/bin/env python
# coding: utf-8

# Case Study I

# In[2]:


#1
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df


# In[11]:


#2
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df1=df.ix[0:5,0:2] #method1
df2=df[['float_col','int_col']] #method2
df3=df.loc[:,'float_col':'int_col'] #method3
df4=df.iloc[:,0:2] #method4
df4


# In[16]:


#3
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df1=df[df['float_col']>0.15]
df2=df[df['float_col']==0.1]
print(df1)
print(df2)


# In[20]:


#4
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df1=df[(df['float_col']>0.1) & (df['int_col']>2)]
df1


# In[21]:


#5
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df1=df[(df['float_col']>0.1) | (df['int_col']>2)]
df1


# In[31]:


#6
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df1=df[df['float_col'] <= 0.1]
df1


# In[37]:


#7
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df2=df.rename(columns={"int_col":"new_name"})
df2


# In[38]:


#8
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df.rename(columns={"int_col":"new_name"},inplace=True)
df


# In[40]:


#9
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df=df.dropna()
df


# In[43]:


#10
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df['float_col']=df['float_col'].fillna(df['float_col'].mean())
df


# In[70]:


#11
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
#df.ix[(df['str_col'] != False), 'str_col'] = 'map_'+ df.ix[(df['str_col'] != False), 'str_col'] #method using .ix method

#Alternate method
for col_val in df['str_col'].iteritems():
    if col_val[-1] != None:
        df.iloc[col_val[0],2] = 'map_'+ col_val[-1]
    else:
        continue
df


# In[71]:


#12
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
grouped_obj=df.groupby('str_col')
for grp_name,grp_val in grouped_obj:
    print("Group Name:",grp_name)
    flt_avg=grp_val['float_col'].mean()
    print("Mean value of Flot Column:",flt_avg)


# In[72]:


#13
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df[['float_col','int_col']].cov()


# In[73]:


#14
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
df=pd.DataFrame(data)
df[['float_col','int_col']].corr()


# In[88]:


#15
import pandas as pd
import numpy as np
data={'float_col':[0.1,0.2,0.2,10.1,np.nan],'int_col':[1,2,6,8,-1],'str_col':['a','b',None,'c','a']}
x=pd.DataFrame(data)
data1={'some_val':[1,2],'str_col':['a','b']}
other=pd.DataFrame(data1)
print("Inner Join:\n",pd.merge(x,other,on='str_col',how='inner')) #inner
print("Outer Join:\n",pd.merge(x,other,on='str_col',how='outer')) #outer
print("Right Join:\n",pd.merge(x,other,on='str_col',how='right')) #right
print("Left Join:\n",pd.merge(x,other,on='str_col',how='left')) #left


# In[128]:


#16
import pandas as pd
import numpy as np
names=['Anil','sunita','suman','lokesh','Sumita','John','Johny']
ser=pd.Series(names)
ser.to_csv("names.txt",header=False,index=False)
f=open("body.txt","w")
f.write("I am going to Delhi. Lets meet on 7th Jan 2018\nHave a great day\nRegards\nTeam Victory")
f.close()
df=pd.read_csv("names.txt",header=-1)
for i in range(len(names)):
    with open("body.txt") as f:
        with open(names[i]+".txt", "w") as f1:
            f1.write("Hello %s\n"%names[i])
            for line in f:
                f1.write(line)


# Case Study II

# In[161]:


#1
import pandas as pd
import folium
df=pd.read_csv("Police_Department_Incidents_Year_2016_.csv")
df1=df.head(100)
#lon=list(df1["X"])
#lat=list(df1["Y"])
#area=list(df1["PdDistrict"])
map = folium.Map(location=[df1['X'].mean(),df1['Y'].mean()],zoom_start=10)
fg=folium.FeatureGroup(name="Crime Analysis")
for lon,lat,area in zip(df1['X'],df1['Y'],df1["PdDistrict"]):
    fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(area)),icon=folium.Icon(icon_color='green')))
map.add_child(fg)
map.save(outfile="BasicWebMap.html")
map


# In[162]:


#2
import pandas as pd
import folium
from datetime import *
#from datetime import date, datetime, timedelta
df=pd.read_csv("Police_Department_Incidents_Year_2016_.csv")
df1=df[df['Category']=='ROBBERY']
df1=df1[['Date','X','Y',"PdDistrict"]]
df1['new_date']= [datetime.strptime(d,'%m/%d/%Y %I:%M:%S %p') for d in df1['Date']]
df2=df1.sort_values(by='new_date',ascending=False)
DD = timedelta(days=7)
df3=df2[df2['new_date']>df2['new_date'].max()-DD]
map = folium.Map(location=[df3['X'].mean(),df3['Y'].mean()],zoom_start=10)
fg=folium.FeatureGroup(name="Robbery latest 7 Days")
for lon,lat,area in zip(df3['X'],df3['Y'],df3["PdDistrict"]):
    fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(area)),icon=folium.Icon(icon_color='blue')))
map.add_child(fg)
map.save(outfile="Robbery_7Days.html")
map


# In[168]:


#3
import pandas as pd
import folium
from datetime import *
#from datetime import date, datetime, timedelta
df=pd.read_csv("Police_Department_Incidents_Year_2016_.csv")
df1=df[(df['Category']=='FRAUD') | (df['Category']=='GAMBLING') ]
df1=df1[['Date','X','Y',"PdDistrict"]]
df1['new_date']= [datetime.strptime(d,'%m/%d/%Y %I:%M:%S %p') for d in df1['Date']]
df2=df1.sort_values(by='new_date',ascending=False)
DD = timedelta(days=15)
df3=df2[df2['new_date']>(df2['new_date'].max()-DD)]
map = folium.Map(location=[df3['X'].mean(),df3['Y'].mean()],zoom_start=10)
fg=folium.FeatureGroup(name="Fraud and Gambling latest 15 Days")
for lon,lat,area in zip(df3['X'],df3['Y'],df3["PdDistrict"]):
    fg.add_child(folium.Marker(location=[lat,lon],popup=(folium.Popup(area)),icon=folium.Icon(color="red",icon="hamburger", prefix='fa')))
map.add_child(fg)
map.save(outfile="Fraud and Gambling_15Days.html")
map


# In[175]:


#4
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df1=pd.read_csv("Divvy_Stations_2016_Q3.csv")
df2=pd.read_csv("Divvy_Stations_2016_Q4.csv")
sns.heatmap(df1.corr(),annot=True)
sns.heatmap(df2.corr(),annot=True)


# In[ ]:




