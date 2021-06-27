from datetime import datetime as dt 

class TimeDifference(time):
    def __init__(self):
        self.res=''
        self.minute=dt.time(0,1,0)
        self.fifteenmins=dt.time(0,5,0)
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
        self.day=dt.time(23,59,59)

    def absTimeDif(self,one,two):
        if(self.one > self.two):
            return self.one - self.two
        else:
            return self.two - self.one

    def timeAprox(self,time):
        if(time < self.minute):
            return 'less than a minute(what kind of activity is this)'
        elif(absTimeDif(self.fifteenmins,time) < absTimeDif(self.thirtymins,time)):
            return 'around 15 mins'
        elif(absTimeDif(self.thirtymins,time) < absTimeDif(self.hour,time)):
            return 'around 30 mins'
        elif(absTimeDif(self.hour,time) < absTimeDif(self.hourthirty,time)):
            return 'around an hour'
        elif(absTimeDif(self.hourthirty,time) < absTimeDif(self.twohrs,time)):
            return 'around hour and 30 mins'
        elif(absTimeDif(self.twohrs,time) < absTimeDif(self.threehrs,time)):
            return 'around 2 hours'
        elif(absTimeDif(self.threehrs,time) < absTimeDif(self.fourhrs,time)):
            return 'around 3 hours'
        elif(absTimeDif(self.fourhrs,time) < absTimeDif(self.fivehrs,time)):
            return 'around 4 hours'
        elif(absTimeDif(self.fivehrs,time) < absTimeDif(self.sixhrs,time)):
            return 'around 5 hours'
        elif(absTimeDif(self.sixhrs,time) < absTimeDif(self.sevenhrs,time)):
            return 'around 6 hours'
        elif(absTimeDif(self.sevenhrs,time) < absTimeDif(self.eighthrs,time)):
            return 'around 7 hours'
        elif(absTimeDif(self.eighthrs,time) < absTimeDif(self.ninehrs,time)):
            return 'around 8 hours'
        elif(absTimeDif(self.ninehrs,time) < absTimeDif(self.tenhrs,time)):
            return 'around 9 hours'
        elif(absTimeDif(self.tenhrs,time) < absTimeDif(self.fifteenhrs,time)):
            return 'around 10 hours'
        elif(absTimeDif(self.fifteenhrs,time) < absTimeDif(self.twentyhrs,time)):
            return 'around 15 hours'
        elif(absTimeDif(self.twentyhrs,time) < absTimeDif(self.day,time)):
            return 'around 20 hours'
        elif(self.day < time):
            return 'almost a whole day, damn'
        else:
            return 'more than a day -- chill bro'

if __name__ == "__main__":
    print("Can't do that, sorry")
    exit(0)
    pass