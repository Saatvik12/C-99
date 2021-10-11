import os
import shutil

source = input('enter source folder name:  ')
destination = input('enter destination folder name:  ')

source= source + '/'
destination = destination + '/'

fileList=os.listdir(source)
for file in fileList:
    shuttle.move((source+file),destination)
    
    
