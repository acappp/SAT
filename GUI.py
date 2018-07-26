import tkinter as tk
top = tk.Tk()

top.title('Movie/Tv Show Planner Other')

top.resizable(False, False)
top.geometry('700x500')


def monthset(month):
    if month == "January":
        month = 1
    elif month == "February":
        month = 2
    elif month == "March":
        month = 3
    elif month == "April":
        month = 4
    elif month == "May":
        month = 5
    elif month == "June":
        month = 6
    elif month == "July":
        month = 7
    elif month == "August":
        month = 8
    elif month == "September":
        month = 9
    elif month == "October":
        month = 10
    elif month == "November":
        month = 11
    elif month == "December":
        month = 12
    return month


def scheduleMenu():
    schedule = tk.Tk()
    schedule.title("Schedule")
    schedule.resizable(False, False)
    schedule.geometry('500x400')
    # Importing calender allows me to have a calender (schedule) in the gui

    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]



    ## For drop boxes in schedule
    tkvar2 = tk.StringVar(top)
    monthDropDownMenu = tk.OptionMenu(schedule, tkvar2, *month, command=monthset)
    monthDropDownMenu.pack()

    import calendar
    cal = calendar.month(2018, month)
    l = tk.Label(schedule, text=cal)
    l.pack()


#year = ["2017", "2018", "2019"]
#tkvar = tk.StringVar(top)







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

VDbutton = tk.Button(top, text="View Database", fg="black", height = 4, width = 14, command = database)
VDbutton.pack()

Editbutton = tk.Button(top, text="Edit Entry", fg="black", height = 4, width = 14, command = editmenu)
Editbutton.pack()

VSbutton = tk.Button(top, text="View Schedule", fg="black", height = 4, width = 14, command = scheduleMenu)
VSbutton.pack()

Addbutton = tk.Button(top, text="Add Entry", fg="black", height = 4, width = 14, command = addEntry)
Addbutton.pack()

Removebutton = tk.Button(top, text="Remove Entry", fg="black", height = 4, width = 14, command = removeEntry)
Removebutton.pack()

Closebutton = tk.Button(top, text="Close", fg="black", height = 4, width = 14, command = quit)
Closebutton.pack()



top.mainloop()
