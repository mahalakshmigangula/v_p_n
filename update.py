class UpdateData:
    def __init__(self, id):
        self.window = tkinter.Tk()
        self.window.wm_title("Here you can update your data")

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
        self.indoorgameslist = ["Football", "Cricket", "Badminton", "Soccer", "Table Tennis", "Lawn Tennis", "Chess",
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

        # Set previous values
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

        # Button widgets
        tkinter.Button(self.window, width=20, text="Update", bg='#ffc912', font=('Verdana 10 bold'), command=self.Update).grid(pady=15, padx=5, column=1,row=14)
        tkinter.Button(self.window, width=20, text="Reset", bg='#ed7124', font=('Verdana 10 bold'), command=self.Reset).grid(pady=15, padx=5, column=2, row=14)
        tkinter.Button(self.window, width=20, text="Close", bg='#ed243b', font=('Verdana 10 bold'), command=self.window.destroy).grid(pady=15, padx=5, column=3,
                                                                                              row=14)

        self.window.mainloop()

    def Update(self):
        self.database = UserDatabase()
        self.database.Update( self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(),
                             self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(),
                             self.phoneNoEntry.get(), self.emailIdEntry.get(), self.indoorGameBox.get(), self.outdoorGameBox.get(),self.id)
        tkinter.messagebox.showinfo("Updated data", "User Data Updated Successfully!!!")

    # To Reset all form fields
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
