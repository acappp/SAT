import tkinter as tk

top = tk.Tk()

top.title('Movie/Tv Show Planner Other')

top.resizable(False, False)
top.geometry('750x400')


bgc = "#515151" # default background colour (dark grey)
hdc = "#272727" # default header colour (darker grey)
lightbgc = "#CDCDCD" # light grey background colour (for light theme)
lighthdc = "#AAAAAA" # light grey header colour (for light theme)
Red = "#ff0000" # red
Orange = "#ff7f00" # orange
Yellow = "#ffff00" # yellow
Green = "#00ff00" # green
Blue = "#0000ff" # blue
Indigo = "#4b0082" # indigo
Violet = "#9400d3" # violet
LightBlue = "#C9FFFF"
Black = "#000000"
White = "#FFFFFF"
Pink = "#ff40e7" # Pink


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

    header = tk.Frame(add, bg=LightBlue, height=50, width=1000)
    header.pack()
    header.place(x=0, y=0)

    f = tk.Frame(add, bg=Black, height=8, width=750)
    f.pack()
    f.place(x = 0, y = 50)

    Title = tk.Label(add, text="Enter the details of your entry:")
    Title.pack()
    Title.configure(bg=LightBlue)
    Title.place(x=275, y=15)

    L1 = tk.Label(add, text="Name:")
    L1.pack()
    L1.place(x=10, y=95)
    E1 = tk.Entry(add, bd=5)
    E1.pack()
    E1.place(x=150, y=90)

    L2 = tk.Label(add, text="Director:")
    L2.pack()
    L2.place(x=10, y=165)
    E2 = tk.Entry(add, bd=5)
    E2.pack()
    E2.place(x=150, y=160)


    L3 = tk.Label(add, text="rating:")
    L3.pack()
    L3.place(x=10, y=235)
    E3 = tk.Entry(add, bd=5)
    E3.pack()
    E3.place(x=150, y=230)

    L4 = tk.Label(add, text="Year of release:")
    L4.pack()
    L4.place(x=10, y=305)
    E4 = tk.Entry(add, bd=5)
    E4.pack()
    E4.place(x=150, y = 300)


    L5 = tk.Label(add, text="Description:")
    L5.pack()
    L5.place(x = 525, y = 90)
    E5 = tk.Entry(add, bd = 5)
    E5.pack()
    E5.place(x = 475, y = 125)


    L6 = tk.Label(add, text='Is the Entry a movie or Tv Show?')
    L6.pack()
    L6.place(x = 450, y = 200)
    radiomovie = tk.StringVar()
    radiom = tk.Radiobutton(add, text="Movie", variable=radiomovie)
    radiom.pack()
    radiom.place(x = 450, y = 250)
    radioTVShow = tk.StringVar()
    radioT = tk.Radiobutton(add, text="TV Show", variable=radioTVShow)
    radioT.pack()
    radioT.place(x = 450, y = 300)

    addButton = tk.Button(add, text="Add Entry", command = lambda: getentry(E1, E2, E3, E4, E5))
    addButton.pack()
    addButton.place(x = 275, y = 350)

    DoneButton = tk.Button(add, text="Done", command = exit)
    DoneButton.pack()
    DoneButton.place(x=375, y=350)


def getentry(E1, E2, E3, E4, E5):
    name = E1.get()
    director = E2.get()
    rating = E3.get()
    yearOfRelease = E4.get()
    description = E5.get()
    f = open('database', 'w')
    f.write(name)
    f.write(director)
    f.write(rating)
    f.write(yearOfRelease)
    f.write(description)


def database():
    data = tk.Tk()
    data.title("database")
    data.resizable(False, False)
    data.geometry('500x400')

    header = tk.Frame(data, bg=LightBlue, height=50, width=1000)
    header.pack()
    header.place(x=0, y=0)

    L1 = tk.Label(data, text="View Database:")
    L1.pack()
    L1.configure(bg=LightBlue)
    L1.place(x = 200, y = 15)


def editmenu():
    edit = tk.Tk()
    edit.title("Edit an Existing entry")
    edit.resizable(False, False)
    edit.geometry('500x400')

    header = tk.Frame(edit, bg=LightBlue, height=50, width=1000)
    header.pack()
    header.place(x=0, y=0)

    L1 = tk.Label(edit, text="Edit an Entry:")
    L1.pack()
    L1.configure(bg=LightBlue)
    L1.place(x=200, y=15)

    L2 = tk.Label(edit, text="Enter the name of the entry you wish to change:")
    L2.pack()
    L2.place(x = 100, y = 50)
    E2 = tk.Entry(edit, bd=5)
    E2.pack()
    E2.place(x = 150, y = 100)

def removeEntry():
    remove = tk.Tk()
    remove.title("Remove Entry")
    remove.resizable(False, False)
    remove.geometry('500x400')

    header = tk.Frame(remove, bg=LightBlue, height=50, width=1000)
    header.pack()
    header.place(x=0, y=0)

    L1 = tk.Label(remove, text="Remove an Entry:")
    L1.pack()
    L1.configure(bg=LightBlue)
    L1.place(x=200, y=15)

    L2 = tk.Label(remove, text="Enter the name of the entry you wish to remove:")
    L2.pack()
    L2.place(x=100, y=50)
    E2 = tk.Entry(remove, bd=5)
    E2.pack()
    E2.place(x=150, y=100)



t = tk.Frame(top, bg = LightBlue, height = 1000, width = 1000)
t.pack()
t.place(x = 0, y = 0)

bottomf = tk.Frame(top, bg = Black, height = 500, width = 750)
bottomf.pack()
bottomf.place(x = 0, y = 60)


title = tk.Label(top, text="-\nTV SHOW AND MOVIE PLANNER\n-")
title.pack()
title.configure(bg = LightBlue)

VDbutton = tk.Button(top, text="View Database", fg="Black", height = 10, width = 40, command = database)
VDbutton.pack()
VDbutton.place(x=0, y=55)

Addbutton = tk.Button(top, text="Add Entry", fg="black", height = 10, width = 15, command = addEntry)
Addbutton.pack()
Addbutton.place(x=350, y=55)

Removebutton = tk.Button(top, text="Remove Entry", fg="black", height = 10, width = 30, command = removeEntry)
Removebutton.pack()
Removebutton.place(x=500, y=55)

Editbutton = tk.Button(top, text="Edit Entry", fg="black", height = 10, width = 30, command = editmenu)
Editbutton.pack()
Editbutton.place(x=0, y=230)

VSbutton = tk.Button(top, text="View Schedule", fg="black", height = 10, width = 30, command = scheduleMenu)
VSbutton.pack()
VSbutton.place(x=270, y=230)

Closebutton = tk.Button(top, text="Close", fg= "Black", height = 10, width = 23, command = quit)
Closebutton.pack()
Closebutton.place(x=540, y=230)


f = tk.Frame(top, bg = Black, height = 8, width = 750)
f.pack()




top.mainloop()
