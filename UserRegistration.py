#Reference and code taken from https://pynative.com/python-sqlite-insert-into-table/
import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3
import tkinter.font



class HomePage:
    #initializing homepage
    def __init__(self):
        self.homePageWindow = tkinter.Tk() # creating window
        self.homePageWindow.wm_title("Home Page")

        #main page lable
        tkinter.Label(self.homePageWindow, text="Welcome To Summer Camp Registration", font=('Verdana 22 bold'), width=50).grid(pady=10, column=1,
                                                                                                row=1)
        #homepage buttons
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Register New User", bg='#0096D6', font=('Verdana 15 bold'), command=self.Insert).grid(pady=10, column=1, row=2)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Update Existing Record", bg='#ffc912', font=('Verdana 15 bold'), command=self.Update).grid(pady=15, column=1, row=3)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Search Existing Record", bg='#65d73a', font=('Verdana 15 bold'), command=self.Search).grid(pady=15, column=1, row=4)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Delete Existing Record", bg='#ed7124', font=('Verdana 15 bold'), command=self.Delete).grid(pady=15, column=1, row=5)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Display All User Record", bg='#64ad6a', font=('Verdana 15 bold'), command=self.Display).grid(pady=15, column=1,
                                                                                                 row=6)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Exit", bg='#ed243b', font=('Verdana 15 bold'), command=self.homePageWindow.destroy).grid(pady=15,
                                                                                                             column=1,
                                                                                                            row=7)
        #application main-loop, application ready to run
        self.homePageWindow.mainloop()

    #defining insert
    def Insert(self):
        self.insertData = InsertData()

    #defining update
    def Update(self):
        self.updateIDWindow = tkinter.Tk()
        self.updateIDWindow.wm_title("Update Data")

        # Initializing all the variables
        self.id = tkinter.StringVar()

        # Label
        #insert form to update existing record
        tkinter.Label(self.updateIDWindow, text="Enter the Student ID to update", width=50).grid(pady=20, row=1)

        # Entry widgets
        #update window
        self.idEntry = tkinter.Entry(self.updateIDWindow, width=5, textvariable=self.id)

        self.idEntry.grid(pady=10, row=2)

        # Button widgets
        # Update window button
        tkinter.Button(self.updateIDWindow, width=20, text="Update", bg='#ffc912', font=('Verdana 10 bold'), command=self.updateID).grid(pady=10, row=3)
        # update task ready to run, main loop
        self.updateIDWindow.mainloop()

    def updateID(self):
        self.updateWindow = UpdateData(self.idEntry.get())
        # to destroy update window after submiting data
        self.updateIDWindow.destroy()

    # to search function to search record
    def Search(self):
        self.searchWindow = SearchDeleteData("Search")

    # to delete function to delete record
    def Delete(self):
        self.deleteWindow = SearchDeleteData("Delete")

    # display database view, calling from UserData class
    def Display(self):
        self.database = UserDatabase()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)


#Inserting data
class InsertData:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.wm_title("Camp User Registraion")

        # Initializing all the variables
        #Input type text field
        self.id = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.dob = tkinter.StringVar()
        self.mob = tkinter.StringVar()
        self.yob = tkinter.StringVar()
        self.gender = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phoneNo = tkinter.StringVar()
        self.emailId = tkinter.StringVar()
        self.indoorGame = tkinter.StringVar()
        self.outdoorGame = tkinter.StringVar()
        #input type list menu
        self.genderList = ["Male", "Female", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.yearList = list(range(1900, 2020))
        self.indoorgameslist = ["karate", "wushu", "Squash", "Soccer", "Table Tennis", "Lawn Tennis", "Chess",
                                "Swimming"]
        self.outdoorgameslist = ["Football", "Cricket", "Badminton", "Soccer", "Table Tennis", "Lawn Tennis", "Chess",
                                 "Swimming"]

        # List of labels for user registration form
        tkinter.Label(self.window, text="Student ID", width=25).grid(pady=5, column=1, row=1)
        tkinter.Label(self.window, text="First Name", width=25).grid(pady=5, column=1, row=2)
        tkinter.Label(self.window, text="Last Name", width=25).grid(pady=5, column=1, row=3)
        tkinter.Label(self.window, text="D.O.B", width=25).grid(pady=5, column=1, row=4)
        tkinter.Label(self.window, text="M.O.B", width=25).grid(pady=5, column=1, row=5)
        tkinter.Label(self.window, text="Y.O.B", width=25).grid(pady=5, column=1, row=6)
        tkinter.Label(self.window, text="Gender", width=25).grid(pady=5, column=1, row=7)
        tkinter.Label(self.window, text="Address", width=25).grid(pady=5, column=1, row=8)
        tkinter.Label(self.window, text="Phone Number", width=25).grid(pady=5, column=1, row=9)
        tkinter.Label(self.window, text="Email ID", width=25).grid(pady=5, column=1, row=10)
        tkinter.Label(self.window, text="Indoor Games", width=25).grid(pady=5, column=1, row=11)
        tkinter.Label(self.window, text="Outdoor Games", width=25).grid(pady=5, column=1, row=12)

        # Form Fields
        # Input text Entry widgets
        self.idEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.id)
        self.fNameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.fName)
        self.lNameEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.lName)
        self.addressEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.address)
        self.phoneNoEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.phoneNo)
        self.emailIdEntry = tkinter.Entry(self.window,  width = 25, textvariable = self.emailId)

        # Setting-up entry widgets row by numbering order
        self.idEntry.grid(pady = 5, column = 3, row = 1)
        self.fNameEntry.grid(pady = 5, column = 3, row = 2)
        self.lNameEntry.grid(pady = 5, column = 3, row = 3)
        self.addressEntry.grid(pady = 5, column = 3, row = 8)
        self.phoneNoEntry.grid(pady = 5, column = 3, row = 9)
        self.emailIdEntry.grid(pady = 5, column = 3, row = 10)

        # Drop-Down widgets
        # Input text using drop-down list
        self.dobBox = tkinter.ttk.Combobox(self.window, values = self.dateList, width = 20)
        self.mobBox = tkinter.ttk.Combobox(self.window, values = self.monthList, width = 20)
        self.yobBox = tkinter.ttk.Combobox(self.window, values = self.yearList, width = 20)
        self.genderBox = tkinter.ttk.Combobox(self.window, values = self.genderList, width = 20)
        self.indoorGameBox = tkinter.ttk.Combobox(self.window, values = self.indoorgameslist, width = 20)
        self.outdoorGameBox = tkinter.ttk.Combobox(self.window, values = self.outdoorgameslist, width = 20)

        # Setting-up entry widgets row by numbering order
        self.dobBox.grid(pady = 5, column = 3, row = 4)
        self.mobBox.grid(pady = 5, column = 3, row = 5)
        self.yobBox.grid(pady = 5, column = 3, row = 6)
        self.genderBox.grid(pady = 5, column = 3, row = 7)
        self.indoorGameBox.grid(pady = 5, column = 3, row = 11)
        self.outdoorGameBox.grid(pady = 5, column = 3, row = 12)

        # Button widgets
        #Insert, Reset, Close
        tkinter.Button(self.window, width = 20, text = "Insert", bg='#0096D6', font=('Verdana 10 bold'), command = self.Insert).grid(pady = 15, padx = 5, column = 1, row = 14)
        tkinter.Button(self.window, width = 20, text = "Reset", bg='#ffc912', font=('Verdana 10 bold'),  command = self.Reset).grid(pady = 15, padx = 5, column = 2, row = 14)
        tkinter.Button(self.window, width = 20, text = "Close", bg='#ed243b', font=('Verdana 10 bold'), command = self.window.destroy).grid(pady = 15, padx = 5, column = 3, row = 14)

        #window.mainloop ready to run
        self.window.mainloop()

    #Insert function to get values from user
    def Insert(self):
        self.values = FormValidation() #From FormValidation for validation
        self.database = UserDatabase() #From Database class
        self.fieldvalid = self.values.Validation(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(), self.phoneNoEntry.get(), self.emailIdEntry.get())
        if (self.fieldvalid == "SUCCESS"): #Checking validation
            self.database.Insert(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(), self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(), self.phoneNoEntry.get(), self.emailIdEntry.get(), self.indoorGameBox.get(), self.outdoorGameBox.get())
            tkinter.messagebox.showinfo("Data Inserted", "Data has been inserted successfully!!!")

        else:
            self.valueErrorMessage = "Invalid input " + self.fieldvalid
            tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    #To Reset all form fields
    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)
        self.dobBox.set("")
        self.mobBox.set("")
        self.yobBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.phoneNoEntry.delete(0, tkinter.END)
        self.emailIdEntry.delete(0, tkinter.END)
        self.indoorGameBox.set("")
        self.outdoorGameBox.set("")


#Validation class for
#Form field id, fName, lName, phoneNo & emailId
class FormValidation:
    def Validation(self, id, fName, lName, phoneNo, emailId):
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif not (fName.isalpha()):
            return "fName"
        elif not (lName.isalpha()):
            return "lName"
        elif not (phoneNo.isdigit() and (len(phoneNo) == 10)):
            return "phoneNo"
        elif not (emailId.count("@") == 1 and emailId.count(".") > 0):
            return "emailId"
        else:
            return "SUCCESS"


#Database class with database connection
class UserDatabase:
    def __init__(self):
        self.dbConnection = sqlite3.connect("dbfile.db") #database file will create using name "dbfile.db"
        self.dbCursor = self.dbConnection.cursor() #DB connection
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS user_record (id PRIMARYKEY text, fName text, lName text, dob text, mob text, yob text, gender text, address text, phoneNo text, emailId text, indoorGame text, OutdoorGame text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close() #to close DB connection

#inserting data into database
    def Insert(self, id, fName, lName, dob, mob, yob, gender, address, phoneNo, emailId, indoorGame, outdoorGame):
            self.dbCursor.execute("INSERT INTO user_record VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                id, fName, lName, dob, mob, yob, gender, address, phoneNo, emailId, indoorGame, outdoorGame))
            self.dbConnection.commit()

#to update data in the database
    def Update(self, fName, lName, dob, mob, yob, gender, address, phoneNo, emailId, indoorGame, outdoorGame, id):
        self.dbCursor.execute(
            "UPDATE user_record SET fName = ?, lName = ?, dob = ?, mob = ?, yob = ?, gender = ?, address = ?, phoneNo = ?, emailId = ?, indoorGame = ?, outdoorGame = ? WHERE id = ?",
            (fName, lName, dob, mob, yob, gender, address, phoneNo, emailId, indoorGame, outdoorGame, id))
        self.dbConnection.commit()

#to search specific user details based on ID
    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM user_record WHERE id = ?", (id,))
        searchResults = self.dbCursor.fetchall()
        return searchResults

#to delete specific user details based on ID
    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM user_record WHERE id = ?", (id,))
        self.dbConnection.commit()

#to display specific user details based on ID
    def Display(self):
        self.dbCursor.execute("SELECT * FROM user_record")
        records = self.dbCursor.fetchall()
        return records


#DatabaseView class to view existing record from databse
class DatabaseView:
    def __init__(self, data):
        self.databaseViewWindow = tkinter.Tk()
        # Window title for to view particular user details
        self.databaseViewWindow.wm_title("Database View")

        # Label widgets
        # Searching for Particular User Record
        tkinter.Label(self.databaseViewWindow, text = "Available data in Database",  width = 25).grid(pady = 5, column = 1, row = 1)

        self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
        self.databaseView.grid(pady = 5, column = 1, row = 2)
        self.databaseView["show"] = "headings"
        self.databaseView["columns"] = ("id", "fName", "lName", "dob", "mob", "yob", "gender", "address", "phoneNo", "emailId", "indoorGame", "outdoorGame")

        # Database View Headings id, fName, lName, dob, mob, yob, gender, address, phoneNo, emailId, indoorGame, outdoorGame
        self.databaseView.heading("id", text = "Student ID")
        self.databaseView.heading("fName", text = "First Name")
        self.databaseView.heading("lName", text = "Last Name")
        self.databaseView.heading("dob", text = "D.O.B")
        self.databaseView.heading("mob", text = "M.O.B")
        self.databaseView.heading("yob", text = "Y.O.B")
        self.databaseView.heading("gender", text = "Gender")
        self.databaseView.heading("address", text = "Address")
        self.databaseView.heading("phoneNo", text = "Phone Number")
        self.databaseView.heading("emailId", text = "Email ID")
        self.databaseView.heading("indoorGame", text = "Indoor Game")
        self.databaseView.heading("outdoorGame", text = "Outdoor Game")


        # column view
        self.databaseView.column("id", width = 40)
        self.databaseView.column("fName", width = 100)
        self.databaseView.column("lName", width = 100)
        self.databaseView.column("dob", width = 60)
        self.databaseView.column("mob", width = 60)
        self.databaseView.column("yob", width = 60)
        self.databaseView.column("gender", width = 60)
        self.databaseView.column("address", width = 200)
        self.databaseView.column("phoneNo", width = 100)
        self.databaseView.column("emailId", width = 200)
        self.databaseView.column("indoorGame", width = 100)
        self.databaseView.column("outdoorGame", width = 100)


        for record in data:
            self.databaseView.insert('', 'end', values=(record))

        self.databaseViewWindow.mainloop()

class UpdateData:
    def __init__(self, id):
        self.window = tkinter.Tk()
        self.window.wm_title("Update existing record")

        # Initializing all the variables
        self.id = id
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.dob = tkinter.StringVar()
        self.mob = tkinter.StringVar()
        self.yob = tkinter.StringVar()
        self.gender = tkinter.StringVar()
        self.address = tkinter.StringVar()

        self.phoneNo = tkinter.StringVar()
        self.emailId = tkinter.StringVar()
        self.indoorGame = tkinter.StringVar()
        self.outdoorGame = tkinter.StringVar()

        self.genderList = ["Male", "Female", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]
        self.yearList = list(range(1900, 2020))
        self.indoorgameslist = ["karate", "wushu", "Squash", "Soccer", "Table Tennis", "Lawn Tennis", "Chess",
                                "Swimming"]
        self.outdoorgameslist = ["Football", "Cricket", "Badminton", "Soccer", "Table Tennis", "Lawn Tennis", "Chess",
                                 "Swimming"]

        # List of labels for user registration form
        tkinter.Label(self.window, text="Student ID", width=25).grid(pady=5, column=1, row=1)
        tkinter.Label(self.window, text=id, width=25).grid(pady=5, column=3, row=1)
        tkinter.Label(self.window, text="First Name", width=25).grid(pady=5, column=1, row=2)
        tkinter.Label(self.window, text="Last Name", width=25).grid(pady=5, column=1, row=3)
        tkinter.Label(self.window, text="D.O.B", width=25).grid(pady=5, column=1, row=4)
        tkinter.Label(self.window, text="M.O.B", width=25).grid(pady=5, column=1, row=5)
        tkinter.Label(self.window, text="Y.O.B", width=25).grid(pady=5, column=1, row=6)
        tkinter.Label(self.window, text="Gender", width=25).grid(pady=5, column=1, row=7)
        tkinter.Label(self.window, text="Address", width=25).grid(pady=5, column=1, row=8)
        tkinter.Label(self.window, text="Phone Number", width=25).grid(pady=5, column=1, row=9)
        tkinter.Label(self.window, text="Email ID", width=25).grid(pady=5, column=1, row=10)
        tkinter.Label(self.window, text="Indoor Games", width=25).grid(pady=5, column=1, row=11)
        tkinter.Label(self.window, text="Outdoor Games", width=25).grid(pady=5, column=1, row=12)

        # Set previous values in form
        self.database = UserDatabase()
        self.searchResults = self.database.Search(id)
        tkinter.Label(self.window, text=self.searchResults[0][1], width=25).grid(pady=5, column=2, row=2)
        tkinter.Label(self.window, text=self.searchResults[0][2], width=25).grid(pady=5, column=2, row=3)
        tkinter.Label(self.window, text=self.searchResults[0][3], width=25).grid(pady=5, column=2, row=4)
        tkinter.Label(self.window, text=self.searchResults[0][4], width=25).grid(pady=5, column=2, row=5)
        tkinter.Label(self.window, text=self.searchResults[0][5], width=25).grid(pady=5, column=2, row=6)
        tkinter.Label(self.window, text=self.searchResults[0][6], width=25).grid(pady=5, column=2, row=7)
        tkinter.Label(self.window, text=self.searchResults[0][7], width=25).grid(pady=5, column=2, row=8)
        tkinter.Label(self.window, text=self.searchResults[0][8], width=25).grid(pady=5, column=2, row=9)
        tkinter.Label(self.window, text=self.searchResults[0][9], width=25).grid(pady=5, column=2, row=10)
        tkinter.Label(self.window, text=self.searchResults[0][10], width=25).grid(pady=5, column=2, row=11)
        tkinter.Label(self.window, text=self.searchResults[0][11], width=25).grid(pady=5, column=2, row=12)


        # Fields
        # Input text Entry widgets
        self.fNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fName)
        self.lNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lName)
        self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
        self.phoneNoEntry = tkinter.Entry(self.window, width=25, textvariable=self.phoneNo)
        self.emailIdEntry = tkinter.Entry(self.window, width=25, textvariable=self.emailId)

        # Setting-up entry widgets the alignment
        self.fNameEntry.grid(pady=5, column=3, row=2)
        self.lNameEntry.grid(pady=5, column=3, row=3)
        self.addressEntry.grid(pady=5, column=3, row=8)
        self.phoneNoEntry.grid(pady=5, column=3, row=9)
        self.emailIdEntry.grid(pady=5, column=3, row=10)

        # Drop-Down widgets
        # Input text using drop-down list
        self.dobBox = tkinter.ttk.Combobox(self.window, values=self.dateList, width=20)
        self.mobBox = tkinter.ttk.Combobox(self.window, values=self.monthList, width=20)
        self.yobBox = tkinter.ttk.Combobox(self.window, values=self.yearList, width=20)
        self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderList, width=20)
        self.indoorGameBox = tkinter.ttk.Combobox(self.window, values=self.indoorgameslist, width=20)
        self.outdoorGameBox = tkinter.ttk.Combobox(self.window, values=self.outdoorgameslist, width=20)

        # Setting-up entry widgets row by numbering order
        self.dobBox.grid(pady=5, column=3, row=4)
        self.mobBox.grid(pady=5, column=3, row=5)
        self.yobBox.grid(pady=5, column=3, row=6)
        self.genderBox.grid(pady=5, column=3, row=7)
        self.indoorGameBox.grid(pady=5, column=3, row=11)
        self.outdoorGameBox.grid(pady=5, column=3, row=12)

        #Kepping values index wise
        self.fNameEntry.insert(0, self.searchResults[0][1])
        self.lNameEntry.insert(0, self.searchResults[0][2])
        self.dobBox.insert(0, self.searchResults[0][3])
        self.mobBox.insert(0, self.searchResults[0][4])
        self.yobBox.insert(0, self.searchResults[0][5])
        self.genderBox.insert(0, self.searchResults[0][6])
        self.addressEntry.insert(0, self.searchResults[0][7])
        self.phoneNoEntry.insert(0, self.searchResults[0][8])
        self.emailIdEntry.insert(0, self.searchResults[0][9])
        self.indoorGameBox.insert(0, self.searchResults[0][10])
        self.outdoorGameBox.insert(0, self.searchResults[0][11])



        # Button widgets
        tkinter.Button(self.window, width=20, text="Update", bg='#ffc912', font=('Verdana 10 bold'), command=self.Update).grid(pady=15, padx=5, column=1,row=14)
        tkinter.Button(self.window, width=20, text="Reset", bg='#ed7124', font=('Verdana 10 bold'), command=self.Reset).grid(pady=15, padx=5, column=2, row=14)
        tkinter.Button(self.window, width=20, text="Close", bg='#ed243b', font=('Verdana 10 bold'), command=self.window.destroy).grid(pady=15, padx=5, column=3,
                                                                                              row=14)

        self.window.mainloop()

    #get values from user form
    def Update(self):
        self.database = UserDatabase()
        self.database.Update( self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(),
                             self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(),
                             self.phoneNoEntry.get(), self.emailIdEntry.get(), self.indoorGameBox.get(), self.outdoorGameBox.get(),self.id)
        tkinter.messagebox.showinfo("Updated data", "User Data Updated Successfully!!!")

    # To Reset all form fields
    def Reset(self):
        #self.idEntry.delete(0, tkinter.END)
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)
        self.dobBox.set("")
        self.mobBox.set("")
        self.yobBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.phoneNoEntry.delete(0, tkinter.END)
        self.emailIdEntry.delete(0, tkinter.END)
        self.indoorGameBox.set("")
        self.outdoorGameBox.set("")


#to searching data on ID basis
class SearchDeleteData:
    def __init__(self, task):
        window = tkinter.Tk()
        window.wm_title(task + " data")

        # Initializing all the variables
        self.id = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.heading = "Please enter Student ID to " + task

        # Labels
        tkinter.Label(window, text=self.heading, width=50).grid(pady=20, row=1)
        tkinter.Label(window, text="Student ID", width=10).grid(pady=5, row=2)

        # Entry widgets
        self.idEntry = tkinter.Entry(window, width=5, textvariable=self.id)

        self.idEntry.grid(pady=5, row=3)


        # Button widgets
        # Search & Delete button
        if (task == "Search"):
            tkinter.Button(window, width=20, text=task, bg='#65d73a', font=('Verdana 10 bold'), command=self.Search).grid(pady=10, row=14)
        elif (task == "Delete"):
            tkinter.Button(window, width=20, text=task, bg='#ed7124', font=('Verdana 10 bold'), command=self.Delete).grid(pady=10, row=14)


    #defining search function
    def Search(self):
        self.database = UserDatabase()
        self.data = self.database.Search(self.idEntry.get()) # get from ID
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database = UserDatabase()
        self.database.Delete(self.idEntry.get()) # deleting id
        tkinter.messagebox.showinfo("Delete Data", "User Data Deleted Successfully!!!")


homePage = HomePage()
