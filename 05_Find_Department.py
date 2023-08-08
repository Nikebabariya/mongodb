from pymongo import MongoClient

client=MongoClient("mongodb+srv://nikebabariya:DiptiDB31@nikedb.ybbjxfd.mongodb.net/?retryWrites=true&w=majority")

db=client["Office"]
coll=db["workers"]
print('connected to MongoDB cloud successfully')


Dept=input('Enter workers Department : ')

qr={}
qr['dept']=Dept


x = coll.find(qr,{'_id': 0, 'name': 1,
                'post': 1, 'salary': 1})

for data in x:

        print(data)

