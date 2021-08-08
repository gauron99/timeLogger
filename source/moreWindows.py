import tkinter as tk

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

class ManualMenu:
  def __init__(self,widget):
    self.widget = widget
    self.displayed = False
    self.tl = None
    self.widget.bind('<Button-1>',self.onclick)
    
    

    self.labels = []
    self.inputs = None

    pass

  def onclick(self,event=None):
    if self.displayed:
      self.displayed = False
      self.hideMenu()
    else:
      self.displayed = True
      self.showMenu()
    pass

  def loadRows(self,widget,labels):
    inputs = {}

    for text in self.labels:
      row = tk.Frame(widget)

      label = tk.Label(row,text=text+":",width=10,anchor='w',font=('American Typewriter',12,'bold'))
      entry = tk.Entry(row)

      row.pack(side=tk.TOP, padx=2, pady=1)
      label.pack(side=tk.LEFT)
      entry.pack(side=tk.RIGHT,fill=tk.X)
      

    return inputs

  def showMenu(self):
    x = y = 0
    x,y,xx,yy = self.widget.bbox("insert")

    x += self.widget.winfo_rootx() + 25
    y += self.widget.winfo_rooty() + 25
    
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
    self.labels = ['Name','from','to','Category']
    self.inputs = self.loadRows(self.tl,self.labels)
  

  def hideMenu(self,e=None):
    self.widget.master.focus_get()
    tl = self.tl
    self.tl = None
    if tl:
      tl.destroy()
    pass

################################################################################

if __name__ == "__main__":
  print("cant run as main")
  pass