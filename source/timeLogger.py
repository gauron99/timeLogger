#!/usr/bin/python3
import tkinter as tk
import os
import string
import sys

import datetime as dtOG
from datetime import datetime as dt

import config as Config
import filework as fw
import timeDifference as td

# window size
wXaxis = '500'
wYaxis = '250'


# ------------------- ADD YOUR OWN CATEGORIES AND KEYWORDS ------------------- #
#       -- new category -> add to _categories list
#                       -> create keywords for said category
#       -- new key words-> add them in _keywords list
#                       -> pair categories & keyowrds in (GiveKeyWordGetCategory())
#
# --> can we I add this as config options? :thinking:
# ------------------- ADD YOUR OWN CATEGORIES AND KEYWORDS ------------------- #


_categories = ['gaming','programming','food','outside','hygiene','school','nothing']

# list of all keaywords, they are separated by categories for better visual orientation
# each line represents different category(add your own here & in func GiveKeyWordGetCategory()
# so they can be asigned to given category)
_keywords = ['rocket league','horizon zero dawn','games','gaming',
            'coding','code','testing code','programming',
            'lunch','breakfast','dinner','food','eating',
            'running','exercise','workout','walk','outside',
            'hygiene','shower',
            'studying','school','learning',
            'watching tv','watching twitch']

def GiveKeyWordGetCategory(word):
    if word in ['rocket league','horizon zero dawn','games','gaming']:
        return 'gaming'
    elif word in ['coding','code','testing code','programming']:
        return 'programming'
    elif word in ['lunch','breakfast','dinner','food','eating']:
        return 'food'
    elif word in ['running','exercise','workout','walk','outside']:
        return 'outside'
    elif word in ['hygiene','shower']:
        return 'hygiene'
    elif word in ['studying','school','learning']:
        return 'school'
    elif word in ['watching tv','watching twitch']:
        return 'nothing'
    else:
        return 'nothing'

class MyApp:
    """
    All variables needed by functions are saved in a class for easier manipulation
    since editting needs to be used by ex.: mainWindowViewTrigger & actStartedViewTrigger()
    """
    def __init__(self):
        # create a window
        self.root = tk.Tk()

        # variable for input text for name of activity
        self.inputValActName = tk.StringVar()
        self.dropboxVariable = tk.StringVar()
        

        self.fillerLabel = tk.Label(self.root,text='')
        self.inputLabel = tk.Label()
        self.lastAct = tk.Label(self.root,text='',font=('times',13,'bold'))
        self.runningTimeLabel = tk.Label(self.root,text='',font=('times',13,'bold'))
        self.runningAproxTime = None
        self.activityIsRunning = False

        self.inputEntry = tk.Entry()

        self.dropBoxCategory = tk.OptionMenu(self.root,self.dropboxVariable,*_categories)

        self.buttonStartStop = tk.Button()
        self.buttonLog = tk.Button()

        #when activity is running, press this to delete it
        #instead of adding it to log(basically -> don't log this)
        self.buttonDelAct = tk.Button() 

        self.timeStarted = None

    pass

def showLog():
    # go to filework module
    fw.openLog()
    pass

def timeSpent(start,end):

    # print("Time spent:",end - start)

    timeDiff = end - start
    ## this is kinda complex ##
    # tDifMod.timeAprox is class func from timeDifference module & it takes in dt.time struct
    #
    # When performing arithmetics [datetime.datetime - datetime.datetime] object returned
    # is datetime.timedelta BUT in timeDifference.py module it is to be compared to
    # datetime.time because thats how they are created manualy(look in __init__ @timeDIfference.py).
    #
    # Therefore timeDiff is datetime.timedelta it's value in seconds is sent to
    # convertSecondsToDT_Time() which simply converts seconds to hours & minutes & seconds
    # respectively AND returns datetime.time object. It is passed to timeAprox func where
    # it can be properly compared and it returns string with given value(see in timeDifference.py).
    timeDiffAproximation = tDifMod.timeAprox(convertSecondsToDT_Time(timeDiff.total_seconds()))

    return timeDiff,timeDiffAproximation

# ~~~~~~~~~~~~~~~~~~~~~ functions binds for specific keys ~~~~~~~~~~~~~~~~~~~~~ #
# ~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~ #
 
def return_key_pressed_on_input(event):
    if app.inputEntry.focus_get() != None: # if focus is on the window (not pressed enter randomly)
        actStartedViewTrigger() #as if "start-activity button was pressed"

def select_all_text_on_input(event):
    app.inputEntry.select_range(0,'end')
    app.inputEntry.icursor('end')

    #universal / general approach thanks to event variable
    # event.widget.select_range(0,'end')
    # event.widget.icursor('end')

def delete_ctr_backspace_on_input(event):
    ent = event.widget
    endIndx = ent.index(tk.INSERT)
    startIndx = ent.get().rfind(" ",None,endIndx)
    ent.select_range(startIndx,endIndx)

def ctrl_e_bring_focus_on_input(event):
    if app.inputEntry.focus_get() != None:
        app.inputEntry.focus()

def key_release_category_suggest(event):
    string = app.inputEntry.get()
    if string == None or string == '':
        return

    matched = [i for i in _keywords if string in i]
    if len(matched) == 1:
        app.dropboxVariable.set(GiveKeyWordGetCategory("".join(matched)))
    pass

# ~~~~~~~~~~~~~~~~~~~~~ popWindow on del press binds ~~~~~~~~~~~~~~~~~~~~~ #
def pop_window_confirm_yes(event):
    # print("pop_window_confirm_yes")
    ent = event.widget
    if ent.focus_get() != None:
        actDelete()
        ent.destroy()

def pop_window_confirm_no(event):
    # print("pop_window_confirm_no")
    ent = event.widget
    if ent.focus_get() != None:
        ent.destroy()
# ~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~ #


# call this at the beginning of the program to set up a window
def initWindowViewTrigger():

    app.root.title('TimeLogger')
    app.root.geometry(wXaxis + 'x' + wYaxis) #set window size ( in string format: '500x250')
    app.root.resizable(0, 0) #dont allow resizing of the window

    # create a label widget for text input
    app.inputLabel = tk.Label(app.root, text="Doing nothing", font=('times',13,'bold'))
    app.inputEntry = tk.Entry(app.root,textvariable = app.inputValActName,font=('times',15,'normal'),width=35,bd=3)

    #1BEE14 green
    #C4C4C4 light grey
    #9C9C9C dark grey
    #FF2929 light red
    #E20000 dark red

    # ---- INIT BUTTONS ---- #
    app.buttonStartStop = tk.Button(app.root, text="Start Activity",font=('times',13,'bold'),relief=tk.GROOVE,command=actStartedViewTrigger,pady=15,padx=15,bg='#C4C4C4',activebackground='#9C9C9C')
    app.buttonLog = tk.Button(app.root, text="Show Log",font=('times',13,'bold'),relief=tk.GROOVE,pady=15,padx=15,command=showLog,bg='#C4C4C4',activebackground='#9C9C9C')
    app.buttonDelAct = tk.Button(app.root,text="del",font=('times',13,'italic'),relief=tk.GROOVE,command=popupDeleteConfirm,bg="#C4C4C4",activebackground="#FF2929")

    # ---- PLACE WIDGETS IN THE WINDOW ---- #
    # put it up on the screen 
    app.inputLabel.grid(row=0,pady=5,sticky='ew')
    app.inputEntry.grid(row=1,padx=5)
    app.dropBoxCategory.grid(row=1,column=2)

    # app.buttonStartStop.grid(row=4,padx=10,pady=45,sticky='w')
    app.buttonStartStop.place(y=169,x=10)
    # app.buttonLog.grid(row=4) #didnt work for some reason, cant be padded to the side or negatively(left) 
    app.buttonLog.place(y=169,x=375) #y=169#x=375

    app.buttonDelAct.place(y=1,x=450)

# binds for text - easier use (select all, ctrl delete, enter press)
    app.inputEntry.bind("<Return>",return_key_pressed_on_input) #bind enter (return) to call same func as 'START' button
    app.inputEntry.bind("<Control-KeyRelease-a>",select_all_text_on_input)
    app.inputEntry.bind("<Control-BackSpace>",delete_ctr_backspace_on_input)
    app.inputEntry.bind("<KeyRelease>",key_release_category_suggest)

    app.root.bind("<Control-e>",ctrl_e_bring_focus_on_input)

    #delete BUTTON CONFIG
    app.buttonDelAct.config(state=tk.DISABLED)

#when del button is pressed popup confirm window
def popupDeleteConfirm():
    popWindow = tk.Toplevel()
    popLabel = tk.Label(popWindow,text='DELETE this activity?',font=('times',13,'bold'))
    popLabel.grid(row=0,pady=8,padx=12,columnspan = 2)

    popButtonYes = tk.Button(popWindow,text='Yes',font=('times',13,'bold'),bg='green',activebackground="green",padx=20,pady=10,command=actDelete)
    popButtonYes.grid(row=1,column=0)

    popButtonNo = tk.Button(popWindow,text='No',font=('times',13,'bold'),bg='red',activebackground="red",padx=20,pady=10,command=lambda e: e.widget.destroy())
    popButtonNo.grid(row=1,column=1)

    popWindow.bind("<Return>",pop_window_confirm_yes)

    popWindow.bind("<Escape>",pop_window_confirm_no)
    popWindow.bind("<FocusOut>",lambda e: e.widget.destroy())


# delete current activity, and DON'T log it
def actDelete():
    #config
    app.activityIsRunning = False
    app.inputEntry.config(state=tk.NORMAL)
    app.inputLabel.config(text='Doing nothing')
    app.buttonStartStop.config(text='Start Activity',command=actStartedViewTrigger)
        
    app.dropBoxCategory.config(state='normal')

    checkRunningTime()

    app.inputEntry.delete(0,tk.END) #delete text inside entry


def checkRunningTime():
    if app.activityIsRunning:
        # time is datetime.time object
        timeNow = dt.now()
        timeDelta = timeNow - app.timeStarted
        time = convertSecondsToDT_Time(timeDelta.total_seconds())
        tmp = tDifMod.timeAprox(time)
        if app.runningAproxTime != tmp or app.runningAproxTime == None:
            app.runningAproxTime = tmp
            app.runningTimeLabel.config(text='Started @%s | Running for %s'%(str(app.timeStarted)[10:-7],app.runningAproxTime))
        app.root.after(300000,checkRunningTime)# after 5 mins
    else:
        app.runningTimeLabel.config(text='')
        app.runningAproxTime = None

def actStartedViewTrigger(): #pressed START button

    #cant start activity with no name
    if(app.inputValActName.get() == ''):
        return

    app.timeStarted = dt.now()
    # print(app.timeStarted)

    # config
    app.activityIsRunning = True
    app.inputEntry.config(state=tk.DISABLED)
    app.inputLabel.config(text="%s" %app.inputValActName.get().upper())
    app.buttonStartStop.config(text='Stop Activity',command=defWindowViewTrigger)

    # place the label
    app.runningTimeLabel.place(y=100,x=10)
    
    app.dropBoxCategory.config(state='disabled')

    #invoke check if to show info about 'running activity'
    checkRunningTime()

    #delete BUTTON CONFIG
    app.buttonDelAct.config(state=tk.NORMAL)
    pass

def convertSecondsToDT_Time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return dtOG.time(int(hours),int(minutes),int(seconds))

def defWindowViewTrigger(): #pressed STOP button

    timeEnd = dt.now()

    #config
    app.activityIsRunning = False
    app.inputEntry.config(state=tk.NORMAL)
    app.inputLabel.config(text='Doing nothing')
    app.buttonStartStop.config(text='Start Activity',command=actStartedViewTrigger)
        
    app.lastAct.place(y=130,x=10)
    # print(dt.now())

    app.dropBoxCategory.config(state='normal')

    #invoke check for 'running' info text display or not
    checkRunningTime()

    #timeDiff == time spent;; timeDiffAproximation == string, compared time with predetermined values in timeDifference.py
    #check timeSpent func to see how timeDiffAproximation is calculated
    timeDiff,timeDiffAproximation = timeSpent(app.timeStarted,timeEnd)

    app.lastAct.config(text='Last: ' + app.inputValActName.get() + ' |' + str(timeEnd)[10:-7] + ' | ' + timeDiffAproximation)

    # log info
    fw.writeToLog(app.inputValActName.get(),app.timeStarted,timeEnd,timeDiff,dt.now(),app.dropboxVariable.get())

    app.inputEntry.delete(0,tk.END) #delete text inside entry

    #delete BUTTON CONFIG
    app.buttonDelAct.config(state=tk.DISABLED)
    pass


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        Config.handleConfig()

    else:            
        app = MyApp()
        tDifMod = td.TimeDifference()
        
        initWindowViewTrigger()

    # create a main loop (works until the program ends - close the window with X)
        app.root.mainloop()

else:
    print("nopee, this program has been run second hand, that won't fly here")
    exit(0)
