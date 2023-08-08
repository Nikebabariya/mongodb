from pymongo import MongoClient

client=MongoClient("mongodb+srv://nikebabariya:DiptiDB31@nikedb.ybbjxfd.mongodb.net/?retryWrites=true&w=majority")

db=client["Office"]
coll=db["workers"]
col=db["exworkers"]
print('connected to MongoDB cloud successfully')
print('*'*40)
print('This Programme is about to move single document from one collection to another')
print('*'*40)
input1=(input('Enter id: '))
ser={}
ser["_id"]=input1
print('*'*40)
try:
    X=coll.find_one_and_delete(ser)
    print(X)
    col.insert_one(X)
    print('*'*40)
    print('above shown document removed from worker collection and added to exworkers collection')
    print('*'*40)
except:
    print("document not found in database")


