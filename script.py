from os import listdir
from os.path import isfile, join
import os
import shutil
import pathlib

def organize_files(mypath):
    
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    filetype_list=[]
    filetype_path={}
    
    # create list,dict for each filetype
    for file in files:
        # get file extension
        filetype=pathlib.Path(file).suffix 
        
        #filetype not in list
        if filetype not in filetype_list:
            filetype_list.append(filetype)
            new_folder_name=mypath+'/'+ filetype + '_folder'
            filetype_path[str(filetype)]=str(new_folder_name)
            
            #folder exists
            if os.path.isdir(new_folder_name)==True: 
                continue
            else:
                os.mkdir(new_folder_name)
                
    # move files to respective folders
    for file in files:
        src_path=mypath+'/'+file
        filetype=pathlib.Path(file).suffix
        
        #filetype in dict
        if filetype in filetype_path.keys():
            dest_path=filetype_path[str(filetype)]
            shutil.move(src_path,dest_path)
            print(src_path + '>>>' + dest_path)
if __name__=="__main__":
    mypath="D:/dummy_test"
    organize_files(mypath)