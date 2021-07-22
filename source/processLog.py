#!/usr/bin/python3

#author: Fridrich David
# processes log files from timeLogger app
# log has predetermined delimeters & positions
#
# might update (generalize) this sometime in the future
#
# takes one command line argument -- path to log file
# simply prints the results to console
#
# TODO add another option -- to "make log look prettier" -- align "|" and such

import os,sys,re
import inspect

class LogOutputConfig(object):
  def __init__(self,debug_lvl=0):
    # --- lvl 3 = everything
    # -- lvl 2 = activities
    # - lvl 1 = categories
    # lvl 0 = statistics
    # each level up contains the previous lvl info + it's new (0 is least info)
    self.version = "1.0"
    self.author = "gauron {David Fridrich}"

    self.debug_lvl = debug_lvl
    # dictionary -> { 'category' : time-spent }
    self.time_spent_in_category = {}
    # dictionary -> { 'activity' : time-spent }
    self.time_spent_in_activity = {}    

    self.time_spent_in_category_day = {}
    self.time_spent_in_activity_day = {}
    self.standard_log_day = {}

  def presets(self):
    print('##### ⎯⎯⎯ LOG PRESETS ⎯⎯⎯ #####')
    print('debug_lvl %s: '%self.debug_lvl)
    print('##### ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ #####')

  def addData(activity,category,time):
    pass
  def __repr__(self):

    return '##### ⎯⎯⎯ BASIC INFO ⎯⎯⎯ #####\nVersion: %s\nAuthor: %s\n##### ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ #####\n' %(self.version,self.author)

  def printErr(self,msg):
    print("Error in %s: %s"%("processLog.py",msg))
    exit(1)

def printHelp():
  print("""
      ~~~ processLog.py! ~~~

> this is a sub program to timeLogger
> reads log file of timeLogger format
> takes one command line argument -> path to log file
> log's format is equal to timeLogger's log format
> unkown CL arguments will be ignored
  """)
  exit(0)


# LOG FORMAT 
# --- TimeOfLog       | Activity            | TimeSpent | TimeBegin                | TimeEnd                | Category
# 2021-07-20 08:47:07 | breakfast           | 0:47:22   | from:2021-07-20 07:59:44 | to:2021-07-20 08:47:07 | food

def newData(data):
  """
  If debug_info is >3 print standard log & save info
  otherwise just save info to print later (per activity etc.)
  """
  parsed = data.split(" | ")
  parsed = [i.strip() for i in parsed]
  if(logConfig.debug_lvl >= 3):
    time = parsed[0].split(' ')[1]
    print("| ",time,'-',parsed[1],"("+parsed[2]+")")


def newDay(data):
  """
  @param1: data - expected format is '2021 07 21'
  this prints new days
  """
# '⊢'
  data = '╭ '+data+' ⎯⎯⎯⎯⎯⎯⎯⎯⎯'
  print(data)
  pass

def parser_processor():
  with open(sys.argv[1],'r+') as log:
    print(logConfig) # call __repr__
    logConfig.presets()
    for data in log.readlines():
      if data.startswith('---'):
        if re.match(".*[0-9]+",data): #if its not the first line in log
          print()
          data = data.split(" | ")
          newDay(data[0].replace("-","").replace('\n','').strip())
      else:
        newData(data)
        
if __name__ == "__main__":
  
  if len(sys.argv) >= 2:
    if sys.argv[1].lower() in ['-h','--help','help','h']:
      printHelp()

    logConfig = LogOutputConfig()
    if len(sys.argv) > 2 and sys.argv[2].lower() in ['-d','--debug','--debug_lvl']:
      try:
        logConfig.debug_lvl = int(sys.argv[3])
      except ValueError:
        logConfig.printErr("Debug_lvl must be a number, not '%s'" %sys.argv[3])
      
    parser_processor()

  else:
    printHelp()