# v_p_n
group 2:python assignment
#Searching and Delete File
#Reference and code taken from https://code-projects.org/car-booking-system-in-python-with-source-code/

import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3



class SearchDeleteWindow:
    def __init__(self, task):
        window = tkinter.Tk()
        window.wm_title(task + " data")

        # Variable initialization
        self.id = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.heading = "Please enter student id to " + task

        # Labels for searching for window
        tkinter.Label(window, text=self.heading, width=50).grid(pady=20, row=1)
        tkinter.Label(window, text="STUDENT ID", width=10).grid(pady=5, row=2)

        # Entry widgets for searching window
        self.idEntry = tkinter.Entry(window, width=5, textvariable=self.id)

        self.idEntry.grid(pady=5, row=3)

        # Buttons
        if (task == "Search"):
            tkinter.Button(window, width=20, text=task, command=self.Search).grid(pady=15, padx=5, column=1, row=14)
        elif (task == "Delete"):
            tkinter.Button(window, width=20, text=task, command=self.Delete).grid(pady=15, padx=5, column=1, row=14)

    def Search(self):
        self.database = Database()
        self.data = self.database.Search(self.idEntry.get())
        self.databaseView = DatabaseView(self.data)

    def Delete(self):
        self.database = Database()
        self.database.Delete(self.idEntry.get())







