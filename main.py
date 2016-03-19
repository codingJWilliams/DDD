
#DDD
#19/03/16

#Program for text based game

from tkinter import *
from tkinter import messagebox
import datetime
import os
pathname = "usernames.txt"
window=Tk()
window.geometry("400x200")
window.title("DDD Login")
playerLocation = [1,1]

#=======================ARRAYS==========
currentLevelArray=[]
validCommandArray=["Forward","Back","Right","Left","Log"]
logArray=[]

#=======================Canvas'==========

#========Startup Canvas===
openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)

Label(openCanvas,text="Username").grid(row=0,column=0)

userNameEntry=Entry(openCanvas)
userNameEntry.grid(row=0,column=1)




#================================================================START OF FUNCTIONS========================    

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

def clearScreen():
    os.system("cls")
        
#Function that checks the user's credentials in database
def checkCredentials(event):

    #Gets the credentials from Entry
    userNameString=userNameEntry.get()

    content=getReadlines("usernames.txt")
    userNameArray=[]
    if content != None:
        for line in content:
            userNameArray.append(line)
            
        

    #If the userName is valid do this
    if userNameString in userNameArray:
        askMessage("Valid","User name valid")

        window.destroy()
        
        return userNameString

    #If the username is not recognised do this
    else:
        askError("Invalid","Unknown user")
        addToLog("Unknown User")
        if messagebox.askyesno("Unknown user.", "Create new user?"):
            with open(pathname, "a") as f:
                addToLog("Created new user")
                f.write("\n")
                f.write(userNameString)
                f.close()
#Function to get array from info from .txt file  
def getReadlines(pathname):
    try:
        file=open(pathname,"r")
    except:
        askError("Not Found","File Not Found")
        addToLog("File Not Found")
    else:
        content=file.readlines()
        newContent=[]
        for line in content:
            line=line.rstrip()
            newContent.append(line)
            
        file.close()
        return newContent
    

#Function to load a txt file into the current level array
def importLevel(fileName):


    #Read in line by line
    global currentLevelArray
    content=getReadlines(fileName)

    #Validation
    if content != None:
        currentLevelArray=[]
        for line in content:
            currentLevelArray.append(line)

    print(currentLevelArray)

        
#=============Initital setup funtions=========

#This function runs when enter key is pressed.
def checkUser(event):
    userName=checkCredentials("")

    #Only if userName is valid will the game launch
    if userName != None:
        addToLog("Starting new game")
        startNewGame(userName)
        

def viewLog():
    for item in logArray:
        print(item)


def addToLog(data):
    temp=""
    currentTime=str(datetime.datetime.now().time())
    temp+=currentTime
    temp+="  "
    temp+=data
    logArray.append(temp)
#================================================================END OF FUNCTIONS========================    


#============================ACTUAL GAME FUNCTION=============
"""
Start new game function
In future updates take argument to determine which level to load
"""



def startNewGame(playername):


    
    
    hp = 80

    #Initialises a class for the player
    currentPlayer=player()
    print(currentPlayer)

    #While loop that runs until the player is dead
    while hp > 0:
        print("==============STARTING NEW GAME==================")
        clearScreen()
        print(" You are at ({0}, {1}), and facing -->".format(playerLocation[0], playerLocation[1]))
        for line in currentLevelArray:
            print(line)
            
        print("\n"*21)
        cmd = input(">")

        #Converts input into capital
        cmd=cmd.capitalize()

        #Indexes The array to find a mathcing function
        matchCommandArray=[player.moveForward,player.moveBack,player.turnRight,player.turnLeft,viewLog]
        if cmd in validCommandArray:
            
            position=validCommandArray.index(cmd)
            
            match=matchCommandArray[position]

            #Trys to run the function
            try:
                match()
            except:
                print("Error starting command")

        #If the command is not found tell the user       
        else:
            print("Invalid Command")
        
#=============Initital setup funtions=========



#====================================================================CLASSES==========================

class player:

    def moveForward():

        playerLocation[0] = playerLocation[0] + 1
        print("Moved Forward")
        addToLog("Moved Forward")

    def moveBack():
        print("Moved Backwards")
        addToLog("Moved Back")

    def turnRight():
        print("Turned Right")
        addToLog("Turned Right")

    def turnLeft():
        print("Turned Left")
        addToLog("Turned Left")

        
#=============RETURN FUNCTIONS=======
importLevel("level 1.txt")
    

#=============BINDINGS============
userNameEntry.bind("<Return>",checkUser)

window.mainloop()
