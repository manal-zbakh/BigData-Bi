import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# le nom de bdd
db = client['Projet']

# le nom de collection
collection = db['data']
# collection = db['scopus']

# le chemin de data sous form json
with open('C:/Users/user/Documents/Scrapy_project/BI/projet/data.json') as file:
    # with open('C:/Users/user/Documents/Scrapy_project/BI/projet/Scopus.json') as file:
    file_data = json.load(file)

collection.insert_many(file_data)

client.close()
