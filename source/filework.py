import os
import string
import sys
import webbrowser
from pathlib import Path


def logFileW(str):
    print("filework.py: log: %s" %str)

class fileConfiguration(object):
    log_dir=''
    log_name=''
    log=None

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
                printErr("Unknown variable provided to 'configurate'",1)
            

    def getLogFileFullPath(self):
        if(self.log_dir == '' or self.log_name == ''):
            pass #TODO
        else:
            return (self.log_dir+"/"+self.log_name)
        

    def getLogDir(self):
        return self.log_dir

    def getLogName(self):
        return self.log_name

    def loadConfigFile(self,file):
        for line in file.readlines():
            if line.startswith("log_dir="): #log_dir
                self.log_dir = line.replace("log_dir=",'').replace("\n",'')
            elif line.startswith("log_name="):
                self.log_name = line.replace("log_name=",'').replace("\n",'')

fConf = fileConfiguration()

def printErr(str,errcode):
    print("filework.py: Error: %s" % str)
    # errcode = 2 --> ENOENT - no such file or directory
    exit(errcode)

def openActualLog():

    if sys.platform.startswith('linux'):
        try:
            #try to open the actual log file
            os.system('xdg-open %s'%fConf.getLogFileFullPath())
        except:
            printErr("Couldn't open log file, look in filework.py->openActualLog() for info")
        # webbrowser.open_new_tab(fConf.getLogFileFullPath())

def openLog():
    #log info is already updated locally
    if fConf.log_dir != '' and fConf.log_name != '':
        openActualLog()
        
    else:
        file,identif = getConfigFile()
        if file == None:
            exit(0)
        elif identif == 0:
            fConf.loadConfigFile(file)
        elif identif == 1:
            try:    
                logFileW("Trying to generate basic config file(writing in)...")
                log_dir="log_dir="+os.getcwd()+"\n"
                log_name="log_name=log.log\n"
                file.writelines([log_dir,log_name])

                #keep info in Class
                fConf.log_dir=os.getcwd()
                fConf.log_name='log.log'
            except:
                printErr("Trying to write into config file failed",1)
            logFileW("Success!")
        else:
            printErr("Unknown identif value, this message shouldn't be printed ever, basically",1)
        
        #open the file
        try:
            fConf.log = open(fConf.getLogFileFullPath(),"r+")
        except FileNotFoundError as e:
            print("Log File doesn't exist, wanna create it? [y][n]",end=' ')
            tmp = input()
            if tmp.lower() in ['yes','y','']:
                fConf.log = open(fConf.getLogFileFullPath(),'w')

            else:
                print("Create the log file first please... exiting")
                exit(0)

        openActualLog()

    pass

# returns None if program is to be exited, otherwise returns opened file for 'rw'
#identif == 0 if file exists and has been opened successfuly
#identif == 1 if file was asked to be generated automatically - fill with predetermined values -- opened successfully
def getConfigFile():
    toopen = Path(os.getcwd())
    fToOpen = os.path.join(toopen,"config.txt")
        #check if filework.py is a file in a current dir and check if config.py is a file in current dir
        #in order to establish if current dir is /source - aka - subdir in timeLogger dir
    if (os.path.isfile(Path(os.getcwd()+sys.argv[0]))): #im in ./source subdir
        logFileW("warning: If you get this message you might've run the program from subdir - use make commands in main dir")
        try:
            file = open(fToOpen, 'r+')
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
                    print("Please create config file manualy to continue, use '--help' for help...exiting")
                    return None,None
                else:
                    printErr("Unknown input given",1)
        except:
            printErr("Couldn't open/create a config file.",2)
    
    pass

def writeToConfig():
    pass

#only changes where to look for the config file, doesnt actually move the file itself
def changeLogDir(newdir):
    
    if os.path.isdir(newdir):
        fileConfiguration.log_dir=newdir
    else:
        printErr("Given path is not a valid directory: %s" % newdir,2)
    pass

if __name__ == '__main__':
    printErr("Can't run filework.py as main, sorry",1)
    
def writeToLog(activity,tBegin,tEnd,tDiff,tNow):

    # print("LOG: %s | %s | %s | from:%s | to:%s " %(str(tNow)[:-7],activity,str(tDiff)[:-7],str(tBegin)[:-7],str(tEnd)[:-7]))
    if fConf.log == None:
        ### to be merged ###
        configFile,_ = getConfigFile()
        if(configFile == None):
            exit(0)
        fConf.loadConfigFile(configFile)
        ### to be merged ###

    #open file
    try:
        logFile = open(fConf.getLogFileFullPath(),'a')
    except:
        printErr("Couldn't open log file",2)
        
    fConf.log = logFile

    if os.stat("%s"%fConf.getLogFileFullPath()).st_size == 0:
        fConf.log.write("TimeOfLog | Activity | TimeSpent | timeBegin | TimeEnd\n")

    # write into log
    fConf.log.write("%s | %s | %s | from:%s | to:%s\n" %(str(tNow)[:-7],activity,str(tDiff)[:-7],str(tBegin)[:-7],str(tEnd)[:-7]))

    #close the file
    fConf.log.close()
    pass