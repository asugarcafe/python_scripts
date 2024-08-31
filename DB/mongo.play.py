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

#document = {"coc_base_stats": {"STR": 50, "CON": 50, "SIZ": 50, "DEX": 50, "APP": 50, "INT": 50, "POW": 50, "EDU": 50,}}
document = {"coc_base_skills": {'Accounting' : 5,
        'Acting' : 5,
        'Animal Handling' : 5,
        'Anthropology' : 1,
        'Appraise' : 5,
        'Archaeology' : 1,
        'Art and Craft' : 5,
        'Artillery' : 1,
        'Astronomy' : 1,
        'Axe' : 15,
        'Biology' : 1,
        'Botany' : 1,
        'Bow' : 15,
        'Brawl' : 25,
        'Chainsaw' : 10,
        'Charm' : 15 ,
        'Chemistry' : 1,
        'Climb' : 20 ,
        'Computer Use' : 5,
        'Credit Rating' : 0,
        'Cryptography' : 1,
        'Cthulhu Mythos' : 0,
        'Demolitions' : 1,
        'Disguise' : 5,
        'Diving' : 1,
        'Dodge' : 25,
        'Drive Auto' : 20,
        'Electrical Repair' : 10,
        'Electronics' : 1,
        'Fast Talk' : 5,
        'Fine Art' : 5,
        'First Aid' : 30,
        'Flail' : 10,
        'Flamethrower' : 10,
        'Forensics' : 5,
        'Forgery' : 1,
        'Garrote' : 15,
        'Geology' : 1,
        'Handgun' : 20,
        'Heavy Weapons' : 10,
        'History' : 5,
        'Hypnosis' : 1,
        'Intimidate' : 15,
        'Jump' : 20,
        'Language Other' : 1,
        'Language Own' : 90,
        'Law' : 5,
        'Library Use' : 20,
        'Listen' : 20,
        'Locksmith' : 1,
        'Machine Gun' : 10,
        'Mathematics' : 1,
        'Mechanical Repair' : 10,
        'Medicine' : 1 ,
        'Meteorology' : 1,
        'Natural World' : 10,
        'Navigate' : 10,
        'Occult' : 5,
        'Operate Heavy Machinery' : 1,
        'Persuade' : 10,
        'Pharmacy' : 1,
        'Photography' : 5,
        'Physics' : 1,
        'Pilot' : 1,
        'Psychoanalysis' : 1,
        'Psychology' : 10,
        'Read Lips' : 1,
        'Ride' : 5,
        'Rifle' : 25,
        'Science' : 1,
        'Shotgun' : 25,
        'Sleight of Hand' : 10,
        'Spear' : 20,
        'Spot Hidden' : 25,
        'Stealth' : 20 ,
        'Submachine Gun' : 15,
        'Survival' : 10,
        'Sword' : 20,
        'Swim' : 20 ,
        'Throw' : 20,
        'Track' : 10,
        'Whip' : 5,
        'Zoology' : 1}}


#my_collection.insert_one(document)

# pballs = []
# all_numbers = []
# #filter_criteria = Where("data","dataset")
# # Find documents in the collection
# collection = my_collection.find({})
# for doc in collection[0].get("data"):
#     numbers = doc[9].split(" ")
#     pballs.append(int(numbers[5]))
#     for n in numbers:
#         all_numbers.append(int(n))

# counts = count_dictionary(all_numbers)
# pcounts = count_dictionary(pballs)
# # print(counts)
# sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
# sorted_pcounts = dict(sorted(pcounts.items(), key=lambda item: item[1], reverse=True))

# print(sorted_counts)
# print(sorted_pcounts)


# # Define the update operation
# update_operation = {"$set": {"age": 31, "city": "Updated City"}}

# # Update a single document
# my_collection.update_one(filter_criteria, update_operation)

# # Print the updated document
# updated_document = my_collection.find_one(filter_criteria)
# print(updated_document)


# my_collection.delete_one(result)
# my_collection.delete_many(filter_criteria)