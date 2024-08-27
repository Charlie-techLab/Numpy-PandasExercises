#!/usr/bin/env python
# coding: utf-8

# # Numpy Exercise

# #### 1. Import the numpy package under the name as np  

# In[1]:


import numpy as np


# #### 2. Print the numpy version and the configuration 

# In[4]:


print(np.__version__)
print(np.show_config())


# #### 3. Create a null vector of size 10

# In[5]:


arr = np.zeros(10)
print(arr)


# #### 4.  How to find the memory size of any array

# In[6]:


a = arr.size
b = arr.itemsize
print("{} bytes".format(a*b))


# #### 5.  How to get the documentation of the numpy add function from the command line? 

# In[7]:


get_ipython().run_line_magic('pinfo', 'np.add')


# #### 6.  Create a null vector of size 10 but the fifth value which is 1

# In[8]:


arr = np.zeros(10)
arr[4] = 1
print(arr)


# #### 7.  Create a vector with values ranging from 10 to 49

# In[9]:


arr = np.arange(10, 50, 5)
arr


# #### 8.  Reverse a vector (first element becomes last)

# In[10]:


np.flipud(arr)


# #### 9.  Create a 3x3 matrix with values ranging from 0 to 8

# In[11]:


arr = np.random.randint(0, 9, (3, 3))
arr


# #### 10. Find indices of non-zero elements from \[1,2,0,0,4,0\]

# In[14]:


arr = np.array([1, 2, 0, 0, 4, 0])
#ans = np.where(arr==0)
ans = np.nonzero(arr)
ans


# #### 11. Create a 3x3 identity matrix

# In[15]:


np.eye(3, 3)


# #### 12. Create a 3x3x3 array with random values

# In[16]:


np.random.random((3, 3, 3))


# #### 13. Create a 10x10 array with random values and find the minimum and maximum values

# In[18]:


arr = np.random.random((10, 10))
print(arr, sep="\n")
a = np.max(arr)
b = np.min(arr)
print(a, b, sep="\n")


# #### 14. Create a random vector of size 30 and find the mean value

# In[19]:


arr = np.random.random((30))
ans = np.mean(arr)
ans


# #### 15. Create a 2d array with 1 on the border and 0 inside

# In[20]:


ans = np.ones((5, 5))
ans[1:-1, 1:-1] = 0
ans


# #### 16. How to add a border (filled with 0's) around an existing array?

# In[21]:


ans = np.ones((5, 5))
np.pad(ans, pad_width = 1, mode = 'constant', constant_values = 0)


# #### 17. What is the result of the following expression?

# ```python
# 0 * np.nan
# np.nan == np.nan
# np.inf > np.nan
# np.nan - np.nan
# np.nan in set([np.nan])
# 0.3 == 3 * 0.1
# ```

# In[22]:


print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(np.nan in set([np.nan]))
print(0.3 == 3 * 0.1)


# #### 18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

# In[26]:


ans = np.diag([1, 2, 3, 4], -1)
ans


# #### 19. Create a 8x8 matrix and fill it with a checkerboard pattern

# In[27]:


ans = np.zeros((8, 8), dtype=int)
ans[1::2, ::2] = 1
ans[::2, 1::2] = 1
ans


# #### 20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?

# In[29]:


np.unravel_index(99, (6, 7, 8))

