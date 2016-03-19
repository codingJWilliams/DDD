
#DDD
#19/03/16

from tkinter import *

window=Tk()
window.geometry("400x200")
#=======================Canvas'==========

#========Startup Canvas===
openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)

Label(openCanvas,text="Username").grid(row=0,column=0)
Label(openCanvas,text="Password").grid(row=1,column=0)

userNameEntry=Entry(openCanvas)
userNameEntry.grid(row=0,column=1)

passwordEntry=Entry(openCanvas,show="*")
passwordEntry.grid(row=1,column=1)

window.mainloop()
