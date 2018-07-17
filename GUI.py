# Code to add widgets will go here...


from tkinter import *



# Importing calender allows me to have a calender (schedule) in the gui
# import calendar
#  cal = calendar.month (Insert year, Insert month)
# print cal


root = Tk()
frame = Frame(root)
frame.pack()
all_list = []


root.resizable(False, False)
root.geometry('700x500')

# def edit():


# Removes all buttons on the main menu
def RemoveAll():
    for i in all_list:
        i.grid_remove()

# Adds all the entry boxes for the "add Entry" option
def add():
    top = Tk()
    L1 = Label(top, text="Name:")
    L1.grid()
    E1 = Entry(top, bd=5)
    E1.grid()
    L2 = Label(top, text="Year of release:")
    L2.grid()
    E2 = Entry(top, bd=5)
    E2.grid()
    L3 = Label(top, text="Description:")
    L3.grid()
    E3 = Entry(top, bd=5)
    E3.grid()
    L4 = Label(top, text="Director:")
    L4.grid()
    E4 = Entry(top, bd=5)
    E4.grid()
    L5 = Label(top, text="rating:")
    L5.grid()
    E5 = Entry(top, bd=5)
    E5.grid()



bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

# All Buttons for the main menu, ".grid()" Locks them all in their positions
VDbutton = Button(frame, text="View Database", fg="black", height = 4, width = 14, command = RemoveAll)
VDbutton.grid(row = 1, column = 0)

Editbutton = Button(frame, text="Edit Entry", fg="black", height = 4, width = 14, command = RemoveAll)
Editbutton.grid(row = 2, column = 0)

VSbutton = Button(frame, text="View Schedule", fg="black", height = 4, width = 14, command = RemoveAll)
VSbutton.grid(row = 3, column = 0)

Addbutton = Button(bottomframe, text="Add Entry", fg="black", height = 4, width = 14, command = RemoveAll and add)
Addbutton.grid(row = 4, column = 0)

Removebutton = Button(bottomframe, text="Remove Entry", fg="black", height = 4, width = 14, command = RemoveAll)
Removebutton.grid(row = 5, column = 0)

Closebutton = Button(bottomframe, text="Close", fg="black", height = 4, width = 14, command = quit)
Closebutton.grid(row = 6, column = 0)

BackButton = Button(bottomframe, text="back", fg="black", height = 4, width = 14, command = add)
BackButton.grid()

#Adds all main menu buttons to a list
all_list.append(VDbutton)
all_list.append(Editbutton)
all_list.append(VSbutton)
all_list.append(Addbutton)
all_list.append(Removebutton)
all_list.append(Closebutton)



root.mainloop()
