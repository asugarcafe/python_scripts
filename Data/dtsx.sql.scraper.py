# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:12:20 2024

@author: BeRoberts
"""
import os
import xml.etree.ElementTree as ET

sql_path = './Executable/Executables/Executable/ObjectData/SqlTaskData/@SqlStatementSource'
ns_sql_path = './DTS:Executable/DTS:Executables/DTS:Executable/DTS:ObjectData' #'/SQLTask:SqlTaskData'
sql_path_no_att = './Executable/Executables/Executable/ObjectData/SqlTaskData/'
dts_ext = '.dtsx'
namespaces = {'DTS': 'www.microsoft.com/SqlServer/Dts'}

dts_folder = 'C:/temp/dev/dev/MonthlyReports/MonthlyReports'
output_path = 'C:/temp/MonthlyReports/sql_dump/'

for file in os.listdir(dts_folder):
    print(file)
    if file.endswith(dts_ext) and not file.startswith('OBSOLETE'):
        file_sql_statements = []
        
        FULL_FILE_PATH = dts_folder + '/' + file
        #print(FULL_FILE_PATH)

        root = ET.parse(FULL_FILE_PATH)
        result = ''
        #break
        f = root.getroot().findall("{www.microsoft.com/SqlServer/Dts}ObjectData") # /@DTS:ObjectName
        attr_object_name = root._root.attrib['{www.microsoft.com/SqlServer/Dts}ObjectName']
        ser = '{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlStatementSource'
        for node in root.iter():
            for subnode in node.items():
                if subnode[0] == '{www.microsoft.com/sqlserver/dts/tasks/sqltask}SqlStatementSource':
                    print('Found::' + subnode[0])
                    print(subnode[1])
                    file_sql_statements.append(subnode[1])
                elif subnode[0] == 'name' and subnode[1] == 'SqlCommand':
                    print('Found::SqlCommand')
                    print(node.text)
                    file_sql_statements.append(node.text)
                # else:
                #     print(subnode)                    
                    
                    
                    
            #print(node.keys())
        print(len(file_sql_statements))
        if len(file_sql_statements) > 0:            
            output_file_name = output_path + file.replace(".dtsx", ".sqlx")
            with open(output_file_name, 'w', encoding='utf-8') as file:
                # Read the entire contents of the file into a string
                file.writelines(FULL_FILE_PATH + '\r\n\r\n')
                for sql in file_sql_statements:
                    file.writelines('--==============================================--\r\n')
                    file.writelines('\r\n')
                    file.writelines( str(sql) + '\r\n\r\n')
                    file.writelines('--==============================================--\r\n')
        
            
            print(FULL_FILE_PATH)
            print(output_file_name)
            #print(file_sql_statements)
        
        #break
        
