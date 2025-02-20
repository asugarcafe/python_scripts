# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 11:28:06 2025

@author: BeRoberts
"""

import extract_msg
import re

folder = 'C:/Users/beroberts/Documents/SLCOLIB/Initiative/Statistics/2025-02/'
f = "Summary report for network 'WVA-AP' January 2025.msg"

reg1 = "Total Data Transferred (\\d+.\\d+) ([GT]B)"
reg2 = "Number of Clients Granted Access\\s+(\\d+)"

#f = r'MS_Outlook_file.msg'  # Replace with yours
msg = extract_msg.Message(folder + f)
msg_message = msg.body
msg.close()

msg_message = msg_message[msg_message.index("Total Data Transferred"):msg_message.index("Top applications by usage")]
msg_message = msg_message.replace('\r\n', ' ')
msg_message = msg_message.replace('\r', ' ')
msg_message = msg_message.replace('\n', ' ')
#print(msg_message)

a = re.search(reg1, msg_message)
b = re.search(reg2, msg_message)

#gather the Total Data Transferred
tdt = float(a.groups()[0])
tdt_unit = a.groups()[1]
if tdt_unit == 'TB':
    tdt = tdt * 1024

ncga = b.groups()[0]

print([tdt, tdt_unit, ncga])
