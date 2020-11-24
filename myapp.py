
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
dataReady = { "Experiment": "12345", "Createdt" : datetime.now() }
x = insertData( mycol, dataReady)
print(x)

# testing inserting multiple documents into collection
dataReadyMany =[
{'Experiment': '1A', "Createdt": datetime.now()},
{'Experiment': '1B', "Createdt": datetime.now()}
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
q = queryVal(mycol, query)
for i in q:
    print(i)

#Return Only Some Fields
