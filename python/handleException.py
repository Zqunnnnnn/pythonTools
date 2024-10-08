import pymysql 
from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os 
os.chdir('C:\\Users\\sjkj\\Desktop\\代码和数据')
df = pd.read_csv('MotorcycleData.csv',encoding='gbk',na_values='Na')

def handle(x):
    if isinstance(x, str):
        if '$' in str(x):
            x = str(x).strip('$')
            x = str(x).replace(',', '')
        else:
            x = str(x).replace(',', '')
        return float(x)
    return x
df['Price'] = df['Price'].apply(handle)

# 异常值检测之标准差法
xbar = df.Price.mean()  # 计算均值
xstd = df.Price.std()   # 计算标准差

# 对价格进行描述性统计
general = df.Price.describe()
#设置绘图风格
# plt.style.use('seaborn')
#绘制直方图
# df.Price.plot(kind='hist',bins=20)
#绘制核密度图
# df.Price.plot(kind='kde')
# plt.show()

