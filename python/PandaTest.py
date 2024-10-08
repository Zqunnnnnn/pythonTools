import pandas as pd
import numpy as np

Series1 = pd.Series([1, 99,23, 269, 31, 42, 5],['10', 919,3, 69, 1, 2, 50],name='这是一个测试的Series1')

# print(Series1.name)
# 构造数据框
list1 = [['jack',23,'男'], ['tom',25,'男'], ['lucy',22,'女']]
# 数据框其实就是一个二维表结构，是数据分析中，最常用的数据结构
dataframe1 = pd.DataFrame(list1,columns=['姓名','年龄','性别'],index=['第一行','第二行','第三行'])
dataframe2 = pd.DataFrame({'name':['jack','tom','lucy'],'age':[23,25,22],'sex':['男','男','女']})
#        姓名  年龄 性别
# 第一行  jack  23  男
# 第二行   tom  25  男
# 第三行  lucy  22  女\

print(dataframe1.size)