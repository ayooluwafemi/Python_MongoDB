# NoSQL database is MongoDB
# MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable

import mongodb

# Try installing pymongo[srv] and certifi
# pip3 install pymongo[srv]
# pip install certifi


myclient = mongodb.myclient
# CREATE DATABASE
# mydb = myclient['mydatabase']

# CREATING A COLLECTION
# mycol = mydb["customers"]
# INSERT INTO COLLECTION
""" mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict) """
# CONFIRM DATABASE
# print(myclient.list_database_names())

# CHECK IF DATABASE EXISTS
""" dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.") """
  
# print(mydb.list_collection_names())
  
# Return the _id Field
""" mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
print(x.inserted_id) """

# Insert Multiple Documents
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)
  
