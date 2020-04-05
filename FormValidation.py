#Code Reference https://datatofish.com/if-elif-else-python/

import tkinter
import sqlite3

class FormVaidation:
    def Validate(self, id, fName, lName, phone, email):
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif not (fName.isalpha()):
            return "fName"
        elif not (lName.isalpha()):
            return "lName"
        elif not (phone.isdigit() and (len(phone) == 10)):
            return "phone"
        elif not (email.count("@") == 1 and email.count(".") > 0):
            return "email"
        else:
            return "SUCCESS"