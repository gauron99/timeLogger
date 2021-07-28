#!/usr/bin/python3

#author: Fridrich David
# processes log files from timeLogger app
# log has predetermined delimeters & positions
#
# might update (generalize) this sometime in the future
#
# takes one command line argument -- path to log file
# simply prints the results to console

import datetime as dt
import operator as op  # for itemgetter
import os
import re
import sys

from timeControl import DateTimeConvertor as dtc


class LogOutputConfig:
  def __init__(self,debug_lvl=0):
    # --- lvl 3 = everything (print every line of log + lvl 2)
    # -- lvl 2 = activities (act time in each day + lvl 1)
    # - lvl 1 = categories (see category-time in each day + lvl 0)
    # lvl 0 = statistics (most compressed one - just overall info)
    # each level up contains the previous lvl info + it's new (0 is least info)
    self.version = "1.0"
    self.author = "gauron {David Fridrich}"

    self.debug_lvl = debug_lvl
    self.date_after = dt.datetime
    self.date_before = dt.datetime
    self.date_only_last = False

    # all time combined together spent in categories
    self.time_spent_day = dt.time(0,0,0)

    # { 'activity': dt.time(spent), ...}
    self.time_spent_in_category_day = {}
    #these hold datetime.time values
    self.time_spent_in_activity_day = {}

    # this holds datetime.datetime values!! -> this can go above 24h therefore
    # if only datetime.time was used, it overflows and starts at 00.00 and doesnt
    # add any days, datetime.datetime can hold more than hours
    self.time_spent_in_category_all = {}

#there is something wrong with '⎯' -> it shows shorter than it actually is in 
#the output when there are multiple of '⎯' on next to each other
# (aka the closing lines of BASIC INFO & LOG PRESENTS) therefore they are longer
# in here so they appear how they should in the output 
  def __repr__(self):
    return '\
##### ⎯⎯⎯ BASIC INFO ⎯⎯⎯ #####\n\
Version: %s\nAuthor: %s\n\
##### ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ #####\n\n\
##### ⎯⎯⎯ LOG PRESETS ⎯⎯⎯ #####\n\
debug_lvl %s\n\
##### ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ #####\n\n' %(self.version,self.author,self.debug_lvl)

  def printErr(self,msg):
    print("Error in %s: %s"%("processLog.py",msg))
    exit(1)

  def sortDict(self,d):
    return sorted(d.items(),key=op.itemgetter(1),reverse=True)

  def printActDay(self):
    sortedList = logConfig.sortDict(self.time_spent_in_activity_day)
    print("├ ACTIVITIES ⎯⎯⎯⎯")
    for key in sortedList:
      part, total = dtc.timeToSecs(key[1]), dtc.timeToSecs(self.time_spent_day)
      print("| (%.2f%%)"%(part/total*100),key[0],key[1])

  def printCatDay(self):
    sortedList = logConfig.sortDict(self.time_spent_in_category_day)
    print("├ CATEGORIES ⎯⎯⎯")
    for key in sortedList:
      part, total = dtc.timeToSecs(key[1]), dtc.timeToSecs(self.time_spent_day)
      print('| (%.2f%%)'%(part/total*100),key[0],key[1])

  def printSummary(self):
    sortedList = logConfig.sortDict(self.time_spent_in_category_all)
    #add all times from list to one variable
    total = dtc.sumTime(sortedList)
    print("╭ SUMMARY ⎯⎯")
    
    for name,time in sortedList:
      days,timeTmp = convertSecondsToDatetime(time)
      print("| (%.2f%%)"%(time/total*100),name,"| spent " + str(days)+" days, "+str(timeTmp))
      pass

  def clearActDay(self):
    self.time_spent_in_activity_day.clear()
  
  def clearCatDay(self):
    self.time_spent_in_category_day.clear()

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

    elif what == 'summary':
      # print("+",info,time)
      #this is just seconds kept! (not time object like 2 objects above in dicts)
      if info in self.time_spent_in_category_all:
        self.time_spent_in_category_all[info] += dtc.timeToSecs(dtc.tdeltaTime(time)) 
        # print("+",self.time_spent_in_category_all[info])
      else:
        self.time_spent_in_category_all[info] = dtc.timeToSecs(dtc.tdeltaTime(time))
        # print("=",self.time_spent_in_category_all[info])
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
  seconds = int(seconds)
  days = seconds // (3600*24)
  seconds = seconds % (3600*24)

  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  seconds = seconds % 60

  return days,dt.time(hour=hours,minute=minutes,second=seconds)

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

  # print('+',logConfig.time_spent_day,timeDeltaObj,"(time_spent_all_day)")
  logConfig.time_spent_day = dtc.addTdelta(logConfig.time_spent_day,timeDeltaObj)

  if(logConfig.debug_lvl >= 2):#save activities per day
    # print("<<",parsed[2],parsed[2].__class__)
    # print(">>",timeDeltaObj,timeDeltaObj.__class__)
    logConfig.addData("activity",parsed[1],timeDeltaObj)

  if logConfig.debug_lvl >= 1:#save categories per day
    logConfig.addData("category",parsed[5],timeDeltaObj)

  logConfig.addData("summary",parsed[5],timeDeltaObj)

def newDay(data):
  """
  @param1: data - expected format is '2021 07 21'
  prints new days with format
  """
# '⊢ ╭'
  if logConfig.debug_lvl > 0:
    print()#newline between days
    data = '╭ '+data+' ⎯⎯⎯⎯⎯⎯⎯⎯⎯'
    print(data)
  pass

def parserProcessor():
  with open(sys.argv[1],'r+') as log:
    print(logConfig) # call __repr__
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

        logConfig.time_spent_day = dt.time(0,0,0)

        data = data.split(" | ")
        newDay(data[0].replace("-","").replace('\n','').strip())
      else:
        newData(data)
    #END OF FOR LOOP

    #print last day info since its in for loop which ends before printing it out
    if(logConfig.debug_lvl>=2):
      logConfig.printActDay()
      logConfig.clearActDay()
      print("|") # separate ACTIVITIES & CATEGORIES in output

    if(logConfig.debug_lvl>=1):
      logConfig.printCatDay()
      logConfig.clearCatDay()

    logConfig.printSummary()


def parseArgs():
  
  if len(sys.argv) < 2:
    print("Not enough arguments, log file missing...")
    printHelp()

  argcmd = sys.argv
# then different arguments are possible:
#   -d, --debug   -> change level of depth of what to print (default = 0)
#   -a, --after   -> choose a date to start with(aka dont consider activities before)
#   -b, --before  -> dont consider activities after this date
#   -l, --last    -> consider only last day in log
  skip = False
  for i in range(2,len(sys.argv)): # skip argv[1] coz it has to be a log file
    if skip:
      skip = False
      continue
    if argcmd[i].lower() in ['-h','--help']:
      printHelp()
    elif argcmd[i].lower() in ['-d','--debug']:
      try:
        logConfig.debug_lvl = int(argcmd[i+1])
      except IndexError:
        print("Error: Debug_lvl (-d) argument needs a value (type=int)")
        exit(1)
      except ValueError:
        print("debug_lvl (-d) value must be of type int")
        exit(1)
      else:
        skip = True

    elif argcmd[i].lower() in ['-a','--after']:
      try:
        date = argcmd[i+1]   #format is-> day-mon-year (all in numbers) [01-02-2005]
        date = dt.datetime.strptime(date,"%d-%-d-%Y")
      except:
        pass
      else:
        if isinstance(date,dt.datetime):
          logConfig.date_after = date
          skip = True
        else:
          raise "Argument for '--after' is not datetime.datetime object after converting."

        
if __name__ == "__main__":

  #class init
  logConfig = LogOutputConfig()

  #check cmd arguments a assign them if possible
  parseArgs()
  exit(0)

  #begin process
  parserProcessor()
