from os import listdir
from os.path import isfile, join
import os
import shutil
import pathlib
def sort_files_in_a_folder(mypath):
    '''
    A function to sort the files in a download folder
    into their respective categories
    '''
    print("stated")
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    file_type_variation_list=[]
    filetype_folder_dict={}
    print("Before")
    for file in files:
        filetype=pathlib.Path(file).suffix
        print(filetype)
        if filetype not in file_type_variation_list:
            print("if")
            file_type_variation_list.append(filetype)
            new_folder_name=mypath+'/'+ filetype + '_folder'
            filetype_folder_dict[str(filetype)]=str(new_folder_name)
            if os.path.isdir(new_folder_name)==True: 
                print("Exist")#folder exists
                continue
            else:
                os.mkdir(new_folder_name)
    print("After")
    for file in files:
        src_path=mypath+'/'+file
        filetype=file.split('.')[1]
        if filetype in filetype_folder_dict.keys():
            print("ifs")
            dest_path=filetype_folder_dict[str(filetype)]
            shutil.move(src_path,dest_path)
        print(src_path + '>>>' + dest_path)
if __name__=="__main__":
    mypath="D:/dummy_test"
    sort_files_in_a_folder(mypath)