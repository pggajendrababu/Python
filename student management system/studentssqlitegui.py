from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import studentslist as sl
import custom as cs
import sqlite3


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
studentsList = [ ]
studentsDict = { } 


#==========================
def createTable( ):
        conn = sqlite3.connect('studentssqlite.db')
        cursor = conn.cursor( )
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                        idNumber INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        course TEXT NOT NULL,
                        subject TEXT NOT NULL,
                        gender TEXT NOT NULL,
                        cellNumber INTEGER NOT NULL,
                        email TEXT,
                        birthday TEXT NOT NULL
                )
        ''')
        #messagebox.showinfo("Info-createTable", "Table created sucessfully.")
        conn.commit( )
        conn.close( )
        
        
def loadGlobalVariables( ):
        try:
                with open("studentssqlite.db", "r") as file:
                        conn = sqlite3.connect('studentssqlite.db')
                        cursor = conn.cursor( )
                        cursor.execute('SELECT idNumber, name, course, subject, gender, cellNumber, email, birthday FROM students')
                        for idNumber, name, course, subject, gender, cellNumber, email, birthday in cursor.fetchall( ):
                                lst = [idNumber, name, course, subject, gender, cellNumber, email, birthday]
                                studentsDict[idNumber] = lst
                        #messagebox.showinfo("Info-loadGlobalVariables", f"studentsDict = {studentsDict}")
                        conn.commit( )
                        conn.close( )
        except FileNotFoundError:
                pass
                
                
def saveStudentsList( ): 
        with open("studentssqlite.db", "a") as file:
                #messagebox.showinfo("Info-saveStudentsList", f"studentsList = {studentsList}")
                conn = sqlite3.connect("studentssqlite.db")
                cursor = conn.cursor( )
                #cursor.execute('DELETE FROM students')  # Clear existing data
                cursor.execute('INSERT INTO students (name, course, subject, gender, cellNumber, email, birthday) VALUES (?, ?, ?, ?, ?, ?, ?)', (studentsList[0], studentsList[1], studentsList[2], studentsList[3], studentsList[4], studentsList[5], studentsList[6]))
                conn.commit( )
                conn.close( )
                
                
def updateStudentsDict( ): # path1
        global idNumber
        with open("studentssqlite.db", "a") as file:
                #messagebox.showinfo("Info-saveStudentsDict", f"studentsDict = {studentsDict}")
                conn = sqlite3.connect("studentssqlite.db")
                cursor = conn.cursor( )
                #cursor.execute('DELETE FROM students')  # Clear existing data
                idNumber, name, course, subject, gender, cellNumber, email, birthday = studentsDict[int(idNumber)]
                cursor.execute('UPDATE students SET name = ?, course = ?, subject = ?, gender = ?, cellNumber = ?, email = ?, birthday = ? WHERE idNumber = ?', (name, course, subject, gender, cellNumber, email, birthday, idNumber))
                conn.commit( )
                conn.close( )


"""                
def saveStudentsDict( ): # path2 (not an efficient way)
        with open("studentssqlite.db", "a") as file:
                #messagebox.showinfo("Info-saveStudentsDict", f"studentsDict = {studentsDict}")
                conn = sqlite3.connect("studentssqlite.db")
                cursor = conn.cursor( )
                cursor.execute('DELETE FROM students')  # Clear existing data
                for key, value in studentsDict.items( ):
                        cursor.execute('INSERT INTO students (idNumber, name, course, subject, gender, cellNumber, email, birthday) VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7]))
                conn.commit( )
                conn.close( )
"""


def deleteStudentStudentsDict( ):
        with open("studentssqlite.db", "a") as file:
                #messagebox.showinfo("Info-deleteStudentStudentsDict", f"studentsDict = {studentsDict}")
                conn = sqlite3.connect("studentssqlite.db")
                cursor = conn.cursor( )
                cursor.execute("DELETE FROM students WHERE idNumber = ?", (int(idNumber),))
                conn.commit( )
                conn.close( )
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
        global studentsList
        
        
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
                studentsList.append(name)
                studentsList.append(course)
                studentsList.append(subject)
                studentsList.append(gender)
                studentsList.append(int(cellNumber))
                if email == "": # empty space
                        studentsList.append(None)
                else:
                        studentsList.append(email)
                studentsList.append(birthday)
                
                
                saveStudentsList( )
                studentsList = [ ]
                loadGlobalVariables( ) 
                idNumber = max(list(studentsDict.keys( )))
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
def doesIdNumberExist(idNumber):
        #idNumberType = type(idNumber)
        #messagebox.showinfo("Info-doesIdNumberExist", f"idNumberType = {idNumberType}")
        #messagebox.showinfo("Info-doesIdNumberExist", f"studentsDict.keys( ) = {studentsDict.keys( )}") # aaa_3
        try:
                lst = studentsDict[idNumber]
                return True, lst
        except KeyError:
                return False, "Given id number does not match any existing student's ID."
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
                #saveStudentsDict( )
                updateStudentsDict( )
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
#=========================       
def deleteExecute(leftFrame):
        permission = messagebox.askyesno("Confirmation", "Are you sure that you want to delete the student's record?")
        if permission == True: # we can use "if permission:" also
                deletedStudent = studentsDict.pop(int(idNumber)) # This will delete student from RAM (dictionary)
                deleteStudentStudentsDict( ) # This will delete student from studentssqlite.db
                messagebox.showinfo("Info", f"{deletedStudent} was deleted.", parent=leftFrame)
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
        createTable( )
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



