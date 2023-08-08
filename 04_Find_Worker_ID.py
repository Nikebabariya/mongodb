from pymongo import MongoClient

client=MongoClient("mongodb+srv://nikebabariya:DiptiDB31@nikedb.ybbjxfd.mongodb.net/?retryWrites=true&w=majority")

db=client["Office"]
coll=db["workers"]
print('connected to MongoDB cloud successfully')
input1=(input('Enter id: '))
ser={}
ser["_id"]=input1

X=coll.find_one(ser)
print(X)
