# -*- coding: utf-8 -*-

from pymongo import MongoClient


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create or access a database
my_database = client["portable_data"]

# Create or access a collection
my_collection = my_database["work"]

# Insert a document into the collection
document = {"name": "John Doe", "age": 30, "city": "Example City"}
my_collection.insert_one(document)

filter_criteria = {"name": "John Doe"}
# Find documents in the collection
result = my_collection.find_one(filter_criteria)
print(result)




# Define the update operation
update_operation = {"$set": {"age": 31, "city": "Updated City"}}

# Update a single document
my_collection.update_one(filter_criteria, update_operation)

# Print the updated document
updated_document = my_collection.find_one(filter_criteria)
print(updated_document)


# my_collection.delete_one(result)
my_collection.delete_many(filter_criteria)
