import datetime as dt 

class TimeDifference(object):
    def __init__(self):
        self.res=''
        self.minute=dt.time(0,1,0)
        self.fivemins=dt.time(0,5,0)
        self.fifteenmins=dt.time(0,15,0)
        self.thirtymins=dt.time(0,30,0)
        self.hour=dt.time(1,0,0)
        self.hourthirty=dt.time(1,30,0)
        self.twohrs=dt.time(2,0,0)
        self.threehrs=dt.time(3,0,0)
        self.fourhrs=dt.time(4,0,0)
        self.fivehrs=dt.time(5,0,0)
        self.sixhrs=dt.time(6,0,0)
        self.sevenhrs=dt.time(7,0,0)
        self.eighthrs=dt.time(8,0,0)
        self.ninehrs=dt.time(9,0,0)
        self.tenhrs=dt.time(10,0,0)
        self.fifteenhrs=dt.time(15,0,0)
        self.twentyhrs=dt.time(20,0,0)
        self.day=dt.time(23,59,59,999999)

# just to debug stuff
    def log(self,str):
        print("timeDifference.py> log: %s" % str)

# absolute time difference between the two
# (doesn't accept anything more than time -- no dates from datetime etc.)
    def absTimeDif(self,one,two):
        #combine into datetime (not only time) to allow subtraction
        one = dt.datetime.combine(dt.date.today(),one)
        two = dt.datetime.combine(dt.date.today(),two)
        
        # self.log("one: %s| two: %s" % (one, two))
        
        if(one > two):
            return one - two
        else:
            return two - one

    def timeAprox(self,time):
        if(time < self.minute):
            return 'less than a minute'
        elif(self.absTimeDif(self.fivemins,time) < self.absTimeDif(self.fifteenmins,time)):
            return 'around 5 mins'
        elif(self.absTimeDif(self.fifteenmins,time) < self.absTimeDif(self.thirtymins,time)):
            return 'around 15 mins'
        elif(self.absTimeDif(self.thirtymins,time) < self.absTimeDif(self.hour,time)):
            return 'around 30 mins'
        elif(self.absTimeDif(self.hour,time) < self.absTimeDif(self.hourthirty,time)):
            return 'around an hour'
        elif(self.absTimeDif(self.hourthirty,time) < self.absTimeDif(self.twohrs,time)):
            return 'around hour and 30 mins'
        elif(self.absTimeDif(self.twohrs,time) < self.absTimeDif(self.threehrs,time)):
            return 'around 2 hours'
        elif(self.absTimeDif(self.threehrs,time) < self.absTimeDif(self.fourhrs,time)):
            return 'around 3 hours'
        elif(self.absTimeDif(self.fourhrs,time) < self.absTimeDif(self.fivehrs,time)):
            return 'around 4 hours'
        elif(self.absTimeDif(self.fivehrs,time) < self.absTimeDif(self.sixhrs,time)):
            return 'around 5 hours'
        elif(self.absTimeDif(self.sixhrs,time) < self.absTimeDif(self.sevenhrs,time)):
            return 'around 6 hours'
        elif(self.absTimeDif(self.sevenhrs,time) < self.absTimeDif(self.eighthrs,time)):
            return 'around 7 hours'
        elif(self.absTimeDif(self.eighthrs,time) < self.absTimeDif(self.ninehrs,time)):
            return 'around 8 hours'
        elif(self.absTimeDif(self.ninehrs,time) < self.absTimeDif(self.tenhrs,time)):
            return 'around 9 hours'
        elif(self.absTimeDif(self.tenhrs,time) < self.absTimeDif(self.fifteenhrs,time)):
            return 'around 10 hours'
        elif(self.absTimeDif(self.fifteenhrs,time) < self.absTimeDif(self.twentyhrs,time)):
            return 'around 15 hours'
        elif(self.absTimeDif(self.twentyhrs,time) < self.absTimeDif(self.day,time)):
            return 'around 20 hours'
        elif(time <= self.day):
            return 'almost a whole day, damn'
        else:
            return 'more than a day -- chill bro'

if __name__ == "__main__":
    print("Can't do that, sorry")
    exit(0)
    pass