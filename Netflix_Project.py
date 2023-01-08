#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


netflix=pd.read_csv("C:/Users/User/OneDrive/Desktop/Software/DA/netflix_titles.csv")


# In[4]:


netflix


# In[5]:


netflix.head()


# In[6]:


netflix.tail()


# In[11]:


netflix.columns


# In[8]:


netflix.describe(include="all")


# In[15]:


netflix.info()


# In[16]:


netflix.shape


# In[21]:


netflix.isnull().sum()


# In[25]:


netflix.nunique()


# In[26]:


netflix.duplicated().sum()


# In[27]:


df=netflix.copy()


# In[35]:


df=df.dropna()
df.shape


# In[40]:


df.columns


# In[48]:


df["date_added"]=pd.to_datetime(df["date_added"])
df["day_added"]=df["date_added"].dt.day
df["year_added"]=df["date_added"].dt.year
df["month_added"]=df["date_added"].dt.month
df["day_added"].astype(int)
df["year_added"].astype(int)


# In[49]:


df.columns


# In[50]:


df.head()


# In[70]:


sns.countplot(netflix["type"])
fig=plt.gcf()
fig.set_size_inches(10,10)
plt.title("Type")


# In[72]:


sns.countplot(netflix["rating"])
#sns.countplot(netflix['rating']).set_xticklabels(sns.countplot(netflix['rating']).get_xticklabels(), rotation=90, ha="right")
fig=plt.gcf()
fig.set_size_inches(10,10)
#plt.title("Rating")


# In[84]:


sns.countplot(x="rating",hue="type",data=netflix)
fig=plt.gcf()
fig.set_size_inches(10,10)


# In[107]:


labels = ['Movie', 'TV show']
size = netflix['type'].value_counts()
colors = plt.cm.Wistia(np.linspace(0, 1, 2))
explode = [0, 0.1]
plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(size,labels=labels, colors = colors, explode = explode, shadow = True, startangle =180)
plt.legend()
plt.show()


# In[111]:


netflix['rating'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True,figsize=(10,10))
plt.show()


# In[123]:


from wordcloud import WordCloud


# In[134]:


plt.subplots(figsize=(20,20))
wordcloud = WordCloud(
                          background_color='white',
                          width=1920,
                          height=1080
                         ).generate(" ".join(df.country))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('country.png')
plt.show()


# In[135]:


plt.subplots(figsize=(25,15))
wordcloud = WordCloud(
                          background_color='white',
                          width=1920,
                          height=1080
                         ).generate(" ".join(df.director))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('director.png')
plt.show()


# In[136]:


plt.subplots(figsize=(25,15))
wordcloud = WordCloud(
                          background_color='white',
                          width=1920,
                          height=1080
                         ).generate(" ".join(df.listed_in))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('category.png')
plt.show()


# In[137]:


df.columns


# In[139]:


df["release_year"].value_counts


# In[150]:


plt.figure(figsize=(13,10))
g = netflix[netflix['release_year'] > 2010].release_year.value_counts().plot.bar(figsize=(10, 7))
g.set_xlabel("Release Year")
g.set_ylabel("No of Released Movies")
g.set_title("Year Wise Releases")


# In[151]:


netflix[netflix['type'] == 'Movie'].sort_values('release_year')[0:10]


# In[154]:


netflix[netflix['type'] == 'TV Show'].sort_values('release_year')[0:10]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




