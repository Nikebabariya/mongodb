from pymongo import MongoClient

client=MongoClient("mongodb+srv://nikebabariya:DiptiDB31@nikedb.ybbjxfd.mongodb.net/?retryWrites=true&w=majority")


'''db=client["Office"]
    coll=db["workers"]
itself create Office as a database and workers as a collection'''


db=client["Office"]
coll=db["workers"]
print('connected to MongoDB cloud successfully')