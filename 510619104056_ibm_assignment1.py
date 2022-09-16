#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Basic Python

# ## 1. Split this string

# In[ ]:


s = "Hi there Sam!"


# In[3]:


s="Hi there Sam!"
print(s.split( ))


# ## 2. Use .format() to print the following string. 
# 
# ### Output should be: The diameter of Earth is 12742 kilometers.

# In[ ]:


planet = "Earth"
diameter = 12742


# In[4]:


planet="Earth"
diameter=12742
print("The diameter of {} is {} kilometers".format(planet,diameter))


# ## 3. In this nest dictionary grab the word "hello"

# In[ ]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[19]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])


# # Numpy

# In[ ]:


import numpy as np


# ## 4.1 Create an array of 10 zeros? 
# ## 4.2 Create an array of 10 fives?

# In[ ]:


import numpy as np
array1=[0,0,0,0,0,0,0,0,0,0]


# In[ ]:


import numpy as np
array2=[5,5,5,5,5,5,5,5,5,5]


# ## 5. Create an array of all the even integers from 20 to 35

# In[24]:


array3=[]
for i in range(20,35):
    if(i%2==0):
        array3.append(i)
print(array3)


# ## 6. Create a 3x3 matrix with values ranging from 0 to 8

# In[32]:


import numpy as np

array4=[[0,1,2],[3,4,5],[6,7,8]]
print(array4)


# ## 7. Concatinate a and b 
# ## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])

# In[45]:


import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])

print(np.concatenate((a,b),axis=0))


# # Pandas

# ## 8. Create a dataframe with 3 rows and 2 columns

# In[64]:


import pandas as pd

dp=pd.DataFrame(index=[1,2,3],columns=[1,2])
print(dp)


# ## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023

# In[66]:


import pandas as pd
date=pd.date_range(start='1-1-2023',end='10-2-23')
for dates in date:
    print(dates)


# ## 10. Create 2D list to DataFrame
# 
# lists = [[1, 'aaa', 22],
#          [2, 'bbb', 25],
#          [3, 'ccc', 24]]

# In[ ]:


lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]


# In[71]:


import pandas as pd
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
df=pd.DataFrame(lists)
print(df)


# In[ ]:




