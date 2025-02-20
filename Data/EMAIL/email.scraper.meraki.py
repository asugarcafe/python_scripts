# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:28:06 2025

@author: BeRoberts
"""

import extract_msg
import re
import os
import pandas as pd

folder = 'C:/Users/beroberts/Documents/SLCOLIB/Initiative/Statistics/2025-02/'
f = "Summary report for network 'WVA-AP' January 2025.msg"
fname_pattern = "Summary report for network '(\\w+)-AP'\\s+([\\w]+)\\s+([\\d]+).msg"

'''
TODO: read all files in a folder by a naming pattern, compile a datadet woth all the values
'''

reg1 = "Total Data Transferred (\\d+.\\d+) ([GT]B)"
reg2 = "Number of Clients Granted Access\\s+(\\d+)"

cols = ['Year', 'Month', 'Org', 'Usage GB', 'GB', 'Sessions With Accepted User Agreement']
#report = []
df_rpt = pd.DataFrame(columns=cols)

directory = os.fsencode(folder)
    
for file in os.listdir(directory):
    org = 'Nah'
    mo = "Octember"
    yr = "2025"
    tdt = float(0)
    tdt_unit = 'GB'
    ncga = int(0)

    filename = os.fsdecode(file)
    file_match = re.search(fname_pattern, filename)
    if file_match:
        #print(file_match.groups())
        org = file_match.groups()[0]
        mo = file_match.groups()[1]
        yr = file_match.groups()[2]
        
        msg = extract_msg.Message(folder + filename)
        msg_message = msg.body
        msg.close()

        msg_message = msg_message[msg_message.index("Total Data Transferred"):msg_message.index("Top applications by usage")]
        msg_message = msg_message.replace('\r\n', ' ')
        msg_message = msg_message.replace('\r', ' ')
        msg_message = msg_message.replace('\n', ' ')

        a = re.search(reg1, msg_message)
        b = re.search(reg2, msg_message)
        
        #gather the Total Data Transferred
        tdt = float(a.groups()[0])
        tdt_unit = a.groups()[1]
        if tdt_unit == 'TB':
            tdt = tdt * 1024
            tdt_unit = 'GB'
        
        ncga = b.groups()[0]
        
        df_rpt.loc[-1] = [yr, mo, org, tdt, tdt_unit, ncga]
        df_rpt.index = df_rpt.index + 1
        
#print(report)

