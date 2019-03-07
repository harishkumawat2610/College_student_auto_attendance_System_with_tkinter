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
## Ouput:- 

<img src="https://drive.google.com/uc?id=1N4D-36C_eNqXFwePJ7ys4Fu0HJ7fnlcp" alt="alt text" width="700" height="300"/>


# 5. code for leftframe in bottomframe
```s
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
```
## Output:-
Not Include right side button coding in code portion
<img src="https://drive.google.com/uc?id=1W2W-UTJCOj5casCGgtckhyFzkH0i5ncL" alt="alt text" />
# 6. code for rightframe in bottomframe
```s
rightframe=Frame(bottomframe,padx=50)
#create all image path for buttons and checkbox images
photo1=PhotoImage(file='//home//kuma-company//Attedance_tkinter//add.png')
photo2=PhotoImage(file='//home//kuma-company//Attedance_tkinter//start.png')
photo3=PhotoImage(file='//home//kuma-company//Attedance_tkinter//stop.png')
photo4=PhotoImage(file='//home//kuma-company//Attedance_tkinter//file.png')
photo5=PhotoImage(file='//home//kuma-company//Attedance_tkinter//exit.png')
photo6=PhotoImage(file='//home//kuma-company//Attedance_tkinter//clock.png')
photo7=PhotoImage(file='//home//kuma-company//Attedance_tkinter//camera1.png')
photo8=PhotoImage(file='//home//kuma-company//Attedance_tkinter//upimg.png')

#button bt1 for add new entry
Bt1=Button(rightframe,text="New Entry",image=photo1,activebackground="green", bd=0,width=10)
Bt1.pack(fill=X)

#button bt2 for start webcam
Bt2=Button(rightframe,text="Start",image=photo2,activebackground="green", bd=0)
Bt2.pack(fill=X,pady=10)

##button bt3 for stop camera
Bt3=Button(rightframe,text="Stop(Press'Q')",image=photo3,activebackground="green", bd=0)
Bt3.pack(fill=X,pady=10)

##button bt4 for seen files
Bt4=Button(rightframe,text="files",width=10,image=photo4,activebackground="green", bd=0)
Bt4.pack(fill=X,pady=10)

##button bt5 for Exit programme
Bt5=Button(rightframe,text="EXIT",image=photo5,activebackground="green", bd=0)
Bt5.pack(fill=X,pady=10)

#check_bt for set time period in minutes
h=StringVar()
check_bt=Checkbutton(rightframe,text="Set Time",variable=h, offvalue="uncheck",onvalue="check",activeforeground="green",width=120,image=photo6,compound=TOP)
check_bt.pack(side=LEFT)

#check_bt2 for upload images if person(student notpresent ) or offline making data 
M=StringVar()
check_bt2=Checkbutton(rightframe,text="Upload Image",variable=M, offvalue="uncheck",onvalue="check",activeforeground="green",width=120,image=photo8,compound=TOP)

#check_bt3 for set camera or change camera
k=StringVar()
check_bt3=Checkbutton(rightframe,text="Set Camera",variable=k, offvalue="cameraoff",onvalue="cameraon",activeforeground="green",width=130,image=photo7,compound=TOP)
check_bt3.pack(side=RIGHT)

rightframe.pack(side=RIGHT)
```

## output:-
<img src="https://drive.google.com/uc?id=1SZvTi_tzv39_N21Hn1gykUKuP1FPRsx1" alt="alt text" />

# create menu on root
```s
#create a main_menu on root
main_menu=Menu(root)

#config main_menu with root
root.config(menu=main_menu)
 
#Create fileMenu on main_menu and tearoff = False means not show deses point on menu
fileMenu=Menu(main_menu,tearoff=False)

#add first label on main_main is More options 
main_menu.add_cascade(label="More Options",menu=fileMenu)

# add a label "open files" on fileMenu 
fileMenu.add_command(label="Open files")

#using separator for show labels in one group
fileMenu.add_separator()

#add label "Images
fileMenu.add_command(label="Images")
fileMenu.add_separator()

#add label attendance count
fileMenu.add_command(label="Attendance Count")

# add label attendance search 
fileMenu.add_command(label="Attendance Search")
fileMenu.add_separator()

#Create submenu on fileMenu
Newfile=Menu(fileMenu,tearoff=False)
Newfile.add_command(label="College Website")
Newfile.add_command(label="About")
fileMenu.add_cascade(label="More options",menu=Newfile)
```
# Output:-
<img src="https://drive.google.com/uc?id=1LlC5q2FVqIqhdCGVticDBmotSgW4Tint" alt="alt text" />

# Next day continuous code 
