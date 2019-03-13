
# coding: utf-8

# ## 相關性分析

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.family']='SimHei' #顯示中文

# 政府開放資料平台 - 不動產買賣實價登錄批次資料（http://data.gov.tw/node/6213）
df = pd.read_csv('A_LVR_LAND_A.csv', encoding='big5')
df[:10]


# In[3]:


df.corr()


# In[4]:


plt.rcParams['axes.unicode_minus']=False #正常顯示負號
df.plot(kind='scatter',title='散佈圖（高度正相關）',figsize=(6,4),x='建物移轉總面積平方公尺',y='總價元',marker='+')


# ## 資料預處理

# In[5]:


df = df[df['建物移轉總面積平方公尺']>0]
df = df[df['建物移轉總面積平方公尺']<1000]
df = df[df['總價元']>0]/10000
df.plot(kind='scatter',title='散佈圖（高度正相關）',figsize=(6,4),x='建物移轉總面積平方公尺',y='總價元',marker='+')


# ## 簡單線性迴歸
# ### 切分訓練及測試資料 (1 feature)

# In[6]:


from sklearn.cross_validation import train_test_split
X = df[['建物移轉總面積平方公尺']]
y = df[['總價元']]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3) # 30% for testing, 70% for training
X_train.head()


# In[7]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
plt.style.use('ggplot')

# linear regression 物件
regr = linear_model.LinearRegression()

# 訓練模型
regr.fit(X_train, y_train)

print('各變項參數: \n', regr.coef_)
print("均方誤差 (Mean squared error, MSE): %.2f" % np.mean((regr.predict(X_test) - y_test) ** 2))

plt.scatter(X_test, y_test,  color='blue', marker = 'x')
plt.plot(X_test, regr.predict(X_test), color='green', linewidth=1)

plt.ylabel('總價元(10K)')
plt.xlabel('建物移轉總面積平方公尺')

plt.show()


# ## 多變項線性迴歸
# ### 切分訓練及測試資料 (2 features)

# In[8]:


from sklearn.cross_validation import train_test_split
X = df[['建物移轉總面積平方公尺','建物現況格局-衛']]
y = df[['總價元']]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3) # 30% for testing, 70% for training
X_train.head()


# ### 標準化 (Normalize)

# In[9]:


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_nor = sc.transform(X_train)
X_test_nor = sc.transform(X_test)
X_train_nor[:10]


# In[10]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
plt.style.use('ggplot')

# linear regression 物件
regr = linear_model.LinearRegression()

# 訓練模型
regr.fit(X_train_nor, y_train)

print('各變項參數(normalized): \n', regr.coef_)
print("均方誤差 (Mean squared error, MSE): %.2f" % np.mean((regr.predict(X_test_nor) - y_test) ** 2))


# ## 多項式(Polynomial) 非線性迴歸
# ### 切分訓練及測試資料 (1 feature)

# In[16]:


from sklearn.cross_validation import train_test_split
X = df[['建物移轉總面積平方公尺']]
y = df[['總價元']]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3) # 30% for testing, 70% for training
X_train.head()


# ### 創造高維變項

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures
plt.style.use('ggplot')

quadratic = PolynomialFeatures(degree=2)
X_train_raw = X_train.copy() #原始X_train
X_test_raw = X_test.copy() #原始X_test
X_train = quadratic.fit_transform(X_train_raw) #產生x^0, x^1, x^2
X_test = quadratic.fit_transform(X_test_raw) #產生x^0, x^1, x^2

X_fit = pd.DataFrame(np.arange(0,0.1,0.001))

# linear regression 物件
# regr = linear_model.LinearRegression()

# 訓練模型
# regr.fit(X_train, y_train)

# print('各變項參數: \n', regr.coef_)
# print("均方誤差 (Mean squared error, MSE): %.2f" % np.mean((regr.predict(X_test) - y_test) ** 2))

# Plot outputs
# plt.scatter(X_test_raw, y_test,  color='blue', marker = 'x')
# plt.plot(X_fit, regr.predict(quadratic.fit_transform(X_fit)), color='green', linewidth=1)

# plt.show()

