
#Health Tracker Beta
#Angus Goody

from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("300x200")
window.title("Health Tracker")

mainMenu=Menu(window)
window.config(menu=mainMenu)

#===========================MENUS=================
fileMenu=Menu(mainMenu)

#==========================CANVAS'=================

#====STARTUP CANVAS
openCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
openCanvas.pack(expand=True)

#====Login CANVAS====
loginCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

Label(loginCanvas,text="Username: ").grid(row=0,column=0)

userNameEntry=Entry(loginCanvas,justify=CENTER)
userNameEntry.grid(row=0,column=1,padx=5)

#===View Canvas=====

viewCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)
showNameVar=StringVar()

showInfoFrame=Frame(viewCanvas)
showInfoFrame.pack()

Label(showInfoFrame,text="Name:            ",justify=LEFT).grid(row=0,column=0)
Label(showInfoFrame,text="Height (cm) : ",justify=LEFT).grid(row=1,column=0)
Label(showInfoFrame,text="Weight (kg) : ",justify=LEFT).grid(row=2,column=0)

showNameEntry=Entry(showInfoFrame,justify=CENTER)
showNameEntry.grid(row=0,column=1)

showHeightEntry=Entry(showInfoFrame,justify=CENTER)
showHeightEntry.grid(row=1,column=1)

showWeightEntry=Entry(showInfoFrame,justify=CENTER)
showWeightEntry.grid(row=2,column=1)

#=========NEW CANVAS========

newCanvas=Canvas(window,width=200,height=200,relief=None,highlightthickness=0)

newCanvasFrame=Frame(newCanvas)
newCanvasFrame.pack()

Label(newCanvasFrame,text="Name:            ",justify=LEFT).grid(row=0,column=0)
Label(newCanvasFrame,text="Height (cm) : ",justify=LEFT).grid(row=1,column=0)
Label(newCanvasFrame,text="Weight (kg) : ",justify=LEFT).grid(row=2,column=0)

newNameEntry=Entry(newCanvasFrame,justify=CENTER)
newNameEntry.grid(row=0,column=1)

newHeightEntry=Entry(newCanvasFrame,justify=CENTER)
newHeightEntry.grid(row=1,column=1)

newWeightEntry=Entry(newCanvasFrame,justify=CENTER)
newWeightEntry.grid(row=2,column=1)

#==========================ARRAYS================
canvasArray=[loginCanvas,viewCanvas,newCanvas,openCanvas]
userNameArray=[]
healthDataArray=[]
currentViewArray=[]
dataItems=["Height","Weight"]

lineTrackArray=[]

#=========================FUNCTIONS================
def loadCanvas(currentCanvas):
	for canvas in canvasArray:
		if canvas != currentCanvas:
			canvas.pack_forget()
			
	currentCanvas.pack(expand=True)

def askMessage(pre,message):
	try:
		messagebox.showinfo(pre,message)
	except:
		print(message)
def getContentFromFile(path):

        try:
                file=open(path,"r")
        except:
                askMessage("Error","Could not find file")
        else:
                content=file.readlines()
                file.close()
                newContent=[]
                for line in content:
                        
                        lineTrackArray.append(line)       
                        words=line.split()
                        if len(words) > 0:
                                line=line.rstrip()
                                newContent.append(line)
                        
                return newContent
def getHealthData():
        global userNameArray
        global healthDataArray
        content=getContentFromFile("usernames.txt")
        if content != None:
                userNameArray=[]
                        
                #Finds Usernames
                for segment in content:
                        words=segment.split(",")
                        name=words[0]
                        userNameArray.append(name)
                        words.remove(name)
                        temp=[[name],words]
                        healthDataArray.append(temp)
		

def checkCredentials():
	global currentViewArray
	getHealthData()
	
	data=str(userNameEntry.get())
	found=False
	for item in healthDataArray:
		nameSeg=item[0]
		name=nameSeg[0]

		data=data.capitalize()
		name=name.capitalize()
		
		if data == name:
			found=True
			askMessage("Found", "Infomation Found")
			currentViewArray=item
			showInfo()
			break
			
	if found == False:
		askMessage("Not Found", "User Not Found")

def insertEntry(entry,message):
        entry.delete(0,END)
        entry.insert(END,message)

def showInfo():
        loadCanvas(viewCanvas)

        #Gets name from current view
        nameSegment=currentViewArray[0]
        userName=nameSegment[0]
        #Data Section
        dataSegment=currentViewArray[1]
        

        #Add infomation about userName to screen
        insertEntry(showNameEntry,userName.capitalize())
                
        #Rest of infomation

        print("Data is",dataSegment)
        try:
                userWeight=dataSegment[0]
                userHeight=dataSegment[1]
        except:
                insertEntry(showWeightEntry,"Unknown")
                insertEntry(showHeightEntry,"Unknown")
        else:
                insertEntry(showWeightEntry,userWeight)
                insertEntry(showHeightEntry,userHeight)
                
        
def overwrite():

        currentView=currentViewArray

        originalArray=[]
        for item in currentView:
                originalArray.append(item)
                
        name=showNameEntry.get()
        height=showHeightEntry.get()
        weight=showWeightEntry.get()

        nameSection=currentView[0]
        dataSection=currentView[1]

        #Overwrites Data

        try:
                nameSection[0]=name
                dataSection[0]=height
                dataSection[1]=weight
        except:
                askMessage("Error","Error changing data")
        else:

                #Generates new array
                newArrayToSave=[nameSection,dataSection]
                pass

                #Save new file into main array
                try:
                        position=healthDataArray.index(originalArray)
                except:
                        print(originalArray,"is not in",healthDataArray)
                else:
                        healthDataArray[position]=newArrayToSave
                        print("Saved New data")
                        saveArrayToFile()
                

def saveArrayToFile():

        data=healthDataArray
        print(data)



def createNewUser():

        name=str(newNameEntry.get())
        height=str(newHeightEntry.get())

        weight=str(newWeightEntry.get())

        items=[name,height,weight]

        valid=True
        for item in items:
                words=item.split()
                if len(words) <= 0:
                        valid=False

        if valid == False:
                askMessage("Blank","Please fill in all areas")
        else:
                if name in userNameArray:
                        askMessage("Duplicate","This user allready exists")
                else:
                        tempString=""
                        tempString+=name
                        tempString+=","
                        tempString+=height
                        tempString+=","
                        tempString+=weight
                        tempString+="\n"

                        print("Going to save...",tempString)
                        found=False
                        for item in lineTrackArray:
                                if item == tempString:
                                        found=True

                        if found == False:
                        
                                file=open("usernames.txt","a")
                                file.write(tempString)

                                file.close()
                                askMessage("Complete","Saved New User")

                        else:
                                askMessage("Duplicate","Duplicate Detected")
                
        
                
                   
                
#========================MENU COMMANDS===========

mainMenu.add_cascade(label="File",menu=fileMenu)
mainMenu.add_command(label="New",command=lambda canvas=newCanvas: loadCanvas(canvas))
fileMenu.add_command(label="Home",command=lambda canvas=openCanvas: loadCanvas(canvas))
fileMenu.add_separator()
fileMenu.add_command(label="Login",command=lambda canvas=loginCanvas: loadCanvas(canvas))

#===================BUTTONS====================
overWriteButton=Button(viewCanvas,text="Overwrite",relief=FLAT,bg="light green",command=overwrite,width=10)
overWriteButton.pack(pady=19)

submitNewUserButton=Button(newCanvas,text="Create",relief=FLAT,bg="light blue",command=createNewUser,width=10)
submitNewUserButton.pack(pady=19)

loginButton=Button(openCanvas,text="Login",relief=FLAT,bg="light blue",width=12,command=lambda canvas=loginCanvas: loadCanvas(canvas))
loginButton.pack(fill=Y,pady=15)

newButton=Button(openCanvas,text="New",relief=FLAT,bg="light green",width=12,command=lambda canvas=newCanvas: loadCanvas(canvas))
newButton.pack(fill=Y,pady=15)

#===================RETURN COMMANDS============
getHealthData()
#===================BINDINGS COMMANDS============
userNameEntry.bind("<Return>",lambda event: checkCredentials())
window.mainloop()
