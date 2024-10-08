import requests
from bs4 import BeautifulSoup
import openpyxl
import matplotlib.pyplot as plt
import uuid

baseUrl = 'https://www.bilibili.com/blackboard/activity-trending-topic.html'
response = requests.get(baseUrl)
html = response.content
soup = BeautifulSoup(html, 'html.parser')
hothit_list = []
soupContents = soup.find_all('div', class_='trending-title')
# trending_title_div = soup.find('div', {'class': 'trending-title'})
# title_text = trending_title_div.get_text()
if soupContents:
    for item in soupContents:
        hothit_list.append(item.text.strip())
    else:
        print('未找到包含热搜数据的元素')


workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = 'bilibili 热搜'
for i in range(len(hothit_list)):
    sheet.cell(row=i+2, column=1, value=hothit_list[i])

unique_id = uuid.uuid4()
filename = f'saveFiles\\bilibili热搜{unique_id}.xlsx'
workbook.save(filename)
print('热搜数据已保存')
# -*- coding:utf-8  -*-
# import re
# from bs4 import BeautifulSoup
# import urllib
# import pandas as pd

# class Spider():
# 	# '''
#     #     Description:
#     #         Spider program to crawl data from bilibili.com hot search rank list
#     #     Attributes:
#     #         None
#     # '''
#     def __init__(self):
#         self.url = 'https://www.bilibili.com/ranking?spm_id_from=333.851.b_7072696d61727950616765546162.3'
		
# 		# regular matching pattern
#         self.pattern = re.compile(r'<a class="title" href="(.*?)" target="_blank">(.*?)</a>')

#         self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
	
# 	# '''
#     #     Description:
#     #         crawl page from the given URL
#     #     Args:
#     #         url: the URL of page need to get
#     #     Returns:
#     #         page of the given URL
#     '''
#     def crawl(self):
#         self.request = urllib.request.Request(headers = self.headers, url = self.url)
#         self.response = urllib.request.urlopen(self.request)
#         page = self.response.read().decode('utf-8')

#         return page
	
# 	# '''
#     #     Description:
#     #         extract data from the given page by bs4 and re library, return the list of data
#     #     Args:
#     #         None
#     #     Returns:
#     #         list of data extract from given page
#     # '''
#     def extract(self):
#         page = self.crawl()
#         beautifulSoup = BeautifulSoup(page, 'html.parser')

#         results = []

#         for frame in beautifulSoup.find_all('div', class_ = 'content'):
#             frame = str(frame)
#             result = re.findall(self.pattern, frame)[0]
#             results.append(result)

#         return results

# if __name__ == "__main__":
#     spider = Spider()
#     results = spider.extract()
#     print(pd.DataFrame(results))
