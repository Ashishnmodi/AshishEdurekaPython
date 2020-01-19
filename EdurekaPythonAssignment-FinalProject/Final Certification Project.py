#!/usr/bin/env python
# coding: utf-8

# #Final Certification Project

# In[40]:


#1
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mew2ktykm4.csv")
d1 = df[["zip","e"]]
d2 = d1['zip'].value_counts().head(10)
print("Top 10 Zip Codes are as below:\n",d2)
n=0
zip_list=[19446.0, 19090.0]
while n < len(zip_list):
    for zipcode in zip_list:
        i=0
        for zp in df['zip']:
            if zp == zipcode:
                print("Zipcode %d is present in list"%int(zipcode))
                n+=1
                i+=1
                break
            else:
                continue    
        if i == 0:
            print("Zipcode %d is not present in list"%int(zipcode))
            n+=1
            i+=1
            break
        else:
            continue


# In[41]:


#2
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mew2ktykm4.csv")
d1 = df[["twp","e"]]
d2 = d1['twp'].value_counts().head(4)
print("Top 4 Township are as below:\n",d2)
n=0
twp_list=['LOWER POTTSGROVE', 'NORRISTOWN', 'HORSHAM', 'ABINGTON']
while n < len(twp_list):
    for twpship in twp_list:
        i=0
        for twn in df['twp']:
            if twn == twpship:
                print("Township %s is present in list"%twpship)
                n+=1
                i+=1
                break
            else:
                continue    
        if i == 0:
            print("Township %s is not present in list"%twpship)
            n+=1
            i+=1
            break
        else:
            continue


# In[47]:


#3
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mew2ktykm4.csv")
d1 = df[["title","e"]]
d2 = d1['title'].value_counts().head(2)
data=pd.DataFrame(d2)
max_val=data['title'].max()
min_val=data['title'].min()
for col_val in data['title'].iteritems():
    if col_val[-1] == int(max_val):
        re_max=col_val[0]
    else:
        re_min=col_val[0]
print("The most common reason for 911 call is %s with %d no. of calls "%(re_max,max_val))
print("The second common reason for 911 call is %s with %d no. of calls "%(re_min,min_val))


# In[14]:


#4
#3
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("mew2ktykm4.csv")
data = df['title'].value_counts()
d1=pd.DataFrame(data)
plt.figure(figsize=(18,7))
plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large')
plt.yticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-large')
plt.bar(d1.index,d1['title'])
plt.xlabel('Reason',size=20)
plt.ylabel('911 Calls Count',size=20)
plt.title('911 Reason Plot',size=30)
plt.show()

#Horizontal Bar plot can be done by plt.barh


# In[103]:


#5
import pandas as pd
import matplotlib.pyplot as plt
from datetime import *
import seaborn as sns
df = pd.read_csv("mew2ktykm4.csv")
d2 = df[["timeStamp","title","e"]]
d2['new_date']= [datetime.strptime(d,'%Y-%m-%d %H:%M:%S') for d in d2['timeStamp']]
d2['day']=d2['new_date'].dt.strftime('%A')
d1=d2[df['title'].str.contains('EMS:') == True]
d3=d1[["day","e"]]
d3=d3['day'].value_counts()
data=pd.DataFrame(d3)
max_val=data['day'].max()
for col_val in data['day'].iteritems():
    if col_val[-1] == int(max_val):
        da_max=col_val[0]
        break
    else:
        continue
print("The maximum EMS calls were %d on %s"%(max_val,da_max))


# In[95]:


#6
import pandas as pd
import matplotlib.pyplot as plt
from datetime import *
import seaborn as sns
df = pd.read_csv("mew2ktykm4.csv")
d2 = df[["timeStamp","title","e"]]
d2['new_date'] = [datetime.strptime(d,'%Y-%m-%d %H:%M:%S') for d in d2['timeStamp']]
#d2['week_no']=d2['new_date'].dt.week
d2['day']=d2['new_date'].dt.strftime('%a')
d1=d2[df['title'].str.contains('Traffic') == True]
sns.countplot(x=d1['day'],hue=d1['title'])
plt.show()
d3=d1[["day","e"]]
d3=d3['day'].value_counts()
data=pd.DataFrame(d3)
min_val=data['day'].min()
for col_val in data['day'].iteritems():
    if col_val[-1] == int(min_val):
        da_min=col_val[0]
        break
    else:
        continue
print("The minimum traffic calls were %d on %sday"%(min_val,da_min))


# In[89]:


#7
import pandas as pd
import matplotlib.pyplot as plt
from datetime import *
import seaborn as sns
df = pd.read_csv("mew2ktykm4.csv")
d2 = df[["timeStamp","title","e"]]
d2['new_date']= [datetime.strptime(d,'%Y-%m-%d %H:%M:%S') for d in d2['timeStamp']]
#d2['week_no']=d2['new_date'].dt.week
d2['month']=d2['new_date'].dt.strftime('%b')
d1=d2[df['title'].str.contains('Fire:') == True]
sns.countplot(x=d1['month'])
plt.show()
d3=d1[["month","e"]]
d3=d3['month'].value_counts()
data=pd.DataFrame(d3)
max_val=data['month'].max()
for col_val in data['month'].iteritems():
    if col_val[-1] == int(max_val):
        mo_max=col_val[0]
        break
    else:
        continue
print("The highest calls due to Fire were %d on %s month"%(max_val,mo_max))


# In[2]:


#8
import folium
import pandas as pd
df = pd.read_csv("mew2ktykm4.csv")
d1=df[df['title'].str.contains('Traffic') == True].head(10)
d2 = d1[["addr","title","e","lat","lng"]]
# lon1=list(d2["lng"])
# lat1=list(d2["lat"])
# area=list(d2["addr"])
map = folium.Map(location=[d2['lat'].mean(),d2['lng'].mean()],zoom_start=10)
fg=folium.FeatureGroup(name="Traffic Call Area")
for lat1,lon1,area in zip(d2['lat'],d2['lng'],d2['addr']):
    fg.add_child(folium.Marker(location=[lat1,lon1],popup=(folium.Popup(area)),icon_color='green'))
map.add_child(fg)
map.save(outfile="absmap.html")
map


# In[ ]:





# In[ ]:




