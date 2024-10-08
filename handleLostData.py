import pymysql 
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import os 
os.chdir('C:\\Users\\sjkj\\Desktop\\代码和数据')
# 如果遇到单元格中的值为字符串"Na"，那么这个值将被解释为缺失值（NaN）
df = pd.read_csv('MotorcycleData.csv',encoding='gbk',na_values='Na')
# 修改工作目录

x = df.apply(lambda x: sum(x.isnull())/len(x),axis=0)#每一列的重复比例（所有重复值的数量/所有数据的长度）
# 删除法
anyDelete1=df.dropna(how='any',axis=1)#只要有重复就删除.删除了包含至少一个缺失值的列，所以最后输出的DataFramedf只剩下了两列
anyDelete2=df.dropna(how='any',axis=0)#只要有重复就删除.删除了包含至少一个缺失值的行，所以最后输出的DataFramedf只剩下了两行
partDelete=df.dropna(how='any',axis=0,subset=['Condition','Price','Mileage'])#只有全部重复才删除.删除了所有值都为缺失值的列，所以最后输出的DataFramedf只剩下了两列
partDelete2=df.dropna(how='any',axis=0,subset=['Condition_Desc'])#只有全部重复才删除.删除了所有值都为缺失值的行，所以最后输出的DataFramedf只剩下了两行
# print(partDelete2)


# 替换法
def handle(x):
    if '$' in str(x):
        x = str(x).strip('$')
        x = str(x).replace(',','')
    else:
        x = str(x).replace(',','')
    return float(x)
df['Mileage'] = df['Mileage'].apply(handle)

# 检查Mileage列中的每个值是否为数字
# df['Mileage'] = pd.to_numeric(df['Mileage'], errors='coerce')
# 将非数字值替换为None
# df['Mileage'] = df['Mileage'].where(pd.notnull(df['Mileage']), None)
# mask = df['Mileage'].notna()&(df['Mileage']!=1)&(df['Mileage']!=0)#当Mileage列不为空且Mileage列不为1时，返回True，否则返回False
# average_mileage = df.loc[mask, 'Mileage'].mean()#计算Mileage列的平均值
# print("原始平均里程数:", df['Mileage'].mean())
# userAverageFillMileage = df.Mileage.fillna(average_mileage)
# print(userAverageFillMileage.head(10))
mean = df.Mileage = df.Mileage.fillna(df.Mileage.mean())
print(mean.iloc[[1693,1604]])
