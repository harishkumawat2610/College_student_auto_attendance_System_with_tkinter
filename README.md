# College_student_auto_attendance_System_with_tkinter
Face detection and recognition and automatic attendance system 
#  Tkinter
Tkinter is a Python binding to the Tk GUI toolkit. Tk is the original GUI library for the Tcl language. Tkinter is implemented as a Python wrapper around a complete Tcl interpreter embedded in the Python interpreter. There are several other popular Python GUI toolkits. Most popular are wxPython, PyQt, and PyGTK.

# 1.install Tkinter
```sh
$ sudo apt-get install python3-tk
```
# 2.Raw GUI for My Project
<img src="https://drive.google.com/uc?id=1qqRsIB37cMcizGDzfCK1vmECndPbwSnu" alt="alt text" width="1216" height="491"/>

# 3. Create All Frames 

```sh
#import tkintter
from tkinter import *

#Create window
root = Tk()

#window title
root.title("Ad-hoc Networks Attendance System")

#Create topframe with top side
topframe=Frame(root)
topframe.pack(side=TOP)

#Create bottomframe with bottom side
bottomframe=Frame(root)

#Create leftframe in bottomframe with  left side
leftframe=Frame(bottomframe,bg='black')
leftframe.pack(side=LEFT)

#Create rightframe in bottomframe with right side
rightframe=Frame(bottomframe,padx=50)
rightframe.pack(side=RIGHT)
#Set window geometry width 1210 and height 750 and open position on screen left to 150 and top to 150
root.geometry("1210x750+150+150")
#stable main window on infinity time
root.mainloop()

```
# 4. Code for topframe
```sh
#Create topframe on root window
topframe=Frame(root)

#create coustom font for my company
my_font=Font(family="Rekha",size=30,weight="bold",slant="italic")
#create label on root window
label=Label(root,text="Ad-hoc Networks Attendance System",font=my_font,foreground="#283142").pack()
#pack topframe on top side
topframe.pack(side=TOP)
```
# Code Continuous...
