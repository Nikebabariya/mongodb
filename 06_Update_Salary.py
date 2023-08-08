from pymongo import MongoClient

client=MongoClient("mongodb+srv://nikebabariya:DiptiDB31@nikedb.ybbjxfd.mongodb.net/?retryWrites=true&w=majority")

db=client["Office"]
coll=db["workers"]
print('connected to MongoDB cloud successfully')

Eid=input('Enter workers ID : ')
qr={}
qr['_id']=Eid

for doc in coll.find(qr,{'_id': 0, 'name': 1,'salary': 1}):
    print(doc)

newsal=float(input('Enter new Salary : '))
ch={}
ch['salary']=newsal

upd={'$set':ch}

coll.update_one(qr,upd)
print('Worker salary updated...')
for doc in coll.find(qr,{'_id': 1, 'name': 1,
                 'post': 1, 'salary': 1}):
    print(doc)
