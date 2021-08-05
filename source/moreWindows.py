import tkinter as tk

################################################################################

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
    displayed = False

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

################################################################################

if __name__ == "__main__":
  print("cant run as main")
  pass