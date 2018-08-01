import tkinter as tk
top = tk.Tk()

top.title('Movie/Tv Show Planner Other')

top.resizable(False, False)
top.geometry('750x400')




ExistingEntries = []
year = ["2017", "2018", "2019"]
#tkvar = tk.StringVar(top)



def scheduleMenu():
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]
    schedule = tk.Tk()
    schedule.title("Schedule")
    schedule.resizable(False, False)
    schedule.geometry('500x400')
    # Importing calender allows me to have a calender (schedule) in the gui


    ## For drop boxes in schedule
    tkvar2 = tk.StringVar(top)
    monthDropDownMenu = tk.OptionMenu(schedule, tkvar2, *month)
    monthDropDownMenu.pack()

    nmonth = 1
    if month == "January":
        nmonth = 1
    elif month == "February":
        nmonth = 2
    elif month == "March":
        nmonth = 3
    elif month == "April":
        nmonth = 4
    elif month == "May":
        nmonth = 5
    elif month == "June":
        nmonth = 6
    elif month == "July":
        nmonth = 7
    elif month == "August":
        nmonth = 8
    elif month == "September":
        nmonth = 9
    elif month == "October":
        nmonth = 10
    elif month == "November":
        nmonth = 11
    elif month == "December":
        nmonth = 12

    import calendar
    cal = calendar.month(2018, nmonth)
    l = tk.Label(schedule, text=cal)
    l.pack()



def addEntry():
    add = tk.Tk()
    add.title("Add An Entry")
    add.resizable(False, False)
    add.geometry('500x400')
    L1 = tk.Label(add, text="Name:")
    L1.pack()
    E1 = tk.Entry(add, bd=5)
    E1.pack()
    L2 = tk.Label(add, text="Year of release:")
    L2.pack()
    E2 = tk.Entry(add, bd=5)
    E2.pack()
    L3 = tk.Label(add, text="Description:")
    L3.pack()
    E3 = tk.Entry(add, bd=5)
    E3.pack()
    L4 = tk.Label(add, text="Director:")
    L4.pack()
    E4 = tk.Entry(add, bd=5)
    E4.pack()
    L5 = tk.Label(add, text="rating:")
    L5.pack()
    E5 = tk.Entry(add, bd=5)
    E5.pack()


def database():
    data = tk.Tk()
    data.title("database")
    data.resizable(False, False)
    data.geometry('500x400')
    L1 = tk.Label(data, text="placeholder:")
    L1.pack()

def editmenu():
    edit = tk.Tk()
    edit.title("Edit an Existing entry")
    edit.resizable(False, False)
    edit.geometry('500x400')
    L1 = tk.Label(edit, text="Enter the name of the entry you wish to change:")
    L1.pack()
    E1 = tk.Entry(edit, bd=5)
    E1.pack()



def removeEntry():
    remove = tk.Tk()
    remove.title("Remove Entry")
    remove.resizable(False, False)
    remove.geometry('500x400')
    L1 = tk.Label(remove, text="Enter the name of the entry you wish to remove:")
    L1.pack()
    E1 = tk.Entry(remove, bd=5)
    E1.pack()




VDbutton = tk.Button(top, text="View Database", fg="black", height = 10, width = 14, command = database)
VDbutton.pack()
VDbutton.place(x=30, y=55)

Addbutton = tk.Button(top, text="Add Entry", fg="black", height = 4, width = 10, command = addEntry)
Addbutton.pack()
Addbutton.place(x=350, y=100)

Removebutton = tk.Button(top, text="Remove Entry", fg="black", height = 4, width = 10, command = removeEntry)
Removebutton.pack()
Removebutton.place(x=600, y=100)

Editbutton = tk.Button(top, text="Edit Entry", fg="black", height = 4, width = 10, command = editmenu)
Editbutton.pack()
Editbutton.place(x=60, y=250)

VSbutton = tk.Button(top, text="View Schedule", fg="black", height = 4, width = 14, command = scheduleMenu)
VSbutton.pack()
VSbutton.place(x=325, y=250)

Closebutton = tk.Button(top, text="Close", fg="black", height = 4, width = 14, command = quit)
Closebutton.pack()
Closebutton.place(x=575, y=250)




top.mainloop()
