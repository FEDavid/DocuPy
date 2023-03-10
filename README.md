# DocuPy

- Link to repository -  [https://github.com/FEDavid/DocuPy](https://github.com/FEDavid/DocuPy)
- Link to page - [https://fedavid.github.io/DocuPy/](https://fedavid.github.io/DocuPy/)

A script that uses pydoc and path modules to loop through any subdirectories within the root and output the documentation for those .py files.

## What does it look like
* Eventually, you will end up with a series of files in a documentation folder like this, which when combined with a link to your index.html file - [LINK](https://htmlpreview.github.io/?https://raw.githubusercontent.com/FEDavid/DocuPy/main/documentation/index.html) - will give you a shareable and simple copy of all your documentation.

```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        27/02/2023     20:00                documentation
d-----        27/02/2023     20:23                project_docs
d-----        27/02/2023     20:00                __pycache__
-a----        27/02/2023     19:34           1928 .gitignore
-a----        27/02/2023     19:34           1083 LICENSE
-a----        27/02/2023     20:08           2657 main.py
-a----        27/02/2023     19:34            153 README.md
```

## How does it work
* Through a usage of several modules (subprocess, os, shutil, and dominate) this script will loop through all subdirectories linked to the root folder (including itself) and will locate any python files. 

* After it has done this the script will take note of any directories found and will then loop through them individually and run the subprocess module, which allows the script to run python terminal commands.

* Once all the files have been output, due to the way pydoc works, all the documentated files will be within their respective directories which is not very organised. As such, the script then does a similar loop through all the directories, instead looking for .html files, and then moves all of these to the documentation folder (Which if doesn't exist when the script is launched, is created)

* Finally, the script will generate some very basic .html into an index file which will link relative to all other documentated html files. Using this in combination with https://htmlpreview.github.io/ - You can create a link in your README to the RAW link of your index file while including the htmlpreview site beforehand to render the index file and all other documents!

## Setup

1. Download the source file and place it in your root folder, assuring all files requiring documentation are either in the root file with it or in a subdirectory.

2. Insert some documentation into your code (I used [pydoc](https://docs.python.org/3/library/pydoc.html)).

3. {Only if you're using the documentation for GitHub, otherwise you can remove the `pydoc_HTML()` function} 
Edit the `github_repo` variable within the source file to match your username and repo name.

4. {Only if you're using the documentation for GitHub} 
Once the files are outputted, commit them to your repo and take the url for your raw index and slot it into your README markdown while adding the htmlpreview prefix.

* If you are not intending on using this for Github, as stated above, simply remove the `pydoc_HTML()' function and the files will simply all be output to your documentation folder locally.
