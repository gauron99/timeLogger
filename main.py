#!/usr/bin/python3
import os, sys
import tkinter as tk
from datetime import datetime as dt
import config as Config
# import timeDifference

# window size
wXaxis = '500'
wYaxis = '250'
#  --------------- states --------------- #
#state when app is run
APP_DEFAULT_STATE = 0
#when 'buttonStartStop' button is pressed
APP_ACTIVE_RUNNING_STATE = 1
#  --------------- states --------------- #

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
        
        self.fillerLabel = tk.Label(self.root,text='')
        self.inputLabel = tk.Label()
        self.lastAct = tk.Label(self.root,text='',font=('times',13,'bold'))
        
        self.inputEntry = tk.Entry()

        self.buttonStartStop = tk.Button()
        self.buttonLog = tk.Button()
        
        self.timeStarted = None

    pass

#most likely gonna be in different module
def showLog():
    pass

def timeSpent(start,end):
    #TODO
    # if(end < start): #if time went over 00:00
    #     tmp = dt.today().replace(hour=23,minute=59,second=59,microsecond=999999)
    #     timeDiff = tmp-(start-end)
    # else:
    timeDiff = end - start

    print(timeDiff)
    #use timeDifference.py module
    return timeDiff


def return_key_pressed_on_input(event):
    if app.inputEntry.focus_get() != None: # if focus is on the window (not pressed enter randomly)
        actStartedViewTrigger() #as if "start-activity button was pressed"

# call this at the beginning of the program to set up a window
def initWindowViewTrigger():

    app.root.title('TimeLogger')
    app.root.geometry(wXaxis + 'x' + wYaxis) #set window size ( in string format: '500x250')
    app.root.resizable(0, 0) #dont allow resizing of the window

    # create a label widget for text input
    app.inputLabel = tk.Label(app.root, text="State: Nothing is running", font=('times',13,'bold'))
    app.inputEntry = tk.Entry(app.root,textvariable = app.inputValActName,font=('times',15,'normal'),width=48,bd=3)

    #1BEE14 green
    #C4C4C4 light grey
    #9C9C9C dark grey
    app.buttonStartStop = tk.Button(app.root, text="Start Activity",font=('times',13,'bold'),relief=tk.GROOVE,command=actStartedViewTrigger,pady=15,padx=15,bg='#C4C4C4',activebackground='#9C9C9C')
    app.buttonLog = tk.Button(app.root, text="Show Log",font=('times',13,'bold'),relief=tk.GROOVE,pady=15,padx=15,command=showLog,bg='#C4C4C4',activebackground='#9C9C9C')

    # put it up on the screen 
    app.inputLabel.grid(row=0,pady=5,sticky='ew')
    app.inputEntry.grid(row=1,padx=5)

    app.fillerLabel.grid(row=2,pady=20)

    # app.buttonStartStop.grid(row=4,padx=10,pady=45,sticky='w')
    app.buttonStartStop.place(y=169,x=10)
    # app.buttonLog.grid(row=4) #didnt work for some reason, cant be padded to the side or negatively(left) 
    app.buttonLog.place(y=169,x=375) #y=169#x=375

    app.inputEntry.bind("<Return>",return_key_pressed_on_input) #bind enter (return) to call same func as 'START button


def actStartedViewTrigger(): #pressed START button

    app.timeStarted = dt.now()
    # print(app.timeStarted)

    # config
    app.inputEntry.config(state=tk.DISABLED)
    app.inputLabel.config(text="State: Currently Running")
    app.buttonStartStop.config(text='Stop Activity',command=defWindowViewTrigger)

    pass

def defWindowViewTrigger(): #pressed STOP button

    timeEnd = dt.now()
    #config
    app.inputEntry.config(state=tk.NORMAL)
    app.inputLabel.config(text='State: Nothing is running')
    app.buttonStartStop.config(text='Start Activity',command=actStartedViewTrigger)
        
    app.lastAct.place(y=100,x=10)
    # print(dt.now())

    timeDiff = timeSpent(app.timeStarted,timeEnd)
    app.lastAct.config(text='Last: '+app.inputValActName.get()+' | ' + str(timeEnd)[:-5])


    # TODO call log info func here

    app.inputEntry.delete(0,tk.END) #delete text inside entry
    pass


if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        Config.handleConfig()

    else:            
        app = MyApp()
        initWindowViewTrigger()

    # create a main loop (works until the program ends - close the window with X)
        app.root.mainloop()

else:
    print("nopee, this program has been run second hand, that won't fly here")
    exit(0)