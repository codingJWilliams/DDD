
#DDD
#19/03/16

from tkinter import *

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

#Function that checks the user's credentials
def checkCredentials(event):

    #Gets the credentials from Entry
    userNameString=userNameEntry.get()
    print(userNameString)

    #Add Json Stuff Here


    #Destroys Window Here (Uncomment when ready)
    
    #window.destroy()
    

#Function that 
def startNewGame():
    pass

    
    

#=============BINDINGS============
userNameEntry.bind("<Return>",checkCredentials)

window.mainloop()
