import pymysql 
from sqlalchemy import create_engine

import numpy as np

import pandas as pd

# 1.数据清洗一般先从重复值和缺失值开始处理
# 2.重复值一般采取删除法来处理
# 3.但有些重复值不能删除，例如订单明细数据或交易明细数据等

# 修改工作目录
import os 
os.chdir('C:\\Users\\sjkj\\Desktop\\代码和数据')
# 如果遇到单元格中的值为字符串"Na"，那么这个值将被解释为缺失值（NaN）
df = pd.read_csv('MotorcycleData.csv',encoding='gbk',na_values='Na')

def handle(x):
    if '$' in str(x):
        x = str(x).strip('$')
        x = str(x).replace(',','')
    else:
        x = str(x).replace(',','')
    return float(x)

df['Price'] = df['Price'].apply(handle)
df['Mileage'] = df['Mileage'].apply(handle)
# print(df[['Price','Mileage']].head(5))



#重复值处理:删除重复值
duplicatedValues = df.duplicated() # 查看重复值
# print(np.sum(duplicatedValues))#计算一个布尔型数组 duplicatedValues 中 True 值的总数
df.drop_duplicates(subset=['Condition','Price','Location','Condition_Desc'],inplace=True) # 删除重复值
# print(any(df.duplicated())) # 检查是否还有重复值
print(df['Mileage'])