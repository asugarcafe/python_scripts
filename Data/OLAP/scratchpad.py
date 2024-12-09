# -*- coding: utf-8 -*-

from cubes import Workspace, Cell

# Create a workspace
workspace = Workspace()

# Define the data store (e.g., SQLite)
workspace.register_default_store("sql", url="sqlite:///data.sqlite")

# Load the data (assuming you have a CSV file)
from cubes.tutorial.sql import create_table_from_csv

create_table_from_csv(
    workspace.engine, 
    "sales_data.csv", 
    table_name="sales", 
    fields=[
        ("product", "string"), 
        ("region", "string"), 
        ("year", "integer"), 
        ("sales", "integer")
    ], 
    create_id=True
)

# Create a model for the cube
cube = workspace.create_cube("sales_cube", {
    "dimensions": [
        {"name": "product"}, 
        {"name": "region"}, 
        {"name": "year"}
    ],
    "measures": [
        {"name": "sales", "aggregator": "sum"}
    ]
})

# Create a browser to interact with the cube
browser = workspace.browser(cube)

# Perform aggregation
result = browser.aggregate()

# Access the summary data
print(result.summary["sales_sum"]) 

# Drill down by a dimension
result = browser.aggregate(drilldown=["region"])

# Print the results
for record in result:
    print(record)