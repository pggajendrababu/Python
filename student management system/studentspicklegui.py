from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import studentslist as sl
import custom as cs
import pickle


idEntry = 0
idLabel2 = ""
nameEntry = ""  # empty space
courseEntry = ""
subjectEntry = ""
genderEntry = ""
cellNumberEntry = 0
emailEntry = ""
birthDayEntry = 0
birthMonthEntry = 0
birthYearEntry = 0
idNumber = 0
studentsDict = { } # aaa_0


#==========================
def loadGlobalVariables( ):
        global idNumber, studentsDict # aaa_1
        try:
                with open("globalvariablespickle.pkl", "rb") as file:
                        dct = pickle.load(file)
                        idNumber = dct["idNumber"]
                        #messagebox.showinfo("Info", f"idNumber = {idNumber}")
        except FileNotFoundError:
                pass
                
                
        try:
                with open("studentspickle.pkl", "rb") as file:
                        studentsDict = pickle.load(file) # aaa_2
                        #messagebox.showinfo("Info-loadGlobalVariables", f"studentsDict = {studentsDict}")
                        #messagebox.showinfo("Info-loadGlobalVariables", f"studentsDict.keys( ) = {studentsDict.keys( )}")
        except FileNotFoundError:
                pass        
        
        
def saveGlobalVariables( ):
        global idNumber
        with open("globalvariablespickle.pkl", "wb") as file:
                dct = {"idNumber" : idNumber}
                pickle.dump(dct, file)
                
                
def saveStudentsDict( ):
        with open("studentspickle.pkl", "wb") as file:
                #messagebox.showinfo("Info-saveStudentsDict", f"studentsDict = {studentsDict}")
                pickle.dump(studentsDict, file)
#==========================
def clearScreen(frame):
        for widget in frame.winfo_children( ):
                widget.destroy( )
                
                
def exitApp(root):
        root.destroy( )
        

def resetFieldsExcludingIdNumber( ):
        #idEntry.delete(0, END)
        nameEntry.delete(0, END)
        courseEntry.delete(0, END)
        subjectEntry.delete(0, END)
        genderEntry.delete(0, END)
        cellNumberEntry.delete(0, END)
        emailEntry.delete(0, END)
        birthDayEntry.delete(0, END)
        birthMonthEntry.delete(0, END)
        birthYearEntry.delete(0, END)
        
        
def resetFields( ):
        idEntry.delete(0, END)
        nameEntry.delete(0, END)
        courseEntry.delete(0, END)
        subjectEntry.delete(0, END)
        genderEntry.delete(0, END)
        cellNumberEntry.delete(0, END)
        emailEntry.delete(0, END)
        birthDayEntry.delete(0, END)
        birthMonthEntry.delete(0, END)
        birthYearEntry.delete(0, END)
#==========================
def doesIdNumberExist(idNumber):
        #idNumberType = type(idNumber)
        #messagebox.showinfo("Info-doesIdNumberExist", f"idNumberType = {idNumberType}")
        #messagebox.showinfo("Info-doesIdNumberExist", f"studentsDict.keys( ) = {studentsDict.keys( )}") # aaa_3
        try:
                lst = studentsDict[idNumber]
                return True, lst
        except KeyError:
                return False, "Given id number does not match any existing student's ID."
                

def createNewId( ):
        global idNumber
        idNumber += 1
        idNumberExistResult, idNumberExistMessage = doesIdNumberExist(idNumber)
        if idNumberExistResult == False:
                saveGlobalVariables( )
                return idNumber
        else:
                #print(f"{idNumberExistMessage} already exists with same id")
                idNumber += 1
                saveGlobalVariables( )
                createNewId( )
#===========================
def displayIdNumber(leftFrame, hyphenInsertedIdNumber):
        
        clearScreen(leftFrame)
        #global idEntry
        
        
        idLabel = Label(leftFrame, text="ID", font=cs.font1, bd=2, fg=cs.colour5, bg=cs.colour1)
        idLabel.grid(row=0, column=0, sticky="ew")
        idEntry = Entry(leftFrame, bd=2)
        idEntry.grid(row=0, column=1)
        
        
        idEntry.insert(0, hyphenInsertedIdNumber)


def areAllFieldsOk(name, course, subject, gender, cellNumber,  birthDay, birthMonth, birthYear):
        
        
        nameValidResult, nameValidMessage = sl.isValidName(name)
        courseValidResult, courseValidMessage = sl.isValidCourse(course)
        subjectValidResult, subjectValidMessage = sl.isValidSubject(subject)
        genderValidResult, genderValidMessage = sl.isValidGender(gender)
        cellNumberValidResult,  cellNumberValidMessage = sl.isValidCellNumber(cellNumber)
        birthDayValidResult, birthDayValidMessage = sl.isValidBirthDay(birthDay)
        birthMonthValidResult, birthMonthValidMessage = sl.isValidBirthMonth(birthMonth)
        birthYearValidResult, birthYearValidMessage = sl.isValidBirthYear(birthYear)
        
       
        if nameValidResult == False:
                return nameValidMessage
        elif courseValidResult == False:
                return courseValidMessage
        elif subjectValidResult == False:
                return subjectValidMessage
        elif genderValidResult == False:
                return genderValidMessage
        elif cellNumberValidResult == False:
                return cellNumberValidMessage
        elif birthDayValidResult == False:
                return birthDayValidMessage
        elif birthMonthValidResult == False:
                return birthMonthValidMessage
        elif birthYearValidResult == False:
                return birthYearValidMessage
        else:
                return True
             

def addNewExecute(leftFrame):
        student = [ ]
        
        
        name = nameEntry.get( ).strip( )
        course = courseEntry.get( ).strip( )
        subject = subjectEntry.get( ).strip( )
        gender = genderEntry.get( ).strip( )
        cellNumber = cellNumberEntry.get( ).strip( ).replace("-", "") # replace "-" with empty space = removes "-"
        email = emailEntry.get( ).strip( )
        birthDay = birthDayEntry.get( ).strip( )
        birthMonth = birthMonthEntry.get( ).strip( )
        birthYear = birthYearEntry.get( ).strip( )
        birthday = sl.correctBirthday(birthDay, birthMonth, birthYear)
        
        
        result = areAllFieldsOk(name, course, subject, gender, cellNumber,  birthDay, birthMonth, birthYear)
        if result == True:
                idNumber = createNewId( )
                student.append(idNumber)
                student.append(name)
                student.append(course)
                student.append(subject)
                student.append(gender)
                student.append(int(cellNumber))
                if email == "": # empty space
                        student.append(None)
                else:
                        student.append(email)
                student.append(birthday)
                
                
                studentsDict[idNumber] = student # aaa_4
                saveStudentsDict( )
                resetFieldsExcludingIdNumber( ) 
                hyphenInsertedIdNumber = sl.insertHyphen(str(idNumber), 4)
                displayIdNumber(leftFrame, hyphenInsertedIdNumber)
                messagebox.showinfo("Sucess", f"A new student info has been added. \nID number = {hyphenInsertedIdNumber}", parent=leftFrame)
        else:
                messagebox.showerror("Error!",f"{result}", parent=leftFrame)



def addNew(leftFrame):
        clearScreen(leftFrame)
        global nameEntry, courseEntry, subjectEntry, genderEntry, cellNumberEntry, emailEntry, birthDayEntry,birthMonthEntry, birthYearEntry
        
        
        days = [str(i) for i in range(1, 32)]
        months = [str(i) for i in range(1, 13)]
        years = [str(i) for i in range(1900, 2101)]
        
        
        nameLabel = Label(leftFrame, text="Name", font=cs.font1, bd=2, bg=cs.colour1)
        nameLabel.grid(row=1, column=0, sticky="ew")
        nameEntry = Entry(leftFrame, bd=2)
        nameEntry.grid(row=1, column=1)
        
        
        courseLabel = Label(leftFrame, text="Course", font=cs.font1, bd=2, bg=cs.colour1)
        courseLabel.grid(row=2, column=0, sticky="ew")
        courseEntry = Entry(leftFrame, bd=2)
        courseEntry.grid(row=2, column=1)
        
        
        subjectLabel = Label(leftFrame, text="Subject", font=cs.font1, bd=2, bg=cs.colour1)
        subjectLabel.grid(row=3, column=0, sticky="ew")
        subjectEntry = Entry(leftFrame, bd=2)
        subjectEntry.grid(row=3, column=1)
        
        
        genderLabel = Label(leftFrame, text="Gender", font=cs.font1, bd=2, bg=cs.colour1)
        genderLabel.grid(row=4, column=0, sticky="ew")
        genderEntry = Entry(leftFrame, bd=2)
        genderEntry.grid(row=4, column=1)


        cellNumberLabel = Label(leftFrame, text="Cell number", font=cs.font1, bd=2, bg=cs.colour1)
        cellNumberLabel.grid(row=5, column=0, sticky="ew")
        cellNumberEntry = Entry(leftFrame, bd=2)
        cellNumberEntry.grid(row=5, column=1)


        emailLabel = Label(leftFrame, text="Email", font=cs.font1, bd=2, bg=cs.colour1)
        emailLabel.grid(row=6, column=0, sticky="ew")
        emailEntry = Entry(leftFrame, bd=2)
        emailEntry.grid(row=6, column=1)
        
        
        birthDayLabel = Label(leftFrame, text="Birth day", font=cs.font1, bd=2, bg=cs.colour1)
        birthDayLabel.grid(row=7, column=0, sticky="ew")
        birthDayEntry = ttk.Combobox(leftFrame, values=days)
        birthDayEntry.set("Day") 
        birthDayEntry.grid(row=7, column=1)
        
        
        birthMonthLabel = Label(leftFrame, text="Birth month", font=cs.font1, bd=2, bg=cs.colour1)
        birthMonthLabel.grid(row=8, column=0, sticky="ew")
        birthMonthEntry = ttk.Combobox(leftFrame, values=months)
        birthMonthEntry.set("Month")
        birthMonthEntry.grid(row=8, column=1)


        birthYearLabel = Label(leftFrame, text="Birth year", font=cs.font1, bd=2, bg=cs.colour1)
        birthYearLabel.grid(row=9, column=0, sticky="ew")
        birthYearEntry = ttk.Combobox(leftFrame, values=years)
        birthYearEntry.set("Year")
        birthYearEntry.grid(row=9, column=1)
        
        
        addNewButton = Button(leftFrame, text="Add New", font=cs.font1, bd=2, command=lambda: addNewExecute(leftFrame), fg=cs.colour3, bg=cs.colour4)
        addNewButton.grid(row=4, column=3, sticky="ew")
#==========================
def viewDetails(leftFrame):
        clearScreen(leftFrame)
        global idEntry, nameEntry, courseEntry, subjectEntry, genderEntry, cellNumberEntry, emailEntry, birthDayEntry,birthMonthEntry, birthYearEntry
        
        
        days = [str(i) for i in range(1, 32)]
        months = [str(i) for i in range(1, 13)]
        years = [str(i) for i in range(1900, 2101)]
        
        
        idLabel = Label(leftFrame, text="ID", font=cs.font1, bd=2, fg=cs.colour5, bg=cs.colour1)
        idLabel.grid(row=0, column=0, sticky="ew")
        idEntry = Entry(leftFrame, bd=2)
        idEntry.grid(row=0, column=1)
        
        
        nameLabel = Label(leftFrame, text="Name", font=cs.font1, bd=2, bg=cs.colour1)
        nameLabel.grid(row=1, column=0, sticky="ew")
        nameEntry = Entry(leftFrame, bd=2)
        nameEntry.grid(row=1, column=1)
        
        
        courseLabel = Label(leftFrame, text="Course", font=cs.font1, bd=2, bg=cs.colour1)
        courseLabel.grid(row=2, column=0, sticky="ew")
        courseEntry = Entry(leftFrame, bd=2)
        courseEntry.grid(row=2, column=1)
        
        
        subjectLabel = Label(leftFrame, text="Subject", font=cs.font1, bd=2, bg=cs.colour1)
        subjectLabel.grid(row=3, column=0, sticky="ew")
        subjectEntry = Entry(leftFrame, bd=2)
        subjectEntry.grid(row=3, column=1)
        
        
        genderLabel = Label(leftFrame, text="Gender", font=cs.font1, bd=2, bg=cs.colour1)
        genderLabel.grid(row=4, column=0, sticky="ew")
        genderEntry = Entry(leftFrame, bd=2)
        genderEntry.grid(row=4, column=1)


        cellNumberLabel = Label(leftFrame, text="Cell number", font=cs.font1, bd=2, bg=cs.colour1)
        cellNumberLabel.grid(row=5, column=0, sticky="ew")
        cellNumberEntry = Entry(leftFrame, bd=2)
        cellNumberEntry.grid(row=5, column=1)


        emailLabel = Label(leftFrame, text="Email", font=cs.font1, bd=2, bg=cs.colour1)
        emailLabel.grid(row=6, column=0, sticky="ew")
        emailEntry = Entry(leftFrame, bd=2)
        emailEntry.grid(row=6, column=1)
        
        
        birthDayLabel = Label(leftFrame, text="Birth day", font=cs.font1, bd=2, bg=cs.colour1)
        birthDayLabel.grid(row=7, column=0, sticky="ew")
        birthDayEntry = ttk.Combobox(leftFrame, values=days)
        birthDayEntry.set("Day") 
        birthDayEntry.grid(row=7, column=1)
        
        
        birthMonthLabel = Label(leftFrame, text="Birth month", font=cs.font1, bd=2, bg=cs.colour1)
        birthMonthLabel.grid(row=8, column=0, sticky="ew")
        birthMonthEntry = ttk.Combobox(leftFrame, values=months)
        birthMonthEntry.set("Month")
        birthMonthEntry.grid(row=8, column=1)


        birthYearLabel = Label(leftFrame, text="Birth year", font=cs.font1, bd=2, bg=cs.colour1)
        birthYearLabel.grid(row=9, column=0, sticky="ew")
        birthYearEntry = ttk.Combobox(leftFrame, values=years)
        birthYearEntry.set("Year")
        birthYearEntry.grid(row=9, column=1)


def showDetails(leftFrame, idNumberExistMessage):
        
        hyphenInsertedIdNumber = sl.insertHyphen(str(idNumberExistMessage[0]), 4)
        hyphenInsertedCellNumber = sl.insertHyphen(str(idNumberExistMessage[5]), 4)
        if idNumberExistMessage[6] == None:
                idNumberExistMessage[6] = "" # empty space
        birthDay = idNumberExistMessage[7][0:2]
        birthMonth = idNumberExistMessage[7][2:4]
        birthYear = idNumberExistMessage[7][4:8]
        
        
        viewDetails(leftFrame)
        resetFields( )
        idEntry.insert(0, hyphenInsertedIdNumber)
        nameEntry.insert(0, idNumberExistMessage[1])
        courseEntry.insert(0, idNumberExistMessage[2])
        subjectEntry.insert(0, idNumberExistMessage[3])
        genderEntry.insert(0, idNumberExistMessage[4])
        cellNumberEntry.insert(0, hyphenInsertedCellNumber)
        emailEntry.insert(0, idNumberExistMessage[6])
        birthDayEntry.insert(0, birthDay)
        birthMonthEntry.insert(0, birthMonth)
        birthYearEntry.insert(0, birthYear)


def viewDetailsExecute(leftFrame):
        idNumber = idEntry.get( ).strip( ).replace("-", "") # replace "-" with empty space = removes "-"
        idNumberValidResult, idNumberValidMessage = sl.isValidIdNumber(idNumber)
        if idNumberValidResult == True:
                idNumberExistResult, idNumberExistMessage = doesIdNumberExist(int(idNumber))
                if idNumberExistResult == True:
                        showDetails(leftFrame, idNumberExistMessage)
                else:
                         messagebox.showerror("Error!", f"{idNumberExistMessage}", parent=leftFrame)
        else:
                messagebox.showerror("Error!", f"{idNumberValidMessage}", parent=leftFrame)


def getIdNumberViewDetails(leftFrame):
        
        clearScreen(leftFrame)
        global idEntry
        
        
        idLabel = Label(leftFrame, text="ID", font=cs.font1, bd=2, fg=cs.colour5, bg=cs.colour1)
        idLabel.grid(row=0, column=0, sticky="ew")
        idEntry = Entry(leftFrame, bd=2)
        idEntry.grid(row=0, column=1)
        
        viewDetailsLabel = Label(leftFrame, text="View Details", font=cs.font1, bd=2, fg=cs.colour6, bg=cs.colour1)
        viewDetailsLabel.grid(row=4, column=3, sticky="ew")
        submitButton = Button(leftFrame, text="Submit", font=cs.font1, bd=2, command=lambda: viewDetailsExecute(leftFrame), fg=cs.colour3, bg=cs.colour4)
        submitButton.grid(row=4, column=4, sticky="ew")
#==========================
def updateExecute(leftFrame):
        student = [ ]
        
        
        name = nameEntry.get( ).strip( )
        course = courseEntry.get( ).strip( )
        subject = subjectEntry.get( ).strip( )
        gender = genderEntry.get( ).strip( )
        cellNumber = cellNumberEntry.get( ).strip( ).replace("-", "") # replace "-" with empty space = removes "-"
        email = emailEntry.get( ).strip( )
        birthDay = birthDayEntry.get( ).strip( )
        birthMonth = birthMonthEntry.get( ).strip( )
        birthYear = birthYearEntry.get( ).strip( )
        birthday = sl.correctBirthday(birthDay, birthMonth, birthYear)
        
        
        result = areAllFieldsOk(name, course, subject, gender, cellNumber,  birthDay, birthMonth, birthYear)
        if result == True:
                #messagebox.showinfo("updateExecute", f"idEntry type = {type(idEntry)}", parent=leftFrame)
                #messagebox.showinfo("updateExecute", f"idEntry = {idEntry}", parent=leftFrame)
                #idNumber = idEntry.get( ).strip( ).replace("-", "") # removes "-"
                #idNumber = idLabel2.cget("text").strip( ).replace("-", "") # get the ID from the label and clean it up
                #messagebox.showinfo("updateExecute", f"idNumber = {idNumber}", parent=leftFrame)
                student.append(int(idNumber))
                student.append(name)
                student.append(course)
                student.append(subject)
                student.append(gender)
                student.append(int(cellNumber))
                if email == "": # empty space
                        student.append(None)
                else:
                        student.append(email)
                student.append(birthday)
                
                
                # modify existing studentsDict by assigning a value
                studentsDict[int(idNumber)] = student
                saveStudentsDict( )
                messagebox.showinfo("Sucess", "student's info was updated.", parent=leftFrame)
                clearScreen(leftFrame)
        else:
                messagebox.showerror("Error!",f"{result}",parent=leftFrame)
                
                
def update(leftFrame):
        clearScreen(leftFrame)
        global idLabel2, nameEntry, courseEntry, subjectEntry, genderEntry, cellNumberEntry, emailEntry, birthDayEntry,birthMonthEntry, birthYearEntry
        
        
        days = [str(i) for i in range(1, 32)]
        months = [str(i) for i in range(1, 13)]
        years = [str(i) for i in range(1900, 2101)]
        
        
        idLabel = Label(leftFrame, text="ID", font=cs.font1, bd=2, fg=cs.colour5, bg=cs.colour1)
        idLabel.grid(row=0, column=0, sticky="ew")
        idLabel2 = Label(leftFrame, text="ID", font=cs.font1, bd=2, fg=cs.colour6, bg=cs.colour1)
        idLabel2.grid(row=0, column=1, sticky="ew")
        
        
        nameLabel = Label(leftFrame, text="Name", font=cs.font1, bd=2, bg=cs.colour1)
        nameLabel.grid(row=1, column=0, sticky="ew")
        nameEntry = Entry(leftFrame, bd=2)
        nameEntry.grid(row=1, column=1)
        
        
        courseLabel = Label(leftFrame, text="Course", font=cs.font1, bd=2, bg=cs.colour1)
        courseLabel.grid(row=2, column=0, sticky="ew")
        courseEntry = Entry(leftFrame, bd=2)
        courseEntry.grid(row=2, column=1)
        
        
        subjectLabel = Label(leftFrame, text="Subject", font=cs.font1, bd=2, bg=cs.colour1)
        subjectLabel.grid(row=3, column=0, sticky="ew")
        subjectEntry = Entry(leftFrame, bd=2)
        subjectEntry.grid(row=3, column=1)
        
        
        genderLabel = Label(leftFrame, text="Gender", font=cs.font1, bd=2, bg=cs.colour1)
        genderLabel.grid(row=4, column=0, sticky="ew")
        genderEntry = Entry(leftFrame, bd=2)
        genderEntry.grid(row=4, column=1)


        cellNumberLabel = Label(leftFrame, text="Cell number", font=cs.font1, bd=2, bg=cs.colour1)
        cellNumberLabel.grid(row=5, column=0, sticky="ew")
        cellNumberEntry = Entry(leftFrame, bd=2)
        cellNumberEntry.grid(row=5, column=1)


        emailLabel = Label(leftFrame, text="Email", font=cs.font1, bd=2, bg=cs.colour1)
        emailLabel.grid(row=6, column=0, sticky="ew")
        emailEntry = Entry(leftFrame, bd=2)
        emailEntry.grid(row=6, column=1)
        
        
        birthDayLabel = Label(leftFrame, text="Birth day", font=cs.font1, bd=2, bg=cs.colour1)
        birthDayLabel.grid(row=7, column=0, sticky="ew")
        birthDayEntry = ttk.Combobox(leftFrame, values=days)
        birthDayEntry.set("Day") 
        birthDayEntry.grid(row=7, column=1)
        
        
        birthMonthLabel = Label(leftFrame, text="Birth month", font=cs.font1, bd=2, bg=cs.colour1)
        birthMonthLabel.grid(row=8, column=0, sticky="ew")
        birthMonthEntry = ttk.Combobox(leftFrame, values=months)
        birthMonthEntry.set("Month")
        birthMonthEntry.grid(row=8, column=1)


        birthYearLabel = Label(leftFrame, text="Birth year", font=cs.font1, bd=2, bg=cs.colour1)
        birthYearLabel.grid(row=9, column=0, sticky="ew")
        birthYearEntry = ttk.Combobox(leftFrame, values=years)
        birthYearEntry.set("Year")
        birthYearEntry.grid(row=9, column=1)
        
        
        updateButton = Button(leftFrame, text="Update", font=cs.font1, bd=2, command=lambda: updateExecute(leftFrame), fg=cs.colour3, bg=cs.colour4)
        updateButton.grid(row=4, column=3, sticky="ew")


def showDetailsUpdate(leftFrame, idNumberExistMessage):
        
        hyphenInsertedIdNumber = sl.insertHyphen(str(idNumberExistMessage[0]), 4)
        hyphenInsertedCellNumber = sl.insertHyphen(str(idNumberExistMessage[5]), 4)
        if idNumberExistMessage[6] == None:
                idNumberExistMessage[6] = "" # empty space
        birthDay = idNumberExistMessage[7][0:2]
        birthMonth = idNumberExistMessage[7][2:4]
        birthYear = idNumberExistMessage[7][4:8]
        
        
        update(leftFrame)
        resetFieldsExcludingIdNumber( )
        idLabel2.config(text= hyphenInsertedIdNumber)
        nameEntry.insert(0, idNumberExistMessage[1])
        courseEntry.insert(0, idNumberExistMessage[2])
        subjectEntry.insert(0, idNumberExistMessage[3])
        genderEntry.insert(0, idNumberExistMessage[4])
        cellNumberEntry.insert(0, hyphenInsertedCellNumber)
        emailEntry.insert(0, idNumberExistMessage[6])
        birthDayEntry.insert(0, birthDay)
        birthMonthEntry.insert(0, birthMonth)
        birthYearEntry.insert(0, birthYear)     
        
        
def checkUpdate(leftFrame):
        global idNumber
        #messagebox.showinfo("checkUpdate", f"idEntry type = {type(idEntry)}", parent=leftFrame)
        #messagebox.showinfo("checkUpdate", f"idEntry = {idEntry}", parent=leftFrame)
        idNumber = idEntry.get( ).strip( ).replace("-", "") # replace "-" with empty space = removes "-"
        #messagebox.showinfo("checkUpdate", f"idNumber = {idNumber}", parent=leftFrame)
        idNumberValidResult, idNumberValidMessage = sl.isValidIdNumber(idNumber)
        if idNumberValidResult == True:
                idNumberExistResult, idNumberExistMessage = doesIdNumberExist(int(idNumber))
                if idNumberExistResult == True:
                        showDetailsUpdate(leftFrame, idNumberExistMessage)
                else:
                         messagebox.showerror("Error checkUpdate!", f"{idNumberExistMessage}", parent=leftFrame)
        else:
                messagebox.showerror("Error!", f"{idNumberValidMessage}", parent=leftFrame)
                
                      
def getIdNumberUpdate(leftFrame):
        
        clearScreen(leftFrame)
        global idEntry
        
        
        idLabel = Label(leftFrame, text="ID", font=cs.font1, bd=2, fg=cs.colour5, bg=cs.colour1)
        idLabel.grid(row=0, column=0, sticky="ew")
        idEntry = Entry(leftFrame, bd=2)
        idEntry.grid(row=0, column=1)
        
        updateLabel = Label(leftFrame, text="Update", font=cs.font1, bd=2, fg=cs.colour6, bg=cs.colour1)
        updateLabel.grid(row=4, column=3, sticky="ew")
        submitButton = Button(leftFrame, text="Submit", font=cs.font1, bd=2, command=lambda: checkUpdate(leftFrame), fg=cs.colour3, bg=cs.colour4)
        submitButton.grid(row=4, column=4, sticky="ew")
#==========================
def deleteExecute(leftFrame):
        permission = messagebox.askyesno("Confirmation", "Are you sure that you want to delete the student's record?")
        if permission == True: # we can use "if permission:" also
                del studentsDict[int(idNumber)]
                saveStudentsDict( )
                messagebox.showinfo("Info", "student's info was deleted.", parent=leftFrame)
                clearScreen(leftFrame)
        else:
                messagebox.showinfo("Info", "deletion canceled.", parent=leftFrame)
                clearScreen(leftFrame)
                
                
def delete(leftFrame):
        clearScreen(leftFrame)
        global idLabel2, nameEntry, courseEntry, subjectEntry, genderEntry, cellNumberEntry, emailEntry, birthDayEntry,birthMonthEntry, birthYearEntry
        
        
        days = [str(i) for i in range(1, 32)]
        months = [str(i) for i in range(1, 13)]
        years = [str(i) for i in range(1900, 2101)]
        
        
        idLabel = Label(leftFrame, text="ID", font=cs.font1, bd=2, fg=cs.colour5, bg=cs.colour1)
        idLabel.grid(row=0, column=0, sticky="ew")
        idLabel2 = Label(leftFrame, text="ID", font=cs.font1, bd=2, fg=cs.colour6, bg=cs.colour1)
        idLabel2.grid(row=0, column=1, sticky="ew")
        
        
        nameLabel = Label(leftFrame, text="Name", font=cs.font1, bd=2, bg=cs.colour1)
        nameLabel.grid(row=1, column=0, sticky="ew")
        nameEntry = Entry(leftFrame, bd=2)
        nameEntry.grid(row=1, column=1)
        
        
        courseLabel = Label(leftFrame, text="Course", font=cs.font1, bd=2, bg=cs.colour1)
        courseLabel.grid(row=2, column=0, sticky="ew")
        courseEntry = Entry(leftFrame, bd=2)
        courseEntry.grid(row=2, column=1)
        
        
        subjectLabel = Label(leftFrame, text="Subject", font=cs.font1, bd=2, bg=cs.colour1)
        subjectLabel.grid(row=3, column=0, sticky="ew")
        subjectEntry = Entry(leftFrame, bd=2)
        subjectEntry.grid(row=3, column=1)
        
        
        genderLabel = Label(leftFrame, text="Gender", font=cs.font1, bd=2, bg=cs.colour1)
        genderLabel.grid(row=4, column=0, sticky="ew")
        genderEntry = Entry(leftFrame, bd=2)
        genderEntry.grid(row=4, column=1)


        cellNumberLabel = Label(leftFrame, text="Cell number", font=cs.font1, bd=2, bg=cs.colour1)
        cellNumberLabel.grid(row=5, column=0, sticky="ew")
        cellNumberEntry = Entry(leftFrame, bd=2)
        cellNumberEntry.grid(row=5, column=1)


        emailLabel = Label(leftFrame, text="Email", font=cs.font1, bd=2, bg=cs.colour1)
        emailLabel.grid(row=6, column=0, sticky="ew")
        emailEntry = Entry(leftFrame, bd=2)
        emailEntry.grid(row=6, column=1)
        
        
        birthDayLabel = Label(leftFrame, text="Birth day", font=cs.font1, bd=2, bg=cs.colour1)
        birthDayLabel.grid(row=7, column=0, sticky="ew")
        birthDayEntry = ttk.Combobox(leftFrame, values=days)
        birthDayEntry.set("Day") 
        birthDayEntry.grid(row=7, column=1)
        
        
        birthMonthLabel = Label(leftFrame, text="Birth month", font=cs.font1, bd=2, bg=cs.colour1)
        birthMonthLabel.grid(row=8, column=0, sticky="ew")
        birthMonthEntry = ttk.Combobox(leftFrame, values=months)
        birthMonthEntry.set("Month")
        birthMonthEntry.grid(row=8, column=1)


        birthYearLabel = Label(leftFrame, text="Birth year", font=cs.font1, bd=2, bg=cs.colour1)
        birthYearLabel.grid(row=9, column=0, sticky="ew")
        birthYearEntry = ttk.Combobox(leftFrame, values=years)
        birthYearEntry.set("Year")
        birthYearEntry.grid(row=9, column=1)
        
        
        deleteButton = Button(leftFrame, text="Delete", font=cs.font1, bd=2, command=lambda: deleteExecute(leftFrame), fg=cs.colour7, bg=cs.colour4)
        deleteButton.grid(row=4, column=3, sticky="ew")


def showDetailsDelete(leftFrame, idNumberExistMessage):
        
        hyphenInsertedIdNumber = sl.insertHyphen(str(idNumberExistMessage[0]), 4)
        hyphenInsertedCellNumber = sl.insertHyphen(str(idNumberExistMessage[5]), 4)
        if idNumberExistMessage[6] == None:
                idNumberExistMessage[6] = "" # empty space
        birthDay = idNumberExistMessage[7][0:2]
        birthMonth = idNumberExistMessage[7][2:4]
        birthYear = idNumberExistMessage[7][4:8]
        
        
        delete(leftFrame)
        resetFieldsExcludingIdNumber( )
        idLabel2.config(text= hyphenInsertedIdNumber)
        nameEntry.insert(0, idNumberExistMessage[1])
        courseEntry.insert(0, idNumberExistMessage[2])
        subjectEntry.insert(0, idNumberExistMessage[3])
        genderEntry.insert(0, idNumberExistMessage[4])
        cellNumberEntry.insert(0, hyphenInsertedCellNumber)
        emailEntry.insert(0, idNumberExistMessage[6])
        birthDayEntry.insert(0, birthDay)
        birthMonthEntry.insert(0, birthMonth)
        birthYearEntry.insert(0, birthYear)     


def checkDelete(leftFrame):
        global idNumber
        #messagebox.showinfo("checkUpdate", f"idEntry type = {type(idEntry)}", parent=leftFrame)
        #messagebox.showinfo("checkUpdate", f"idEntry = {idEntry}", parent=leftFrame)
        idNumber = idEntry.get( ).strip( ).replace("-", "") # replace "-" with empty space = removes "-"
        #messagebox.showinfo("checkUpdate", f"idNumber = {idNumber}", parent=leftFrame)
        idNumberValidResult, idNumberValidMessage = sl.isValidIdNumber(idNumber)
        if idNumberValidResult == True:
                idNumberExistResult, idNumberExistMessage = doesIdNumberExist(int(idNumber))
                if idNumberExistResult == True:
                        showDetailsDelete(leftFrame, idNumberExistMessage)
                else:
                         messagebox.showerror("Error checkUpdate!", f"{idNumberExistMessage}", parent=leftFrame)
        else:
                messagebox.showerror("Error!", f"{idNumberValidMessage}", parent=leftFrame)
                
                
def getIdNumberDelete(leftFrame):
        
        clearScreen(leftFrame)
        global idEntry
        
        
        idLabel = Label(leftFrame, text="ID", font=cs.font1, bd=2, fg=cs.colour5, bg=cs.colour1)
        idLabel.grid(row=0, column=0, sticky="ew")
        idEntry = Entry(leftFrame, bd=2)
        idEntry.grid(row=0, column=1)
        
        deleteLabel = Label(leftFrame, text="Delete", font=cs.font1, bd=2, fg=cs.colour6, bg=cs.colour1)
        deleteLabel.grid(row=4, column=3, sticky="ew")
        submitButton = Button(leftFrame, text="Submit", font=cs.font1, bd=2, command=lambda: checkDelete(leftFrame), fg=cs.colour3, bg=cs.colour4)
        submitButton.grid(row=4, column=4, sticky="ew")               
#==========================
def main( ):
        loadGlobalVariables( )
        
        
        root = Tk( )


        leftFrame = Frame(root, bg=cs.colour1)
        leftFrame.pack(side=LEFT, fill=BOTH, expand=True)
        rightFrame = Frame(root, bg=cs.colour2)
        rightFrame.pack(side=RIGHT, fill=BOTH, expand=True)
        
        
        """
        The sticky="ew" parameter 
        ensures that the buttons 
        expand horizontally to fill the 
        available space.
        """
        addButton = Button(rightFrame, text="Add New", font=cs.font1, bd=2, command=lambda: addNew(leftFrame), fg=cs.colour3, bg=cs.colour4)
        addButton.grid(row=0, column=0, sticky="ew")
        
        
        viewButton = Button(rightFrame, text="View Details", font=cs.font1, bd=2, command=lambda: getIdNumberViewDetails(leftFrame), fg=cs.colour3, bg=cs.colour4)
        viewButton.grid(row=1, column=0, sticky="ew")
        
        
        updateButton = Button(rightFrame, text="Update", font=cs.font1, bd=2, command=lambda: getIdNumberUpdate(leftFrame), fg=cs.colour3, bg=cs.colour4)
        updateButton.grid(row=2, column=0, sticky="ew")
        
        
        deleteButton = Button(rightFrame, text="Delete", font=cs.font1, bd=2, command=lambda: getIdNumberDelete(leftFrame), fg=cs.colour3, bg=cs.colour4)
        deleteButton.grid(row=3, column=0, sticky="ew")
        
        
        clearButton = Button(rightFrame, text="Clear", font=cs.font1, bd=2, command=lambda: clearScreen(leftFrame), fg=cs.colour3, bg=cs.colour4)
        clearButton.grid(row=4, column=0, sticky="ew")
        
        
        exitButton = Button(rightFrame, text="Exit", font=cs.font1, bd=2, command=lambda: exitApp(root), fg=cs.colour3, bg=cs.colour4)
        exitButton.grid(row=5, column=0, sticky="ew")
        
        
        root.mainloop( )
        
        
if __name__ == "__main__":
        main( )


"""
aaa_0, aaa_1, aaa_2, aaa_3, aaa_4


Two things happened.
1) when I first added two students 
using "Add New" button 
(def main( )), it succesfully added 
students. Then I Exited the app. 
Then I re-started the app and 
added another student 
using "Add New" 
button (def main( )). but this time, it 
erased all the old entries (students) 
and added only the last added 
student.
2) studentsDict.keys( ) in aaa_3 only showed "empty list [ ]", eventhough studentsDict in aaa_0 contained entries (students).


Reason : 
-----------------

In aaa_1 initially I did not give 
studentsDict as global. 
so studentsDict in aaa_2 remained 
local (to the function 
"def loadGlovalVariables( )").


so when entries were loaded from 
studentspickle.pkl via aaa_2, it did 
not change aaa_0. so, studentsDict 
in aaa_0 remained as empty 
dictionary ({ }). THAT is the reason 
for the above two phenomenons.


see also 
(python_programs/keywords)
global_example1.py,
global_example2.py,
global_example5.py


Next Doubt : 
---------------------


Then, why did studentsDict in aaa_4 change studentsDict in aaa_0, *without global keyword* ? and why did not studentsDict in aaa_2 change studentsDict in aaa_0, *without global keyword* ?


Answer :
---------------

aaa_4 only changes the elements 
of studentsDict object in aaa_0 (It 
do not change 
the entire studentsDict object).
whereas, studentsDict in aaa_2 try 
to change the entire studentDict 
object in aaa_0. 


see 
(python_programs/keywords)
global_examplea1.py,
global_examplea2.py

"""

