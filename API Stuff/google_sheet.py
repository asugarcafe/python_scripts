# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 16:24:46 2023

@author: sucre
"""
from oauth2client.service_account import ServiceAccountCredentials
import gspread, gsheets
import pandas as pd

# Replace these strings with your actual credentials
api_key_dict = {
    "type": "service_account",
    "project_id": "your-project-id",
    "private_key_id": "your-private-key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\nYour_Private_Key_Here\n-----END PRIVATE KEY-----",
    "client_email": "your-client-email@your-project-id.iam.gserviceaccount.com",
    "client_id": "your-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-client-email%40your-project-id.iam.gserviceaccount.com"
}

# Set up credentials
credentials = ServiceAccountCredentials.from_json_keyfile_dict(api_key_dict, scope=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])

# Authorize using the credentials
gc = gspread.authorize(credentials)

# Open the Google Spreadsheet using its title
spreadsheet_title = 'Your Google Spreadsheet Title'
worksheet = gc.open(spreadsheet_title).sheet1  # You can specify the sheet by name or index

# Get all values from the worksheet
data = worksheet.get_all_values()

# Create a Pandas DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Display the DataFrame
print(df)
