# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JPatoc,2023-08-08,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants

strFile = "ToDoList.txt"    # Name of the text file what the program will reference
objFile = None  # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
lstRow = []    # A list that will hold individual rows from the table
strMenu = """
    Menu of Options:
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """   # A menu of user options
strChoice = ""  # Capture the user option selection
strTask = ""    # Capture the Task
strPriority = ""    # Capture the Priority


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, 'r')
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == "1":
        for row in lstTable:
            strTask = row["Task"]
            strPriority = row["Priority"]
            print(strTask, " | ", strPriority)
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == "2":
        strTask = input("Enter a Task: ")
        strPriority = input("Enter a Priority: ")
        lstTable.append({"Task": strTask, "Priority": strPriority})     # add data to table using tuple unpacking
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        strTask = input("Which Task Would You Like to Remove?: ")
        for row in lstTable:
            if row["Task"].lower() == strTask.lower():
                lstTable.remove(row)
                print("Row Removed")
                break
        else:
            print("Task Not Found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("Data Saved to File!")
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Program Closing. Goodbye!")
        break  # and Exit the program
    else:
        print("Invalid Selection. Please Make a Selection From The Following Menu:")
