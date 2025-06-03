# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:29:37 2024

@author: BeRoberts
"""
import pandas as pd
import pyodbc
import sys

runId = 10013 # 10062
output_file = 'C:/REPO/python_scripts_re/DB/ben.temp.xlsx'
arg_dict = {}
template = "I:/Rachel/REPORTS/Monthly Stats/2024/DoorCount/year_mo_DoorCount.template.xlsx"

# def build_output_file_name(args):
    
    
    

print(sys.argv)
for i in range(len(sys.argv)):
    if sys.argv[i].startswith('/') and ':' in sys.argv[i]:
        split = sys.argv[i].split(':', maxsplit=1)
        arg_dict[split[0][1:].lower()] = split[1]

if arg_dict['runid']:
    runId = int(arg_dict['runid'])

if arg_dict['output']:
    print(arg_dict['output'])
    output_file = arg_dict['output']

if True:
    excel = pd.read_excel(template,'year', header=None)
    excel.to_excel(output_file, index=False)

    # Database connection parameters
    username = "BenReports";
    password = "copianotit_R3p0R+$S|_C1$";
    host = 'DATALAKE'
    port = '1433'
    database_name = 'Stage'
    
    # pyodbc stuff for MS SQL Server Express
    driver='{SQL Server}'
    server=host
    database=database_name
    trusted_connection='no'
    
    conn = pyodbc.connect(f'Driver={driver};'
                            f'Server={server};'
                            f'Database={database};'
                            f'UID={username};'
                            f'PWD={password};'
                            f'Trusted_Connection={trusted_connection};')
    # cursor = conn.cursor()
    # # Do the insert
    # cursor.execute("insert into products(id, name) values ('pyodbc', 'awesome library')")
    # #commit the transaction
    # conn.commit()        
    #engine = create_engine(connection_string)
    # sql_query = f"EXEC [stat].[VisitorsWelcomed_Compile] @RunId = {runId}"
    
    # df = pd.read_sql(sql_query, conn)
    
    # df.at[df.index[-1], 'Date'] = ''
    
    # df.to_excel(output_file, index=False, startrow=3)
    
