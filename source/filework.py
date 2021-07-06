import os
from pathlib import Path
import string

class fileConfiguration:
    configFile = None

def logFileW(str):
    print("filework.py: log> %s" %str)

def printErr(str,errcode):
    print("filework.py: Error: %s" % str)
    exit(errcode) # ENOENT - no such file or directory

def openLog():
    readFromConfig()
    pass

def readFromConfig():
        #check if filework.py is a file in a current dir and check if config.py is a file in current dir
        #in order to establish if current dir is /source - aka - subdir in timeLogger dir
    if (os.path.isfile(Path(os.getcwd()+"/filework.py")) and (os.path.isfile(Path(os.getcwd()+"/config.py")))): #im in ./source subdir
        
        try:
            toopen = Path(os.getcwd()).parent
            fToOpen = os.path.join(toopen,"config.txt")
            file = open(fToOpen, 'rw')
            return file

        except:
            printErr("Config file 'config.txt' not found in %s" %toopen,2)

    # if curr dir is already a main dir, check for a config.txt file only in cwd
    else:
        try:
            file = open("config.txt", 'rw')
            return file
        except:
            printErr("Config file 'config.txt' not found in %s" %os.getcwd(),2)
    pass

def writeToConfig():
    pass

def changeLogDir(newdir):
    
    if os.path.isdir(newdir):
        log_dir=newdir
    else:
        printErr("Given path is not a valid directory: %s" % newdir,2)
pass

if __name__ == '__main__':
    printErr("Can't run filework.py as main, sorry",1)
    