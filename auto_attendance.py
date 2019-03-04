#import tkintter
from tkinter import *

#Create window
root = Tk()

#window title
root.title("Ad-hoc Networks Attendance System")

#Create topframe with top side
#Create topframe on root window
topframe=Frame(root)

#create coustom font for my company
my_font=Font(family="Rekha",size=30,weight="bold",slant="italic")
#create label on root window
label=Label(root,text="Ad-hoc Networks Attendance System",font=my_font,foreground="#283142").pack()
#pack topframe on top side
topframe.pack(side=TOP)

#Create bottomframe with bottom side
bottomframe=Frame(root)

#Create leftframe in bottomframe with  left side
#create leftframe in bottomframe with left side
leftframe=Frame(bottomframe,bg='black')

#create a canvas for image on leftframe
canvas=Canvas(leftframe,width=627,height=663)
canvas.pack()

#photo for canvas with photo path
photo=PhotoImage(file='//home//kuma-company//Attedance_tkinter//adhocprofile.png')
#create position of canvas and image start at NW
canvas.create_image(50,10,image=photo,anchor=NW)
leftframe.pack(side=LEFT)
#Create rightframe in bottomframe with right side
rightframe=Frame(bottomframe,padx=50)
rightframe.pack(side=RIGHT)
#Set window geometry width 1210 and height 750 and open position on screen left to 150 and top to 150
root.geometry("1210x750+150+150")
#stable main window on infinity time
root.mainloop()


