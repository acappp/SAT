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
    add.geometry('750x400')
    L1 = tk.Label(add, text="Name:")
    L1.pack()
    L1.place(x=10, y=15)

    E1 = tk.Entry(add, bd=5)
    E1.pack()
    E1.place(x=150, y=10)

    L2 = tk.Label(add, text="Director:")
    L2.pack()
    L2.place(x=10, y=65)
    E2 = tk.Entry(add, bd=5)
    E2.pack()
    E2.place(x=150, y=60)


    L3 = tk.Label(add, text="rating:")
    L3.pack()
    L3.place(x=10, y=115)
    E3 = tk.Entry(add, bd=5)
    E3.pack()
    E3.place(x=150, y=110)

    L4 = tk.Label(add, text="Year of release:")
    L4.pack()
    L4.place(x=10, y=175)
    E4 = tk.Entry(add, bd=5)
    E4.pack()
    E4.place(x=150, y = 170)


    L5 = tk.Label(add, text="Description:")
    L5.pack()
    L5.place(x = 525, y = 10)
    E5 = tk.Entry(add, bd=5)
    E5.pack()
    E5.place(x = 475, y = 30)


    L6 = tk.Label(add, text='')

    radiomovie = tk.StringVar()
    radiom = tk.Radiobutton(add, text="Movie", variable=radiomovie)
    radiom.pack()
    radiom.place(x = 450, y = 200)

    radioTVShow = tk.StringVar()
    radioT = tk.Radiobutton(add, text="TV Show", variable=radioTVShow)
    radioT.pack()
    radioT.place(x = 450, y = 250)



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


title = tk.Label(top, text="------------\nTV SHOW AND MOVIE PLANNER\n------------")
title.pack()

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
