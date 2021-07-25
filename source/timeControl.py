import datetime as dt

class DateTimeConvertor:

  @staticmethod
  def addTdelta(t,tdelta):
    return (dt.datetime.combine(dt.date.today(),t) + tdelta).time()  

  @staticmethod
  def tdeltaTime(timeD):
    return (dt.datetime.min + timeD).time()

  @staticmethod
  def timeTimeDelta(time):
    return dt.datetime.combine(dt.date.min,time) - dt.datetime.min

  @staticmethod
  def strTime(s):
    #delimeter must be ":"
    try:
      return dt.datetime.strptime(s,"%H:%M:%S").time()
    except:
      print("Delimeter is probably wrong[DateTimeConvertor -> strTime()]")
      exit(1)

  @staticmethod
  def convert(data,inCls,outCls): #in class / out class
    if inCls is outCls: #if they are the same class
      return data

    # print(data,inCls,outCls)
    if outCls is dt.timedelta:
      if inCls is dt.time:#TIME TO TIME DELTA
        return DateTimeConvertor.timeTimeDelta(data)

      if inCls is str: #STRING TO TIMEDELTA
        time = DateTimeConvertor.strTime(data)#str to time
        return DateTimeConvertor.timeTimeDelta(time)#time to timedelta

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
