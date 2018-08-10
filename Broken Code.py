
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