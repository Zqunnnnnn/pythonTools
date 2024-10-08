import pandas as pd
import numpy as np

# 读取excle文件
def readExcel(path, excel_file,sheet_name):
    return pd.read_excel(path + excel_file,sheet_name)

if __name__ == '__main__':
    #修改为自己的文件路径'
    file_path = 'C:\\Users\\sjkj\\Desktop\\' 
    # 文件名
    file_name = 'zhejiang.xlsx'
    sheet_name = '业务部'
    sheetInfo = readExcel(file_path, file_name, sheet_name)
    # sheet.to_csv(file_path + 'zhejiang2.csv')
    # print(sheet)
    # print(sheet.shape)
    print(sheetInfo.loc[:3,['销售大区']])


