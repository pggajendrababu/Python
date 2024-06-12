from tkinter import *
from tkinter import messagebox
import custom as cs
import studentslist as sl


idEntry = ""
nameEntry = ""  # empty space
courseEntry = ""
subjectEntry = ""
genderEntry = ""
cellNumberEntry = 0
emailEntry = ""
birthDayEntry = 0
birthMonthEntry = 0
birthYearEntry = 0
itemNumber = 0
updateButton = "" # empty space (string object)
deleteButton = "" 


#==========================
def clearScreen(frame):
        for widget in frame.winfo_children( ):
                widget.destroy( )
                
                
def exitApp(root):
        root.destroy( )
        

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
                idNumber = sl.createNewId( )
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
                
                
                sl.studentsList.append(student)
                sl.saveStudentsList( )
                resetFields( ) 
                hyphenInsertedIdNumber = sl.insertHyphen(idNumber, 4)
                idEntry.insert(0, hyphenInsertedIdNumber)
                messagebox.showinfo("Sucess", f"A new student info has been added. \nID number = {hyphenInsertedIdNumber}", parent=leftFrame)
        else:
                messagebox.showerror("Error!",f"{result}",parent=leftFrame)



def addNew(leftFrame):
        clearScreen(leftFrame)
        global idEntry, nameEntry, courseEntry, subjectEntry, genderEntry, cellNumberEntry, emailEntry, birthDayEntry,birthMonthEntry, birthYearEntry
        
        
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
        birthDayLabel.grid(row=0, column=2, sticky="ew")
        birthDayEntry = Entry(leftFrame, bd=2)
        birthDayEntry.grid(row=0, column=3)
        
        
        birthMonthLabel = Label(leftFrame, text="Birth month", font=cs.font1, bd=2, bg=cs.colour1)
        birthMonthLabel.grid(row=1, column=2, sticky="ew")
        birthMonthEntry = Entry(leftFrame, bd=2)
        birthMonthEntry.grid(row=1, column=3)


        birthYearLabel = Label(leftFrame, text="Birth year", font=cs.font1, bd=2, bg=cs.colour1)
        birthYearLabel.grid(row=2, column=2, sticky="ew")
        birthYearEntry = Entry(leftFrame, bd=2)
        birthYearEntry.grid(row=2, column=3)
        
        
        addNewButton = Button(leftFrame, text="Add New", font=cs.font1, bd=2, command=lambda: addNewExecute(leftFrame), fg=cs.colour3, bg=cs.colour4)
        addNewButton.grid(row=4, column=3, sticky="ew")
#==========================
def showDetails(idNumberExistMessage):
        resetFields( )
        hyphenInsertedIdNumber = sl.insertHyphen(idNumberExistMessage[0], 4)
        hyphenInsertedCellNumber = sl.insertHyphen(str(idNumberExistMessage[5]), 4)
        birthDay = idNumberExistMessage[7][0:2]
        birthMonth = idNumberExistMessage[7][2:4]
        birthYear = idNumberExistMessage[7][4:8]
        
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
                idNumberExistResult, idNumberExistMessage = sl.doesIdNumberExist(idNumber)
                if idNumberExistResult == True:
                        showDetails(idNumberExistMessage)
                else:
                         messagebox.showerror("Error!", f"{idNumberExistMessage}", parent=leftFrame)
        else:
                messagebox.showerror("Error!", f"{idNumberValidMessage}", parent=leftFrame)
        
        

def viewDetails(leftFrame):
        clearScreen(leftFrame)
        global idEntry, nameEntry, courseEntry, subjectEntry, genderEntry, cellNumberEntry, emailEntry, birthDayEntry,birthMonthEntry, birthYearEntry
        
        
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
        birthDayLabel.grid(row=0, column=2, sticky="ew")
        birthDayEntry = Entry(leftFrame, bd=2)
        birthDayEntry.grid(row=0, column=3)
        
        
        birthMonthLabel = Label(leftFrame, text="Birth month", font=cs.font1, bd=2, bg=cs.colour1)
        birthMonthLabel.grid(row=1, column=2, sticky="ew")
        birthMonthEntry = Entry(leftFrame, bd=2)
        birthMonthEntry.grid(row=1, column=3)


        birthYearLabel = Label(leftFrame, text="Birth year", font=cs.font1, bd=2, bg=cs.colour1)
        birthYearLabel.grid(row=2, column=2, sticky="ew")
        birthYearEntry = Entry(leftFrame, bd=2)
        birthYearEntry.grid(row=2, column=3)
        
        
        viewDetailsButton = Button(leftFrame, text="View Details", font=cs.font1, bd=2, command=lambda: viewDetailsExecute(leftFrame), fg=cs.colour3, bg=cs.colour4)
        viewDetailsButton.grid(row=4, column=3, sticky="ew")
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
                idNumber = idEntry.get( ).strip( ).replace("-", "") # removes "-"
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
                
                
                # modify existing studentsList by assigning a value
                sl.studentsList[itemNumber] = student
                sl.saveStudentsList( )
                messagebox.showinfo("Sucess", "student's info was updated.", parent=leftFrame)
                idEntry.config(state="normal")
                updateButton.config(state="disabled")
                resetFields( )
        else:
                messagebox.showerror("Error!",f"{result}",parent=leftFrame)


def checkUpdate(leftFrame):
        global itemNumber
        idNumber = idEntry.get( ).strip( ).replace("-", "") # replace "-" with empty space = removes "-"
        idNumberValidResult, idNumberValidMessage = sl.isValidIdNumber(idNumber)
        if idNumberValidResult == True:
                idNumberExistResult, idNumberExistMessage = sl.doesIdNumberExist(idNumber)
                if idNumberExistResult == True:
                        #get item number in the studentsList
                        itemNumber = sl.studentsList.index(idNumberExistMessage)
                        showDetails(idNumberExistMessage)
                        idEntry.config(state='disabled')
                        updateButton.config(state="normal")
                else:
                         messagebox.showerror("Error!", f"{idNumberExistMessage}", parent=leftFrame)
        else:
                messagebox.showerror("Error!", f"{idNumberValidMessage}", parent=leftFrame)
        
        

def update(leftFrame):
        clearScreen(leftFrame)
        global idEntry, nameEntry, courseEntry, subjectEntry, genderEntry, cellNumberEntry, emailEntry, birthDayEntry,birthMonthEntry, birthYearEntry, updateButton
        
        
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
        birthDayLabel.grid(row=0, column=2, sticky="ew")
        birthDayEntry = Entry(leftFrame, bd=2)
        birthDayEntry.grid(row=0, column=3)
        
        
        birthMonthLabel = Label(leftFrame, text="Birth month", font=cs.font1, bd=2, bg=cs.colour1)
        birthMonthLabel.grid(row=1, column=2, sticky="ew")
        birthMonthEntry = Entry(leftFrame, bd=2)
        birthMonthEntry.grid(row=1, column=3)


        birthYearLabel = Label(leftFrame, text="Birth year", font=cs.font1, bd=2, bg=cs.colour1)
        birthYearLabel.grid(row=2, column=2, sticky="ew")
        birthYearEntry = Entry(leftFrame, bd=2)
        birthYearEntry.grid(row=2, column=3)
        
        
        checkButton = Button(leftFrame, text="Check", font=cs.font1, bd=2, command=lambda: checkUpdate(leftFrame), fg=cs.colour3, bg=cs.colour4)
        checkButton.grid(row=4, column=2, sticky="ew")
        
        
        updateButton = Button(leftFrame, text="Update", font=cs.font1, bd=2, command=lambda: updateExecute(leftFrame), fg=cs.colour3, bg=cs.colour4, state="disabled")
        updateButton.grid(row=4, column=3, sticky="ew")
#==========================
def deleteExecute(leftFrame):
        permission = messagebox.askyesno("Confirmation", "Are you sure that you want to delete the student's record?")
        if permission == True: # we can use "if permission:" also
                del sl.studentsList[itemNumber]
                sl.saveStudentsList( )
                messagebox.showinfo("Info", "student's info was deleted.", parent=leftFrame)
                idEntry.config(state="normal")
                deleteButton.config(state="disabled")
                resetFields( )
        else:
                messagebox.showinfo("Info", "deletion canceled.", parent=leftFrame)
                idEntry.config(state="normal")
                deleteButton.config(state="disabled")
                resetFields( )


def checkDelete(leftFrame):
        global itemNumber
        idNumber = idEntry.get( ).strip( ).replace("-", "") # replace "-" with empty space = removes "-"
        idNumberValidResult, idNumberValidMessage = sl.isValidIdNumber(idNumber)
        if idNumberValidResult == True:
                idNumberExistResult, idNumberExistMessage = sl.doesIdNumberExist(idNumber)
                if idNumberExistResult == True:
                        #get item number in the studentsList
                        itemNumber = sl.studentsList.index(idNumberExistMessage)
                        showDetails(idNumberExistMessage)
                        idEntry.config(state='disabled')
                        deleteButton.config(state="normal")
                else:
                         messagebox.showerror("Error!", f"{idNumberExistMessage}", parent=leftFrame)
        else:
                messagebox.showerror("Error!", f"{idNumberValidMessage}", parent=leftFrame)
        


def delete(leftFrame):
        clearScreen(leftFrame)
        global idEntry, nameEntry, courseEntry, subjectEntry, genderEntry, cellNumberEntry, emailEntry, birthDayEntry,birthMonthEntry, birthYearEntry, deleteButton
        
        
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
        birthDayLabel.grid(row=0, column=2, sticky="ew")
        birthDayEntry = Entry(leftFrame, bd=2)
        birthDayEntry.grid(row=0, column=3)
        
        
        birthMonthLabel = Label(leftFrame, text="Birth month", font=cs.font1, bd=2, bg=cs.colour1)
        birthMonthLabel.grid(row=1, column=2, sticky="ew")
        birthMonthEntry = Entry(leftFrame, bd=2)
        birthMonthEntry.grid(row=1, column=3)


        birthYearLabel = Label(leftFrame, text="Birth year", font=cs.font1, bd=2, bg=cs.colour1)
        birthYearLabel.grid(row=2, column=2, sticky="ew")
        birthYearEntry = Entry(leftFrame, bd=2)
        birthYearEntry.grid(row=2, column=3)
        
        
        checkButton = Button(leftFrame, text="Check", font=cs.font1, bd=2, command=lambda: checkDelete(leftFrame), fg=cs.colour3, bg=cs.colour4)
        checkButton.grid(row=4, column=2, sticky="ew")
        
        
        deleteButton = Button(leftFrame, text="Delete", font=cs.font1, bd=2, command=lambda: deleteExecute(leftFrame), fg=cs.colour7, bg=cs.colour4, state="disabled")
        deleteButton.grid(row=4, column=3, sticky="ew")
#=========================        

        

def main( ):
        sl.loadGlobalVariables( )
        sl.resetSerialNumber( )
        
        
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
        
        
        viewButton = Button(rightFrame, text="View Details", font=cs.font1, bd=2, command=lambda: viewDetails(leftFrame), fg=cs.colour3, bg=cs.colour4)
        viewButton.grid(row=1, column=0, sticky="ew")
        
        
        updateButton = Button(rightFrame, text="Update", font=cs.font1, bd=2, command=lambda: update(leftFrame), fg=cs.colour3, bg=cs.colour4)
        updateButton.grid(row=2, column=0, sticky="ew")
        
        
        deleteButton = Button(rightFrame, text="Delete", font=cs.font1, bd=2, command=lambda: delete(leftFrame), fg=cs.colour3, bg=cs.colour4)
        deleteButton.grid(row=3, column=0, sticky="ew")
        
        
        clearButton = Button(rightFrame, text="Clear", font=cs.font1, bd=2, command=lambda: clearScreen(leftFrame), fg=cs.colour3, bg=cs.colour4)
        clearButton.grid(row=4, column=0, sticky="ew")
        
        
        exitButton = Button(rightFrame, text="Exit", font=cs.font1, bd=2, command=lambda: exitApp(root), fg=cs.colour3, bg=cs.colour4)
        exitButton.grid(row=5, column=0, sticky="ew")
        
        
        root.mainloop( )
        
        
if __name__ == "__main__":
        main( )