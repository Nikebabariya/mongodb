from pymongo import MongoClient

client=MongoClient("mongodb+srv://nikebabariya:DiptiDB31@nikedb.ybbjxfd.mongodb.net/?retryWrites=true&w=majority")

db=client["Office"]
coll=db["workers"]
print('connected to MongoDB cloud successfully')

wid=input('Enter worker id : ')
nm=input('Enter name : ')
dp=input('Enter department : ')
po=input('Enter post : ')
city=input('Enter location : ')
sal=float(input('Enter salary : '))
mb=int(input('Enter Mobile Name : '))
email=input('Enter email address : ')

dic={}
dic['_id']=wid
dic['name']=nm
dic['dept']=dp
dic['post']=po
dic['location']=city
dic['salary']=sal
dic['Mobile_no']=mb
dic['Email_id']=email

coll.insert_one(dic)
print('document added to workers collection')