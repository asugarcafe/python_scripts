# -*- coding: utf-8 -*-

import pandas as pd
df = pd.read_excel(open('C:/Users/beroberts/Documents/SLCOLIB/SQL/PolarisPro.ForeignKeys.xlsx','rb'))

#df.sort_values(['referenced_table', 'referenced_column'], ascending=[True, True])

keyed_tables = df['referenced_table'].value_counts()
keyed_columns = df['referenced_column'].value_counts()

df_biblio_r = df.loc[df['referenced_table'] == 'BibliographicRecords']
df_biblio = df.loc[df['table'] == 'BibliographicRecords']
df_orgs = df.loc[df['referenced_table'] == 'Organizations']

find = 'org'
df_curr_t = df.loc[df['table'].str.contains(find)]
df_curr_tref = df.loc[df['referenced_table'].str.contains(find)]
