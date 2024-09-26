# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:29:37 2024

@author: BeRoberts
"""
import pandas as pd
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

dbs = ['ReportServer',
'ReportServerTempDB',
'LibraryProgramming',
'Web',
'CFForum2000',
'LIbraryProgram_test',
'SEExtranet2013',
'SEExtranet2015',
'incidentz',
'NopCommerceTest',
'NopCommerceLiveTest',
'incidentzTest',
'StaffPortalSample',
'OWLCamp2021_Test',
'OWLCamp2021Prod',
'ToshoConDB',
'ToshoConDB_UAT',
'SLCO_LIBRARY_WEB',
'WebEvent']

# connect to the master DB
# Database connection parameters
database_type = 'mssql+pyodbc' #'postgresql' # Change this to your database type
username = 'SLCLS\BenAdmin'
password = 'nah'
host = 'WEBSQL2014'
port = '1433'
database_name = 'master'

# pyodbc stuff for MS SQL Server Express
driver='{SQL Server}'
server=host
database=database_name
trusted_connection='yes'

# pyodbc connection string
connection_string = f'DRIVER={driver};SERVER={server};'
connection_string += f'DATABASE={database};'
connection_string += f'TRUSTED_CONNECTION={trusted_connection}'
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

# Create a connection string
connection_string = f'{database_type}://{host}:{port}/{database_name}?trusted_connection=yes'
connection_string = f'mssql+pyodbc://@{host}:{port}/{database_name}?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server'
connection_string = connection_url

# Create a database engine
engine = create_engine(connection_string)
#print(engine)

for db in dbs:

    # SQL query
    sql_query = f"SELECT deqs.last_execution_time AS [Time], dest.text AS [Query], dest.* FROM sys.dm_exec_query_stats AS deqs CROSS APPLY sys.dm_exec_sql_text(deqs.sql_handle) AS dest  WHERE dest.dbid = DB_ID('{db}')   ORDER BY deqs.last_execution_time DESC"

    # Execute the query and read the results into a DataFrame
    df = pd.read_sql(sql_query, engine)

    df.to_csv(f'{db}.csv', index=False) 

print('dun')