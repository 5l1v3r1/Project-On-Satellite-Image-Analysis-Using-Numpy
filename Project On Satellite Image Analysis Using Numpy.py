#!/usr/bin/env python
# coding: utf-8

# Loading The Libraries We Need:Numpy, Scipy, Matplotlib.

# In[31]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
import imageio


#  We Create Numpy From The Image File We are Using :
#  
#  We are choose a Satellite Image file as ndarray and Displayed The Type.

# In[32]:


from skimage import data

photo_data = imageio.imread('sd-3layers.jpg')

type(photo_data)


# We Would Like To See How The Image Look like.

# In[33]:


plt.figure(figsize=(12,12))
plt.imshow(photo_data)


# We Like To Know The Shape Of The Satellite

# In[4]:


photo_data.shape


# The Shape Of the ndarray shows we have 3 layered Matrix.
# 
# The first number(3725) indicate the lenght, the second number(4797), indicate the wildth
# 
# The last number(i.e, 3), indicate the layers : RED, BLUE and GREEN
# 
# 
# RGB in the Photo
# 
# **RED Pixel indicates the Altitude**
# 
# **BLUE Pixel indciates Aspect**
# 
# **GREEN Pixel indicates Slope**
# 

# In[5]:


photo_data.size


# We Check the maximum and minimum data value

# In[6]:


photo_data.min(), photo_data.max()


# In[7]:


photo_data.mean()


# Pixel on the 150th row and 250 columns

# In[8]:


photo_data[150, 250]


# In[9]:


photo_data[150, 250, 1]


# We want to set the Pixel to all Zeros

# In[12]:


#photo_data = imageio.imread('sd-3layers.jpg')
photo_data[150, 250] = 0
plt.figure(figsize=(9, 9))
plt.imshow(photo_data)


# We also Try to Change The Colour In a Range
# 
# We set the Green layer for rows 200 - 800 to full intensity

# In[13]:


photo_data = imageio.imread('sd-3layers.jpg')

photo_data[200:800, : ,1] = 255
plt.figure(figsize=(9, 9))
plt.imshow(photo_data)


# We set the data to forma, when we set the rows from 200 - 800 are full intensity

# In[15]:


photo_data = imageio.imread('sd-3layers.jpg')

photo_data[200:800, :] = 255
plt.figure(figsize=(9, 9))
plt.imshow(photo_data)


# We are also doing it for Black, instead of 255, We set to = 0

# In[16]:


photo_data = imageio.imread('sd-3layers.jpg')

photo_data[200:800, :] = 0
plt.figure(figsize=(9, 9))
plt.imshow(photo_data)


# We are To Pick All Pixels with Low Values 
# 
# We use comparison to select all value that are less than 200 or we can call it point of less interest

# In[21]:


photo_data = imageio.imread('sd-3layers.jpg')
print("Shape of photo_data:", photo_data.shape)
low_value_filter = photo_data < 200
print("Shape of low_value_filter:", low_value_filter.shape)


# We Filter Out  Low Values
# 
# So whenever low_value is True , set value = 0

# In[22]:


plt.figure(figsize=(9, 9))
plt.imshow(photo_data)
photo_data[low_value_filter] = 0
plt.figure(figsize=(9, 9))
plt.imshow(photo_data)


# More Rows and Columns Operations.
# 
# Here we try a linear relationship between rows and columns

# In[24]:


rows_range = np.arange(len(photo_data))
cols_range = rows_range
print(type(rows_range))


# In[25]:


photo_data[rows_range, cols_range] = 255


# In[27]:


plt.figure(figsize=(12, 12))
plt.imshow(photo_data)


# In[ ]:




