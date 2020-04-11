#Code Reference https://datatofish.com/if-elif-else-python/

import tkinter
import tkinter.ttk
import tkinter.messagebox
import sqlite3

class FormVaidation:
    def Validation(self, id, fName, lName, phoneNo, email):
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif not (fName.isalpha()):
            return "fName"
        elif not (lName.isalpha()):
            return "lName"
        elif not (phoneNo.isdigit() and (len(phoneNo) == 10)):
            return "phoneNo"
        elif not (email.count("@") == 1 and email.count(".") > 0):
            return "email"
        else:
            return "SUCCESS"