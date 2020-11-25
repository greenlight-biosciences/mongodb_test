
import settings
import os
import pymongo
from datetime import *
from CRUD import *

connectionStr = os.getenv("CONN")

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient = pymongo.MongoClient(connectionStr)

mydb = myclient["experiments"] # gets database
mycol = mydb["experiment"] # gets collection or table

#Testing insert of single document into collection
dataReady = { "Experiment": "12345", "Createdt" : "test" }
x = insertData( mycol, dataReady)
print(x)

# testing inserting multiple documents into collection
dataReadyMany =[
{'Experiment': '1A', "Createdt": datetime.now()},
{'Experiment': 'Z1B', "Createdt": datetime.now()},
{'Experiment': 'W1A', "Createdt": datetime.now()},
{'Experiment': 'L1B', "Createdt": datetime.now()}
]
m = insertMany(mycol,dataReadyMany)
print(m)

# testing query
query = {'Experiment': '1A'}
fields = { "Experiment": 1 }
q = queryVal(mycol, query, fields)
for i in q:
    print(i)

# testing regex query
query  = { "Experiment": { "$regex": "^1" } }
q = queryVal(mycol, query, fields = fields, sort =True, sortField = 'Createdt')
for i in q:
    print(i)

#Return Only Some Fields

# Updating one document
query  = { "Experiment": "1A" }
data  = { "$set": { "Project": "Flowers" } }
updateOne( mycol, query, data)

# Updating many document
data  = { "$set": { "Project": "Flowers2" } }

# where exp starts with 1 and project not equeal to Flowers
query  = { "Experiment": { "$regex": "^1" } , "Project" :{"$ne" : 'Flowers'}}
updateMany( mycol, query, data)
