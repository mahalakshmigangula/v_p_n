from tkinter import *
#Reference purpose
#Taken from https://www.geeksforgeeks.org/python-simple-registration-form-using-tkinter
# defining Functions to set focus
def focus1(event):
    # course_field box
    lname_field.focus_set()

def focus2(event):
    # contact_no_field box
    contact_no_field.focus_set()

def focus3(event):
    # email_id_field box
    email_id_field.focus_set()

def focus4(event):
    # address_field box
    address_field.focus_set()

# Defining Function for clearing the contents of text entry boxes
def clear():
    # to clear contents of registration form
    fname_field.delete(0, END)
    lname_field.delete(0, END)
    contact_no_field.delete(0, END)
    email_id_field.delete(0, END)
    address_field.delete(0, END)

    # set focus on the name_field box
    fname_field.focus_set()

    # clear() function to clean all field
    clear()


# Driver code
if __name__ == "__main__":
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("registration form")

    # set the configuration of GUI window
    root.geometry("500x300")


    # label registration form
    heading = Label(root, text="Summer Camp Registration", bg="light green")

    # lable First Name
    fname = Label(root, text="First Name", bg="light green")

    # lable Last Name
    lname = Label(root, text="Last Name", bg="light green")

    # label Contact
    contact_no = Label(root, text="Contact No.", bg="light green")

    # label Email id
    email_id = Label(root, text="Email id", bg="light green")

    # label address
    address = Label(root, text="Address", bg="light green")

    # grid method to place form element index wise
    heading.grid(row=0, column=1)
    fname.grid(row=1, column=0)
    lname.grid(row=2, column=0)
    contact_no.grid(row=3, column=0)
    email_id.grid(row=4, column=0)
    address.grid(row=5, column=0)

    # text entry box creation
    # for user information input
    fname_field = Entry(root)
    lname_field = Entry(root)
    contact_no_field = Entry(root)
    email_id_field = Entry(root)
    address_field = Entry(root)

    # bind method of widget is used for
    # the binding the function with the events
    # whenever the enter key is pressed

    # calling the focus1 function
    fname_field.bind("<Return>", focus1)

    # calling the focus2 function
    lname_field.bind("<Return>", focus2)

    # calling the focus5 function
    contact_no_field.bind("<Return>", focus3)

    #calling the focus6 function
    email_id_field.bind("<Return>", focus4)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    fname_field.grid(row=1, column=1, ipadx="100")
    lname_field.grid(row=2, column=1, ipadx="100")
    contact_no_field.grid(row=3, column=1, ipadx="100")
    email_id_field.grid(row=4, column=1, ipadx="100")
    address_field.grid(row=5, column=1, ipadx="100")

    # Submit Button and placing into the root window
    submit = Button(root, text="Submit", fg="Black",
                    bg="Blue")
    submit.grid(row=8, column=1)

    # GUI start from here
    root.mainloop()
