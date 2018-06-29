# Code to add widgets will go here...


from tkinter import *


#import tkinter
#top = tkinter.Tk()

#B1 = tkinter.Button(top, text ="circle", relief=RAISED,\
             #            cursor="circle")
#B2 = tkinter.Button(top, text ="plus", relief=RAISED,\
              #           cursor="plus")
#B1.pack()
#B2.pack()
#top.mainloop()


# Importing calender allows me to have a calender (schedule) in the gui
# import calendar
#  cal = calendar.month (Insert year, Insert month)
# print cal


root = Tk()
frame = Frame(root)
frame.pack()
all_list = []


def RemoveAll():
    for i in all_list:
        i.grid_remove()


# def edit():




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


# All Buttons for the main menu, ".grid()" Locks them all in their positions
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)


VDbutton = Button(frame, text="View Database", fg="black", command = RemoveAll)
VDbutton.grid()
Editbutton = Button(frame, text="Edit Entry", fg="black", command = RemoveAll)
Editbutton.grid()
VSbutton = Button(frame, text="View Schedule", fg="black", command = RemoveAll)
VSbutton.grid()
Addbutton = Button(bottomframe, text="Add Entry", fg="black", command = RemoveAll and add)
Addbutton.grid()
Removebutton = Button(bottomframe, text="Remove Entry", fg="black", command = RemoveAll)
Removebutton.grid()
Closebutton = Button(bottomframe, text="Close", fg="black", command = quit)
Closebutton.grid()


all_list.append(VDbutton)
all_list.append(Editbutton)
all_list.append(VSbutton)
all_list.append(Addbutton)
all_list.append(Removebutton)
all_list.append(Closebutton)



root.mainloop()
