
#DDD
#19/03/16

from tkinter import *

window=Tk()
window.geometry("400x200")
window.title("DDD")

#=======================Canvas'==========

#========Startup Canvas===
openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)

Label(openCanvas,text="Username").grid(row=0,column=0)

userNameEntry=Entry(openCanvas)
userNameEntry.grid(row=0,column=1)



#=======================FUNCTIONS=============

#Function that checks the user's credentials
def checkCredentials(event):

    #Gets the credentials from Entry
    userNameString=userNameEntry.get()
    


#=============BINDINGS============
userNameEntry.bind("<Enter>",checkCredentials)

window.mainloop()
