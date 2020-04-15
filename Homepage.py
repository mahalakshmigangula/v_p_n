import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3
import tkinter.font


#Creating Class for HOMEPAGE
class HomePage:
    #Initializing
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Home Page") 
        tkinter.Label(self.homePageWindow, text="Welcome To Summer Registration Camp", width=100).grid(pady=20, column=1,
                                                                                                row=1)
        #Creating  buttons ForHome page with proper size color and good UI
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Register New User", bg='#0096D6', font=('Verdana 15 bold'), command=self.Insert).grid(pady=10, column=1, row=2)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Update Existing Record", bg='#ffc912', font=('Verdana 15 bold'), command=self.Update).grid(pady=15, column=1, row=3)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Search Existing Record", bg='#65d73a', font=('Verdana 15 bold'), command=self.Search).grid(pady=15, column=1, row=4)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Delete Existing Record", bg='#ed7124', font=('Verdana 15 bold'), command=self.Delete).grid(pady=15, column=1, row=5)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Display All User Record", bg='#64ad6a', font=('Verdana 15 bold'), command=self.Display).grid(pady=15, column=1,
                                                                                                 row=6)
        tkinter.Button(self.homePageWindow, height=1, width=25, text="Exit", bg='#ed243b', font=('Verdana 15 bold'), command=self.homePageWindow.destroy).grid(pady=15,
                                                                                                             column=1,
                                                                                                             row=7)
        #Using Mainloop For Halting and Running the Homepage in Loop
        self.homePageWindow.mainloop()
          # Defining Functions and calling classes
    def Insert(self):
        self.insertData = InsertData()

    def Update(self):
        self.updateIDWindow = tkinter.Tk()
        self.updateIDWindow.wm_title("Update Data ")

        # Initializing all the variables
        self.id = tkinter.StringVar()

        # Label For the Update Column
        tkinter.Label(self.updateIDWindow, text="Enter the Student ID to update", width=50).grid(pady=20, row=1)

        # Entry widgets
        self.idEntry = tkinter.Entry(self.updateIDWindow, width=5, textvariable=self.id)

        self.idEntry.grid(pady=10, row=2)

        # Button widgets
        # Update window button
        tkinter.Button(self.updateIDWindow, width=20, text="Update", bg='#ffc912', font=('Verdana 10 bold'), command=self.updateID).grid(pady=10, row=3)

        self.updateIDWindow.mainloop()

    def updateID(self):
        self.updateWindow = UpdateData(self.idEntry.get())
        self.updateIDWindow.destroy()

    def Search(self):
        self.searchWindow = SearchDeleteData("Search")

    def Delete(self):
        self.deleteWindow = SearchDeleteData("Delete")

    def Display(self):
        self.database = UserDatabase()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)
