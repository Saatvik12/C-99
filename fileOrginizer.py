import os
import shutil

path=input('name of directery to be sorted:  ')
fileList=os.listdir(path)
for file in fileList:
    name,ext=os.path.splitext(file)
    ext=ext[1:]
    if ext=='':
        countinue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file
