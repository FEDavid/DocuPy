import subprocess
import os
import shutil
import dominate
from dominate.tags import *

mainpath = os.getcwd()
destinationpath = 'documentation/'
count = 0
github_repo = "https://raw.githubusercontent.com/FEDavid/DocuPy/main/documentation/"
file_list = {}

def pydoc_output():
    global count
    try:
        os.chdir(destinationpath)
        for old_files in os.listdir("."):
            if old_files.endswith(".html"):
                os.remove(old_files)
    except:
        print("No documentation folder found, creating..")
        os.mkdir("documentation")
    paths = []
    os.chdir(mainpath)
    
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith('.py'):
                count+=1
                #print("File found:",file)
                paths.append(root)
    #print("\nIn directories;")
    paths = list(dict.fromkeys(paths))
    #print(paths)
    for directory in paths:
        os.chdir(mainpath)
        dirname = os.path.relpath(directory)
        os.chdir(dirname)
        #print("\nCWD: ",dirname,sep="")
        subprocess.run(["python3","-m","pydoc","-w",".\\"])

def pydoc_move():
      
    os.chdir(mainpath)
    for root, dirs, files in os.walk(".", topdown=False):
        for file in files:
            if file.endswith('.html'):
                try:
                    #print("File moved:",file)
                    shutil.move(os.path.join(root,file), os.path.join(destinationpath,file))
                except:
                    print("Something went wrong with the",file,"file.")
                    exit(-1)
    print("\nFiles documented - ",count,sep="")

def pydoc_HTML():
    os.chdir(destinationpath)
    for html_file in os.listdir("."):
        if html_file.endswith(".html"):
            html_file_new = github_repo+html_file
            print(html_file_new)
            file_list.update({html_file: html_file_new})

    html_code = dominate.document(title='DocuPy')  

    with html_code:
        with div(id='Title'):
            h1("DocuPy")

        with div(id='Documentation'):
            html_file_list = ul()
            for file_name, file_path in file_list.items():
                html_file_list+= li(a(file_name,href=file_path))

    try:
        index_file = open('index.html','w')
        index_file.write(str(html_code))
        index_file.close()
    except:
        print("Something went wrong with the index.html file.")

if __name__ == "__main__":
    pydoc_output()
    pydoc_move()
    pydoc_HTML()
    # Debugging
    # os.chdir(mainpath)
    # shutil.rmtree(destinationpath)