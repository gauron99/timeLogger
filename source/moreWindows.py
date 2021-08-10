import datetime as dt
import tkinter as tk

import filework as fw
import timeControl as tc

################################################################################

#### maybe init the values which are gonna be in the "menu" so if user closes
# they are kept?
#### buttons --> update & discard ?
# need app class for settings window info so user knows whats the current setup !!!


# |------------------------| 
# |     Settings Menu      | 
# |------------------------| 
# | config file: ________  | 
# | log file:    ________  | 
# |                        | 
# |                        | 
# |                        | 
# |                        | 
# |                        | 
# |                        | 
# |                        | 
# |                        | 
# |                        | 
# |                        | 
# |  UPDATE       DISCARD  | 
# |------------------------| 

# no need for such class in manual log, its gonna be just values to add and log
# its gonna calculate time spent

# |------------------------| 
# |      Manual Log        | 
# |------------------------| 
# |  name:       ________  | 
# |  from:       ________  | 
# |  to:         ________  | 
# |  category:   ________  | 
# |                        | 
# |                        | 
# |                        | 
# |                        | 
# |  WRITE        DISCARD  | 
# |------------------------| 



class SettingsMenu:
  def __init__(self,widget):
      self.widget = widget
      self.displayed = False
      
      self.widget.bind('<Button-1>',self.onclick)

      pass

  def onclick(self,event=None):
    if self.displayed:
      self.displayed = False
      self.hideMenu()
    else:
      self.displayed = True
      self.showMenu()
    pass

  def showMenu(self):
    pass

  def hideMenu(self):
    pass

################################################################################
_manual_log_inputs = {} #to remember entries

class ManualMenu:
  def __init__(self,widget,parent):
    self.widget = widget
    self.parent = parent

    self.displayed = False
    self.tl = None
    self.widget.bind('<Button-1>',self.onclick)
    self.parent.bind("<Configure>",self.sync_with_parent)

    self.labels = ['Name','from','to','Category']

    self.inner_inputs = {}
    for x in self.labels:
      self.inner_inputs[x] = ''

  def sync_with_parent(self,e=None):
    if self.tl:
      x = self.parent.winfo_x() + 26
      y = self.parent.winfo_y() + 26
      self.tl.geometry("+%d+%d" % (x,y))

  def onclick(self,event=None):
    if self.displayed:
      self.displayed = False
      self.hideMenu()
    else:
      self.displayed = True
      self.showMenu()
    pass

  def loadRows(self):

    for text in self.labels:
      row = tk.Frame(self.tl)

      label = tk.Label(row,text=text+":",width=10,anchor='w',font=('American Typewriter',12,'bold'))
      # tv = text.lower()+'_entry'
      entry = tk.Entry(row,font=('American Typewriter',12))#,textvariable=tv)

      row.pack(side=tk.TOP, padx=2, pady=1)
      label.pack(side=tk.LEFT)
      entry.pack(side=tk.RIGHT,fill=tk.X)

      #insert into entry
      try:
        entry.insert(0,_manual_log_inputs[text])
      except:
        entry.insert(0,'')
      finally:
        self.inner_inputs[text] = entry

  def showMenu(self):
    x = y = 0
    
    # x,y,xx,yy = self.widget.bbox("insert")
    # x += self.widget.winfo_rootx() + 25
    # y += self.widget.winfo_rooty() + 25

    x = self.parent.winfo_x() + 26 #is offset from root window because sync between windows is easier this way
    y = self.parent.winfo_y() + 26
    
    self.tl = tk.Toplevel(self.widget,highlightbackground='black',highlightthickness=3)
    self.tl.wm_overrideredirect(True)
    self.tl.wm_geometry("+%d+%d" % (x, y))
    
    ###   Key catches don't work with wm_overrideredirect(True)    ### 
     ## Therefore the window can only be opened/closed with button ## 
    # <FocusOut> doesnt work with wm_overrideredirect(True)
    # self.tl.bind("<Escape>", self.hideMenu)
    # self.tl.bind('<FocusOut>',self.hideMenu) 
 
    main_label = tk.Label(self.tl,text="Manual Log",font=('American Typewriter',13,'bold'))
    main_label.pack(side=tk.TOP)
    
    # load lines to widget
    self.loadRows()

    #get focus for first entry
    self.inner_inputs['Name'].focus()

    write_button = tk.Button(self.tl, text='Write', font=('American Typewriter',
    13,'bold'),highlightbackground='black',highlightthickness=1,fg='green',
    activebackground='green', command=self.write)

    write_button.pack(side=tk.LEFT,padx=2,pady=2)

    discard_button = tk.Button(self.tl, text='Discard', font=('American Typewriter'
    ,13,'bold'), highlightbackground='black',highlightthickness=1,fg='red',
    activebackground='red', command=self.discard)  

    discard_button.pack(side=tk.RIGHT,padx=2,pady=2)

  def hideMenu(self,e=None):
    self.widget.master.focus() #does this do anything? TODO DEBUG

    #save text written in entries
    for key in self.inner_inputs:
      _manual_log_inputs[key] = self.inner_inputs[key].get()

    tl = self.tl
    self.tl = None
    if tl:
      tl.destroy()
    pass
    
  def formatDateTime(self,data : str):
    """
    Give string, check if is of valid datetime format, return datetime object\n
    > Uses timeControl.py module for conversion of string to datetime
    > All data has to be provided in numbers
    >>> Year with century as a decimal number -- (2014, 1987 ...)\n
    >>> Month as a zero-padded decimal number -- (01, ..., 12)\n
    >>> Day of the month as a zero-padded decimal -- (01, ..., 31)\n
    >>> Hour \n
    >>> Minute \n
    >>> Second \n
    """
    passed = False
    
    data = data.strip()
    
    # sequence of try-except to try to convert - if one is success, return
    #   
    pass


  def write(self):
    now = dt.datetime.now()
# activity -> (string) name of activity
# tBegin -> (datetime) beginning of activity
# tEnd -> (datetime) end of activity
# tDiff -> () how long has the activity been running for
# tNow -> (datetime) time of log (NOW)
# category -> (string) name of category
    
#   info taken from __init__ --> self.labels = ['Name','from','to','Category']

    begin = self.formatDateTime(self.labels['from'])
    end = self.formatDateTime(self.labels['to'])

    spent = end - begin

    print(now,self.labels['Name'],spent,begin,end,self.labels['Category'])
    fw.writeToLog()
    pass

  def discard(self):
    #empty the entries
    _manual_log_inputs.clear()

    #update entries
    for x in self.inner_inputs:
      self.inner_inputs[x].delete(0,tk.END)

################################################################################

if __name__ == "__main__":
  print("cant run as main")
  pass
