# insert data
def insertData( collection, data):
    print('running insert')
    return(collection.insert_one(data))

# insert many documents aka records
def insertMany(collection, dataList):
    print("inserting Many")
    return(collection.insert_many(dataList))

# update one record
def updateOne( collection, query, data):
    print('running update one')
    return(collection.update_one(query, data))

# query data
def queryVal(collection, query,fields = None):
    print('running query')
    return(collection.find(query,fields))
