from datetime import datetime as dt, timedelta

"""
If there is sudden power cut, 
same ID will be creted for two 
different people. so to avoid 
such scenario, we should always 
store all global variables in a 
separate txt file. All global 
variables should be updated 
immediately. All global variables 
should be *only* loaded from 
that txt file.


similarly, all students data 
should be stored in a separate 
txt file.
"""

# 2024-04-28 12.00 AM
serialNumberPreviousResetTime = dt(2024, 4, 28, 0)
serialNumber = 1
studentsList = [ ]


#============================
def loadGlobalVariables( ):
        global serialNumberPreviousResetTime, serialNumber
        try:
                with open("globalvariables.txt") as file:
                        line1 = file.readline( )
                        line2 = file.readline( )
                        
                        lst = line1.strip( ).split(",")
                        #print(lst)
                        year = int(lst[0][1: ])
                        #print(year)
                        month = int(lst[1])
                        #print(month)
                        day = int(lst[2])
                        hour = int(lst[3])
                        minute = int(lst[4])
                        second = int(lst[5][ : -1])
                        #print(second)
                        serialNumberPreviousResetTime = dt(year, month, day, hour, minute, second)
                        
                        
                        serialNumber =  int(line2.strip( ))
        except FileNotFoundError:
                pass
                
                
        try:
                with open("studentslist.txt", "r") as file:
                        student = [ ]
                        # read first line
                        line = file.readline( ) # aaa_3
                        while line: # aaa_2
                                lst = line.strip( ).split(",") # aaa_4
                                #print(f"lst = {lst}")
                                
                                
                                idNumber = lst[0][1: ].strip(" '") # double quote, empty space, single quote, double quote (removes empty space and single quote from LHS and RHS of the line.). [1: ] will remove left square bracket from idNumber while reading back from the studentslist.txt
                                name = lst[1].strip(" '") # aaa_5
                                
                                #print(f"name = {name}")
                                course = lst[2].strip(" '")
                                subject = lst[3].strip(" '")
                                #print(subject)
                                gender = lst[4].strip(" '")
                                cellNumber = int(lst[5])
                                #print(f"cellNumber = {cellNumber}")
                                email = lst[6].strip(" '")
                                birthday = lst[7][ :-1].strip(" '") # [ :-1] will remove right square bracket from birthday while reading back from the studentslist.txt
                                
                                
                                student.append(idNumber)
                                student.append(name)
                                student.append(course)
                                student.append(subject)
                                student.append(gender)
                                student.append(cellNumber)
                                student.append(email)
                                student.append(birthday)
                                studentsList.append(student)
                                
                                
                                student = [ ]
                                # read next line
                                line = file.readline( )
        except FileNotFoundError:
                pass        
        
        
def saveGlobalVariables( ):
        global serialNumberPreviousResetTime, serialNumber
        with open("globalvariables.txt", "w") as file:
                lst = [ ]
                year = serialNumberPreviousResetTime.year
                month = serialNumberPreviousResetTime.month
                day = serialNumberPreviousResetTime.day
                hour = serialNumberPreviousResetTime.hour
                minute = serialNumberPreviousResetTime.minute
                second = serialNumberPreviousResetTime.second
                lst.append(year)
                lst.append(month)
                lst.append(day)
                lst.append(hour)
                lst.append(minute)
                lst.append(second)
                file.write(str(lst) + "\n")
                file.write(str(serialNumber) + "\n")
                
                
def saveStudentsList( ):
        with open("studentslist.txt", "w") as file:
                for lst in studentsList:
                        #print(f"lst = {lst}")
                        file.write(str(lst) + "\n")

                
                
def resetSerialNumber( ):
        global serialNumber, serialNumberPreviousResetTime
        
        
        currentTime = dt.now( )
        timeDifference = currentTime - serialNumberPreviousResetTime
        
        
        """
        we can't write like the following statement
        if timeDifference >= 24:
          
              
        we will get error like :
        TypeError: '>=' not supported               
        between instances of 'datetime.         
        timedelta' (object) and 'int'.
        
        
        so we convert 24 hours into an object using "timedelta"
        """
        #print(timedelta(hours=24))
        
        if timeDifference >= timedelta(hours = 24):
                serialNumber = 1
                year = currentTime.year
                month = currentTime.month
                day = currentTime.day
                # current date, but time = 12.00.00AM
                # Following line will change serialNumberPreviousResetTime 
                # in the RAM
                serialNumberPreviousResetTime = dt(year, month, day, 0)
                # Following line will change serialNumberPreviousResetTime 
                # in the globalvariables.txt
                saveGlobalVariables( )
#============================
def insertHyphen(givenString, number):
        lst = list(givenString)
        hyphenInsertedList = [ ]
        #print(f"len(lst) = {len(lst)}")
        for i in range(len(lst)):
                if i != 0 and i % number == 0:
                        hyphenInsertedList.append("-")
                hyphenInsertedList.append(lst[i])
        hyphenInsertedString = "".join(hyphenInsertedList)
        return hyphenInsertedString


def insertHyphenBirthDay(givenString):
        lst = list(givenString)
        hyphenInsertedList = [ ]
        #print(f"len(lst) = {len(lst)}")
        for i in range(len(lst)):
                if i == 2 or i == 4:
                        hyphenInsertedList.append("-")
                hyphenInsertedList.append(lst[i])
        hyphenInsertedString = "".join(hyphenInsertedList)
        return hyphenInsertedString


def correctBirthday(birthDay, birthMonth, birthYear):
        day = str(birthDay).zfill(2)
        month = str(birthMonth).zfill(2)
        year  = str(birthYear).zfill(4)
        birthday = day + month + year
        return birthday
                
                
def checkType( ):
        count = 1
        for list in studentsList: # studentsList may be a "list of lists" or "list of strings"
            print(f"count = {count}")
            for  element in list: # list may be a list or string
                    print(f"element = {element}")
                    print(f"type(element) = {type(element)}")
            count += 1
            print("-"*40)         
#============================
def isValidIdNumber(givenString):
        if givenString == "": # empty space
                return False, "id number cannot be empty."
        else:
                for char in givenString:
                        if char.isdecimal( ) == True or char == "-":
                                pass      
                        else:
                                return False, f"'{char}' is not allowed. Except numbers and hyphen (-), other letters are not allowed in id number." # in order to print space, I have given ' on both sides of {char}.
                return True, None
                
                
def isValidName(givenString):
        if givenString == "": # empty space
                return False, "name cannot be empty."
        else:
                for char in givenString:
                        if char.isalpha( ) == True or char.isspace( ) == True or char == ".":
                                pass      
                        else:
                                return False, f"{char} is not allowed. Except alphabets, space and dot, other letters are not allowed in name."
                return True, None
        
        
def isValidCourse(givenString):
        if givenString == "": # empty space
                return False, "course cannot be empty."
        else:
                for char in givenString:
                        if char.isalpha( ) == True or char.isspace( ) == True or char == ".":
                                pass      
                        else:
                                return False, f"{char} is not allowed. Except alphabets, space and dot, other letters are not allowed in course."
                return True, None


def isValidSubject(givenString):
        if givenString == "": # empty space
                return False, "subject cannot be empty."
        else:
                for char in givenString:
                        if char.isalpha( ) == True or char.isspace( ) == True or char == ".":
                                pass      
                        else:
                                return False, f"{char} is not allowed. Except alphabets, space and dot, other letters are not allowed in subject."
                return True, None


def isValidGender(givenString):
        if givenString == "": # empty space
                return False, "gender cannot be empty."
        else:
                for char in givenString:
                        if char.isalpha( ) == True or char.isspace( ) == True or char == ".":
                                pass      
                        else:
                                return False, f"{char} is not allowed. Except alphabets, space and dot, other letters are not allowed in gender."
                return True, None


def isValidCellNumber(givenString):
        if givenString == "": # empty space
                return False, "cell number cannot be empty."
        else:
                for char in givenString:
                        if char.isdecimal( ) == True or char == "-":
                                pass      
                        else:
                                return False, f"'{char}' is not allowed. Except numbers and hyphen (-), other letters are not allowed in cell number." # in order to print space, I have given ' on both sides of {char}.
                return True, None


def isValidBirthDay(givenString):
        acceptableRange = range(1, 32)
        if givenString == "": # empty space
                return False, "birth day cannot be empty."
        else:
                #case1
                for char in givenString:
                        if char.isdecimal( ) == True:
                                pass      
                        else:
                                return False, f"'{char}' is not allowed. Except numbers, other letters are not allowed in birth day."
                #case2
                if int(givenString) not in acceptableRange:
                        return False, "birth day should be between 1 and 31."
                return True, None


def isValidBirthMonth(givenString):
        acceptableRange = range(1, 13)
        if givenString == "": # empty space
                return False, "birth month cannot be empty."
        else:
                #case1
                for char in givenString:
                        if char.isdecimal( ) == True:
                                pass      
                        else:
                                return False, f"'{char}' is not allowed. Except numbers, other letters are not allowed in birth month."  # in order to print space, I have given ' on both sides of {char}
                #case2
                if int(givenString) not in acceptableRange:
                        return False, "birth month should be between 1 and 12."
                return True, None


def isValidBirthYear(givenString):
        year = dt.now( ).year
        acceptableRange = range(year-130, year+1)
        if givenString == "": # empty space
                return False, "birth year cannot be empty."
        else:
                #case1
                for char in givenString:
                        if char.isdecimal( ) == True:
                                pass      
                        else:
                                return False, f"'{char}' is not allowed. Except numbers, other letters are not allowed in birth year."  # in order to print space, I have given ' on both sides of {char}
                #case2
                if int(givenString) not in acceptableRange:
                        return False, f"birth year should be >= {year-130} and <= {year}."
                return True, None
#============================
def doesIdNumberExist(idNumber):
        for list in studentsList:
                if idNumber == list[0]:
                        return True, list
        return False, "Given id number does not match any existing student's ID."


def createNewId( ):
        global serialNumber
        day = dt.now( ).day
        month = dt.now( ).month
        year = dt.now( ).year
        idNumber =  str(day).zfill(2) + str(month).zfill(2) + str(year).zfill(4) + str(serialNumber).zfill(7)
        idNumberExistResult, idNumberExistMessage = doesIdNumberExist(idNumber)
        if idNumberExistResult == False:
                serialNumber += 1
                saveGlobalVariables( )
                return idNumber
        else:
                #print(f"{idNumberExistMessage} already exists with same id")
                serialNumber += 1
                saveGlobalVariables( )
                createNewId( )
#============================
def areAllFieldsOk( ):
        
        while True:
                name = input("Enter name : ").strip( )
                nameValidResult, nameValidMessage = isValidName(name)
                if nameValidResult == True:
                        break
                else:
                        print(nameValidMessage)
        while True:
                course = input("Enter course : ").strip( )
                courseValidResult, courseValidMessage = isValidCourse(course)
                if courseValidResult == True:
                        break
                else:
                        print(courseValidMessage)
        while True:
                subject = input("Enter subject : ").strip( )
                subjectValidResult, subjectValidMessage = isValidSubject(subject)
                if subjectValidResult == True:
                        break
                else:
                        print(subjectValidMessage)
        while True:
                gender = input("Enter gender : ").strip( )
                genderValidResult, genderValidMessage = isValidGender(gender)
                if genderValidResult == True:
                        break
                else:
                        print(genderValidMessage)
        while True:
                cellNumber = input("Enter cell number : ").strip( ).replace("-", "") # replace "-" with empty space = removes "-"
                cellNumberValidResult,  cellNumberValidMessage = isValidCellNumber(cellNumber)
                if cellNumberValidResult == True:
                        break
                else:
                        print(cellNumberValidMessage)
        email = input("Enter email : ")
        while True:
                birthDay = input("Enter birth day : ").strip( )
                birthDayValidResult, birthDayValidMessage = isValidBirthDay(birthDay)
                if birthDayValidResult == True:
                        break
                else:
                        print(birthDayValidMessage)
        while True:
                birthMonth = input("Enter birth month : ").strip( )
                birthMonthValidResult, birthMonthValidMessage = isValidBirthMonth(birthMonth)
                if birthMonthValidResult == True:
                        break
                else:
                        print(birthMonthValidMessage)
        while True:
                birthYear = input("Enter birth year : ").strip( )
                birthYearValidResult, birthYearValidMessage = isValidBirthYear(birthYear)
                if birthYearValidResult == True:
                        break
                else:
                        print(birthYearValidMessage)
        return True, name, course, subject, gender, cellNumber, email, birthDay, birthMonth, birthYear


def addNew( ):
        student = [ ]
        
        result, name, course, subject, gender, cellNumber, email,  birthDay, birthMonth, birthYear = areAllFieldsOk( )
        if result == True:
                birthday = correctBirthday(birthDay, birthMonth, birthYear)
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
        
        
                studentsList.append(student)
                saveStudentsList( )
                hyphenInsertedIdNumber = insertHyphen(idNumber, 4)
                print(f"A new student info has been added. \nID number = {hyphenInsertedIdNumber}")
        else:
                pass
#============================
def showDetails(idNumberExistMessage):
        hyphenInsertedIdNumber = insertHyphen(idNumberExistMessage[0], 4)
        hyphenInsertedCellNumber = insertHyphen(str(idNumberExistMessage[5]), 4)
        hyphenInsertedBirthDay = insertHyphenBirthDay(idNumberExistMessage[7])
        print(f"id = {hyphenInsertedIdNumber}")
        print(f"name = {idNumberExistMessage[1]}")
        print(f"course = {idNumberExistMessage[2]}")
        print(f"subject = {idNumberExistMessage[3]}")
        print(f"gender = {idNumberExistMessage[4]}")
        print(f"cell number = {hyphenInsertedCellNumber}")
        print(f"email = {idNumberExistMessage[6]}")
        print(f"birthday = {hyphenInsertedBirthDay}")                
        
def getIdNumber( ):
        while True:
                givenString = input("Enter student's id number : ").strip( ).replace("-", "") # removes hyphen
                idNumberValidResult, idNumberValidMessage = isValidIdNumber(givenString)
                if idNumberValidResult == True:
                        return givenString
                else:
                        print(idNumberValidMessage)


def viewDetails( ):
        idNumber = getIdNumber( )
        idNumberExistResult, idNumberExistMessage = doesIdNumberExist(idNumber)
        if idNumberExistResult == True:
                showDetails(idNumberExistMessage)
        else:
                print(idNumberExistMessage)   
#============================      
def update( ):
        idNumber = getIdNumber( )
        idNumberExistResult, idNumberExistMessage = doesIdNumberExist(idNumber)
        if idNumberExistResult == True:
                showDetails(idNumberExistMessage)
                print("-"*40)
                #get item number in the studentsList
                itemNumber = studentsList.index(idNumberExistMessage)
                
                student = [ ]
                #get updated info
                result, name, course, subject, gender, cellNumber, email,  birthDay, birthMonth, birthYear = areAllFieldsOk( )
                birthday = correctBirthday(birthDay, birthMonth, birthYear)
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
                studentsList[itemNumber] = student
                saveStudentsList( )
                print( )
                print("student's info was updated.")
        else:
                print(idNumberExistMessage) 
#============================ 
def delete( ):
        idNumber = getIdNumber( )
        idNumberExistResult, idNumberExistMessage = doesIdNumberExist(idNumber)
        if idNumberExistResult == True:
                showDetails(idNumberExistMessage)
                print("-"*40)
                #get item number in the studentsList
                itemNumber = studentsList.index(idNumberExistMessage)
                permission = input("Are you sure you want to delete the above student (yes/no)?")
                if permission.lower( ) == "yes":
                        del studentsList[itemNumber]
                        saveStudentsList( )
                        print(f"{idNumberExistMessage} \n\nwas deleted")
                elif permission.lower( ) == "no":
                        print("deletion canceled.")
                else:
                        print("Invalid input. deletion canceled.")
        else:
                print(f"Given id number does not match any existing student's ID.")
          

def main( ):
        loadGlobalVariables( )
        resetSerialNumber( )
        #for list in studentsList:
                #print(list)
        #checkType( )
        
         
        while True:
                print("\n1. Add Student\n2. View Details\n3. Update\n4. Delete Student\n5. Exit")
                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                        addNew( )
                elif choice == '2':
                        viewDetails( )
                elif choice == '3':
                        update( )
                elif choice == '4':
                        delete( )
                elif choice == '5':
                        print("Exiting program. Goodbye!")
                        break
                else:
                        print("Invalid choice. Please enter a number between 1 and 5.")
        
        

if __name__ == "__main__":
        main( )
        

        
"""
file.readline() reads a single line 
from the file, starting from the 
current position of the file pointer, 
and moves the pointer to the next 
line.


file.read() reads the entire file and 
returns its contents as a *string*. 


file.readlines() reads *all the lines of the file* and returns them as a *list of strings*, where each string represents a single line. 

I think, 
file.read( ).splitlines( ) = file.readlines( )


Is the following two are absolutely equal?
1) file.read( ).splitlines( )
2) file.readlines( )

chatGPT


Both methods, file.read().splitlines() 
and file.readlines(), essentially read 
lines from a file, but they're not 
absolutely equal.


file.read().splitlines() reads the 
entire file into memory as a single 
string and then splits it into lines 
based on newline characters. This 
could be memory-intensive for 
large files.


file.readlines() reads all the lines of 
the file and returns them as a list. 
It's more memory-efficient because 
it doesn't load the entire file into 
memory at once. However, it still 
reads the entire file into memory, 
so for extremely large files, it might 
not be the best choice either.

#*********************************
So, they are similar but have 
differences in terms of memory 
usage and potentially performance 
depending on the size of the file.
#*********************************

"""
                
                                
        
"""
aaa_0
when I just used
data = file.read( )

instead of using
data = file.read( ).splitlines( )

I got a strange confusing following 
error :
SyntaxError: '[' was never closed

Then chatGPT suggested using splitlines(), which will split data into separate lines whenever it sees "\n",which actually solved the error.
so, always use splitlines() along with file.read().


#*********************************
aaa_3 

very important lesson
------------------------------------

Initially I used a line like
file.read( ).splitlines( ).
(Infact file.readlines( ) also will do 
the same following thing)

This will make a list from a txt file like (if we read from a txt file)
[ '[', 'R', 'a', 'k', 'e', 's', 'h', ' ', '9', '6', '2', '9', '4', '5',  '5', '1', '2', '3', ' ', ......']' ]

Instead of treating "Rakesh" as a single string, file.read( ).splitlines( )
makes "every letter" as a separate string ['R', 'a', 'k', 'e', 's', 'h'], which makes it difficult to reconstruct a list from the txt file.

so while reading from a file 
(especially for lists and 
dictionaries), 
always use file.readline( ) as in this file (def loadGlobalVariables( ) line aaa_3). 


file.read( ).splitlines( ),
file.readlines( ) are only
suitable to read some text from
a file. They are not suitable to read a list or dictionary from a txt file.
#*********************************



aaa_1

Why using using eval( ) is not recommended?

chatGPT


Using eval() in programming is 
often discouraged due to security 
risks and potential performance 
issues.


Security Risks: eval() executes 
code passed to it as a string, which 
can be dangerous if the string 
originates from an untrusted 
source. It can lead to code injection 
vulnerabilities, allowing attackers 
to execute arbitrary code on the 
system.


Performance: eval() is generally 
slower compared to other methods 
of executing code because it needs 
to parse and interpret the string 
each time it's called.


Instead of 
using eval(), it's better to use 
alternative methods such as 
specific functions, libraries, or 
language constructs designed for 
the task at hand. This helps ensure 
better security and performance.


Sure, here's an example to illustrate the potential risks of using eval():


# Example 1: Using eval() with user input (Unsafe)

user_input = input("Enter a mathematical expression: ")
result = eval(user_input)
print("Result:", result)


In this example, if a user inputs 
os.system('rm -rf /'), 
eval() would execute it, leading to 
the deletion of files on the system. 
This is a serious security 
vulnerability known as code 
injection.


Now, let's see how to achieve the same functionality without using eval():
    
    
# Example 2: Safe alternative without eval()

user_input = input("Enter a mathematical expression: ")

try:
    result = eval(user_input)
    print("Result:", result)
except Exception as e:
    print("Error:", e)
    

In this safer version, we use a try 
block to catch any errors that might 
occur during the evaluation of the 
expression. However, even with 
this handling, it's still risky to use 
eval() with untrusted input.


A better 
approach would be to use specific 
functions or libraries designed for 
mathematical evaluation, such as 



the ast module or libraries like 
numexpr or sympy, 


depending on 
the requirements of the application.
These methods provide safer and 
more controlled ways of evaluating 
expressions without the security 
risks associated with eval().


aaa_2
#*********************************
In python
"positive value" is considered as True.
0 or empty is considered as False.

line exists means True.
line does not exists means False.


In the line, 
while line: # means
"while line is not empty"
while line != "" # (empty string)
while line != EOF # end of file
#*********************************
It's a common idiom 
in Python to use the truthiness of 
objects in control flow statements.


Both while line and while line != "" # (empty string)
will work in this case because 
when file.readline() reaches the 
end of the file, it returns an empty 
string, which evaluates to False in a 
boolean context, causing the loop 
to exit.

#*********************************
method1:
x = 0
while x < 5:
    do something
    x += 1
    
    
method2:
x = 5
while x != 0:
    do something
    x -= 1


similar to method2:
line = file.readline.strip( )
while line: # while line != "" (empty string)
    do something
    # read the next line
    line = file.readline.strip( )
#-----------------------------------
method3 :
x = 5
while True: # Always execute the while loop continuously
    do something
    if x = 0:
        break
    x -= 1


similar to method3:
while True: # Always execute the while loop continuously
    line = file.readline().strip()
    if not line:  # EOF (End of file) see Note.
        break
    do something

Note :
if line: means
if line != "" # empty string = EOF
similarly,
if not line: means
if line = "" # empty string = EOF
#*********************************   


aaa_4
lst = line.split(",").strip( )
Will it first strip and then split? Or
Will it first split and then strip?


chatGPT


The code lst = line.split(",").strip() 
will cause an error because `split` 
returns a list, and lists do not have 
a `strip` method.

However, assuming the intention is 
to first strip the string and then 
split it, the correct code should be:


lst = line.strip().split(",")


This code will first strip any leading 
and trailing whitespace from the 
string `line` and then split the 
stripped string by commas. 


So, the 
sequence of operations is: 

LHS to RHS
1. Strip the string.
2. Split the stripped string.


aaa_5
extra square brackets problem :
---------------------------------------------------
["['150520240000008", 't', 't', 't', 't', 4, '4', "05042000']"]
['150520240000009', 'er', 'er', 'er', 'er', 56, None, '04042000']


The above lines are from 
studentslist.txt
whenever I added a new item, new 
square bracket was added to old 
items. This error happened 
because of the following lines.
This happens because while 
reading back from the file, python 
does not remove the left and right 
square brackets from the item. It 
happened because of the following 
lines.
    
    
idNumber = lst[0].strip(" '") # double quote, empty space, single quote, double quote (removes empty space and single quote from LHS and RHS of the line.)
                                name = lst[1][1: ].strip(" '") # aaa_5
                                
look at aaa_5. 
[1: ] appears in name, but not in idNumber (previous line).
*THAT* is the problem. If [1: ] was in idNumber, then that left square bracket would have been removed.


"""




    