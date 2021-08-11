#!/usr/bin/python3

import datetime as dt
import sys

class DateTimeConvertor:

  def __init__(self):
    
    pass 

  @classmethod
  def __inner_check_year(cls):
    pass

  @classmethod
  def __inner_check_month(cls):
    pass

  @staticmethod
  def initialCheck(cls, s : str):
    "First check of the string [main loop: formatDateTime()]"

    


    pass


  @staticmethod
  def formatDateTime(s : str):
    """
    Final form will be: whatever kind of string is provided, process delimeters
      & formats provided for year,month,day,hour,... and try to convert
      string to datetime object
    Currently supports:
    ---
    """
    # decide if its gonna be datetime or date or time
    # first, parse the string maybe char by char to get an idea of what it is
    # divider between date and time should ALWAYS BE " "(space)
    
    #functions below check validity of the given string

    clsObj = DateTimeConvertor()

    if not initialCheck(s):
      raise "Error in formatDateTime()... given string did not pass initialCheck(1)"        
    



    pass

################################################################################
################################################################################
###### static methods that dont need an initiated instance of this class #######

  @staticmethod
  def timeToSecs(t: dt.time):
    return (dt.datetime.combine(dt.date.min,t) - dt.datetime.min).total_seconds()

  @staticmethod
  def addTdelta(t, tdelta: dt.timedelta):

    if t.__class__ is dt.time:
      return (dt.datetime.combine(dt.date.today(),t) + tdelta).time()
    elif t.__class__ is dt.datetime:
      try:
        print("addTdelta:",(dt.datetime.combine(t.date(),t.time())+tdelta))
      except:
        pass
      return (dt.datetime.combine(t.date(),t.time())+tdelta)

  @staticmethod
  def tdeltaTime(timeD: dt.timedelta):
    "takes datetime.timedelta and returns datetime.time" 
    return (dt.datetime.min + timeD).time()

  @staticmethod
  def timeTimeDelta(time: dt.time):
    return dt.datetime.combine(dt.date.min,time) - dt.datetime.min

  @staticmethod
  def sumTime(data):
    """
    @param1: data - list of tuples,dictionary(NOT IMPLEM.) ... where second argument
                    (or value of key) is the time value (in datetime.time)

                              'name' &  datetime(day,hour,minute,second)
                    example:  { 'name' : dt.datetime(4,15,30,45), ... }
                              [('name', dt.datetime(4,15,30,45)), ... ] 
    """
    res = 0.0
    if data.__class__ is list and data[0].__class__ is tuple:
      for x,y in data:
        #### TODO implement strings and what not
        
        # if time is a class of float 
        if y.__class__ is float:
          res += y
          pass

    elif data.__class__ is dict:
      print("Warning: [sumTime()] for dictionary not implemented yet")

    else:
      print("Warning: function sumTime() in timeControl.py didn't recognize \
        given object, please use implemented objects")

    return res

  @staticmethod 
  # TODO # 
  # more delimeters.. add random ones / meta solution for all?
  # cut delimeter from string
  # and subsequently use it in conversion if possible
  def strTime(s: str): 
    #delimeter must be ":"
    try:
      return dt.datetime.strptime(s,"%H:%M:%S").time()
    except:
      print("Error: Delimeter is probably wrong[in DateTimeConvertor -> strTime()]")
      exit(1)

# TODO DEBUG
# inCls is useless coz all its needed to do is check the class first thing in this func
# maybe like do inCls & outCls as optional arguments
# if inCls is None (not provided) its gonna check what class data is
# & if outCls is None, its just gonna return what was given since no conversion is asked for
  @classmethod # ALSO IDK WHY THIS IS CLASSMETHOD & IDK WHY THIS WORKS
  def convert(cls,data,inCls,outCls): #in class / out class
    if inCls is outCls: #if they are the same class
      return data

    # print(data,inCls,outCls)
    if outCls is dt.timedelta:
      if inCls is dt.time:#TIME TO TIME DELTA
        return cls.timeTimeDelta(data)

      # TODO DEBUG check what kind of string is being given 
      # AKA could be '10:05:05' or '2021-05-16 10:05"05' -- does this matter?
      if inCls is str: # STRING TO TIMEDELTA 
        time = cls.strTime(data)#str to time
        return cls.timeTimeDelta(time)#time to timedelta

    if outCls is dt.datetime:
      if inCls is dt.time:
        return 
    # datetime
    # date
    #  -- seconds?
    # time
    # timedelta
    # timestamp
    # str

  @staticmethod
  def convertAny(data,toClass):
    """
    @param1: data - object given for conversion
    @param2: toClass - class given to convert object to

    param2 is exactly the class object (ex: str, datetime.time,...)
    """
    return DateTimeConvertor.convert(data,data.__class__,toClass)


# "interactive method" used to calculate how long the time has been running,
### for debug and fixing stuff basically -- just returns datetime difference
### can take whole line of log as argument or two specific times you want to get
### the difference of
  @staticmethod
  def getDiff(*args):
    """
    You can provide either one full string as arg or 2 strings that symbolize
    start and end of whatever activity (you provide just the times)

    one full string specifically from log:
    --- only info needed is FROM & TO (positions 3 & 4 after strip)
    --- example: 
    getDIff("2021-07-20 19:08:54 | dinner | 0:18:09 | from:2021-07-20 18:50:45 | to:2021-07-20 19:08:54 | food")
    
    begin & end separated:
    --- just calculates difference of these two provided times(and dates)
      @param1 - begin of activity --> string of datetime object
      @param2 - end of activity --> string of datetime object
    
    --- example:
    getDIff("from:2021-07-20 18:50:45","to:2021-07-20 19:08:54")
    
    """

    if len(args) == 1:
      #get whole line from log
      string = args[0]
      string = string.split(" | ")
      start = string[3].replace("from:",'')
      end = string[4].replace("to:",'')
    elif len(args) == 2:
      start = args[0]
      end = args[1]

      #format: 2021-07-30 16:50:11
    start = dt.datetime.strptime(start,"%Y-%m-%d %H:%M:%S")
    end = dt.datetime.strptime(end,"%Y-%m-%d %H:%M:%S")
    print(end-start)
    return  

if __name__ == '__main__':
  print("this is for ease of use baby")
  if len(sys.argv) == 2:
    DateTimeConvertor.getDiff(sys.argv[1])
    
  s = input("Gimme time to calculate:\n")
  DateTimeConvertor.getDiff(s)