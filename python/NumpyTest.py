import numpy as np

arr = np.array([1, 5,2, 3, 4, 5])
arr1 = np.sort(arr);
# 将arr中的元素全部转为字符串格式
arr2 = np.array(arr, dtype = 'U')
# 将arr中的元素全部转为浮点数格式
arr3 = np.array(arr2,dtype = 'float')


# 生成0-10间隔为2的数组
arr4 = np.arange(0,11,2)
# 生成0-10，总共6个数的数组，间隔相等
arr5 = np.linspace(0,10,6)
# 生成6*6的0组成的数组
arr6 = np.zeros([6,6])
arr7 = np.array(arr6,dtype = int)

# 排序(默认为升序)
arr8 = np.sort(arr)
# 返回传入数据从小到大的索引
arr9 = np.argsort(arr8)
print(np.flip(arr8))

# arr8中的元素满足大于一的条件赋值为1，反之赋值为-1，存入新数组arr10中
arr10 = np.where(arr8>1,1,-1)
# 只输出满足条件的元素
arr10 = np.extract(arr8>1,arr8)
print(arr10)
