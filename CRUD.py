# insert data
import sys


def insertData( collection, data):
    print('running insert')

    try:
        message = collection.insert_one(data)
        return(message)
    except :
        e = sys.exc_info()
        print('Error - ' + str(e))

# insert many documents aka records
def insertMany(collection, dataList):
    print("inserting Many")
    try:
        message =  collection.insert_many(dataList)
        return(message)
    except :
         e = sys.exc_info()
         print('Error - ' + str(e) )


# update one record
def updateOne( collection, query, data):
    print('running update one')
    return(collection.update_one(query, data))

# update many records
def updateMany( collection, query, data):
    print('running update many')
    return(collection.update_many(query, data))

# query data
def queryVal(collection, query,fields = None, sort = False, sortField = None):
    print('running query')
    if sort and sortField is not None:
        return(collection.find(query,fields).sort(sortField, 1))
    else:
        return(collection.find(query,fields))
