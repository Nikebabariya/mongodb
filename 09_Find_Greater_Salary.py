from pymongo import MongoClient
client=MongoClient("mongodb+srv://nikebabariya:DiptiDB31@nikedb.ybbjxfd.mongodb.net/?retryWrites=true&w=majority")

db=client["Office"]
coll=db["workers"]
print('connected to MongoDB cloud successfully')
print('*'*40)
Salary=int(input('Enter workers Salary : '))
fnd={'$gt': Salary}

print('*'*40)
print('Below Worker have salary more than %d'%Salary)
x = coll.find({ "salary" : fnd},{'_id': 0, 'name': 1,'post': 1, 'salary': 1})

for data in x:

        print(data)