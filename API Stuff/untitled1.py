# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:32:35 2024

@author: BeRoberts
"""

# https://github.com/hbldh/bleak
# https://github.com/kevincar/bless

import asyncio
from bleak import BleakScanner

async def main():
    devices = await BleakScanner.discover()
    for d in devices:
        print(d)

asyncio.run(main())

'''
import asyncio
from bleak import BleakClient

address = "24:71:89:cc:09:05"
MODEL_NBR_UUID = "2A24"

async def main(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

asyncio.run(main(address))
'''
