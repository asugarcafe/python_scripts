# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 15:50:06 2025

@author: sucre
"""

sixtynineboobsfourtwenty = "8C:6A:3B:87:A5:C8"

# simple inquiry example
import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

# for addr, name in nearby_devices:
#     print("  {} - {}".format(addr, name))

#bluetooth.pair(sixtynineboobsfourtwenty)