
def scheduleMenu():
    #month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
    #         "November", "December"]


    schedule = tk.Tk()
    schedule.title("Schedule")
    schedule.resizable(False, False)
    schedule.geometry('500x400')
    # Importing calender allows me to have a calender (schedule) in the gui




    DoneButton = tk.Button(schedule, text="Done", command=schedule.destroy)
    DoneButton.pack()
    DoneButton.place(x=375, y=350)

    #nmonth = 1
    #if month == "January":
    #    nmonth = 1
    #elif month == "February":
    #    nmonth = 2
    #elif month == "March":
    #    nmonth = 3
    #elif month == "April":
    #    nmonth = 4
    #elif month == "May":
    #    nmonth = 5
    #elif month == "June":
    #    nmonth = 6
    #elif month == "July":
    #    nmonth = 7
    #elif month == "August":
    #    nmonth = 8
    #elif month == "September":
    #    nmonth = 9
    #elif month == "October":
    #    nmonth = 10
    #elif month == "November":
    #    nmonth = 11
    #elif month == "December":
    #    nmonth = 12

    #import calendar
    #cal = calendar.month(2018, nmonth)
    #l = tk.Label(schedule, text=cal)
    #l.pack()




#Editbutton = tk.Button(top, text="Edit Entry", fg="black", height = 10, width = 30, command = editmenu)
#Editbutton.pack()
#Editbutton.place(x=0, y=230)

#VSbutton = tk.Button(top, text="View Schedule", fg="black", height = 10, width = 30 ) #command = scheduleMenu)
#VSbutton.pack()
#VSbutton.place(x=270, y=230)



# This is the function for the edit menu
def editmenu():
    edit = tk.Tk()
    edit.title("Edit an Existing entry")
    edit.resizable(False, False)
    edit.geometry('500x400')

    header = tk.Frame(edit, bg=LightBlue, height=50, width=1000)
    header.pack()
    header.place(x=0, y=0)
    F1 = tk.Frame(edit, bg=Black, height=5, width=1000)
    F1.pack()
    F1.place(x=0, y=45)
    L1 = tk.Label(edit, text="Edit an Entry:")
    L1.pack()
    L1.configure(bg=LightBlue, font = ("Futura", 20))
    L1.place(x=200, y=10)
    L2 = tk.Label(edit, text="Select the name of the entry you wish to change:")
    L2.pack()
    L2.place(x = 100, y = 50)


    ## For drop the box
    def generatelist():
        mNames = []
        for i in Movies:
            mNames.append(i.name)
        tkvar = tk.StringVar(edit)
        tkvar.set(mNames[0])

        DropMenu = tk.OptionMenu(edit, tkvar, *mNames)
        DropMenu.pack()
        DropMenu.place(x=125, y=75)
        DropMenu.configure(height=2, width=30)

        return tkvar

    def delete(tkvar):
        p = tkvar.get()
        print(p)
        Movies.pop(0)

    tkvar = generatelist()

    editButton = tk.Button(edit, text="Edit Entry", command=lambda: delete(tkvar))
    editButton.pack()
    editButton.place(x=275, y=350)

    DoneButton = tk.Button(edit, text="Done", command=edit.destroy)
    DoneButton.pack()
    DoneButton.place(x=375, y=350)