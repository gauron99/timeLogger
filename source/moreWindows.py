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
    x = y = 0
    x,y,xx,yy = self.widget.bbox("insert")

    x += self.widget.winfo_rootx() + 25
    y += self.widget.winfo_rooty() + 25
    
    self.tl = tk.Toplevel(self.widget)
    self.tl.wm_overrideredirect(True)
    self.tl.wm_geometry("+%d+%d" % (x, y))
    
    name_label = tk.Label(self.tl,text="Name:",justify='left',font=('American Typewriter',12,'bold'))
    name_label.grid(row=0,column=0)

  def hideMenu(self):
    tl = self.tl
    self.tl = None
    tl.destroy()
    pass

################################################################################

if __name__ == "__main__":
  print("cant run as main")
  pass