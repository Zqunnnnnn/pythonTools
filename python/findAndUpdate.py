import pymysql 
from sqlalchemy import create_engine
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os 
os.chdir('C:\\Users\\sjkj\\Desktop\\代码和数据')
df = pd.read_csv('sam_tianchi_mum_baby.csv',encoding='gbk',dtype=str)
df.loc[df['gender']=='0','gender']='女'
df.loc[df['gender']=='1','gender']='男'
df.loc[df['gender']=='2','gender']='未知'
# print(df.head(5))
#修改列索引
df.rename(columns={'user_id':'用户Id','birthday':'生日','gender':'性别'},inplace=True)
#修改行索引
df.rename(index={'1':'one','10':'ten'},inplace=True)
# print(df[~(df['性别']=='男')&~(df['性别']=='女')])
