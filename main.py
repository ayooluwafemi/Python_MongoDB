# NoSQL database is MongoDB
# MongoDB stores data in JSON-like documents, which makes the database very flexible and scalable

import mongodb

# Try installing pymongo[srv] and certifi
# pip3 install pymongo[srv]
# pip install certifi


myclient = mongodb.myclient
# CREATE DATABASE
mydb = myclient['mydatabase']

# CREATING A COLLECTION
mycol = mydb["customers"]
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
""" mylist = [
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
print(x.inserted_ids) """

# Insert Multiple Documents, with Specified IDs
""" mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids) """

# FIND
""" x = mycol.find_one()
print(x) """

# Return all documents in the "customers" collection, and print each document:
""" for x in mycol.find():
  print(x) """
  
# Return only the names and addresses, not the _ids:
""" for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x) """

# This example will exclude "address" from the result:
""" for x in mycol.find({},{ "address": 0 }):
  print(x) """

# QUERY
# Find document(s) with the address "Park Lane 38":
""" myquery = { "address": "Park Lane 38" }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x) """

# Find documents where the address starts with the letter "S" or higher:
""" myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x) """

# Find documents where the address starts with the letter "S":
""" myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
  print(x) """

# MONGODB SORT
# Sort the result alphabetically by name:
""" mydoc = mycol.find().sort("name")
for x in mydoc:
  print(x) """

# Sort the result reverse alphabetically by name:
""" mydoc = mycol.find().sort("name", -1)
for x in mydoc:
  print(x) """

# MONGODB DELETE DOCUMENT
# Delete the document with the address "Mountain 21":
""" myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery) """

# Delete all documents were the address starts with the letter S:
""" myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.") """

# Delete all documents in the "customers" collection:
""" x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.") """

# MONGODB DROP COLLECTION
""" mycol.drop() """








