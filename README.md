# College_student_auto_attendance_System_with_tkinter
Face detection and recognition and automatic attendance system 
#  Tkinter
Tkinter is a Python binding to the Tk GUI toolkit. Tk is the original GUI library for the Tcl language. Tkinter is implemented as a Python wrapper around a complete Tcl interpreter embedded in the Python interpreter. There are several other popular Python GUI toolkits.
Most popular are wxPython, PyQt, and PyGTK.
Now we are using Tkinter

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

# 7. Create menu on root

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

#  if upload image not checked

# 1. Working function for add button

```sh
def Open_new():
	#import dataset_creator
	#creating blank lists
	known_face_encodings_list=[]
	known_names=[]
	ids=[]
	font=cv2.FONT_HERSHEY_SIMPLEX

	#creating image's directory
	try:
    		cwd=os.getcwd()
    		print(cwd)
    		os.mkdir(cwd+"/dataset_images")
	except:
    		print()
	def image_taker(dir_name,student_id):
		cam=cv2.VideoCapture(0)
		counter=0
		flag=0  
		while cam.isOpened():
			frame=cam.read()[1]
        
			#converting BGR frame to RGB frame
			rgb_frame=frame[:,:,::-1]
        
			#getting locations of faces present
			faces=fr.face_locations(rgb_frame)

			for (top,right,bottom,left) in faces:
            			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            
			cv2.putText(frame, "Press 'C' -> capture image\n q -> Quit", (0 , 35), font, 1.0, (255, 255, 255), 2)
			cv2.imshow("live",frame)
			#handler
			if cv2.waitKey(100) & 0xFF==ord('q'):
				if flag==0:
                			#remove if image is not created to avoid any issue
					os.rmdir(dir_name)
				break	
			if cv2.waitKey(100) & 0xFF==ord('c'):
            
				#saving imaegs
				cv2.imwrite(dir_name+"/image,"+str(student_id)+","+str(counter)+".jpg",frame)
				flag=1
				print("captured")
				cv2.destroyAllWindows()
		cam.release()
		cv2.destroyAllWindows()

	#setting up student Id
	choice='yes'
	#getting last student id and creating next id
	try:
		with open("ids.txt",'rb') as file_data:
			labels=pickle.load(file_data)
		student_id=max(labels)+1
	except FileNotFoundError:
		student_id=0


	while(choice=='yes'):
    
		print(student_id)

		student_name=simpledialog.askstring("Input string","Enter student name: ")
		if student_name is None:
			break
    
		#defining directory name where images will be stored
		cwd=os.getcwd()+"/dataset_images/"
		dir_name=cwd+student_name+","+str(student_id)
		#using try to avoid error when directory is already present
		try:
			os.mkdir(dir_name)
			print("check")
			if(M.get() == "check"):
				result=filedialog.askopenfile(initialdir=os.getcwd(),title="Select file",filetypes=(("Attendance files",".jpg"),("all file","*.*")))
				image_path=os.path.abspath(result.name)
				print(image_path)
				counter=0
				flag=0 
				frame=cv2.imread(image_path)
				rgb_frame=frame[:,:,::-1]
				faces=fr.face_locations(rgb_frame)
				for (top,right,bottom,left) in faces:
					cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
				cv2.putText(frame, '''Press 'C' -> capture image
								q -> Quit''', (0 , 35), font, 1.0, (255, 255, 255), 2)
				#cv2.imshow("live",frame)
				#if cv2.waitKey(100) & 0xFF==ord('q'):
				cv2.imwrite(dir_name+"/image,"+str(student_id)+","+str(counter)+".jpg",frame)
				flag=1
				print("captured")
				cv2.destroyAllWindows()
				
			else:
				image_taker(dir_name,student_id)
				print("check")
		except:
			messagebox.showerror("Error","Student name already exits.")
    
		choice=messagebox.askquestion("Input string","Add another:")
		if choice=='yes':
			student_id=student_id+1
	
	dataset_dir_name=os.getcwd()+"/dataset_images"
	folder_names=os.listdir(dataset_dir_name)
	for i in folder_names:
		dir_name=dataset_dir_name+"/"+i
		face_names=os.listdir(dir_name)
		for face_name in face_names:
			image_name=dir_name+"/"+face_name
			print(image_name)

			#loading images using face_recognition library
			known_face= fr.load_image_file(image_name)
			print(known_face)
        
			#getting encodings of faces
			known_face_encoding=fr.face_encodings(known_face)
			if len(known_face_encoding) > 0:
				known_face_encoding=fr.face_encodings(known_face)[0]
			else:
				print("fail")
			student_name=i.split(",")[0]
			student_id_in=int(i.split(",")[1])
        
			#appending encodings,ids, names into lists
			known_face_encodings_list.append(known_face_encoding)
			known_names.append(student_name)
			ids.append(student_id_in)

	print(known_names)
	print(ids)


	#storing data in files using pickle
	with open("encodings.txt",'wb') as file_data:
		pickle.dump(known_face_encodings_list,file_data)

	with open("name.txt",'wb') as file_data:
		pickle.dump(known_names,file_data)

	with open("ids.txt",'wb') as file_data:
		pickle.dump(ids,file_data)

```

# 2. if upload Image checked

```sh 
calling image_taker(dir_name,student_id)
 in above code means else part excuted
```
 
 # Working with start button
 
 ```sh
 def start():
	def save_att(student_id,name_student):
		d=datetime.date.today()
		ids=[]
		currentDT = datetime.datetime.now()
		date=currentDT.strftime("%I:%M:%S")
		#create csv file with date name
		file_name=d.strftime("%d_%B"+".csv")
		try:       
			with open(file_name,'r+') as file_data:
				file_data.seek(0)
				
				for line in file_data:
					id,name,state,dt=line.split(",")
					ids.append(int(id))
				if student_id not in ids:
					print("not present")
					
					file_data.write(str(student_id)+","+name_student+",p,"+date+"\n")
					file_data.seek(0)
					print("marked",name_student,"present")
	
		except FileNotFoundError:
			with open(file_name,'w') as file_data:
				
				print(date)
				file_data.write(str(student_id)+","+name_student+",p,"+date+"\n")
				print("file created")
	#setting font for puttext
	font=cv2.FONT_HERSHEY_SIMPLEX

#laoding data files and storing in lists
	with open("encodings.txt",'rb') as file_data:
		known_face_encodings=pickle.load(file_data)

	with open("name.txt",'rb') as file_data:
		known_names=pickle.load(file_data)
		print(known_names)
    
	with open("ids.txt",'rb') as file_data:
		student_ids=pickle.load(file_data)
		print(student_ids)
	if(k.get() == "cameraon"):
		cameraNumber =simpledialog.askstring("Input string","Camera Number or ip:port")
		print(cameraNumber)
		print(type(cameraNumber))
		if cameraNumber == '0' or cameraNumber == '1':
			camera=int(cameraNumber)
			print(camera)
			cam=cv2.VideoCapture(camera)
		
		else:
			st="http://"+cameraNumber+"/video?x.mjpg"
			print(st)
			cam=cv2.VideoCapture(st)
			
	else:
		cam=cv2.VideoCapture(0)
	if(h.get() == "check"):
		playtime =simpledialog.askinteger("Input string","Enter Time in Minutes")
		capture_duration = playtime*60
		start_time = time.time()
		timeplay=int(time.time() - start_time)
	else:
		timeplay=1
		capture_duration=2
	while (timeplay < capture_duration):
		frame=cam.read()[1]
		
			

		#converting BGR frame to RGB frame
		rgb_frame=frame[:,:,::-1]

		#gettting face locations
		face_locations=face_recognition.face_locations(rgb_frame)
    
		#getting face encodings
		current_face_encoding=face_recognition.face_encodings(rgb_frame,face_locations)
    
		for (top,right,bottom,left),face_encoding in zip(face_locations,current_face_encoding):

		#compariong face with known faces
			matches=face_recognition.compare_faces(known_face_encodings,face_encoding)
        	#print(matches)
			name="unknown"
        	
			if True in matches:
				#getting index for matched face
				match_index=matches.index(True)
        	    
				#getting name of the person
				name=known_names[match_index]
				student_id_det=student_ids[match_index]
				save_att(student_id_det,name)
			else:
				continue
			
			cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),1)
			if(h.get() == "check"):
				hk=int(time.time() - start_time)
				cv2.putText(frame,str(hk), (0 , 35), font, 1.0, (255, 255, 255), 2)
				cv2.putText(frame, name, (left , top), font, 1.0, (255, 255, 255), 2)
			else:
				cv2.putText(frame, name, (left , top), font, 1.0, (255, 255, 255), 2)
		if(h.get() == "check"):
			timeplay=int(time.time() - start_time)
			
		cv2.imshow("Live",frame)  	
		if cv2.waitKey(1) & 0xFF==ord('q'):
			break	
	cam.release()
	cv2.destroyAllWindows()
 ```
 

