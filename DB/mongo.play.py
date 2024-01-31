# -*- coding: utf-8 -*-

from pymongo import MongoClient
import json
from collections import Counter

def get_client(uri = "mongodb://localhost:27017/"):
    return MongoClient(uri)

def most_common_numbers(arr, k=12):
    # Use Counter to count occurrences of each number in the array
    counts = Counter(arr)
    # Use most_common() to get the top k most common elements and their counts
    most_common_elements = counts.most_common(k)
    # Extract the numbers from the result
    most_common_numbers = [element[0] for element in most_common_elements]
    return most_common_numbers

def count_dictionary(arr):
    # Use Counter to count occurrences of each number in the array
    counts = Counter(arr)
    # Convert Counter object to a dictionary
    counts_dict = dict(counts)

    return counts_dict
def Where(key, value):
    # Create a dictionary with Contact attributes
    return {
        key : value
    }

def And(expr):
    # Create a dictionary with Contact attributes
    return { "$and": [expr] }

# Connect to MongoDB
client = get_client()

# Create or access a database
my_database = client["portable_data"]

# Create or access a collection
my_collection = my_database["play"]

# Insert a document into the collection

# with open("C:/Repos/github_asugarcafe/python_scripts/General Scripts/resume.json", "r") as file:
#     json_data = json.load(file)
#     my_collection.insert_one(json_data)

# document = {"name": "John Doe", "age": 30, "city": "Example City"}
# my_collection.insert_one(document)
pballs = []
all_numbers = []
#filter_criteria = Where("data","dataset")
# Find documents in the collection
collection = my_collection.find({})
for doc in collection[0].get("data"):
    numbers = doc[9].split(" ")
    pballs.append(int(numbers[5]))
    for n in numbers:
        all_numbers.append(int(n))
 
counts = count_dictionary(all_numbers)
pcounts = count_dictionary(pballs)
# print(counts)
sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
sorted_pcounts = dict(sorted(pcounts.items(), key=lambda item: item[1], reverse=True))

print(sorted_counts)
print(sorted_pcounts)


# # Define the update operation
# update_operation = {"$set": {"age": 31, "city": "Updated City"}}

# # Update a single document
# my_collection.update_one(filter_criteria, update_operation)

# # Print the updated document
# updated_document = my_collection.find_one(filter_criteria)
# print(updated_document)


# my_collection.delete_one(result)
# my_collection.delete_many(filter_criteria)
