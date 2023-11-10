from os import listdir
from os.path import isfile, join
import os
import shutil
import pathlib

def organize_files(mypath):
    
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file_type_variation_list=[]
    filetype_folder_dict={}
    
    for file in files:
        filetype=pathlib.Path(file).suffix
        
        if filetype not in file_type_variation_list:
            file_type_variation_list.append(filetype)
            new_folder_name=mypath+'/'+ filetype + '_folder'
            filetype_folder_dict[str(filetype)]=str(new_folder_name)
            
            if os.path.isdir(new_folder_name)==True: #folder exists
                continue
            else:
                os.mkdir(new_folder_name)
    
        print(filetype_folder_dict)
    for file in files:
        src_path=mypath+'/'+file
        filetype=pathlib.Path(file).suffix
        if filetype in filetype_folder_dict.keys():
            dest_path=filetype_folder_dict[str(filetype)]
            shutil.move(src_path,dest_path)
            print(src_path + '>>>' + dest_path)
if __name__=="__main__":
    mypath="D:/dummy_test"
    organize_files(mypath)