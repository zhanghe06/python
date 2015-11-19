# encoding: utf-8
__author__ = 'zhanghe'


from pymongo import MongoClient


client = MongoClient("localhost", 27017)

# 显示数据库名称列表
print client.database_names()

# 获取数据库对象
db = client.get_database('local')
# db = client.local
# db = client['local']
print db

# 显示local库下的所有文档集合（数据表）的名称列表
print db.collection_names()
print db.collection_names(include_system_collections=False)

# 获得文档集合的对象
collection = db.get_collection('startup_log')
# collection = db.startup_log
# collection = db['startup_log']
print collection

# 查询一条记录
print collection.find_one()

# 查询集合记录的总数
print collection.count()
