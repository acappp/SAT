import tkinter as tk
top = tk.Tk()


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



def main():
    main = tk.Tk()
    main.title('Movie Database')
    main.resizable(False, False)
    main.geometry('750x325')

    # These first three blocks are simply adding the frames and titles for the main menu of the GUI
    # I've used .place as I believe it's the most accuracte way of placing things
    t = tk.Frame(main, bg=LightBlue, height=1000, width=1000)
    t.pack()
    t.place(x=0, y=0)

    bottomf = tk.Frame(main, bg=Black, height=500, width=750)
    bottomf.pack()
    bottomf.place(x=0, y=55)

    title = tk.Label(main, text="MOVIE PLANNER")
    title.pack()
    title.configure(bg=LightBlue, font=("Futura", 30))
    title.place(x=300, y=12)

    # The next 6 small blocks of code here add all the needed buttons onto the main menu of the GUI
    # Each calls a different fuction that will open a specific corresponding  window
    settingsbutton = tk.Button(main, text="Settings", fg="Black", command=settings)
    settingsbutton.pack()
    settingsbutton.place(x=650, y=12)
    settingsbutton.configure(highlightbackground=LightBlue)
    VDbutton = tk.Button(main, text="View Database", fg="Black", height=10, width=27, command=database)
    VDbutton.pack()
    VDbutton.place(x=1, y=55)
    Addbutton = tk.Button(main, text="Add Entry", fg="black", height=10, width=28, command=addEntry)
    Addbutton.pack()
    Addbutton.place(x=249, y=55)
    Removebutton = tk.Button(main, text="Remove Entry", fg="black", height=10, width=27, command=removeEntry)
    Removebutton.pack()
    Removebutton.place(x=505, y=55)
    Closebutton = tk.Button(main, text="Close", fg="Black", height=5, width=90, command=quit)
    Closebutton.pack()
    Closebutton.place(x=1, y=231)

    # This frame is the black line seperating the title from the buttons
    f = tk.Frame(main, bg=Black, height=8, width=750)
    f.pack()
    f.place(x=0, y=50)


def login():
    log = tk.Tk()
    log.title("Login")
    log.resizable(False, False)
    log.geometry('500x300')


    def checkdetails():
        Username = UE.get()
        Password = PE.get()

        if Username == 'Josie' and Password == '123':
            main()

        else:
            error.tkraise()
            print('Username or Password is Incorrect')


    errorF = tk.Frame(log, bg = White, height = 30, width = 1000)
    errorF.place(x = 180, y = 200)

    error = tk.Label(log, text="Username or Password is incorrect")
    error.pack()
    error.place(x=180, y=200)
    error.lower()

    header = tk.Frame(log, bg=LightBlue, height=50, width=1000)
    header.pack()
    header.place(x=0, y=0)

    f = tk.Frame(log, bg=Black, height=8, width=750)
    f.pack()
    f.place(x=0, y=50)

    UL = tk.Label(log, text="Username:")
    UL.pack()
    UL.place(x=10, y=95)
    UE = tk.Entry(log, bd=5, width=40)
    UE.pack()
    UE.place(x=150, y=90)

    PL = tk.Label(log, text="Password:")
    PL.pack()
    PL.place(x=10, y=165)
    PE = tk.Entry(log, bd=5, width=40, show="*")
    PE.pack()
    PE.place(x=150, y=160)

    LoginButton = tk.Button(log, text="Login", command=checkdetails)
    LoginButton.pack()
    LoginButton.place(x=300, y=230)












login()
top.mainloop()