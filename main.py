#!/usr/bin/python3
import os
import tkinter as tk

# window size
wXaxis = '500'
wYaxis = '250'

APP_DEFAULT_STATE = 0
APP_ACTIVE_RUNNING_STATE = 1

class MyApp():
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
        self.inputEntry = tk.Entry()
        self.buttonStart = tk.Button()
        self.buttonLog = tk.Button()

        self.state = APP_DEFAULT_STATE
    pass

def key_pressed(event):
    if app.inputEntry.focus_get() != None:
        actStartedViewTrigger() #as if "start-activity button was pressed"

# call this at the beginning of the program to set up a window
def initWindowViewTrigger():

    app.root.title('TimeLogger')
    app.root.geometry(wXaxis + 'x' + wYaxis) #set window size ( in string format: '500x250')
    app.root.resizable(0, 0) #dont allow resizing of the window

    # create a label widget for text input
    app.inputLabel = tk.Label(app.root, text="Write your activity here", font=('times',13,'bold'))
    app.inputEntry = tk.Entry(app.root,textvariable = app.inputValActName,font=('times',15,'normal'),width=48,bd=3)

    #1BEE14 green
    #C4C4C4 light grey
    #9C9C9C dark grey
    app.buttonStart = tk.Button(app.root, text="Start Activity",font=('times',13,'bold'),relief=tk.GROOVE,command=actStartedViewTrigger,pady=15,padx=15,bg='#C4C4C4',activebackground='#9C9C9C')
    app.buttonLog = tk.Button(app.root, text="Show Log",font=('times',13,'bold'),relief=tk.GROOVE,pady=15,padx=15)

    # put it up on the screen 
    app.inputLabel.grid(row=0,pady=5,sticky='ew')
    app.inputEntry.grid(row=1,padx=5)

    app.fillerLabel.grid(row=2,pady=20)

    app.buttonStart.grid(row=4,padx=10,pady=45,sticky='w')
    app.buttonLog.grid(row=4)

    app.inputEntry.bind("<Return>",key_pressed)

def actStartedViewTrigger():
    if app.state == APP_ACTIVE_RUNNING_STATE: #if is already running
        return
    # config
    inputVal = app.inputValActName.get()
    app.inputEntry.config(state=tk.DISABLED,bd=0)
    app.inputLabel.config(text="Currently Running")
    pass


if __name__ == "__main__":
    
    app = MyApp()

    initWindowViewTrigger()

# create a main loop (works until the program ends - close the window with X)
    app.root.mainloop()
else:
    print("nopee, this program has been run second hand, that wont fly here")
    exit(0)