from tkinter import *

root=Tk()
root.geometry('500x500')


frame1=Frame(root,width=500,height=500,bg='green')
frame1.pack()

button1=Button(frame1,text='Hello')
button1.pack(side='bottom')

root.mainloop()