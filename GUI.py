"""
Author: Anthony Cappellucci
Date: xx/xx/2018
Version 1.0

This program is a movie cataloger that allows the user to enter the names and details of movies
and store them inside of a sortable database.
"""

import tkinter as tk


# Setting all colours as callable string value
# so I can just say 'Black' if I want something to appear black
bgc = "#515151" # dark grey
hdc = "#272727" # darker grey
lightbgc = "#CDCDCD" # light grey background colour
lighthdc = "#AAAAAA" # light grey header colour
Red = "#ff0000" # red
Orange = "#ff7f00" # orange
Yellow = "#ffff00" # yellow
Green = "#00ff00" # green
Blue = "#0000ff" # blue
Indigo = "#4b0082" # indigo
Violet = "#9400d3" # violet
LightBlue = "#C9FFFF" # Light Blue
Black = "#000000" #Black
White = "#FFFFFF" # White
Pink = "#ff40e7" # Pink



class Alldata:
    # This Function calls all values entered from the user and adds them to a list of lists
    def __init__(self, name, director, rating, yearOfRelease, description):
        self.name = name
        self.director = director
        self.rating = rating
        self.yearOfRelease = yearOfRelease
        self.description = description


    # This function writes all the values to the file,
    # The '@' symbol is used as seperation because it is not commonly used in entries
    def write(self):
        f = open('database', 'a')
        f.write(self.name)
        f.write("@")
        f.write(self.director)
        f.write("@")
        f.write(self.rating)
        f.write("@")
        f.write(self.yearOfRelease)
        f.write("@")
        f.write(self.description)
        f.close()

def clearfile():
    f = open('database', 'w')
    f.close()

Movies = []


def addEntry():
    add = tk.Tk()
    add.title("Add An Entry")
    add.resizable(False, False)
    add.geometry('500x490')

    header = tk.Frame(add, bg=LightBlue, height=50, width=1000)
    header.place(x=0, y=0)

    f = tk.Frame(add, bg=Black, height=8, width=750)
    f.place(x = 0, y = 50)

    Title = tk.Label(add, text="Enter the details of your entry:")
    Title.configure(bg=LightBlue, font = ("Futura", 20))
    Title.place(x=150, y=15)

    L1 = tk.Label(add, text="Name:")
    L1.place(x=10, y=95)
    E1 = tk.Entry(add, bd=5, width = 40)
    E1.place(x=150, y=90)

    L2 = tk.Label(add, text="Director:")
    L2.place(x=10, y=165)
    E2 = tk.Entry(add, bd=5, width = 40)
    E2.place(x=150, y=160)


    L3 = tk.Label(add, text="rating:")
    L3.place(x=10, y=235)
    E3 = tk.Entry(add, bd=5, width = 40)
    E3.place(x=150, y=230)

    L4 = tk.Label(add, text="Year of release:")
    L4.place(x=10, y=305)
    E4 = tk.Entry(add, bd=5, width = 40)
    E4.place(x=150, y = 300)


    L5 = tk.Label(add, text="Description:")
    L5.place(x = 10, y = 375)
    E5 = tk.Entry(add, bd = 5, width = 40)
    E5.place(x = 150, y = 370)

    addButton = tk.Button(add, text="Add Entry", command = lambda: getentry(E1, E2, E3, E4, E5))
    addButton.place(x = 300, y = 450)

    DoneButton = tk.Button(add, text="Done", command = add.destroy)
    DoneButton.place(x=400, y=450)


def yearsort(Movies):
    # Check to see if the list is only a single item, if so return the single item list
    # Initise the list to return
    sortedList = []

    if len(Movies) < 2:
        return Movies

    # Setting up initial variable for splitting lists
    listLength = len(Movies)
    index = 0
    list1 = []
    list2 = []

    # Loop that splits 1 list into 2 lists of roughly equal length
    while index < listLength:
        if (index + 1 <= int((listLength) / 2)):
            list1.append(Movies[index])
        else:
            list2.append(Movies[index])
        index += 1

    # Take our 2 lists, and give one each to a recursive call of MergeSort (this function)
    returnedList1 = yearsort(list1)
    returnedList2 = yearsort(list2)

    # This loop will run based on the total length of both lists
    for i in range(0, len(list1) + len(list2)):
        # We check if we are out of value for list1
        if len(returnedList1) < 1:
            # If we are out of values append the rest of list2 and end the loop
            for i in returnedList2:
                sortedList.append(i)
            break
        # Same as above, only for list2, then appending list1
        if len(returnedList2) < 1:
            for i in returnedList1:
                sortedList.append(i)
            break
        # Check which value is smaller and add that next to the sorted list
        if int(returnedList1[0].yearOfRelease) < int(returnedList2[0].yearOfRelease):
            sortedList.append(returnedList1.pop(0))
        elif int(returnedList2[0].yearOfRelease) < int(returnedList1[0].yearOfRelease):
            sortedList.append(returnedList2.pop(0))
        # Values must be equal, add both to sorted list
        else:
            sortedList.append(returnedList1.pop(0))
            sortedList.append(returnedList2.pop(0))
    Movies = sortedList
    return Movies

def ratesort(Movies):
    # Check to see if the list is only a single item, if so return the single item list
    # Initise the list to return
    sortedList = []

    if len(Movies) < 2:
        return Movies

    # Setting up initial variable for splitting lists
    listLength = len(Movies)
    index = 0
    list1 = []
    list2 = []

    # Loop that splits 1 list into 2 lists of roughly equal length
    while index < listLength:
        if (index + 1 <= int((listLength) / 2)):
            list1.append(Movies[index])
        else:
            list2.append(Movies[index])
        index += 1

    # Take our 2 lists, and give one each to a recursive call of MergeSort (this function)
    returnedList1 = ratesort(list1)
    returnedList2 = ratesort(list2)

    # This loop will run based on the total length of both lists
    for i in range(0, len(list1) + len(list2)):
        # We check if we are out of value for list1
        if len(returnedList1) < 1:
            # If we are out of values append the rest of list2 and end the loop
            for i in returnedList2:
                sortedList.append(i)
            break
        # Same as above, only for list2, then appending list1
        if len(returnedList2) < 1:
            for i in returnedList1:
                sortedList.append(i)
            break
        # Check which value is smaller and add that next to the sorted list
        if int(returnedList1[0].rating) < int(returnedList2[0].rating):
            sortedList.append(returnedList1.pop(0))
        elif int(returnedList2[0].rating) < int(returnedList1[0].rating):
            sortedList.append(returnedList2.pop(0))
        # Values must be equal, add both to sorted list
        else:
            sortedList.append(returnedList1.pop(0))
            sortedList.append(returnedList2.pop(0))
    Movies = sortedList
    return Movies

# This is where the entries are stored alogside the file



# The purpose of this function is to read the file and add all previous entries into the list
# Entries in the list do not save when the program closes so this is necessary if you wwant the entries
# To save

def startread():
    p = open('database', 'r')
    q=0
    for line in p:
        if line == '\n':
            q=6
        # If it's a new line skip the code, if it isn't don't skip
        else:
            slist = line.split("@")
            Movie = Alldata(slist[0], slist[1], slist[2], slist[3], slist[4])
            Movies.append(Movie)

    p.close()
    return Movies


def removeEntry():
    remove = tk.Tk()
    remove.title("Remove Entry")
    remove.resizable(False, False)
    remove.geometry('500x200')

    header = tk.Frame(remove, bg=LightBlue, height=50, width=1000)
    header.place(x=0, y=0)

    F1 = tk.Frame(header, bg=Black, height=5, width=1000)
    F1.place(x=0, y=45)

    L1 = tk.Label(remove, text="Remove an Entry:")
    L1.configure(bg=LightBlue, font = ("Futura", 20))
    L1.place(x=200, y=10)

    L2 = tk.Label(remove, text="Select the name of the entry you wish to remove:")
    L2.place(x=100, y=50)

    ## For drop the box
    def generatelist():
        mNames = []
        for i in Movies:
            mNames.append(i.name)
        tkvar = tk.StringVar(remove)
        tkvar.set(mNames[0])

        DropMenu = tk.OptionMenu(remove, tkvar, *mNames)
        DropMenu.pack()
        DropMenu.place(x=125, y=75)
        DropMenu.configure(height=2, width=30)

        return tkvar

    def delete(tkvar):
        p = tkvar.get()
        print(p)
        y=0
        for i in Movies:

            if i.name == p:
                Movies.pop(y)
            y+=1

        clearfile()
        for i in Movies:

            i.write()


    # Remove entry command .remove

    tkvar = generatelist()

    DeleteButton = tk.Button(remove, text="Delete", command=lambda: delete(tkvar))
    DeleteButton.place(x=300, y=150)

    DoneButton = tk.Button(remove, text="Done", command=remove.destroy)
    DoneButton.place(x=375, y=150)



def getentry(E1, E2, E3, E4, E5):
    # The purpose of this while loop is to prevent the user from adding entries that are blank,
    # If a blank line is detected by the start read function the program will crash
    repeat = True
    while repeat == True:
        name = E1.get()
        director = E2.get()
        rating = E3.get()
        yearOfRelease = E4.get()
        description = E5.get()

        if name and director and rating and yearOfRelease and description != '':
            Movie = Alldata(name, director, rating, yearOfRelease, description)
            Movies.append(Movie)
            Movie.write()

            repeat = False

            # These clear the entry boxes once the entry has been added to the database
            E1.delete(0, 'end')
            E2.delete(0, 'end')
            E3.delete(0, 'end')
            E4.delete(0, 'end')
            E5.delete(0, 'end')

        else:
            break



def database():
    global data
    data = tk.Tk()
    data.title("database")
    data.resizable(False, True)
    data.geometry('1000x400')


    header = tk.Frame(data, bg=LightBlue, height=50, width=1000)
    header.place(x=0, y=0)

    L1 = tk.Label(data, text="View Database:")
    L1.configure(bg=LightBlue,  font=("Futura", 30))
    L1.place(x = 425, y = 5)

    F1 = tk.Frame(data, bg=Black, height=5, width=1000)
    F1.place(x=0, y=45)

    NameL = tk.Label(data, text='Name:')
    NameL.place(x=40, y=50)
    DirectorL = tk.Label(data, text='Director:')
    DirectorL.place(x=240, y=50)
    RatingsL = tk.Label(data, text='Rating:')
    RatingsL.place(x=400, y=50)
    yearsOfReleaseL = tk.Label(data, text='Year Of Release:')
    yearsOfReleaseL.place(x=500, y=50)
    DescriptionL = tk.Label(data, text='Description:')
    DescriptionL.place(x=650, y=50)

    y = 1
    for i in Movies:
        NLabel = tk.Label(data, text = i.name)
        NLabel.place(x = 40, y = 50+(y*20))

        DirLabel = tk.Label(data, text = i.director)
        DirLabel.place(x = 240, y = 50+(y*20))

        RLabel = tk.Label(data, text = i.rating)
        RLabel.place(x = 400, y = 50+(y*20))

        yORLabel = tk.Label(data, text = i.yearOfRelease)
        yORLabel.place(x = 500, y = 50+(y*20))


        DesLabel = tk.Label(data, text = i.description)
        DesLabel.place(x = 650, y = 50+(y*20))
        y = y+1

    DoneButton = tk.Button(data, text="Done", command = data.destroy)
    DoneButton.place(x=900, y=350)
    #DoneButton.pack(side=LEFT)

    sortRButton = tk.Button(data, text="Sort via Rating", command=commandR) # and close)
    sortRButton.place(x=50, y = 10)
    sortRButton.configure(highlightbackground = LightBlue)

    sortYButton = tk.Button(data, text="Sort via Year", command=commandY)
    sortYButton.place(x=180, y = 10)
    sortYButton.configure(highlightbackground = LightBlue)

def commandR():
    global Movies
    Movies = ratesort(Movies)
    data.destroy()
    database()

def commandY():
    global Movies
    Movies = yearsort(Movies)
    data.destroy()
    database()

def settings():
    setting = tk.Tk()
    setting.title("Settings")
    setting.resizable(False, False)
    setting.geometry('500x400')


    DoneButton = tk.Button(setting, text="Done", command=setting.destroy)
    DoneButton.pack()
    DoneButton.place(x=375, y=350)



def main():
    main = tk.Tk()
    # Setting the title of the initial window, setting it's size
    # and preventing it from being resizable by the user
    main.title('Movie Database')
    main.resizable(False, False)
    main.geometry('750x325')

    # These first three blocks are simply adding the frames and titles for the main menu of the GUI
    # I've used .place as I believe it's the most accuracte way of placing things
    t = tk.Frame(main, bg=LightBlue, height=1000, width=1000)
    t.place(x=0, y=0)

    bottomf = tk.Frame(main, bg=Black, height=500, width=750)
    bottomf.place(x=0, y=55)

    title = tk.Label(main, text="MOVIE PLANNER")
    title.configure(bg=LightBlue, font=("Futura", 30))
    title.place(x=300, y=12)

    def retlog():
        main.destroy()
        login()

    # The next 6 small blocks of code here add all the needed buttons onto the main menu of the GUI
    # Each calls a different fuction that will open a specific corresponding  window
    settingsbutton = tk.Button(main, text="Settings", fg="Black", command=settings)
    settingsbutton.place(x=650, y=12)
    settingsbutton.configure(highlightbackground=LightBlue)

    VDbutton = tk.Button(main, text="View Database", fg="Black", height=10, width=27, command=database)
    VDbutton.place(x=1, y=55)

    Addbutton = tk.Button(main, text="Add Entry", fg="black", height=10, width=28, command=addEntry)
    Addbutton.place(x=249, y=55)

    Removebutton = tk.Button(main, text="Remove Entry", fg="black", height=10, width=27, command=removeEntry)
    Removebutton.place(x=505, y=55)

    Closebutton = tk.Button(main, text="Close", fg="Black", height=5, width=43, command=quit)
    Closebutton.place(x=1, y=231)

    Returnbutton = tk.Button(main, text="Log Off", height = 5, width = 43, command = retlog)
    Returnbutton.place(x = 377, y = 231)

    # This frame is the black line seperating the title from the buttons
    f = tk.Frame(main, bg=Black, height=8, width=750)
    f.pack()
    f.place(x=0, y=50)




def login():
    global log
    log = tk.Tk()
    log.title("Login")
    log.resizable(False, False)
    log.geometry('500x300')

    def checkdetails():
        Username = UE.get()
        Password = PE.get()

        if Username == 'Capp' and Password == '123':
            main()
            log.destroy()

        else:
            error.tkraise()
            print('Username or Password is Incorrect')
            UE.delete(0, 'end')
            PE.delete(0, 'end')

    errorF = tk.Frame(log, bg = White, height = 30, width = 1000)
    errorF.place(x = 180, y = 200)

    error = tk.Label(log, text="Username or Password is incorrect")
    error.place(x=180, y=200)
    error.lower()

    header = tk.Frame(log, bg=LightBlue, height=50, width=1000)
    header.place(x=0, y=0)

    f = tk.Frame(log, bg=Black, height=8, width=750)
    f.place(x=0, y=50)

    Title = tk.Label(log, text="Enter your login details:")
    Title.configure(bg=LightBlue, font=("Futura", 20))
    Title.place(x=175, y=15)

    UL = tk.Label(log, text="Username:")
    UL.place(x=10, y=95)
    UE = tk.Entry(log, bd=5, width=40)
    UE.place(x=150, y=90)

    PL = tk.Label(log, text="Password:")
    PL.place(x=10, y=165)
    PE = tk.Entry(log, bd=5, width=40, show="*")
    PE.place(x=150, y=160)

    LoginButton = tk.Button(log, text="Login", command=checkdetails)
    LoginButton.place(x=300, y=230)

    QuitButton = tk.Button(log, text="Exit", command=quit)
    QuitButton.place(x=375, y=230)



# starts the start read function and opens the Login Screen
# as explained before it adds all the previous entries entered by the user back into the movies list
# It is necessary for this function to run before everything else
startread()
login()




tk.mainloop()