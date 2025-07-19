#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:



df = pd.read_csv("worldpopulationdata.csv")


# In[3]:


import pandas as pd

df = pd.read_csv("worldpopulationdata.csv")


# In[4]:


df.head(5)


# In[5]:


#checking data from bottom
df.tail(5)


# In[6]:


#checking the column of the dataset
df.columns


# ## Some information about the dataset 
# 

# In[7]:


df.info()


# In[8]:


df.describe()


# In[9]:


df.duplicated().sum()


# ## Checking for missing values

# In[10]:


df.isna().sum()


# ## Checking unique values for columns

# In[11]:


print(df['Country Name'].unique())
print("Total no. of unique countries:",df['Country Name'].nunique())


# In[12]:


print(df['Country Code'].unique())
print("Total no. of unique countrie code:",df['Country Code'].nunique())


# # Dropping unnecessary columns

# In[13]:


df.drop(['Series Name','Country Name'],axis=1,inplace=True)


# # Extraction of top 10 countries with respect to total population

# In[14]:


#filter data for total population
total_population_data = df[df['Series Code'] =='SP.POP.TOTL']

#sort data based on the total population for 2022
total_population_sorted=total_population_data.sort_values(by="2022",ascending=False)

# Get the top ten countries with the highest total population for 2022
total_top_ten_countries=total_population_sorted.head(10)

print("Top ten countries of total population \n")
print(total_top_ten_countries[['Country Code']])


# # Bar Plot

# In[15]:


#Top ten countries of total population in year 2022 and 2016 :

plt.figure(figsize=(15,6))
plt.subplot(2, 2, 1)
sns.barplot(x="2022", y="Country Code", data=total_top_ten_countries, palette="coolwarm")
plt.title("Top Ten Countries of Total Population (2022)", fontsize=10)
plt.xlabel("Total Population", fontsize=10)
plt.ylabel("Country code", fontsize=10)

# Second subplot: 2016 data
plt.figure(figsize=(15,6))
plt.subplot(2, 2, 2)
sns.barplot(x="2016", y="Country Code", data=total_top_ten_countries, palette="coolwarm")
plt.title("Top Ten Countries of Total Population (2016)", fontsize=10)
plt.xlabel("Total Population", fontsize=10)
plt.ylabel("Country ", fontsize=10)

plt.tight_layout()
plt.show()


# In[16]:


## Extraction of bottom ten countries with respect to total population


# In[17]:


#sort data based on the total population for 2022
total_population_sorted1=total_population_data.sort_values(by="2022",ascending=True)

# Get the top ten countries with the highest total population for 2022
total_bottom_ten_countries=total_population_sorted1.head(10)

print("Bottom ten countries of total population \n")
print(total_bottom_ten_countries[['Country Code']])


# In[18]:


#Bottom ten countries of total population in year 2022 and 2016 :

plt.figure(figsize=(15,6))
plt.subplot(2, 2, 1)
sns.barplot(x="2022", y="Country Code", data=total_bottom_ten_countries, palette="coolwarm")
plt.title("Bottom Ten Countries of Total Population (2022)", fontsize=10)
plt.xlabel("Total Population", fontsize=10)
plt.ylabel("Country code", fontsize=10)

# Second subplot: 2016 data
plt.figure(figsize=(15,6))
plt.subplot(2, 2, 2)
sns.barplot(x="2016", y="Country Code", data=total_bottom_ten_countries, palette="coolwarm")
plt.title("Bottom Ten Countries of Total Population (2016)", fontsize=10)
plt.xlabel("Total Population", fontsize=10)
plt.ylabel("Country ", fontsize=10)

plt.tight_layout()
plt.show()


# ## Extraction of top 10 countries with highest male population

# In[19]:


#filter data for male population
male_population_data = df[df['Series Code'] =='SP.POP.TOTL.MA.IN']

#Sort data based on the male population for 2022
male_population_sorted =male_population_data.sort_values(by="2022", ascending =False)

#Get the top 10 countries with the highest male population for 2022
male_top_ten_countries = male_population_sorted .head(10)
print("Top ten countries of male population")
print(male_top_ten_countries[['Country Code']])


# 

# In[20]:


#filter data for female population
female_population_data = df[df['Series Code'] =='SP.POP.TOTL.FE.IN']

#Sort data based on the female population for 2022
female_population_sorted =female_population_data.sort_values(by="2022", ascending =False)

#Get the top 10 countries with the highest female population for 2022
female_top_ten_countries = female_population_sorted .head(10)
print("Top ten countries of female population")
print(female_top_ten_countries[['Country Code']])


# ## Top ten countries  with highest male and female population in 2022

# In[21]:


#Create the bar plot 
plt.figure(figsize=(15,6))
plt.subplot(2, 2, 1)
sns.barplot(x="2022", y="Country Code", data=male_top_ten_countries, palette="viridis")
plt.title("Top Ten Countries of Male Population(2022)", fontsize=10)
plt.xlabel("Male Population", fontsize=10)
plt.ylabel("Country code", fontsize=10)

# Second subplot: 2016 data
plt.figure(figsize=(15,6))
plt.subplot(2, 2, 2)
sns.barplot(x="2016", y="Country Code", data=female_top_ten_countries, palette="viridis")
plt.title("Top ten Countries of female population (2022)", fontsize=10)
plt.xlabel("Female Population", fontsize=10)
plt.ylabel("Country ", fontsize=10)

plt.tight_layout()
plt.show()


# ## Stacked Bar Plot

# In[22]:


# Top 10 countries with male and female population


# In[ ]:





# In[23]:


#merge male and female population data on 'Country Code'
merge_data =pd.merge(male_population_data, female_population_data,on='Country Code',suffixes=("_male","_female"))

#merge data
#calculate the total population for each country (male +female)
merge_data["Total population"] =merge_data["2022_male"] +merge_data["2022_female"]


# In[24]:


merge_data.head()


# In[25]:


sorted_data = merge_data.sort_values(by="Total population", ascending=False)


# ## Select the top 10 countries with the highest total population

# In[26]:


top_10_countries =sorted_data.head(10)


# In[27]:


plt.figure(figsize=(12,6))
sns.barplot(x="Country Code", y="2022_female", data=top_10_countries, color='red', label="Female Population")
sns.barplot(x="Country Code", y="2022_male", data=top_10_countries, bottom=top_10_countries["2022_female"], color='green', label="Male Population")
plt.xlabel("Country")
plt.ylabel("Population")
plt.legend()
plt.xticks(rotation=45,ha="right")
plt.show()


# ## Bottom 10 countries with male and female population(2022)

# In[28]:


#select top 10 countries with the highest population
bottom_10_countries = sorted_data.tail(10)


# In[36]:


#Create a stacked bar plot 
plt.figure(figsize=(12,6))
sns.barplot(x="Country Code", y="2022_female", data=bottom_10_countries, color='red', label="Female Population")
sns.barplot(x="Country Code", y="2022_male", data=bottom_10_countries,color='green', label="Male Population")
plt.xlabel("Country")
plt.ylabel("Population")
plt.legend()
plt.xticks(rotation=45,ha="right")
plt.show()


# In[ ]:





# In[ ]:




