#!/usr/bin/env python
# coding: utf-8

# # #My first data science Project
# # # Helicopter Escapes !

# In[9]:


from helper import *


# ## Get the data
# # # print the first 3 rows

# In[14]:


url = "https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes"
data = data_from_url(url)

for row in data[:3]:
    print(row)


# In[16]:


index = 0
for row in data:
    data[index] = row[:-1]
    index +=1
print(data[:10])


# In[17]:


index =0 
for row in data:
    data[index][0] = fetch_year(row[0])
    index+=1
print(data)


# ## get all the years

# In[18]:


min_year = min(data, key=lambda x: x[0])[0]  # gets the min year per row
max_year = max(data, key=lambda x: x[0])[0]
print(min_year)
print(max_year)
years = []
for y in range(min_year, max_year+1): years.append(y)
print(years)


# In[19]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])
# 3)
print(attempts_per_year)


# In[20]:


# this loop increments the 0 by 1 everytime the condition evaluates to be true.
for row in data:
    for ya in attempts_per_year: 
        y = ya[0]
        if row[0] == y:
            ya[1] += 1

print(attempts_per_year)


# In[24]:


attempts_per_year = []
for year in years:
    attempts_per_year.append([year, 0])
# 3)
print(attempts_per_year)


# In[25]:


# this loop increments the 0 by 1 everytime the condition evaluates to be true.
for row in data:
    for ya in attempts_per_year: 
        y = ya[0]
        if row[0] == y:
            ya[1] += 1

print(attempts_per_year)


# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# In[27]:


countries_frequency = df["Country"].value_counts()
print(countries_frequency)
print(df)


# In[28]:


print_pretty_table(countries_frequency = df["Country"].value_counts())


# In[ ]:




