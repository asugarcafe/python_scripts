# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 09:40:36 2022

@author: sucre
"""
import requests
import json

api_key = "6mlrjOendGqpLK2b0vbqNy4IIIyEPggUbW7fcTp4A"

search_address = "https://api.si.edu/openaccess/api/v1.0/search?api_key=" + api_key
search_by_id_address = "https://api.si.edu/openaccess/api/v1.0/content/:id?api_key=" + api_key

def list_freetext_subcat(item_json, freetext_subcat, subcat_text):
    if item_json["response"]["content"]["freetext"]:
        if freetext_subcat in item_json["response"]["content"]["freetext"]:
            print(subcat_text + ": ")
            object_type = item_json["response"]["content"]["freetext"][freetext_subcat]
            for ot in object_type:
                print("\t{} : {}".format( ot["label"], ot["content"]))    

"""
https://americanhistory.si.edu/collections/search/object/nmah_516755
"""

search = "crime"

response = requests.get(search_address + "&q=" + search)
print(response.status_code)
if response.status_code == 200:
    response_text = json.loads(response.text)
    rows = response_text["response"]["rows"]
    for x in rows:
        print("Smithsonian ID: " + x["id"])
        print("Title: " + x["title"])
        print("URL: " + x["url"])
        d = requests.get(search_by_id_address.replace(":id", x["id"]))
        item_json = json.loads(d.text)
        if item_json["response"]["content"]["freetext"]:
            list_freetext_subcat(item_json, "objectType", "Object Types")
            list_freetext_subcat(item_json, "physicalDescription", "Physical Descriptions")
        print("")



