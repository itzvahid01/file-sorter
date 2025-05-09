import os
import logging as log
log.basicConfig(filename='reports.log',filemode='w',level=log.INFO)
log.critical('App Started')
BASE_DIR = os.getcwd()
things = os.walk(BASE_DIR)
file_egnores = ['j2.py','reports.log']
file_egnores = [os.path.join(BASE_DIR,i) for i in file_egnores]
for root,folders,files in things:
    for file in files:
        file_address = os.path.join(root,file)
        if file_address in file_egnores:
            continue
        elif not os.path.exists(file_address):
            continue
        file_addres_without_format , file_format = os.path.splitext(file_address)
        file_format = '.any' if file_format == '' else file_format
        new_folder = os.path.join(root,file_format)
        os.makedirs(new_folder,exist_ok=True)
        new_file = os.path.join(root,file_format,file)
        os.rename(file_address,new_file)
        log.info(f'File {file} Created At {new_file}')
    for folder in folders :
        if folder[0] == '.' or folder == "folders" or folder == '.env' :
            continue
        folders_place = os.path.join(root,'folders')
        os.makedirs(folders_place,exist_ok=True)                                                                                
        folder_place = os.path.join(root,folder)
        new_folder = os.path.join(folders_place,folder)
        os.rename(folder_place,new_folder)
    break
log.critical('App Closed')