import tkinter as tk #for graphics gui
from tkinter import * 
from tkinter import Menu, ttk #for drop downmenu
import re # importing modul for reguler expressions
import studentProcess #importing student process (broker)

class ECR(tk.Tk):
    """Class that inherits other classes (pages) and stores each class as frames to allow program
        to switch between frames or pages.i.e. welocome page to main menu page within the same window"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #initialising tkinter 

        window = tk.Frame(self)
        window.pack(side="top", expand = False)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {} # container that holds all of the frames/pages that we creatje


        frame1 = studentDetails(window, self) #each page is a frame
        frame2 = welcome_page(window, self)
        frame3 = Main_menu(window, self)
        frame4 = coursePage(window, self)
        frame5 = studentUnique(window, self) 
        frame6 = NotificationPage(window, self)
        
        self.frames[studentDetails] = frame1
        self.frames[welcome_page] = frame2
        self.frames[Main_menu] = frame3
        self.frames[coursePage] = frame4
        self.frames[studentUnique] = frame5
        self.frames[NotificationPage] = frame6

        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=0, sticky="nsew")
        frame3.grid(row=0, column=0, sticky="nsew")
        frame4.grid(row=0, column=0, sticky="nsew")
        frame5.grid(row=0, column=0, sticky="nsew")
        frame6.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(welcome_page)


        
    def show_frame(self, page):  #Function that displays the selected frame/page from our container
        """"This function takes a class (page) as an argument and displays that class
            IF it exists in the container"""
        frame = self.frames[page]
        frame.tkraise()

    def disable_frame(self, page): #used to disable frame when prompt message boxes open
        frame = self.frames[page]
        frame.tkraise()
        for items in frame.winfo_children():
            items.configure(state='disable')        


    def enable_frame(self, page): #used to enable frame when prompt message boxes are terminated
        frame = self.frames[page]
        for items in frame.winfo_children():
            items.configure(state='normal')



class welcome_page(tk.Frame):
    """This class creates the welcome page with the college welcoming message"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/bg.png')
        label = tk.Label(self,image=self.bg)
        label.grid(pady=0,padx=0)

        #Begin Button which takes you to main menu
        self.login_button_img = tk.PhotoImage(file='Icons/Buttons/letsBegin.png')#All folders for images in software must be in the root folder
        letsBegin = tk.Button(self,image=self.login_button_img, width=100,height=38,command=lambda:controller.show_frame(Main_menu))
        letsBegin.place(x=635, y=405)





class Main_menu(tk.Frame):
    
    """This class creates the Main_menu page"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/mainMenu.png') #all backgrounds located in root folder
        label = tk.Label(self,image=self.bg)
        label.grid(pady=0,padx=0)

        def welcome_student():
            """This function produces a reminder message on a pop up message
                to remind the student what details will be required"""

            begin_register.config(state='disabled')#de-activates all buttons to stop pop from reproducing and to focus on pop message
            quit_r.config(state='disabled')
            popup_window= tk.Toplevel()
            popup_window.attributes('-alpha', 0.86)
            
            #opacity is reduced to all pop-ups in software for professional look
            
            popup_window.wm_title("Welcome Student")
            photo = PhotoImage(file ='icons/info/Reminder_message.png') #loads message png 
            photo = photo.subsample(2) #shinks message to the correct size
            imageLabel = tk.Label(popup_window, image=photo)
            imageLabel.pack(padx=15, pady=35)
           
            def proc_close_popup():
                """Function that proceeds to students detail page and closes popup when Proceed is pressed"""
                
                begin_register.config(state='active')
                quit_r.config(state='active')
                popup_window.destroy()
                controller.show_frame(studentDetails)#go to student details page

            def canc_close_popup():
                """Function that closes popup when Cancel is pressed"""
                begin_register.config(state='active')#re-activates all buttons when pop-up closed
                quit_r.config(state='active')
                popup_window.destroy()
            
            proceed = ttk.Button(popup_window, text="Proceed", width = 23, command = lambda:proc_close_popup())#pop-up proceed button
            proceed.place(x=160,y=355)
            cancel = ttk.Button(popup_window, text="Cancel", width = 23, command = lambda:canc_close_popup())#pop-up cancel button
            cancel.place(x=330,y=355)

            popup_window.mainloop()

            
     
        self.reminder = tk.PhotoImage(file='Icons/Buttons/Register.png')#Register Button
        begin_register = tk.Button(self,image=self.reminder,command=lambda:welcome_student())
        begin_register.place(x=145, y=205)

        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#quit back to welcome page Button
        quit_r.place(x=1295, y=415)

        
        def prompt_signout():
            """Function incharge of producing pop-up for quitting (back to welcome page)"""
            
            quit_r.config(state='disabled')
            begin_register.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)
            popup_window.wm_title("Are you sure?")

            def quit():
                quit_r.config(state='normal')
                begin_register.config(state='normal')
                controller.show_frame(welcome_page)#back to welcome page
                popup_window.destroy()
            
            def close_popup():
                quit_r.config(state='normal')#re-activates all buttons when pop-up closed
                begin_register.config(state='normal')
                popup_window.destroy()

            
                
            label = ttk.Label(popup_window, text="Are you sure you want to quit",font=("bold",12))#pop up message
            label.grid(row=0, column=0,padx=70,pady=13)

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:quit())
            Okay.grid(row=1, column=0,pady=0, padx=0,)
            
            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.grid(row=2, column=0,pady=0, padx=0,)




class studentDetails(tk.Frame):
    """This class creates the student details and contact page"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/studentDetails.png')#load background
        main_window = tk.Label(self,image=self.bg)
        main_window.grid(pady=0,padx=0)



        
        title = ['Mr', 'Mrs', 'Miss', 'Ms'] #list containing titles for drop down menu


        DoB = tk.Entry(self, width=21,font=("Helvetica", 12, "bold") )
        DoB.place(x=903, y= 52)

        
        #creates title drop down menu
        select_title = ttk.Combobox(self,values=title, justify='center')
        select_title.current(0)  #sets firsts day to monday
        select_title['state'] = 'readonly'
        select_title.place(x=620, y=50,width = 100,height = 30)

        
        fName = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        fName.place(x=550, y=100)
                    
        
        sName = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        sName.place(x=550, y=150)
                    
        
        address1 = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        address1.place(x=550, y=200)

        
        address2 = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        address2.place(x=550, y=250)
        
        
        county = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        county.place(x=550, y=300)

        
        postcode = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        postcode.place(x=550, y=350)

        
        phoneNum = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        phoneNum.place(x=550, y=400)

        
        email = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        email.place(x=550, y=450)

        self.message = '' #pre prepared message for invalid inputs will be stored here and displayed inside the invalid pop up window below




        def invalid_pop():
            
            """This function produces an invalid message on a pop when an input is invalid"""

            next_to_course.config(state='disabled')
            quit_r.config(state='disabled')
            popup_window= tk.Toplevel()
            popup_window.attributes('-alpha', 0.86)
            popup_window.wm_title("invalid details")
            imageLabel = tk.Label(popup_window, text=self.message)
            imageLabel.pack(padx=185, pady=55)

            def canc_close_popup():
                next_to_course.config(state='active')
                quit_r.config(state='active')
                popup_window.destroy()

            ok = ttk.Button(popup_window, text="OK", width = 23, command = lambda:canc_close_popup())# closes pop-up and remains students detail page
            ok.place(x=230,y=95)

            popup_window.mainloop()


        def invalid_pop2():

            """This function produces an invalid message on a pop when a student is already registered"""

            next_to_course.config(state='disabled')
            quit_r.config(state='disabled')
            popup_window= tk.Toplevel()
            popup_window.attributes('-alpha', 0.86)
            popup_window.wm_title("invalid details")
            imageLabel = tk.Label(popup_window, text=self.message)
            imageLabel.pack(padx=185, pady=50)

            def canc_close_popup():
                next_to_course.config(state='active')
                quit_r.config(state='active')
                popup_window.destroy()

            ok = ttk.Button(popup_window, text="OK", width = 23, command = lambda:canc_close_popup())#remains in to student details page 
            ok.place(x=330,y=185)

            popup_window.mainloop()





        def valid_pop():
            
            """This function produces an valid message on a pop when all inputs are invalid"""
            #gets data from all inputs
            getdata = (select_title.get(), DoB.get(), fName.get(), sName.get(), \
                       address1.get(), address2.get(), county.get(), postcode.get(), phoneNum.get(),email.get())

            #communicates with student process
            
            if studentProcess.checkExists(getdata) == True: 
                #if student is already registered gets details for message (speak to reception)
                #title, first name, second name and student id
                #Type of course i.e full time/part time
                # course name
                #start date, end date
                self.message = select_title.get()+' '+ fName.get()+ ' ' + sName.get() + '('+ str(studentProcess.getRegStudId(getdata))+')'\
                               +'\n' +'DoB: ' + DoB.get()+'\n'*2+' is already a registered student studying '\
                               +str(studentProcess.getCourseDetails(studentProcess.getRegCourseId(studentProcess.getRegStudId(getdata)))[2])+ ' ' \
                               +str(studentProcess.getCourseDetails(studentProcess.getRegCourseId(studentProcess.getRegStudId(getdata)))[0])+ ' ' + '('+\
                               str(studentProcess.getRegCourseId(studentProcess.getRegStudId(getdata))) +')'+\
                               '\n'+ 'Duration: ''('+ str(studentProcess.getCourseDetails(studentProcess.getRegCourseId(studentProcess.getRegStudId(getdata)))[3]) + ' - ' \
                               + str(studentProcess.getCourseDetails(studentProcess.getRegCourseId(studentProcess.getRegStudId(getdata)))[4])+')'+'\n'*2\
                               +'if you wish to change course, you must speak to a member of staff at reception.'+'\n'+'Alternatively you can email the registrations team at registration@cov.uk'
                
                invalid_pop2()

            #else display pop up congratulations pop-up for valid details
            next_to_course.config(state='disabled')
            quit_r.config(state='disabled')
            popup_window= tk.Toplevel()
            popup_window.attributes('-alpha', 0.86)
            popup_window.wm_title("invalid details")
            imageLabel = tk.Label(popup_window, text="Congratulations all fields are correct your ready "+"\n"+"to progress to the next stage to select your "+"\n" + "course")
            imageLabel.pack(padx=185, pady=45)



            
            def proc_close_popup():
                
                """This function closes valid pop-up message and stores student
                    details in temporary table by communicating to student processor
                    and moves to course selection stage"""
                
                next_to_course.config(state='active')
                quit_r.config(state='active')
                studentProcess.TempStudDet(getdata)#passing information to student processor
                controller.show_frame(coursePage)#move to course selection page
                popup_window.destroy()
                


            def canc_close_popup():
                
                """This function closes pop-up and remains in student details page"""
                
                next_to_course.config(state='active')
                quit_r.config(state='active')
                popup_window.destroy()

            ok = ttk.Button(popup_window, text="OK", width = 13, command = lambda:proc_close_popup())#proceed to course page
            ok.place(x=230,y=107)

            cancel = ttk.Button(popup_window, text="Cancel", width = 13, command = lambda:canc_close_popup())#remain in student details page
            cancel.place(x=320,y=107)
            
            popup_window.mainloop()


        def check_empty():
            """ This Function checks to see if any mandetory fields are empty, if so creates an error message for pop else it moves on to the
                next error check"""
            if fName.get() == '' or sName.get() == '' or address1.get() == ''or address2.get() == ''\
               or postcode.get() == ''or phoneNum.get() == ''or email.get() == ''or DoB.get() =='':
                
                self.message="Please Enusre all mandetory fields are filled in" #all inputs are checked if empty
                invalid_pop() #if one is empty, invalid pop-up message
            
            else:
                check_DoB()#all are filled run the next check function(date of birth format)

        def check_DoB():
            """This function uses regular expression patterns to validate the date of birth inputed by the student"""
            
            re_pattern = "^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$" #regular expression for UK first line address
    
            if re.match(re_pattern,DoB.get()):
                check_fName()#if date of birth format correct run next check function (name format)

            else:
               self.message = "You have inputted an incorrect date of birth. "+"\n"+"Please input correct date of birth"
               invalid_pop()

                
        def check_fName():
            """This function checks to see if the first name is a valid name"""
            
            for i in fName.get():
                # checks if numbers or non-alphabetical characters are in the first name entry 
                if i not in ('abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ-'):
                     self.message = "First Name can only contain letters within "+"\n"+"the alphabet and should not contain spaces"
                     invalid_pop()
                    
            else:
                confirm_sName()#if name format correct run next check function (surname)

            
        def confirm_sName():
            """This function checks to see if the surname name is a valid name/s"""
            
            for i in sName.get():
                # checks to see if numbers or non-alphabetical characters are in the surname entry 
                if i not in 'abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ-':
                     self.message = "Surname can only contain letters within the alphabet"
                     invalid_pop()
                    
            else:
                check_address1()#if surname format correct run next check function (address line 1)

        def check_address1():
            """This function uses regular expression patterns to validate the Address line 1 inputed by the student"""
            
            re_pattern = "(\d+).*?\s+(.+)" #regular expression for UK first line address
    
            if re.match(re_pattern,address1.get()):# checks address inputted matches UK address standards(door no, street name, street type)
                check_address2()#if address line 1 correct run next check function (address line 2)

            else:
               self.message = "Address line 1 is incorrect, please check and re-enter"
               invalid_pop()

        def check_address2():
            """This function checks if address line 2 is Valid i.e. town  and  city"""

            
            if len(address2.get().split())>2 or len(address2.get().split())<2:
                self.message = "Address line 2 is incorrect, please check and re-enter"
                invalid_pop()
                

            else:
               check_postcode()#if address line 2 correct run next check function (postcode)
        

        def check_postcode():
            """This function uses regular expression patterns to validate the postcode inputed by the student"""
            
            re_pattern = "^([A-Z]{1,2}\d{1,2}|d[A-Z]{1,2}\d[A-Z])\d[A-Z]{2}$" #regular expression for UK postcodes
    
            if re.match(re_pattern,postcode.get()):
                check_phoneNum()#if postcode correct to UK standard postcode format, run next check function (phone number)

            else:
               self.message = "postcode is incorrect, please check and re-enter"
               invalid_pop()
            

            
        def check_phoneNum():
            """This function uses regular expression patterns to validate the mobile number inputed by the student"""
            
            re_pattern = "^(07\d{8,12}|447\d{7,11})$" # regular expression for UK mobile numbers
            re_pattern2 = "^(01\d{8,12}|447\d{7,11})$" # regular expression for UK landlines
            
            if re.match(re_pattern,phoneNum.get()) or re.match(re_pattern2,phoneNum.get()): 
                check_email()#if phonenumber correct to UK standard contact numbers format, run next check function (email)

            else:
               self.message = "PhoneNumber is incorrect, please check and re-enter"
               invalid_pop()

            

        def check_email():
            """This function uses regular expression patterns to validate the email address inputed by the student"""
            re_pattern = "[^@]+@[^@]+\.[^@]+"  # regular expression for emails
            
            if re.match(re_pattern,email.get()):
                valid_pop()#if email correct format run final pop-up for validity to move on to course selection stage

            else:
               self.message = "email is not valid please enter valid email address"
               invalid_pop()
               
            
        #creates next to course page
        self.next = tk.PhotoImage(file='Icons/Buttons/next.png')
        next_to_course = tk.Button(self,image=self.next,command=lambda:check_empty())
        next_to_course.place(x=950, y=220)
        


        #quit button to back to Main Page
        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#including quit
        quit_r.place(x=1295, y=415)

                
            
        def prompt_signout():
            """Function incharge of quitting (back to Main menu page)"""
            quit_r.config(state='disabled')
            next_to_course.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)
            popup_window.wm_title("Are you sure?")

            def quit():
                quit_r.config(state='normal')
                next_to_course.config(state='normal')
                controller.show_frame(Main_menu)
                popup_window.destroy()
                
            def close_popup():
                quit_r.config(state='normal')
                next_to_course.config(state='normal')
                popup_window.destroy()

            
                
            label = ttk.Label(popup_window, text="Are you sure you want to quit",font=("bold",12))
            label.grid(row=0, column=0,padx=70,pady=13)

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:quit())
            Okay.grid(row=1, column=0,pady=0, padx=0,)
            
            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.grid(row=2, column=0,pady=0, padx=0,)




class coursePage(tk.Frame):
    """This class creates the Course page"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/courseDetails.png')
        main_window = tk.Label(self,image=self.bg)
        main_window.grid(pady=0,padx=0)



        #creates the treeview table which contains the course columns
        self.treeviewCourses = ttk.Treeview(main_window)
        self.treeviewCourses.place(x=255, y=115)
        
        dataColumns = ('Course', 'Type', 'Code','Start', 'End', 'Hours','Available Spaces') #column names

        testdata = studentProcess.getCourses()

        
        
        self.treeviewCourses.config(columns = dataColumns, show = 'headings')
        
        for column in dataColumns:
            #inserts column headings and allows headers to click to sort
            self.treeviewCourses.heading(column, text=column.title(), command=lambda col=column: sort(self.treeviewCourses, col, 0))

        for info in testdata:
            #inserting column names into headers
            self.treeviewCourses.insert('', 'end', values=info, tags=('info',))
            
        self.treeviewCourses.column('Course',width = 200, anchor = 'w')#department column
        self.treeviewCourses.column('Type',width = 60, anchor = 'w')#course type column
        self.treeviewCourses.column('Code',width = 90, anchor = 'w')#course code column
        self.treeviewCourses.column('Start',width = 90, anchor = 'w')#start date column
        self.treeviewCourses.column('End',width = 90, anchor = 'w')#end date column
        self.treeviewCourses.column('Hours',width = 60, anchor = 'w')#hours perweek column
        self.treeviewCourses.column('Available Spaces',width = 150, anchor = 'w')#Available spaces column
        
        def sort(tree, column, descend):
            """uses tree sort algorithm when the column headers are clicked on"""
            # selects the values it needs to sort
            value_data = [(tree.set(children, column), children) for children in tree.get_children('')]
            # numeric data changed to a float for sorting
            # now we sort the data into order
            value_data.sort(reverse=descend)
            for i, info in enumerate(dat):
                tree.move(info[1], '', i)
            # now sort the data in the opposite order
            tree.heading(column, command=lambda column=column: sort(tree, column, int(not descend)))
            
        def getselected(treeview):
            """Function that gets/returns the selected course from the course table"""
            selected = self.treeviewCourses.focus()
            item = (self.treeviewCourses.item(selected))
            return(item["values"])#returns row of values from course table
        

        #only allows one course to be selected and returned
        self.treeviewCourses.config(selectmode='browse')
        self.treeviewCourses.bind('<ButtonRelease-1>', getselected)


        def prompt_full():
            """Function that prompts a display message if course is full"""
            
            quit_r.config(state='disabled')
            next_to_id.config(state='disabled')
            prev_to_id.config(state='disabled')
        
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)
            popup_window.wm_title("Course Full")
            #message with course name and course type when full
            imageLabel = tk.Label(popup_window, text="Im sorry but the course you have chosen ("\
                                  + str(getselected(self.treeviewCourses)[0])+ ", " +\
                                  str(getselected(self.treeviewCourses)[2]) +") is full."+ "\n" + \
                                  "Please speak to member of staff at reception if you wish for us "+ "\n" + \
                                  "to email you when this course is free.")
            
            imageLabel.pack(padx=185, pady=50)
            
            
            def close_popup():
                next_to_id.config(state='normal')
                prev_to_id.config(state='normal')
                quit_r.config(state='normal')
                popup_window.destroy()

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:close_popup())
            Okay.place(x=330,y=105)


        def prompt_choose():
            """Function that prompts a display message for final selection of course to take to the next stage"""
            quit_r.config(state='disabled')
            next_to_id.config(state='disabled')
            prev_to_id.config(state='disabled')
        
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)
            popup_window.wm_title("Are you sure?")
            #message with course name and course type when course is free
            imageLabel = tk.Label(popup_window, text="You have chosen to study:-"+ "\n"*2 +\
                                  str(getselected(self.treeviewCourses)[0])+ " (" +\
                                  str(getselected(self.treeviewCourses)[1])+ ")" + " - "  +\
                                  str(getselected(self.treeviewCourses)[2])+ "\n" +\
                                  "Date Starting: " +str(getselected(self.treeviewCourses)[3])+ " \n " +\
                                  "Date Endind: " +str(getselected(self.treeviewCourses)[4])+ "\n" *2 +\
                                  "You wont be able to cance this course once it has been chosen."+ "\n" +\
                                  "In order to cancel you must speak to a member of staff at reception." + "\n" *2 +\
                                  "Are you sure you want to choose this course?")
            
            imageLabel.pack(padx=185, pady=70)
            
            
            def close_popup():
                """function that closes pop-up"""
                next_to_id.config(state='normal')
                prev_to_id.config(state='normal')
                quit_r.config(state='normal')
                popup_window.destroy()

            
            def choose():
                """function that writes to db course chosen"""
                next_to_id.config(state='normal')
                prev_to_id.config(state='normal')
                quit_r.config(state='normal')
                #communicating with student processor
                studentProcess.TempStudCourse(getselected(self.treeviewCourses)[1])
                popup_window.destroy()
                controller.show_frame(studentUnique)
                

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:choose())
            Okay.place(x=270,y=245)

            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.place(x=350,y=245)

            
            

        
        def check_course_free():
            """This function checks if the course is free"""
            if getselected(self.treeviewCourses)[6] == 0:
                prompt_full()#if full run prompt message (full)

            else:
                prompt_choose()#run prompt message (continue)
                

        
        #creates next to student id/password and previous buttons for student detail page
        self.next = tk.PhotoImage(file='Icons/Buttons/next.png')
        next_to_id = tk.Button(self,image=self.next,command=lambda:check_course_free())
        next_to_id.place(x=1050, y=220)

        self.prev = tk.PhotoImage(file='Icons/Buttons/previous.png')
        prev_to_id = tk.Button(self,image=self.prev,command=lambda:check_course_free())
        prev_to_id.place(x=90, y=220)



        #quit button to back to Main Page
        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#including quit
        quit_r.place(x=1295, y=415)

                
            
        def prompt_signout():
            """Function incharge of quitting (back to students details page)"""
            quit_r.config(state='disabled')
            next_to_id.config(state='disabled')
            prev_to_id.config(state='disabled')
        
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
            popup_window.wm_title("Are you sure?")

            def quit():
                next_to_id.config(state='normal')
                prev_to_id.config(state='normal')
                quit_r.config(state='normal')
                controller.show_frame(Main_menu)
                popup_window.destroy()
            
            def close_popup():
                next_to_id.config(state='normal')
                prev_to_id.config(state='normal')
                quit_r.config(state='normal')
                popup_window.destroy()

            
                
            label = ttk.Label(popup_window, text="Are you sure you want to quit",font=("bold",12))
            label.grid(row=0, column=0,padx=70,pady=13)

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:quit())
            Okay.grid(row=1, column=0,pady=0, padx=0,)
            
            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.grid(row=2, column=0,pady=0, padx=0,)



    
class studentUnique(tk.Frame):
    """This class creates the student unique username/password entry page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/userpass.png')
        main_window = tk.Label(self,image=self.bg)
        main_window.grid(pady=0,padx=0)

                    
        uName = tk.StringVar() #username name variable
        uName = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        uName.place(x=550, y=100)

                    
        pWord_ = tk.StringVar() #password variable
        pWord = tk.Entry(self, width=24,font=("Helvetica", 12, "bold"),textvariable= pWord_, show='*')
        pWord.place(x=550, y=150)
                    
        pWord2_ = tk.StringVar() #re-enter password variable
        pWord2 = tk.Entry(self, width=24,font=("Helvetica", 12, "bold"),textvariable= pWord2_, show='*' )
        pWord2.place(x=550, y=200)
        


        #creates button for next to confirmation Notification page and button for previous to course selection page
        self.finish = tk.PhotoImage(file='Icons/Buttons/complete.png')
        self.complete = tk.Button(self,image=self.finish,command=lambda: complete_details()) 
        self.complete.place(x=1050, y=220)

        self.prev = tk.PhotoImage(file='Icons/Buttons/previous.png')
        prev_to_id = tk.Button(self,image=self.prev,command=lambda:controller.show_frame(coursePage))
        prev_to_id.place(x=90, y=220)

        
        
        def prompt_incomplete():
            """Function that prompts a error message for incomplete data in username, password and password 2 entry"""
            quit_r.config(state='disabled')
            self.complete.config(state='disabled')
            prev_to_id.config(state='disabled')
            uName.config(state='disabled')
            pWord.config(state='disabled')
            pWord2.config(state='disabled')
            
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)
            popup_window.wm_title("Are you sure?")
            imageLabel = tk.Label(popup_window, text="The Username or Password is Incorrect, Please check and try again")
            
            imageLabel.pack(padx=185, pady=70)
            
            
            def close_popup():
                """function that closes pop-up"""
                self.complete.config(state='normal')
                prev_to_id.config(state='normal')
                quit_r.config(state='normal')
                uName.config(state='normal')
                pWord.config(state='normal')
                pWord2.config(state='normal')
                popup_window.destroy()

            okay = ttk.Button(popup_window, text="close", command = lambda:close_popup())
            okay.place(x=350,y=105)
                

        def prompt_complete():
            """Function that prompts a display message for registration completion (to take user to notification page)"""
            quit_r.config(state='disabled')
            self.complete.config(state='disabled')
            prev_to_id.config(state='disabled')
            uName.config(state='disabled')
            pWord.config(state='disabled')
            pWord2.config(state='disabled')
            
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
            popup_window.wm_title("Are you sure?")
            imageLabel = tk.Label(popup_window, text="You have chosen the username"+ "\n"*2 +\
                                  uName.get()+ "\n"*2 +\
                                  "Once you complete, You cannot change any details unless you speak to a member of staff at reception"+\
                                  "\n"+"Are you sure you want to continue?")
            
            imageLabel.pack(padx=185, pady=70)
            
            
            def close_popup():
                """function that closes pop-up"""
                self.complete.config(state='normal')
                prev_to_id.config(state='normal')
                quit_r.config(state='normal')
                uName.config(state='normal')
                pWord.config(state='normal')
                pWord2.config(state='normal')
                popup_window.destroy()

            
            def complete_f():
                """function that writes to db course chosen"""
                self.complete.config(state='normal')
                prev_to_id.config(state='normal')
                quit_r.config(state='normal')
                uName.config(state='normal')
                pWord.config(state='normal')
                pWord2.config(state='normal')
                #sends final details to student processor, where student processor finalizes its process and communicates registration process  
                studentProcess.store_username_password((uName.get(),pWord.get()))
                
                controller.show_frame(NotificationPage)
                popup_window.destroy()
                
            
            complete_B = ttk.Button(popup_window, text="Complete", command = lambda:complete_f())
            complete_B.place(x=350,y=185)

            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.place(x=470,y=185)
            


        
        
        def complete_details():
            """This Function checks to see if the password is in the correct format and both passwords match"""
            
            #regular expression for Minimum eight characters,
            #at least one uppercase letter, one lowercase letter and one number
            
            re_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
            if re.match(re_pattern,pWord2.get()) and re.match(re_pattern,pWord.get()):
                if pWord.get()==pWord2.get():
                    prompt_complete()
            else:
                prompt_incomplete()

        def check_availability():
            """Function that checks if username is available and valid format"""
            
            #regular expression for Minimum eight characters,
            #at least one uppercase letter, one lowercase letter and one number
            
            re_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
            
            #username must not exist and must follow regex for it to be valid
            if (bool(re.match(re_pattern,uName.get()))) == False:
                #info invalid username box
                invalid = tk.Label(self, width=18,font=("Helvetica", 8, "bold"),text="Username invalid! ",fg="red" )
                invalid.place(x=596, y=125)

                
            elif studentProcess.CheckUsername(uName.get())==True and re.match(re_pattern,uName.get()):
                #info available username box
                available = tk.Label(self, width=18,font=("Helvetica", 8, "bold"),text="Username Available",fg="green" )
                available.place(x=596, y=125)
                
                
            else:    
                #info available username box
                unavailable = tk.Label(self, width=18,font=("Helvetica", 8, "bold"),text="Username Unavailable",fg="red" )
                unavailable.place(x=596, y=125)
                
        
        self.check_pick = tk.PhotoImage(file='Icons/Buttons/check.png')
        check = tk.Button(self,image=self.check_pick,command=lambda:check_availability())
        check.place(x=772, y=93)


        #quit button to back to Main Page
        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#including quit
        quit_r.place(x=1295, y=415)

                
           
        def prompt_signout():
            """Function incharge of quitting (back to Main page)"""
            quit_r.config(state='disabled')
            prev_to_id.config(state='disabled')
            self.complete.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)
            popup_window.wm_title("Are you sure?")

            def quit():
                quit_r.config(state='normal')
                prev_to_id.config(state='normal')
                self.complete.config(state='normal')
                controller.show_frame(Main_menu)
                popup_window.destroy()
            
            def close_popup():
                quit_r.config(state='normal')
                prev_to_id.config(state='normal')
                self.complete.config(state='normal')
                popup_window.destroy()

            
                
            label = ttk.Label(popup_window, text="Are you sure you want to quit",font=("bold",12))
            label.grid(row=0, column=0,padx=70,pady=13)

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:quit())
            Okay.grid(row=1, column=0,pady=0, padx=0,)
            
            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.grid(row=2, column=0,pady=0, padx=0,)


         
    
class NotificationPage(tk.Frame):
    
    """This class creates the notification page"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/notification.png')
        main_window = tk.Label(self,image=self.bg)
        main_window.grid(pady=0,padx=0)


        def Notification_message():
            """This function retrieves the notification message sent by the notification processor after successful registration"""
            
            Message1 = Text(self, width=54, height= 22,font=("Helvetica", 9, "bold"))
            Message1.place(x=240,y=108)

            #read from notification message 1 which contains the notification regarding the students personal details
            with open("notification_message.txt", 'r') as f:
                Message1.insert(INSERT, f.read())
                Message1.config(state="disabled")

            #read from notification message 2 which contains the notification regarding the students college details
            Message2 = Text(self, wrap=WORD, width=65, height= 22,font=("Helvetica", 9, "bold"))
            Message2.place(x=680,y=108)
            with open("notification_message2.txt", 'r') as f:
                Message2.insert(INSERT, f.read())
            self.after(1000, Notification_message)
        Notification_message()#run the notification function to display message

        self.print_pic = tk.PhotoImage(file='Icons/Buttons/print.png')#print button
        self.print_button = tk.Button(self,image=self.print_pic)
        self.print_button.place(x=1222, y=123)



        def prompt_signout():
            
            """Function incharge of completing registration and temporary table and goes back to startup page"""
            
            self.exit_button.config(state='disabled')
            self.print_button.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)
            popup_window.wm_title("Are you sure?")

            def quit():
                self.exit_button.config(state='disabled')
                self.print_button.config(state='disabled')
                controller.show_frame(welcome_page)
                popup_window.destroy()
            
            def close_popup():
                self.exit_button.config(state='disabled')
                self.print_button.config(state='disabled')
                popup_window.destroy()



            #final pop-up message before returning back to welcome page
            label = ttk.Label(popup_window, text=" "*18+"Make sure you have logged down your Username and Student ID"+"\n"+\
                              " "*6+"Your password for your college email is the same as your College password"+\
                              "\n"*2+" "*38+"Are you sure you want to finish and close?",font=("bold",12))
            label.pack(padx=125, pady=40)

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:quit())
            Okay.place(x=320,y=126)
            
            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.place(x=420,y=126)

        self.exit_pic = tk.PhotoImage(file='Icons/Buttons/exit.png')
        self.exit_button = tk.Button(self,image=self.exit_pic, command=lambda:prompt_signout())
        self.exit_button.place(x=1222, y=283)
        


app = ECR()
app.mainloop()
        
