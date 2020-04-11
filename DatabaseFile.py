#Reference and code taken from https://pynative.com/python-sqlite-insert-into-table/
import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3


class UserDatabase:
    def __init__(self):
        self.dbConnection = sqlite3.connect("regDBFile.db") #database file will create using name "regDBFile.db"
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute("CREATE TABLE IF NOT EXISTS user_record (id integer PRIMARY KEY, fName text, lName text, dob text, mob text, yob text, gender text, address text, phoneNo text, emailId text, indoorGame text, OutdoorGame text)")

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