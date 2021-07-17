import os
import sys

import filework as fw


def logConfig(str):
    print("logConf> %s" % str)

def printErr(str,errC):
    print("config.py: Error: %s" % str)
    exit(errC)

def printHelp():
    print("""
This is timeLogger help message!
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
timeLogger is a program to help manage time and activities during it.

Run without any arguments to ... well, run it! (ex: ./main.py or 'make run')
 - In TimeLogger window:
    -- write your activity at the top of the window
    -- press Start button to start the activity
        -- press Stop whenever you are finished with that activity
        
        (NOT IMPLEMENTED)
        -- press Pause to pause the activity (NOT IMPLEMENTED)

            -- press Resume to continue(NOT IMPLEMENTED)

    -- Log button opens the log file(if has permission)
    -- Shows info in the middle of the window about last activity

Run with 'config' or 'edit' to open "config mode"
    -- default or "lazy" config mode when you are not sure what to do
    -- "fast edit" - give arguments after 'config' of changes to be made
    
    examples:
    -- default "lazy" config: ./main.py config (or 'make config')

    (NOT IMPLEMENTED)
    -- fast config: ./main.py config log_dir=/home/timeLogger/ ###change dir
                    ./main.py config log_name=log.log ### rename/create

Create config.txt manually:
    -- should be in main folder
    -- should contain values: 
        - log_dir (path to directory where log file is located)
        - log_name (name of log file)
        such as:
        
           ┌⎯  config.txt
           ├⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
           | log_dir=/home/path/to/dir
           | log_name=log.log
           ╰⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ 

            [ ^ this can be your whole config.txt]

Run with '--help' or 'help' to show this message
    -- ./main.py -h
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    """)
    exit(0)

def updateConfig(file,fConf):
    """param1: give opened config file handler
       param2: class of fileConfiguration()"""

    #TODO
    # fw.writeToConfig()
    pass

# if user uses fast config option
def configFastEdit():
    "parse command line arguments to quickly edit something + give suggestions if not correct"
    pass

def configDefaultPrint(file,fileVar):

    print("~~ TimeLogger Config! ~~")
    print()
    print("[1] Directory of log file: log_dir=%s" % fileVar.log_dir)
    print("[2] Name of log file: log_name=%s" % fileVar.log_name)
    print("[quit] Exit from config")
    print()
    print("Write an [identifier] of what you want to change:",end=' ')
        
    pass

def configDefault(file,fileVar):
    print("~~ Welcome to TimeLogger Config! ~~\n")
    # "while True to create 'config space'. Type number of what you want to change -> press Enter / type quit to hop out" 
    ## TODO ##
    while(True):
        configDefaultPrint(file,fileVar)
        readStr = input()
        
        #switch
        if readStr == "1":
            fileVar.log_dir = input("New log file directory> log_dir=")
            updateConfig(file)
        elif readStr == '2':
            fileVar.log_name = input("New log file name> log_name=")
            updateConfig(file)
        elif readStr == 'quit':
            exit(0)

    pass

# initial func to handle Config - we get here by knowing there are some arguments
# on the command line to begin with (more than 1)
def handleConfig():
    "begin config stuff"

    #init class variable #DEBUG
    fileVar = fw.fileConfiguration()

    try:
        #get opened config file
        configFile = fw.getConfigFile()
    except:
        printErr("Config file not properly opened",2)

    #load into Class
    fileVar.loadConfigFile(configFile)#now fileVar should have log dir and name (AKA its path)

    if len(sys.argv) > 2:
        configFastEdit(configFile,fileVar)
    elif len(sys.argv) == 2:
        firstArg = (sys.argv[1]).lower()
        if(firstArg == "config" or firstArg == "edit"):
            configDefault(configFile,fileVar)
        elif(firstArg == "-h" or firstArg == "--help" or firstArg == "help"):
            printHelp()
        else:
            printErr("Argument not recognied, use '--help'. Arg given: '%s'" %sys.argv[1],1)
    else:
        printErr("Unknown number of arguments :-(",1)


if __name__ == "__main__":
    "if this is run as main, it might actually do something :thinking:"
    print('might do something with this later, but nothing here yet')
    exit(0)
    
