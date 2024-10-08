from pymongo import MongoClient
import uuid

# 连接到MongoDB数据库
client = MongoClient('121.41.65.206', 27017, username='admin', password='12345@abcd')
db = client.bn2024  # 替换为你自己的数据库名称
collection = db.departmentlocations  # 替换为你想要操作的集合名称

# 获取集合中的所有文档
documents = collection.find()

# 遍历文档并为每个文档添加UUID
for document in documents:
    document['id'] = str(uuid.uuid4())  # 将生成的UUID存储为字符串格式
    
    # 更新文档
    collection.update_one({'_id': document['_id']}, {'$set': document})

print("UUIDs have been added to each document.")
