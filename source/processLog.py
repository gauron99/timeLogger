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

import os,sys

class LogOutputConfig(object):
  def __init__(self,debug_lvl=0):
    self.debug_lvl = debug_lvl
    # categories = dictionary -> { 'category' : times-seen }
    self.categories = {}
    # dictionary -> { 'category' : time-spent }
    self.time_spent_in_category = {}
    # dictionary -> { 'activity' : time-spent }                       
    self.time_spent_in_activity = {}    
    
  def __str__(self):
    return ''

  def log(self,msg):
    if self.debug_lvl == 0:
      print(msg)
    else:
      print(self)

def printHelp():
  print("""
      ~~~ processLog.py! ~~~

> this is a sub program to timeLogger
> reads log file of timeLogger format
> takes one command line argument -> path to log file
  """)
  exit(0)


# LOG FORMAT 
# --- TimeOfLog       | Activity            | TimeSpent | TimeBegin                | TimeEnd                | Category
# 2021-07-20 08:47:07 | breakfast           | 0:47:22   | from:2021-07-20 07:59:44 | to:2021-07-20 08:47:07 | food
def addInfo(data):
  parsed = data.split(" | ")
  parsed = [i.strip() for i in parsed]
  print(parsed[0],";",parsed[1],";",parsed[2])

def parser_processor():
  new_day = False
  with open(sys.argv[1],'r+') as log:
    for data in log.readlines():
      if data.startswith('---'):
        new_day = True
        continue
      addInfo(data)
      
      new_day = False



if __name__ == "__main__":
  if len(sys.argv) == 2:
    if sys.argv[1].lower() in ['-h','--help','help','h']:
      printHelp()

    logConfig = LogOutputConfig()
    #log was provided in cmdl (hopefully)
    parser_processor()

  else:
    #read config??
    printHelp()