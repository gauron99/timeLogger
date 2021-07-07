import os
from pathlib import Path
import string

class fileConfiguration:
    configFile = None

def logFileW(str):
    print("filework.py: log: %s" %str)

def printErr(str,errcode):
    print("filework.py: Error: %s" % str)
    exit(errcode) # ENOENT - no such file or directory

def openLog():
    # returns None if program is to be exited, otherwise returns opened file for 'rw'
    #identif == 0 if file exists and has been opened successfuly
    #identif == 1 if file was asked to be generated automatically - fill with predetermined values
    file,identif = readFromConfig()
    if file == None:
        exit(0)
    elif identif == 0:
        pass
    elif identif == 1:
        try:    
            logFileW("Trying to generate basic config file(writing in)...")
            log_dir="log_dir="+os.getcwd()
            log_name="log_name=log.log"
            file.writelines([log_dir+"\n",log_name+"\n"])
        except:
            printErr("Trying to write into config file failed",1)
        logFileW("Success!")

    pass

def readFromConfig():
    toopen = Path(os.getcwd())
    fToOpen = os.path.join(toopen,"config.txt")
        #check if filework.py is a file in a current dir and check if config.py is a file in current dir
        #in order to establish if current dir is /source - aka - subdir in timeLogger dir
    if (os.path.isfile(Path(os.getcwd()+"/filework.py")) and (os.path.isfile(Path(os.getcwd()+"/config.py")))): #im in ./source subdir

        try:
            file = open(fToOpen, 'rw')
            return file

        except:
            printErr("Config file 'config.txt' not found. Did you maybe try to run TL from /source subdir?",2)
    else:
        try:
            if os.path.isfile(fToOpen):
                return open(fToOpen,'r+'),0
            else:
                #config.txt is not an existing file, ask to create one
                print("config.txt does not exist on path: %s..." %fToOpen)
                print("Do you want to create one? [y][n]:",end='')
                answer = input()
                if(answer.lower() in ['y','yes','']):
                    logFileW("File doesn't exist... trying to create one")
                    return open(fToOpen,'a+'),1
                elif answer.lower() in ['n','no']:
                    print("Please create file manualy to continue,use '--help' for help...exiting")
                    return None,None
                else:
                    printErr("Unknown input given",1)
        except:
            printErr("Couldn't open/create a config file.",2)
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
    