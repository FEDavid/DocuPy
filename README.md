# DocuPy
A script that uses pydoc and path modules to loop through any subdirectories within the root and output the documentation for those .py files.

## What does it look like
* Eventually, you will end up with a series of files in a documentation folder like this, which when combined with a link to your index.html file - [LINK](https://htmlpreview.github.io/) - will give you a shareable and simple copy of all your documentation.

IMAGE

## How does it work
* Through a usage of several modules (subprocess, os, shutil, and dominate) this script will loop through all subdirectories linked to the root folder (including itself) and will locate any python files. 

* After it has done this the script will take note of any directories found and will then loop through them individually and run the subprocess module, which allows the script to run python terminal commands.

* Once all the files have been output, due to the way pydoc works, all the documentated files will be within their respective directories which is not very organised. As such, the script then does a similar loop through all the directories, instead looking for .html files, and then moves all of these to the documentation folder (Which if doesn't exist when the script is launched, is created)

* Finally, the script will generate some very basic .html into an index file which will link relative to all other documentated html files. Using this in combination with https://htmlpreview.github.io/ - You can create a link in your README to the RAW link of your index file while including the htmlpreview site beforehand to render the index file and all other documents!
