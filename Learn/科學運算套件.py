import numpy as np

dist_in_km = [3, 5, 10, 21.1, 42.195]
dist_in_mile = [d *0.62137 for d in dist_in_km]

#      np.array() -> 將原生 list 轉換為 ndarray
mile = np.array(dist_in_km)
mile = mile * 0.62137

print(mile)
print(np.arange(8))
print(np.arange(1,8))
print(np.arange(1,10,2))

arr = np.linspace(1,10,10)
print(arr,arr.dtype)
arr = arr.astype(int)
print(arr,arr.dtype) 

# ndarray 中僅能儲存單一種型別。
lst = [42.195, 'km', True]
for i in lst:
  print(type(i))
arr = np.array(lst)
for i in arr:
  print(type(i))

# 維度 1：向量（vector）  
u = np.array([8,7]).reshape(2,1)
v = np.array([8,7,6]).reshape(3,1)
print(u,'\n')
print(v,'\n')

# 維度 2：矩陣（matrix）
# 創造3x3 矩陣
mat = np.arange(0,9).reshape(3,3)
print(mat,'\n')

# 維度 3：張量（tensor）
ten = np.arange(1,25).reshape(2,4,3)
print(ten)