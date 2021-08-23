#!/usr/bin/python3
import os
import sys
import unittest
from datetime import time
import datetime as dt
import filework as fw

"""testing file for log"""


fc = fw.fileConfiguration()

ac = "test act"
cat = "test cat"

  
_counter = 1

class TestTimeDifferenceModule(unittest.TestCase):
  
  @staticmethod
  def Cnt(s):
    global _counter
    tmp = _counter
    _counter += 1
    return s+str(tmp)

  "Testing log file, predetermined values to write to log"
  """
  ------ all of this needs to go to writeToLog ------
  activity -> (string) name of activity\n
  tBegin -> (datetime) beginning of activity\n
  tEnd -> (datetime) end of activity\n
  tDiff -> (timedelta?) how long has the activity been running for\n
  tNow -> (datetime) time of log (NOW)\n
  category -> (string) name of category
  """
  def test1_yesterday_fill_no_error(self):
    dateNow = dt.datetime.now().date() #date
    timeMidDay = dt.time(12,00,00,1) #time
    dtStart = dt.datetime.combine(dateNow,timeMidDay) #full datetime
    dtCustomStart = dtStart + dt.timedelta()

    dtCustomEnd = dtCustomStart + dt.timedelta(hours=1,microseconds=1)

    diff = dtCustomEnd - dtCustomStart

    fw.writeToLog(self.Cnt(ac),dtCustomStart,dtCustomEnd,diff,dtCustomEnd,cat)
    #writeToLog closes the log file when finished


  def test2_midnight(self):

    dateNow = dt.datetime.now().date() #date
    timeEndOfDayCustom = dt.time(23,50,50,1) #time
    dtCustomStart = dt.datetime.combine(dateNow,timeEndOfDayCustom) #full datetime

    dtCustomEnd = dtCustomStart + dt.timedelta(hours=1,microseconds=1)

    diff = dtCustomEnd - dtCustomStart

    fw.writeToLog(self.Cnt(ac),dtCustomStart,dtCustomEnd,diff,dtCustomEnd,cat)
    #writeToLog closes the log file when finished

if __name__ == "__main__":
    print("Make sure you set up the right log file in config.txt! \
This is gonna write whole bunch of lines to it to test some stuff")
    i = input("Is it all good?[y][n]")
    if i.lower() in ['yes','y','']:
      print("Testing!")
      unittest.main()
    else:
      print('doing nothing...')
      