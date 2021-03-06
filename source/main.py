#!/usr/bin/python3
import datetime as dtOG
import os
import string
import sys
import tkinter as tk
from datetime import datetime as dt
from PIL import Image, ImageTk

import config as Config
import filework as fw
import timeDifference as td
from timeControl import DateTimeConvertor as dtc
from storage import  _categories_keywords
from moreWindows import SettingsMenu, ManualMenu

# window size
wXaxis = '500'
wYaxis = '270'

#### **** COLORS **** ####
#d9d9d9 app-background
#1BEE14 green (in del button)
#C4C4C4 light grey (button default)
#9C9C9C dark grey (button when hovered over)
#FF2929 light red (in del button)
#E20000 dark red (in del button)

class MyApp:
    """
    All variables needed by functions are saved in a class for easier manipulation
    since editting needs to be used by ex.: mainWindowViewTrigger & actStartedViewTrigger()
    """
    def __init__(self):
        # create a window
        self.root = tk.Tk()

        self.popWindow = None #for DEL pop-up window

        ######### ######### TIMES ######### #########
        self.timeStarted = None
        self.timeEnded = None

        ######### ######### STRING VARS ######### #########    
        self.inputValActName = tk.StringVar() #input text var for name of activity
        self.dropboxVariable = tk.StringVar() #categories

        ######### ######### BUTTONS ######### #########
        self.buttonStartStop = tk.Button()
        self.buttonLog = tk.Button()
        self.buttonHitherto = tk.Button()
        self.buttonSettings = tk.Button()
        self.buttonManualLog = tk.Button()

        #when activity is running, press this to delete it
        #instead of adding it to log(basically -> don't log this)
        self.buttonDelAct = tk.Button() 


        ######### ######### LABELS ######### #########
        # self.fillerLabel = tk.Label(self.root,text='')
        self.inputLabel = tk.Label()
        self.lastAct = tk.Label(self.root,text='',font=('times',13,'bold'),justify=tk.LEFT,wraplength=480)
        self.runningTimeLabel = tk.Label(self.root,text='',font=('times',13,'bold'))

        ######### ######### OTHER ######### #########
        self.runningAproxTime = None
        #for interval checkup & display of how long act is running for
        self.activityIsRunning = False

        self.delWindIsAct = False

        self.inputEntry = tk.Entry()

        self.dropBoxCategory = tk.OptionMenu(self.root,self.dropboxVariable,
                                                *_categories_keywords.keys())

        self.breakCheck = tk.Label()
        self.breakCheck_var = tk.BooleanVar() #value for checkbutton (0/1 -> if is selected or not)
    pass
# END OF class MyApp ###########################################################

####
# inspiration
# https://stackoverflow.com/questions/3221956/how-do-i-display-tooltips-in-tkinter?noredirect=1&lq=1
####
class ToolTip:
    """Class for pop up windows (tip window when hovered over a button)"""

    def __init__(self, widget, text='todo: add widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None #for 'after' methods
        self.tw = None #topLevel Window
    
    def enter(self,event=None): #inbetween func coz of event
        self.schedule()

    def leave(self,event=None):
        self.unschedule()
        self.hideTip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime,self.showTip)
    
    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showTip(self,event=None):
        x = y = 0
        x,y,xx,yy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        #create toplevel window
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
            background="#ffffff", relief='solid', borderwidth=1,
            wraplength = self.wraplength)
        label.pack(ipadx=1)
        
    def hideTip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()
# END OF CLASS ToolTip #########################################################

##### WANT TO ADD CATEGORIES / KEYWORDS ? --> go to storage.py
def GiveKeyWordGetCategory(word):
    # person can write 2-word activity with '_' but they are registered with ' '
    word = word.replace("_"," ")

    for key in _categories_keywords:
        if word in _categories_keywords[key]:
            return key

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
    # list of lists returned, as .values is a list for each category
    matched = [i for i in _categories_keywords.values() if string in i]
    if matched:
        #matched is a list of lists so just pick the first value and pass it
        app.dropboxVariable.set(GiveKeyWordGetCategory("".join(matched[0][0])))

# ~~~~~~~~~~~~~~~~~~~~~ popWindow on del press binds ~~~~~~~~~~~~~~~~~~~~~ #
def pop_window_confirm_yes(event):
    try:
        ent = event.widget
        if ent.focus_get() != None:
            actDelete()
            ent.destroy()
            app.delWindIsAct = False
    except:
        actDelete()
        event.destroy()
        app.delWindIsAct = False

def pop_window_confirm_no(event):
    try:
        ent = event.widget
        if ent.focus_get() != None:
            ent.destroy()
            app.delWindIsAct = False
    except:
        event.destroy() #cheat, when event is the widget itself (because of what calls this func)
        app.delWindIsAct = False

def btn_startstop_return_press(event):
    if app.activityIsRunning:
        defWindowViewTrigger()
    else:
        actStartedViewTrigger()

# ~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~ #

# call this at the beginning of the program to set up a window
def initWindowViewTrigger():

    app.root.title('TimeLogger')
    app.root.geometry(wXaxis + 'x' + wYaxis) #set window size ( in string format: '500x250')
    app.root.resizable(0, 0) #dont allow resizing of the window

    # create a label widget for text input
    app.inputLabel = tk.Label(app.root, text="Write your activity here!", font=('American Typewriter',13,'bold'))
    app.inputEntry = tk.Entry(app.root,textvariable = app.inputValActName,font=('times',15,'normal'),width=35,bd=3)
    
    # ---- INIT PHOTOS ---- #
    #using make to run the app, cwd is the root dir (not subdir 'source' where main.py is located)
    imSettings = Image.open(os.getcwd()+"/image/settings_button2.png")
    imSettings = imSettings.resize((26,26),Image.ANTIALIAS)
    phSettings = ImageTk.PhotoImage(imSettings)
    
    imManualHand = Image.open(os.getcwd()+"/image/manual_hand.png")
    imManualHand = imManualHand.resize((26,26),Image.ANTIALIAS)
    phManualHand = ImageTk.PhotoImage(imManualHand)

    imBreakCheck_off = Image.open(os.getcwd()+"/image/outter_circle_2.png")
    imBreakCheck_off = imBreakCheck_off.resize((24,24),Image.ANTIALIAS)
    phBreakCheck_off = ImageTk.PhotoImage(imBreakCheck_off)

    imBreakCheck_on = Image.open(os.getcwd()+"/image/full_circle.png")
    imBreakCheck_on = imBreakCheck_on.resize((24,24),Image.ANTIALIAS)
    phBreakCheck_on = ImageTk.PhotoImage(imBreakCheck_on)

    # ---- INIT BUTTONS ---- #
    app.buttonStartStop = tk.Button(app.root, text="Start Activity",font=('times',13,'bold'),relief=tk.GROOVE,command=actStartedViewTrigger,pady=15,padx=15,bg='#C4C4C4',activebackground='#9C9C9C')
    app.buttonLog = tk.Button(app.root, text="Show Log",font=('times',13,'bold'),relief=tk.GROOVE,pady=15,padx=15,command=showLog,bg='#C4C4C4',activebackground='#9C9C9C')
    app.buttonDelAct = tk.Button(app.root,text="del",font=('times',13,'italic'),relief=tk.GROOVE,command=popupDeleteConfirm,bg="#C4C4C4",activebackground="#FF2929")
    app.buttonHitherto = tk.Button(app.root,text="Hitherto",font=('American Typewriter',9,'bold'),command=logInstant,bg='#C4C4C4',activebackground='#9C9C9C',state=tk.DISABLED)

    app.buttonSettings = tk.Button(app.root,image=phSettings,bg='#C4C4C4',activebackground='#9C9C9C')
    app.buttonSettings.image = phSettings #this line is neeeded for the picture to actually show up

    app.buttonManualLog = tk.Button(app.root,image=phManualHand,bg='#C4C4C4',activebackground='#9C9C9C')
    app.buttonManualLog.image = phManualHand



    app.breakCheck = tk.Checkbutton(app.root,image=phBreakCheck_off,selectimage=phBreakCheck_on,
        indicatoron=False,text="Breaks",compound="left",font=('American Typewriter',11,'bold'),
        borderwidth=0,selectcolor='#d9d9d9',onvalue=True,offvalue=False,
        variable=app.breakCheck_var,command=optionBreaksPress)
    #ATTENTION - IMPORTANT -- this always needs to be added for some reason separately -- picture doesnt show up without these lines
    app.breakCheck.image = phBreakCheck_off #this line is neeeded for the picture to actually show up
    app.breakCheck.selectimage = phBreakCheck_on #this line is neeeded for the picture to actually show up

    # ---- PLACE WIDGETS IN THE WINDOW ---- #
    # put it up on the screen 
    app.inputLabel.grid(row=0,pady=5,padx=10,sticky='ew')
    app.inputEntry.grid(row=1,padx=5)
    app.dropBoxCategory.grid(row=1,column=2)

    app.buttonDelAct.place(y=1,x=450)

    app.buttonStartStop.place(y=200,x=10)
    app.buttonLog.place(y=200,x=375)

    app.buttonHitherto.place(y=170,x=10)
    app.buttonSettings.place(y=1,x=418)

    app.buttonManualLog.place(y=1,x=1)

    app.breakCheck.place(y=80,x=400)

    # ---- BIND KEYS AND CLICKS ---- #
# binds for text - easier use (select all, ctrl delete, enter press)
    app.inputEntry.bind("<Return>",return_key_pressed_on_input) #bind enter (return) to call same func as 'START' button
    app.inputEntry.bind("<Control-KeyRelease-a>",select_all_text_on_input)
    app.inputEntry.bind("<Control-BackSpace>",delete_ctr_backspace_on_input)
    app.inputEntry.bind("<KeyRelease>",key_release_category_suggest)

    app.root.bind("<Control-e>",ctrl_e_bring_focus_on_input)
    app.root.bind("<Configure>",main_window_moving)

    app.buttonStartStop.bind("<Return>",btn_startstop_return_press)

    #delete BUTTON CONFIG
    app.buttonDelAct.config(state=tk.DISABLED)

    ### ----- pop up tip window text setup for buttons ----- ###
    settings_tip = ToolTip(app.buttonSettings,  "Open settings window") 
    deleteAct_tip = ToolTip(app.buttonDelAct,   "Delete current running activity & don't log it")
    hitherto_tip = ToolTip(app.buttonHitherto,  "Use when you want to instantly log activity starting from the end of the last activity until now")
    manuallog_tip = ToolTip(app.buttonManualLog,"Manually log an activity")
    optBreakCheck_tip = ToolTip(app.breakCheck, "When enabled, alerts when certain time has passed (like: It's time for a break)")


    # SettingsMenu(app.buttonSettings) #popup window on click
    ManualMenu(app.buttonManualLog,app.root) #popup window on click
    # optionBreaksPress() might need to call this to inicialize the timer or 
    # something depending on how i implement it
    
#END OF initWindowViewTrigger ##################################################

def optionBreaksPress():
    if app.breakCheck_var.get(): #if value is selected -> apply break system
        pass
    else: #stop break system a restart timer
        pass
    pass

def logInstant():
  
    #activity has not been done before, therefore app.TimeStarted & timeEnded is not set yet!
    if app.timeEnded == None:
        try:
            print("Warning - Hitherto works only if an activity has already been done previously to this")
        except:
            pass
        app.inputValActName.set("You have to do an activity previously")
        app.inputLabel.config(text="failed hitherto")

    #activty has been done before, therefore just set app.timeStarted and trigger 'stop' button
    else:

        #TODO add manual starting time, if not set, use this instead (end of last +1 sec)
        app.timeEnded = dtc.addTdelta(app.timeEnded,dtOG.timedelta(seconds=1))
        app.timeStarted = app.timeEnded #act started should be last act ended +1 sec
        #stop button was pressed

        defWindowViewTrigger()

def main_window_moving(e):
    print("moving main window")
    pw = app.popWindow #if this is not done, it closes parent as well :shrug:
    app.popWindow = None

    if pw:
        pw.destroy()

#when del button is pressed popup confirm window appears!
def popupDeleteConfirm():
    if  app.popWindow is None:
        x=app.root.winfo_rootx()
        y=app.root.winfo_rooty()

        app.popWindow = tk.Toplevel(highlightbackground='black',highlightthickness=3)
        app.popWindow.wm_overrideredirect(True) # if this is here, window doesnt behave like a window
        app.popWindow.geometry("+%d+%d" %(x+285,y))

        # popWindow.wm_attributes('-type','splash')

        popLabel = tk.Label(app.popWindow,text='Sure?',font=('times',13,'bold'))
        popLabel.grid(row=0,pady=8,padx=12,columnspan = 2)

        popButtonYes = tk.Button(app.popWindow,text='Yes',font=('times',13,'bold'),
            bg='green',activebackground="green",padx=20,pady=10,command=lambda: pop_window_confirm_yes(app.popWindow))

        popButtonYes.grid(row=1,column=0)

        popButtonNo = tk.Button(app.popWindow,text='No',font=('times',13,'bold'),bg='red',
            activebackground="red",padx=20,pady=10,command=lambda: pop_window_confirm_no(app.popWindow))

        popButtonNo.grid(row=1,column=1)

        ####does nothing because of overrideredict()
        # popWindow.bind("<Return>",pop_window_confirm_yes)
        # popWindow.bind("<Escape>",pop_window_confirm_no)
        # popWindow.bind("<FocusOut>",lambda e: popWindow.destroy())

# delete current activity, and DON'T log it
def actDelete():
    #config
    app.activityIsRunning = False
    app.inputEntry.config(state=tk.NORMAL)
    app.inputLabel.config(text='Doing nothing')
    app.buttonStartStop.config(text='Start Activity',command=actStartedViewTrigger)
        
    app.buttonDelAct.config(state=tk.DISABLED)
    # app.dropBoxCategory.config(state='normal')

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
            app.runningTimeLabel.config(text='Started %s | Running for %s'%(str(app.timeStarted)[10:-7],app.runningAproxTime))
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

    app.buttonHitherto.config(state=tk.DISABLED)


    # place the label
    app.runningTimeLabel.place(y=100,x=10)
    
    # app.dropBoxCategory.config(state='disabled')

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
    app.timeEnded = timeEnd #added because of Hitherto button

    #config
    app.activityIsRunning = False
    app.inputEntry.config(state=tk.NORMAL)
    app.inputLabel.config(text='Doing nothing')
    app.buttonStartStop.config(text='Start Activity',command=actStartedViewTrigger)
        
    app.lastAct.place(y=130,x=10)
    # print(dt.now())

    # app.dropBoxCategory.config(state='normal')

    #invoke check for 'running' info text display or not
    checkRunningTime()

    #timeDiff == time spent;; timeDiffAproximation == string, compared time with 
    # predetermined values in timeDifference.py
    #check timeSpent func to see how timeDiffAproximation is calculated
    timeDiff,timeDiffAproximation = timeSpent(app.timeStarted,timeEnd)

    app.lastAct.config(text='Last: ' + app.inputValActName.get() + ' |' + \
        str(timeEnd)[10:-7] + ' | ' + "elapsed: "+str(timeDiff)[:-7])

    # log info
    fw.writeToLog(app.inputValActName.get(),app.timeStarted,timeEnd,timeDiff,
        dt.now(),app.dropboxVariable.get())

    app.inputEntry.delete(0,tk.END) #delete text inside entry

    #delete BUTTON CONFIG
    app.buttonDelAct.config(state=tk.DISABLED)
    app.buttonHitherto.config(state=tk.ACTIVE)
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
