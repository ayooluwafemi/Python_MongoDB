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

  
