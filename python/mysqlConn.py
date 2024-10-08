import pymysql 
from sqlalchemy import create_engine

import numpy as np

import pandas as pd

# 创建数据库连接
conn = create_engine('mysql+pymysql://root:123456@localhost:3306/pythons')

import os 
os.chdir('C:\\Users\\sjkj\\Desktop\\代码和数据')

sql = "select * from student"

students = pd.read_sql(sql, conn)

df = pd.read_csv('baby_trade_history.csv')


# 将baby_trade_history.csv写入数据库中去
# try:
#     df.to_sql('testdf2', con = conn, if_exists='replace', index=False)
# except:
#     print('error')

# df.info()

# print(df.head(2))

# print(df[['user_id']])

# print(df[['user_id','day']][3:4])
df['购买量']=np.where(df['buy_mount'] > 3,'高','低')
print(df.head(2))