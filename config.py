import os,sys 

def logConfig(str):
    print("logConf> %s" % str)

def printErr(str):
    print("err: %s" % str)
    exit(1)

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

Run with '--help' or 'help' to show this message
    -- ./main.py -h
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    """)

    exit(0)
# if user uses fast config option
def configFastEdit():
    pass

def configDefault():
    pass

# initial func to handle Config - we get here by knowing there are some arguments
# on the command line to begin with (more than 1)
def handleConfig():
    "begin config stuff"

    logConfig("beginning configuring stuff, checking command line args...")

    if len(sys.argv) > 2:
        configFastEdit()
    else:
        firstArg = (sys.argv[1]).lower()
        if(firstArg == "config" or firstArg == "edit"):
            configDefault()
        elif(firstArg == "-h" or firstArg == "--help" or firstArg == "help"):
            printHelp()
        else:
            printErr("Argument not recognied, use '--help'. Arg given: '%s'" %sys.argv[1])
    pass


if __name__ == "__main__":
    "if this is run as main, it might actually do something :thinking:"
    print('might do something with this later, but nothing here yet')
    exit(0)
    
