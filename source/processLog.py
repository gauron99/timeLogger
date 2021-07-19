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

def printHelp():
  print("""
      ~~~ processLog.py! ~~~

> this is a sub program to timeLogger
> reads log file of timeLogger format
> takes one command line argument -> path to log file
  """)
  exit(0)

#### STATISTICS INFO ####

# categories = dictionary -> { 'category' : times-seen }
categories = {}
# dictionary -> { 'category' : time-spent }
time_spent_in_category = {}
# dictionary -> { 'activity' : time-spent }                       
time_spent_in_activity = {}

#### --------------- ####

def addInfo(data):
  pass

def parser_processor():
  with open(sys.argv[1],'r+') as log:
    for data in log.readlines():
      if data.startswith('---'):
        continue
      addInfo(data)
      



if __name__ == "__main__":
  if len(sys.argv) == 2:
    if sys.argv[1].lower() in ['-h','--help','help','h']:
      printHelp()

    #log was provided in cmdl (hopefully)
    parser_processor()

  else:
    #read config??
    printHelp()