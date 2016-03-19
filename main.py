
#DDD
#19/03/16

#Program for text based game

from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("400x200")
window.title("DDD Login")

#=======================Canvas'==========

#========Startup Canvas===
openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)

Label(openCanvas,text="Username").grid(row=0,column=0)

userNameEntry=Entry(openCanvas)
userNameEntry.grid(row=0,column=1)



#=======================FUNCTIONS=============

def askMessage(pre,message):
    try:
        messagebox.showinfo(pre,message)
    except:
        print(messsage)

def askError(pre,message):
    try:
        messagebox.showerror(pre,message)
    except:
        print(message)
#Function that checks the user's credentials
def checkCredentials(event):

    #Gets the credentials from Entry
    userNameString=userNameEntry.get()

    validUsers=["Angus","Bob","Joe"]

    #If the userName is valid do this
    if userNameString in validUsers:
        askMessage("Valid","User name valid")

        #window.destroy()

    #If the username is not recognised do this
    else:
        askError("Invalid","Unknown user")
            
    
    

"""
Start new game function
In future updates take argument to determine which level to load
"""
def startNewGame():
    pass

    
    

#=============BINDINGS============
userNameEntry.bind("<Return>",checkCredentials)

window.mainloop()
