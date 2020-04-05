#Reference and code taken from https://pynative.com/python-sqlite-insert-into-table/
import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3


class DatabaseFile:
    def __init__(self):
        self.dbConnection = sqlite3.connect("regDbFile.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS user_record (id integer PRIMARY KEY, fName text, lName text, dob text, mob text, yob text, gender text, address text, phoneNum text, emailId text, indoorGame text, OutdoorGame text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

        def Insert(self, id, fName, lName, dob, mob, yob, gender, address, phoneNum, emailId, indoorGame, outdoorGame):
            self.dbCursor.execute("INSERT INTO patient_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                id, fName, lName, dob, mob, yob, gender, address, phoneNum, emailId, indoorGame, outdoorGame))
            self.dbConnection.commit()
