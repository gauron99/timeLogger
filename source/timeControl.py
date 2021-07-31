import datetime as dt

class DateTimeConvertor:

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
  def strTime(s: str):
    #delimeter must be ":"
    try:
      return dt.datetime.strptime(s,"%H:%M:%S").time()
    except:
      print("Error: Delimeter is probably wrong[DateTimeConvertor -> strTime()]")
      exit(1)

  @classmethod
  def convert(cls,data,inCls,outCls): #in class / out class
    if inCls is outCls: #if they are the same class
      return data

    # print(data,inCls,outCls)
    if outCls is dt.timedelta:
      if inCls is dt.time:#TIME TO TIME DELTA
        return cls.timeTimeDelta(data)

      if inCls is str: #STRING TO TIMEDELTA
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
### for debug and fixing stuff basically
### can take whole line of log as argument or two specific times you want to get
### the difference of
  @staticmethod
  def getDiff(*args):
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
