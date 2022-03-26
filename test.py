import os 

path = 'data'
for file in os.scandir(path):
    if file.name.endswith(".xml"):
        os.unlink(file.path)