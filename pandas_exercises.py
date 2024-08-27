#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Pandas</center>
# 
# ![](https://pandas.pydata.org/_static/pandas_logo.png)
# 
# 
# ## Installation
# 
# Simply,
# ```
# pip install pandas
# ```
# 
# 
# ## Reading data from a CSV file
# 
# You can read data from a CSV file using the ``read_csv`` function. By default, it assumes that the fields are comma-separated.

# In[67]:


# import pandas
import pandas as pd
from datetime import datetime


# >The `imdb.csv` dataset contains Highest Rated IMDb "Top 1000" Titles.

# In[68]:


# load imdb dataset as pandas dataframe
imdb_df = pd.read_csv("data/imdb_1000.csv")


# In[69]:


# show first 5 rows of imdb_df
imdb_df.head()


# >The `bikes.csv` dataset contains information about the number of bicycles that used certain bicycle lanes in Montreal in the year 2012.

# In[70]:


# load bikes dataset as pandas dataframe
bikes_df = pd.read_csv("data/bikes.csv", sep=";", parse_dates=['Date'], dayfirst = True, index_col = 'Date')


# In[71]:


# show first 3 rows of bikes_df
bikes_df.head(n=3)


# ## Selecting columns
# 
# When you read a CSV, you get a kind of object called a DataFrame, which is made up of rows and columns. You get columns out of a DataFrame the same way you get elements out of a dictionary.

# In[72]:


# list columns of imdb_df
imdb_df.columns


# In[73]:


# what are the datatypes of values in columns
imdb_df.dtypes


# In[74]:


# list first 5 movie titles
imdb_df['title'].head()


# In[75]:


# show only movie title and genre
imdb_df[['title', 'genre']].head()


# ## Understanding columns
# 
# On the inside, the type of a column is ``pd.Series`` and pandas Series are internally numpy arrays. If you add ``.values`` to the end of any Series, you'll get its internal **numpy array**.

# In[76]:


# show the type of duration column
imdb_df.duration.dtype


# In[77]:


# show duration values of movies as numpy arrays
imdb_df.duration.values[:10]


# ## Applying functions to columns
# 
# Use `.apply` function to apply any function to each element of a column.

# In[43]:


# convert all the movie titles to uppercase
to_uppercase = lambda x: x.upper()
imdb_df['title'].apply(to_uppercase).head()


# ## Plotting a column
# 
# Use ``.plot()`` function!

# In[83]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[115]:


# plot the bikers travelling to Berri1 over the year
bikes_df['Berri1'].plot()


# In[86]:


# plot the bikers travelling to Berri1 over the year
bikes_df['Berri1'].plot()


# In[87]:


# plot all the columns of bikes_df
bikes_df.plot(figsize=(10, 7))


# ## Value counts
# 
# Get count of unique values in a particular column/Series.

# In[88]:


# what are the unique genre in imdb_df?
imdb_df['genre'].value_counts()


# In[89]:


# plotting value counts of unique genres as a bar chart
imdb_df['genre'].value_counts().plot.bar()


# In[90]:


# plotting value counts of unique genres as a pie chart
imdb_df['genre'].value_counts().plot.pie()


# ## Index
# 
# ### DATAFRAME = COLUMNS + INDEX + ND DATA
# 
# ### SERIES = INDEX + 1-D DATA
# 
# **Index** or (**row labels**) is one of the fundamental data structure of pandas. It can be thought of as an **immutable array** and an **ordered set**.
# 
# > Every row is uniquely identified by its index value.

# In[91]:


# show index of bikes_df
bikes_df.index


# In[92]:


# get row for date 2012-01-01
bikes_df.loc['2012-01-01']


# #### To get row by integer index:
# 
# Use ``.iloc[]`` for purely integer-location based indexing for selection by position.

# In[93]:


# show 11th row of imdb_df using iloc
bikes_df.iloc[10]


# ## Selecting rows where column has a particular value

# In[94]:


# select only those movies where genre is adventure
imdb_df[imdb_df['genre'] == 'Adventure'].head()


# In[95]:


# which genre has highest number of movies with star rating above 8 and duration more than 130 minutes?
good_movies_condition = (imdb_df['star_rating'] > 8) & (imdb_df['duration'] > 130)
imdb_df[good_movies_condition]['genre'].value_counts()


# ## Adding a new column to DataFrame

# In[96]:


# add a weekday column to bikes_df
bikes_df['weekday'] = bikes_df.index.weekday


# ## Deleting an existing column from DataFrame

# In[97]:


# remove column 'Unnamed: 1' from bikes_df
bikes_df.drop('Unnamed: 1', axis=1, inplace=True)


# ## Deleting a row in DataFrame

# In[99]:


# remove row no. 1 from bikes_df
bikes_df.drop(bikes_df.index[0]).head()


# ## Group By
# 
# Any groupby operation involves one of the following operations on the original object. They are −
# 
# - Splitting the Object
# 
# - Applying a function
# 
# - Combining the results
# 
# In many situations, we split the data into sets and we apply some functionality on each subset. In the apply functionality, we can perform the following operations −
# 
# - **Aggregation** − computing a summary statistic
# 
# - **Transformation** − perform some group-specific operation
# 
# - **Filtration** − discarding the data with some condition

# In[100]:


# group imdb_df by movie genres
genre_groups = imdb_df.groupby('genre')


# In[101]:


# get crime movies group
genre_groups.get_group('Crime').head()


# In[130]:


# get mean of movie durations for each group
genre_groups.aggregate('star_rating')


# In[119]:


# change duration of all movies in a particular genre to mean duration of the group
imdb_df['new_duration'] = genre_groups['duration'].transform(lambda x: x.mean())


# In[120]:


# drop groups/genres that do not have average movie duration greater than 120.
new_imdb_df = genre_groups.filter(lambda x: x['duration'].mean() > 120)


# In[121]:


# group weekday wise bikers count
weekday_groups = bikes_df.groupby('weekday')


# In[126]:


# get weekday wise biker count
weekday_counts = weekday_groups.aggregate('sum')


# In[123]:


weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# In[124]:


# plot weekday wise biker count for 'Berri1'
weekday_counts['Berri1'].plot.bar()


# ![](https://memegenerator.net/img/instances/500x/73988569/pythonpandas-is-easy-import-and-go.jpg)
