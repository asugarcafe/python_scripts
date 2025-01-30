# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:00:33 2025

@author: BeRoberts
"""

import pandas as pd

class pii_dataset():
    data_frame = None
    
    cols = ['Application',
            'Passes App Review', 
            'Passes Data Review', 
            'Passes Network Review']
    apps = ['Incidentz',
            'KACE - Ticketing',
            'TBS Magna POS',
            'TBS Magna Online Payments',
            'TBS ePrintIT',
            'TBS PaperCut',
            'TBS MyPC',
            'TBS Coin Towers (maybe has data stored)',
            'Ticketing Software (Ariane’s software)',
            'Tech Logic CircIT & Wand',
            'Tech Logic Sorter',
            'Polaris',
            'TraffSys']

    def __init__(self):
        self.set_dictionairies()
        self.get_dataframe()

    @staticmethod
    def dval(key, dictionary):
        return dictionary[key]
    
    def update_row(self, app, col_name, value):
        ind = self.data_frame.index[df['Application'] == row_app][0]
        self.data_frame.at[ind, col_name] = value
        return

    def set_dictionairies(self):
        self.type_classification = {'Public', 'Data that can be freely shared without restrictions.'
        'Internal', 'Data intended for use within the organization but not sensitive.'
        'Confidential', 'Data restricted to specific roles or departments due to business impact or sensitivity.'
        'Secret', 'Data that is highly sensitive and could cause significant harm if leaked.'}
        
        self.type_essentiality = {'Mission-Critical', 'Data that must be available for core operations to function.'
        'Important', 'Data that is essential for smooth operations but not immediately critical.'
        'Non-Critical', 'Data that is supplementary or used for occasional reference.'}
        
        self.type_integrity = {'High','Data that must always be accurate, complete, and reliable.'
        'Moderate','Data where occasional inaccuracies are tolerable but should be minimized.'
        'Low',' Data that can tolerate significant inaccuracies or inconsistencies.'}
        
        self.type_availability = {'Real-Time','Data that must be instantly available for decision-making or operations.'
        'Near-Time','Data that can be slightly delayed but must be accessible within minutes to hours.'
        'Archival','Data that is rarely accessed but stored for legal or historical purposes.'}
        
        self.type_regulation = {'Regulated','Data subject to specific laws or standards.'
        'Unregulated','Data not subject to external regulations.'}
        
        self.type_retention_priority = {'Short-Term','Data required for a brief period.'
        'Medium-Term','Data needed for operational or reporting purposes.'
        'Long-Term','Data with historical or legal value.'}
        
        self.type_deletion_schedule = {'Conditional Deletion','Deleted based on specific triggers, such as account closure or project completion.'
        'Scheduled Deletion',''}
        
        self.type_authentication = {'Password-Based','Standard username and password combination.'
        'Multi-Factor Authentication (MFA)','Combines something the user knows (password) with something they have (device) or something they are (biometric).'
        'Single Sign-On (SSO)','Users authenticate once to access multiple systems.'
        'Token-Based','Uses secure tokens for session-based access.'}
        
        self.type_storage_location = {'Cloud Storage','Data stored in cloud-based solutions.'
        'On-Premises Storage','Data stored in local servers or data centers.'
        'Hybrid Storage','A combination of cloud and on-premises storage.'}
        
        self.type_storage_format = {'File-Based','Specific file formats'
        'Database Storage','Structured storage in databases'}

    def get_dataframe(self):
        df = pd.DataFrame(columns=self.cols)
        for i in range(len(self.apps)):
            df.loc[-1] = [self.apps[i], None, None, None]
            df.index = df.index + 1
            df = df.sort_index()
        self.data_frame = df
        return self.data_frame

#df_todo = pd.DataFrame(columns=cols)



ds = pii_dataset()
df = ds.get_dataframe()

row_app = 'KACE - Ticketing'
# x = ds.apps.index(row_app)
# print(x)

ind = df.index[df['Application'] == row_app]
print(ind[0])
















