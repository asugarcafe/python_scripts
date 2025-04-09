# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:13:06 2023

@author: sucre
"""
import pandas as pd

ledger = 'C:/temp/bk_download.csv'

df = pd.read_csv(ledger)

df_deposits = df[df.Amount > 1.0]
df_deposits = df_deposits[df.Description != 'ATM Fee Rebate']
df_deposits = df_deposits[df.Description != 'USAA Transfer']
df_deposits = df_deposits[df.Description != 'Mobile Deposit']
df_deposits = df_deposits[df.Description != 'Utah State Tax Refund']
df_deposits = df_deposits[df.Description != 'Federal Tax Refund']
df_deposits = df_deposits[df.Description != 'Amazon Prime Membership']
df_deposits = df_deposits[df.Description != 'Debit Card Refund']

df_ira = df_deposits[df.Description == 'Schwab Brokerage']
df_deposits = df_deposits[df.Description != 'Schwab Brokerage']
df_deposits = df_deposits[df.Description != 'Usaa Close']

non_taxed = df_deposits['Amount'].sum()
print(non_taxed)

taxed = df_ira['Amount'].sum()
print(taxed)




