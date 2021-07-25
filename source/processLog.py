#!/usr/bin/python3

#author: Fridrich David
# processes log files from timeLogger app
# log has predetermined delimeters & positions
#
# might update (generalize) this sometime in the future
#
# takes one command line argument -- path to log file
# simply prints the results to console

import os,sys,re
import datetime as dt
from timeControl import DateTimeConvertor as dtc


class LogOutputConfig(object):
  def __init__(self,debug_lvl=0):
    # --- lvl 3 = everything (print every line of log + lvl 2)
    # -- lvl 2 = activities (act time in each day + lvl 1)
    # - lvl 1 = categories (see category-time in each day + lvl 0)
    # lvl 0 = statistics (most compressed one - just overall info)
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

  def printActDay(self):
    x = self.time_spent_in_activity_day
    print("├ ACTIVITIES ⎯⎯⎯")
    for key in x:
      print("| ",key, x[key])
  
  def clearActDay(self):
    self.time_spent_in_activity_day.clear()

  def printCatDay(self):
    x = self.time_spent_in_category_day
    print("├ CATEGORIES ⎯⎯")
    for key in x:
      print("| ",key,x[key])
  
  def clearCatDay(self):
    self.time_spent_in_category_day.clear()

  def presetsShow(self):
    print('##### ⎯⎯⎯ LOG PRESETS ⎯⎯⎯ #####')
    print('debug_lvl %s'%self.debug_lvl)
    print('##### ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ #####')
    print()

  def addData(self,what,info,time):
    #collect data together
    if "," in info:
      info = info.split(',')[0]
    if "_(" in info:
      info = info.split("_(")[0]
    if "(" in info:
      info = info.split("(")[0]

    info = info.lower() #info is activity/category -- determined by 'what'
    if what == "activity":
      if info in self.time_spent_in_activity_day:
        self.time_spent_in_activity_day[info] = \
          dtc.addTdelta(self.time_spent_in_activity_day[info],time)
        # print(" +",info,time)

      else:
        self.time_spent_in_activity_day[info] = dtc.tdeltaTime(time)
        # print(" =",info,time)

    elif what == 'category':
      if info in self.time_spent_in_category_day:
        self.time_spent_in_category_day[info] = \
          dtc.addTdelta(self.time_spent_in_category_day[info],time)
        # print(" +",info,time)

      else:
        self.time_spent_in_category_day[info] = dtc.tdeltaTime(time)
        # print(" =",info,time)

  def __repr__(self):

    return '##### ⎯⎯⎯ BASIC INFO ⎯⎯⎯ #####\nVersion: %s\nAuthor: %s\n##### \
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ #####\n' %(self.version,self.author)

  def printErr(self,msg):
    print("Error in %s: %s"%("processLog.py",msg))
    exit(1)
############## end of class LogOutputConfig ##############

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
# --- TimeOfLog       | Activity | TimeSpent | TimeBegin                | TimeEnd                | Category
# 2021-07-20 08:47:07 | breakfast| 0:47:22   | from:2021-07-20 07:59:44 | to:2021-07-20 08:47:07 | food

def convertSecondsToDatetime(seconds):
    days = seconds // (3600*24)
    seconds = seconds % (3600*24)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    print( days,hours,minutes,seconds)
    return dt.datetime(day=days,hour=hours,minute=minutes,second=seconds)

def newData(data):
  """
  If debug_info is >=3 print standard log & save info
  otherwise just save info to print later (per activity etc.)
  """
  # print(data)
  parsed = data.replace("\n",'').split(" | ")
  parsed = [i.strip() for i in parsed]
  if(logConfig.debug_lvl >= 3):# standard log out
    time = parsed[0].split(' ')[1]
    print("| ",time,'-',parsed[1],"("+parsed[2]+") ["+parsed[5]+']')

  timeDeltaObj = dtc.convertAny(parsed[2],dt.timedelta)
  if(logConfig.debug_lvl >= 2):#save activities per day
    # print("<<",parsed[2],parsed[2].__class__)
    # print(">>",timeDeltaObj,timeDeltaObj.__class__)
    logConfig.addData("activity",parsed[1],timeDeltaObj)

  if logConfig.debug_lvl >= 1:#save categories per day
    logConfig.addData("category",parsed[5],timeDeltaObj)

    

def newDay(data):
  """
  @param1: data - expected format is '2021 07 21'
  prints new days with format
  """
# '⊢ ╭'
  data = '╭ '+data+' ⎯⎯⎯⎯⎯⎯⎯⎯⎯'
  print(data)
  pass

def parser_processor():
  with open(sys.argv[1],'r+') as log:
    print(logConfig) # call __repr__
    logConfig.presetsShow()
    _ = log.readline() #read first line of log (which is just info for user)
    first = log.readline()
    first = first.split(" | ")
    newDay(first[0].replace("-","").replace('\n','').strip())
    for data in log.readlines():
      if data.startswith('---'):
        if(logConfig.debug_lvl>=2):
          logConfig.printActDay()
          logConfig.clearActDay()
          print("|") # separate ACTIVITIES & CATEGORIES in output

        if(logConfig.debug_lvl>=1):
          logConfig.printCatDay()
          logConfig.clearCatDay()

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