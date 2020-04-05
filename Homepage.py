#Code Refrence and taken from https://realpython.com/python-gui-tkinter/
import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3
class HomePage:
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Summer Camp Registration System")

        tkinter.Label(self.homePageWindow, text = "Welcome To Registration Page",  width = 100).grid(pady = 20, column = 1, row = 1)

        tkinter.Button(self.homePageWindow, width = 20, text = "Insert", command = self.Insert).grid(pady = 15, column = 1, row = 2)
        tkinter.Button(self.homePageWindow, width = 20, text = "Update", command = self.Update).grid(pady = 15, column = 1, row = 3)
        tkinter.Button(self.homePageWindow, width = 20, text = "Search", command = self.Search).grid(pady = 15, column = 1, row = 4)
        tkinter.Button(self.homePageWindow, width = 20, text = "Delete", command = self.Delete).grid(pady = 15, column = 1, row = 5)
        tkinter.Button(self.homePageWindow, width = 20, text = "Display", command = self.Display).grid(pady = 15, column = 1, row = 6)
        tkinter.Button(self.homePageWindow, width = 20, text = "Exit", command = self.homePageWindow.destroy).grid(pady = 15, column = 1, row = 7)

        self.homePageWindow.mainloop()

    def Insert(self):
        self.insertWindow = InsertWindow()
    
    def Update(self):
        self.updateIDWindow = tkinter.Tk()
        self.updateIDWindow.wm_title("Update data")

        # Initializing all the variables
        self.id = tkinter.StringVar()

        # Label
        tkinter.Label(self.updateIDWindow, text = "Enter the  Student dID to update", width = 50).grid(pady = 20, row = 1)

        # Entry widgets
        self.idEntry = tkinter.Entry(self.updateIDWindow, width = 5, textvariable = self.id)
        
        self.idEntry.grid(pady = 10, row = 2)
        
        # Button widgets
        tkinter.Button(self.updateIDWindow, width = 20, text = "Update", command = self.updateID).grid(pady = 10, row = 3)

        self.updateIDWindow.mainloop()

    def updateID(self):
        self.updateWindow = UpdateWindow(self.idEntry.get())
        self.updateIDWindow.destroy()

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Delete")

    def Display(self):
        self.database = Database()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)
