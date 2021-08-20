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
import operator as op  # for itemgetter for dictionary sorting magic
import os
import re
import sys
import string

from timeControl import DateTimeConvertor as dtc

#change this to change default value of log; to be used when no log file is provided
_DEFAULT_LOG_VALUE='log/log.log'

class LogOutputConfig:
  def __init__(self,debug_lvl=0):
    # --- lvl 3 = everything (print every line of log + lvl 2)
    # -- lvl 2 = activities (act time in each day + lvl 1)
    # - lvl 1 = categories (see category-time in each day + lvl 0)
    # lvl 0 = statistics (most compressed one - just overall info)
    # each level up contains the previous lvl info + it's new (0 is least info)
    self.version = "1.1"
    self.author = "gauron {David Fridrich}"

    self.debug_lvl = debug_lvl
    self.date_after = None
    self.date_before = None

    self.param_day = False
    self.param_week = False
    self.param_month = False
    self.param_month_optional = None

    self.special_param_prev = False

    # all time combined together spent in categories
    self.time_spent_day = dt.time(0,0,0)

    # { 'activity': dt.time(spent), ...}
    self.time_spent_in_category_day = {}
    #these hold datetime.time values
    self.time_spent_in_activity_day = {}

    # this holds datetime.datetime values!! -> this can go above 24h therefore
    # if only datetime.time was used, it overflows and starts at 00.00 and doesnt
    # add any days, datetime.datetime can hold more than hours
    self.time_spent_in_category_all = {} #dictionary

    self.day_info = []  #list of every log-data in one day; is used & subsequentially
                        # printed out when debug_lvl is >= 3

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

  @staticmethod
  def sortDict(d): #some cool sorting magic #returns list
    return sorted(d.items(),key=op.itemgetter(1),reverse=True)

  """
  TODO - what can be done here is in self.day_info there can be time of log
  passed as well which will serve one purpose and that is to perhaps separate
  all the info which now looks like this:

  ╭ 2021 08 11 ⎯⎯⎯⎯⎯⎯⎯⎯⎯
  |  breakfast 1:14:48 (food)
  |  shower 0:25:29 (hygiene)
  |  coding 1:30:37 (programming)
  |  Max_walk 1:23:48 (outside)
  |  shower 0:04:51 (hygiene)
  |  lunch 1:49:25 (food)
  |  work 8:49:21 (work)

  but it could look something like this:

  ╭ 2021 08 11 ⎯⎯⎯⎯⎯⎯⎯⎯⎯
  |  breakfast 1:14:48 (food)
  |  shower 0:25:29 (hygiene)
  |  coding 1:30:37 (programming)
  |--12PM--
  |  Max_walk 1:23:48 (outside)
  |  shower 0:04:51 (hygiene)
  |  lunch 1:49:25 (food)
  |  work 8:49:21 (work)
  """
  def printDay(self): 
    for line in self.day_info:
      print("| %s %s (%s)"%(line[0],line[1],line[2]))
    self.day_info.clear()

  def printActDay(self):
    if self.time_spent_in_activity_day:
      sortedList = self.sortDict(self.time_spent_in_activity_day)
      if logConfig.debug_lvl >= 3:
        print()
      print("├ ACTIVITIES ⎯⎯⎯⎯")
      for key in sortedList:
        part, total = dtc.timeToSecs(key[1]), dtc.timeToSecs(self.time_spent_day)
        print("| (%.2f%%)"%(part/total*100),key[0],key[1])

      print("|") # separate ACTIVITIES & CATEGORIES in output
      
      #clear dict  
      self.time_spent_in_activity_day.clear()

  def printCatDay(self):
    if self.time_spent_in_category_day:  
      sortedList = self.sortDict(self.time_spent_in_category_day)
      print("├ CATEGORIES ⎯⎯⎯")
      for key in sortedList:
        part, total = dtc.timeToSecs(key[1]), dtc.timeToSecs(self.time_spent_day)
        print('| (%.2f%%)'%(part/total*100),key[0],key[1])
      print()

      #clear dict 
      self.time_spent_in_category_day.clear()

  def printSummary(self):
    sortedList = self.sortDict(self.time_spent_in_category_all)
    #add all times from list to one variable
    total = dtc.sumTime(sortedList)

    # get longest string and set this length to all lines in summ so it looks nicer
    ls = 0
    for a,b in sortedList:
      if len(a) > ls:
        ls = len(a)

    print("╭ SUMMARY ⎯⎯")
    for name,time in sortedList:
      days,timeTmp = convertSecondsToDatetime(time)
      prcnt = (time/total*100)
      if days == 0:
        print("| (%5.2f%%)"%prcnt , "{:<{num}}".format(name,num=ls) , "| spent "+str(timeTmp))
      else:
        if days == 1:
          print("| (%5.2f%%)"%prcnt , "{:<{num}}".format(name,num=ls) , "| spent " + str(days)+" day, "+str(timeTmp))
        else:
          print("| (%5.2f%%)"%prcnt , "{:<{num}}".format(name,num=ls) , "| spent " + str(days)+" days, "+str(timeTmp))
      pass

  def addData(self,what,info,time):
    """
    @param what - identify what kind of info this is\n
    @param info - info to be collected(saved to print later)\n
    @param time - time of this info being logged\n
    --- both info & time are simply taken from one line of log and divided to
        variables for easier reading (look for call of addData for more information)
    """
    #collect data together
    if "," in info:
      info = info.split(',')[0]
    if "_(" in info:
      info = info.split("_(")[0]
    if "(" in info:
      info = info.split("(")[0]

    try:
      info = info.lower() #info is activity/category etc. -- determined by 'what'
    except:
      info[1] = info[1].lower()

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
    
    elif what == 'data':
      self.day_info.append(info)
############## end of class LogOutputConfig ##############

def printErr(s):
  print("Error: %s" % s)
  exit(1)

def printHelp():
  print("""
      ~~~ processLog.py! ~~~

> this is a sub program to timeLogger
> reads log file of timeLogger format
> takes one command line argument -> path to log file
> log's format is equal to timeLogger's log format
> unkown CL arguments will be ignored (and user informed)
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

def getValidMonth(s : str):
  res = None
  s = s.lower()
  _months = ['january','fabruary','march','april','may','june','july','august','september','october','november','december',
             'jan'    ,'fab'     ,'mar'  ,'apr'  ,'may','jun' ,'jul' ,'aug'   ,'sep'      ,'oct'    ,'nov'     ,'dec']

  # month is in letter form
  if s in _months:
    tmp = [i for i,x in enumerate(_months) if s == x]
    if len(tmp) != 1:
      raise "String provided for [MONTH] not recognized"
    res = tmp[0]
  else:
    res = s

  #now all variations have to be a number
  try:
    if int(res) > 12 or int(res) <= 0:
      printErr("There's only 12 months. That's interval of <1,12>. Provided: %s"%res)
  except:
    printErr("Argument [MONTH] couldn't be resolved (probably is not a valid month indicator)")

  res = str(res)
  if len(res) == 1:
    res = '0' + res
    
  return res
    


def newData(data):
  """
  If debug_info is >=3 print standard log & save info
  otherwise just save info to print later (per activity etc.)
  """
  # print(data)
  parsed = data.replace("\n",'').split(" | ")
  parsed = [i.strip() for i in parsed]
  
  if(logConfig.debug_lvl >= 3):# standard log out
    tmp = parsed.copy() #make a copy of parsed[list] so it doesnt change with pops
    tmp.pop(3)
    tmp.pop(3)
    tmp.pop(0) 
    # ^ coz when something is popped, it removes it from the list right,
    # so therefore im removing items on indexes 3 & 4 which are 'from' time and
    # 'to' time.

    logConfig.addData("data",tmp,parsed[0])
    # time = parsed[0].split(' ')[1]
    # print("| ",time,'-',parsed[1],"("+parsed[2]+") ["+parsed[5]+']')

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
    # print()#newline between days
    data = '╭ '+data+' ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯'
    print(data)
  pass


def _special_controler(log):
  print("---------special_log---------")

  exit(0)



def _decider():
  "just an inside function for MainLoop so it's easier to read & manage depth/debug lvls"

  if logConfig.debug_lvl>=3:
    logConfig.printDay()

  if(logConfig.debug_lvl>=2):
    logConfig.printActDay()

  if(logConfig.debug_lvl>=1):
    logConfig.printCatDay()

def MainLoop(logFileHandler):
  with open(logFileHandler,'r+') as log:
    print(logConfig) # call __repr__

    log_data = log.readlines()

    #checks if special parameters are given & prepares for them
    # _special_controler(log_data)

    # first = log_data[1]

    # first = log.readline()
    # first = first.split(" | ")
    # newDay(first[0].replace("-","").replace('\n','').strip())

    for data in log_data:
      if data.startswith('###'): #ignore these lines
        continue
      elif data.startswith('---'): #this is line with new day
        _decider()

        logConfig.time_spent_day = dt.time(0,0,0)

        data = data.split(" | ")
        newDay(data[0].replace("-","").replace('\n','').strip())
      else: #everything else is data, there can't be any errors
        newData(data)
    #END OF FOR LOOP

    #print last day info since its in for loop which ends before printing it out
    _decider()

    logConfig.printSummary()

def parseArgs():
  print("INIT_ARGS:",sys.argv) #DEBUG

  log = _DEFAULT_LOG_VALUE #default value for log
  argcmd = sys.argv

# all arguments can be writen without '-' aka 'h' or 'help' is a valid command.
# then different arguments are possible:

#   -h.   --help      -> print out help message
#   -dl,  --debug_lvl -> change level of depth of what to print (default = 0)
#         --depth     -> an alias for debug

# date commands are not mutually exclusive, you can use '-b 05.05.2020 -l' 
# to print BOTH, everything before 05.05.2020 AND last day in the log

#   -a, --after         -> choose a date to start with(aka dont consider activities before)
#   -b, --before        -> dont consider activities after this date

#   -d, --day           -> show only current day(latest day logged)
#   -w, --week          -> show only current week(latest week logged)
#   -m, --month [MONTH] -> MONTH is optional, can be number or full word(January),
#                          if none is given, latest month in log is chosen

#   -p, --previous          -> this is a special optional argument, that can be added
#   to (-d/-w/-m). Using this will show last "closed" timeframe. Closed timeframe,
#   meaning if today is Wednesday, that means the week is not over yet AKA its not closed.
#   Therefore if using parameters '-w -p' (--week + --previous) it will show last week
#   because last week is fully done, from Monday to Sunday (is complete / closed)
#   This is checked by whether or not there is a log AFTER Sunday in new week.
#   Similarly will work --day and --month 
#
#   Example:
#     - if you wanted to print last day, use parameters '-tl' or '-t -l' 


  #this is just name of the file being run, dont need it
  _ = argcmd.pop(0)

  for i,x in enumerate(argcmd):
    # print(">",i,x) #this wont show values of debug for example, because it's 
    # an argument that always follows '-d' for example, and it is poped inside the ifs & elifs
    if argcmd[i].lower() in ['-h','--help','help']:
      printHelp()
    elif argcmd[i].lower() in ['-dl','--depth','depth','--debug_lvl']:
      try:
        logConfig.debug_lvl = int(argcmd.pop(i+1))
      except IndexError:
        print("Error: Debug_lvl (-d) argument needs a value (type=int)")
        exit(1)
      except ValueError:
        print("debug_lvl (-d) value must be of type int")
        exit(1)

    elif argcmd[i].lower() in ['-a','--after','after']:
      if logConfig.date_after is None:
        try:
          date = argcmd.pop(i+1)   
          #format is-> day-mon-year (all in numbers) [01-02-2005] all zero padded
          date = dt.datetime.strptime(date,"%d-%m-%Y")
        except:
          print("Error: Command == after; Couldn't resolve value %s" % str(date))
        else:
          if isinstance(date,dt.datetime):
            logConfig.date_after = date #final check & save into class var
          else:
            raise "Argument for '--after' wasn't successfully converted"
      else:
        printErr("[in parseArgs()] Can't assign 'after' parameter twice")

    elif argcmd[i].lower() in ['-b','--before','before']:
      if logConfig.date_before is None:
        try:
          date = argcmd.pop(i+1)
          #format is-> day-mon-year (all in numbers) "01-02-2005" all zero padded
          date = dt.datetime.strptime(date,"%d-%m-%Y")
        except:
          printErr("cmd == before; Couldn't resolve value %s" %str(date))
        else:
          if isinstance(date,dt.datetime):
            logConfig.date_before = date
          else:
            raise "Argument for '--before' wasn't successfully converted"
      else:
        printErr("[in parseArgs()] Can't assign 'before' parameter twice")
    elif argcmd[i].lower() in ['-d','--day','day']:
      logConfig.param_day = True
    elif argcmd[i].lower() in ['-w','--week','week']:
      logConfig.param_week = True
    elif argcmd[i].lower() in ['-m','--month','month']:
      logConfig.param_month = True
      
      #check if '-m' was provided with additional argument
      tmp = getValidMonth(argcmd[i+1])
      if tmp != None:
        logConfig.param_month_optional = tmp
        argcmd.pop(i+1) #arg is loaded, get rid of it

    elif argcmd[i].lower() in ['-p','--previous','previous']:
      logConfig.special_param_prev = True

    else: #this way the order of parameters doesnt really matter, as long as theres no wrong ones
      if log == _DEFAULT_LOG_VALUE: #rewrite default if something is provided
        #check what it is first
        log = argcmd[i]
      else: 
        #when log was already loaded, but an argument that wasnt any parameter was
        #still passed
        printErr("An unknown argument was passed: %s, exiting..." %argcmd[i])
  return log

if __name__ == "__main__":

  #class init
  logConfig = LogOutputConfig()

  #check cmd arguments a assign them if possible
  log = parseArgs()
  #begin process
  MainLoop(log)
