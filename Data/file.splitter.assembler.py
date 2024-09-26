# -*- coding: utf-8 -*-

#'''
# File to open and break apart
path = '//polarispro/DatabaseBackups/'
bin_path = '//polarispro/DatabaseBackups/bin/'
db_file = 'PolarisTransactions.bak'
read_size = 1024 * 1_000_000
with open(path + db_file, "rb") as fileR:
 
    chunk = 0
     
    byte = fileR.read(read_size)
    while byte:
     
        # Open a temporary file and write a chunk of bytes
        fileN = "chunk" + str(chunk) + ".bin"
        fileT = open(bin_path + fileN, "wb")
        fileT.write(byte)
        fileT.close()
        print("file written: " + fileR)
        # Read next 1024 bytes
        byte = fileR.read(read_size)
     
        chunk += 1
#'''    

'''
import os

output_file = "C:/Temp/Data/Polaris.bak"
chunk_path = "C:/temp/data/bin_assemble/"
chunk = 0
read_size = 1024 * 100_000

    

# Open original file for reconstruction
fileM = open(output_file, "wb")
 
# Manually enter total amount of "chunks"
chunk = 0
chunks = 991
 
# Piece the file together using all chunks
while chunk <= chunks:
    #print(" - Chunk #" + str(chunk) + " done.")
    fileName = "db.chunk" + str(chunk) + ".bin"
    if os.path.isfile(chunk_path + fileName):
        #continue
        fileTemp = open(chunk_path + fileName, "rb")
     
        #byte = fileTemp.read(read_size)
        byte = fileTemp.read()
        fileM.write(byte)
        print(" - Chunk #" + str(chunk) + " done.")
    else:
        print('missing file:' + chunk_path + fileName)
        break
    chunk += 1
 
fileM.close()

'''