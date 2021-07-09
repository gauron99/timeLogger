import os,sys
from pathlib import Path
import string

def logFileW(str):
    print("filework.py: log: %s" %str)

class fileConfiguration:
    def __init__(self):
        self.log_dir=''
        self.log_name=''

    def configurate(self,**kwargs):
        """ 
        pass arguments below as: new_dir="your value" \n
        new_dir = path to new dir where log can be found \n
        new_name = new name of log"""
        for key,value in kwargs.items():
            if(key == "new_dir"):    
                if( (self.log_dir == '' and value != '') or self.log_dir != value):
                    logFileW("Rewriting log_dir data...")
                    self.log_dir=value
            elif(key == 'new_name'):
                if( (self.log_name == '' and value != '') or self.log_name != value):
                    logFileW("Rewriting log_name data...")
                    self.log_name=value
            else:
                printErr("Unkown variable provided to 'configurate()'",1)

    def getLogDir(self):
        return self.log_dir

    def getLogName(self):
        return self.log_name


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

            #keep info in Class
            fileConfiguration.log_dir=os.getcwd()
            fileConfiguration.log_name='log.log'
        except:
            printErr("Trying to write into config file failed",1)
        logFileW("Success!")
    else:
        printErr("Unknown identif value, this message shouldn't be printed ever, basically",1)
    pass

def readFromConfig():
    toopen = Path(os.getcwd())
    fToOpen = os.path.join(toopen,"config.txt")
        #check if filework.py is a file in a current dir and check if config.py is a file in current dir
        #in order to establish if current dir is /source - aka - subdir in timeLogger dir
    if (os.path.isfile(Path(os.getcwd()+sys.argv[0]))): #im in ./source subdir
        logFileW("warning: If you get this message you might've run the program from subdir - use make commands in main dir")
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
    