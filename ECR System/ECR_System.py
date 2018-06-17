import tkinter as tk
from tkinter import *
from tkinter import Menu, ttk
import studentProcess

class ECR(tk.Tk):
    """Class that inherits other classes (pages) and stores each class as frames to allow program
        to switch between frames or pages.i.e. welocome page to main menu page within the same window"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #initialising tkinter 

        window = tk.Frame(self)
        window.pack(side="top", expand = False)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {} # container that holds all of the frames/pages that we create


        frame1 = studentDetails(window, self) #each page is a frame
        frame2 = welcome_page(window, self)
        frame3 = Main_menu(window, self)
        frame4 = coursePage(window, self)
        frame5 = studentUnique(window, self) #each page is a frame
        
        self.frames[studentDetails] = frame1
        self.frames[welcome_page] = frame2
        self.frames[Main_menu] = frame3
        self.frames[coursePage] = frame4
        self.frames[studentUnique] = frame5

        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=0, sticky="nsew")
        frame3.grid(row=0, column=0, sticky="nsew")
        frame4.grid(row=0, column=0, sticky="nsew")
        frame5.grid(row=0, column=0, sticky="nsew")
        
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

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMNhhhMMMMhhhNMMMdhhNMMMMMMMMMMMM//+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdhyyyydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMN`  NMMm   sMMM` `NMMMMMMMMMMMN  `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`  -:.  :mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMM+  sMM+ ` .MMh  oMMMMdyyymMMMN  `MMMMMdyyyhMMMMdyyydMMMMNhhNmhyhNMNhyymMMMMMNhyyhNMMMMMMMM`  MMMh  -MMNdyyyhNMMMMMNhyymNhhNMMMMdyyhmMMMMM
#MMMm  -MN` s  hM: `NMMy. :/. -mMN  `MMN+` `--:MMo` ./. `sMMh  -`-` `/`-`  oMMN+ `//` +MMMMMMM`  MMMy  :MM:-//-  oMMM+  .-`.  hMMs` :/. :NMMM
#MMMM/  ms -M. /N  oMMh  +mmd` -MN  `MM:  sMMMMMs  +MMM:  yMh  -MMd  `NMN`  MM/  hmmy  sMMMMMM`  --` `/NMMMNhys`  mMo  +MMM.  dMs  smmd  /MMM
#MMMMd  o. yMs `s `NMMo  ......-MN  `MM   MMMMMM:  hMMMs  +Mh  +MMN  .MMM-  NM`  ......oMMMMMM`  yyhmMMMMd- .+o.  mM:  dMMM:  dM:  ....../MMM
#MMMMM: ` .MMN` ` oMMMd  /mMMMNMMN  `MM/  /mMMNMy  :NMN-  dMh  +MMN  .MMM-  NM+  yNMMMNMMMMMMM`  MMMMMMMM-  dMN-  mMy  :mNd`  dMy  +NMMMNMMMM
#MMMMMh   yMMM/  `NMMMMd:` ``` dMN  `MMMs.    .MMh-  . `:dMMh  +MMN  .MMM-  NMMs.  `` -MMMMMMM`  MMMMMMMMh.  ..-  dMMy-  `:-  dMMh-  ````NMMM
#MMMMMMNNNMMMMMNNNMMMMMMMMmmmNMMMMNNNMMMMMNmmmMMMMMMmmmMMMMMMNNNMMMNNNMMMNNNMMMMMNmmmNMMMMMMMMNNNMMMMMMMMMMNmmMMNNMMMMMMMMm` `NMMMMMmmmNMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/`.-.  -dMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhyhdNMMMMMMMMMMMMMMMMM



class welcome_page(tk.Frame):
    """This class creates the welcome page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/bg.png')
        label = tk.Label(self,image=self.bg)
        label.grid(pady=0,padx=0)

        self.login_button_img = tk.PhotoImage(file='Icons/Buttons/letsBegin.png')#All folders for images in software must be in the root folder
        letsBegin = tk.Button(self,image=self.login_button_img, width=100,height=38,command=lambda:controller.show_frame(Main_menu))
        letsBegin.place(x=635, y=405)

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMyyyydMMMMMMNyyyymMMMMMMMMMMMMMMMMMhoodMMMMMMMMMMMMMMMMMMMMMMMNhyyssyyhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMm    `NMMMMM+    +MMMMMMMMMMMMMMMMM.  :MMMMMMMMMMMMMMMMMMMMMMMy   ````  .sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMh  `  /MMMMd  `  :MMMMMNNNNNNMMMMMMmyymMMMNNNMMNNNNMMMMMMMMMMMy   hMMms   oMMMMNNNNNNMMMMMMMMMNNNNMMNNNMMMMMMNNNNNMMMMMMMMMMMMMMMMMMM
#MMMMMMMs  /-  hMMM- `o  .MMMN/-....-/hMMMM:../MMM---y+-.`.:yMMMMMMMMMy   hMMMM`  :MMh:-....-+dMMMMNs:.`.-o+--sMMMNy:....-+mMMMMMMMMMMMMMMMMM
#MMMMMMM+  +y  -MMs  sy  `MMMMoyhdhs   sMMM.  -MMM`   :ss:   sMMMMMMMMy   ymmh/  `yMMmoyhdh/  `dMMm.  .sys.   oMMm- `odds` `dMMMMMMMMMMMMMMMM
#MMMMMMM:  sM-  yN` -Mh   NMMMmhs+//`  -MMM.  -MMM`  -MMMM.  -MMMMMMMMy   `````-+dMMMMmyo+/:   oMM:  `mMMMd   oMM:  -yyyy-  :MMMMMMMMMMMMMMMM
#MMMMMMM.  yMd  .o `dMd   dMMo. `/os-  .MMM.  -MMM`  :MMMM.  -MMMMMMMMy   shddmNMMMMN/` .+ss   +MM.  .MMMMm   oMM`  `-------/MMMMMMMMMMMMMMMM
#MMMMMMM   dMM/  ` oMMN   yMd   sMMN-  .MMM.  -MMM`  :MMMM.  -MMMMMMMMy   hMMMMMMMMMo   mMMm   +MMo   sNMNo   oMM/  .dNNNNNNNMMMMMMMMMMMMMMMM
#MMMMMMm   mMMN`  .NMMM   sMN-  .++-`  .MMM.  -MMM`  :MMMM.  -MMMMMMMMy   hMMMMMMMMMh`  -+/.`  +MMNo`  .-.-   oMMN+` `-///::MMMMMMMMMMMMMMMMM
#MMMMMMmoooMMMMhssdMMMMooohMMNy+//ohdoooMMMsoosMMMoooyMMMMsoosMMMMMMMMdooomMMMMMMMMMMms+//sdyooyMMMMNhsosdh   yMMMMmyo///+oyMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNydmmdy.  .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo  ```  .oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmdddmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM



class Main_menu(tk.Frame):
    
    """This class creates the Main_menu page"""
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/mainMenu.png') #all backgrounds located in root folder
        label = tk.Label(self,image=self.bg)
        label.grid(pady=0,padx=0)

        def welcome_student():
            """This function produces a reminder message on a pop to remind the student what details will be required"""

            begin_register.config(state='disabled')
            quit_r.config(state='disabled')
            popup_window= tk.Toplevel()
            popup_window.attributes('-alpha', 0.86)
            popup_window.wm_title("Welcome Student")
            photo = PhotoImage(file ='icons/info/Reminder_message.png') #loads message for reminding student what info they need
            photo = photo.subsample(2) #shinks message to the correct size
            imageLabel = tk.Label(popup_window, image=photo)
            imageLabel.pack(padx=15, pady=35)
           
            def proc_close_popup():
                begin_register.config(state='active')
                quit_r.config(state='active')
                popup_window.destroy()
                controller.show_frame(studentDetails)

            def canc_close_popup():
                begin_register.config(state='active')
                quit_r.config(state='active')
                popup_window.destroy()
            
            proceed = ttk.Button(popup_window, text="Proceed", width = 23, command = lambda:proc_close_popup())#moves to registeration frame
            proceed.place(x=160,y=355)
            cancel = ttk.Button(popup_window, text="Cancel", width = 23, command = lambda:canc_close_popup())#remains in to Main_menu frame
            cancel.place(x=330,y=355)

            popup_window.mainloop()

            
        #Creating Buttons for each functionilty in our software
        self.reminder = tk.PhotoImage(file='Icons/Buttons/Register.png')
        begin_register = tk.Button(self,image=self.reminder,command=lambda:welcome_student())
        begin_register.place(x=145, y=205)

        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#including quit
        quit_r.place(x=1295, y=415)

        
        def prompt_signout():
            """Function incharge of quitting (back to welcome page)"""
            quit_r.config(state='disabled')
            begin_register.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
            popup_window.wm_title("Are you sure?")

            def quit():
                quit_r.config(state='normal')
                begin_register.config(state='normal')
                controller.show_frame(welcome_page)
                popup_window.destroy()
            
            def close_popup():
                quit_r.config(state='normal')
                begin_register.config(state='normal')
                popup_window.destroy()

            
                
            label = ttk.Label(popup_window, text="Are you sure you want to quit",font=("bold",12))
            label.grid(row=0, column=0,padx=70,pady=13)

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:quit())
            Okay.grid(row=1, column=0,pady=0, padx=0,)
            
            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.grid(row=2, column=0,pady=0, padx=0,)

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMmmddddmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmddddmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMs        -sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs  `MMMMMMMMMMMMMMNdhMMMMMMMMMMMMMMMMMMMMMMMMMMMNdhMMMMh   mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs        -yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMs  `NMNy`  +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMhymMMMMMMMMMMMMMs  `MMMMMMMMMMMMMMMMMMMMMMMMMMy  `MMMMMhydMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs  `NNmy`  sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMs  `MMMM:  /MMMmo-.`.:sMMMMMs:.`.+y--oMMy--:MMMd+-``.:NN-.   --+Md--oh:`/Mm+:..`./yMMM-.   --+Md---NMMMd+-.`.:omMMMy--ss:.`.+mMMMMMMMMs  `MMMM/  :MMy/-.`.-+mMMMMNo-..-oo--hMMMmo-.`.:sMMMM
#MMMs  `hhy/  -mMMy  :yho  -NMm.  -ss:   +MMs  `MMh  .yhysMMs/  `sshMh  ` ./sMM+shhy-  /MMs/  `sshMd   mMM/  .syo   yMMy   .oo-  `mMMMMMMMs  `NNms`  yMMhoyhho  `mMMh`  /ss.   hMMy  :hho  -NMM
#MMMs   `    +MMMm   yyyy-  sM/  -MMMM.  +MMs  `MMh  `+yNMMMMs  `MMMMh   sMMMMMNhs+/-   MMMs  `MMMMd   mMy  `NMMMs  `NMy   NMMM`  sMMMMMMMs       `:hMMMMmyo+/`  oMM`  oMMMm   hMm  `yyyy-  yMM
#MMMs  `MMm-  :MMh   .......sM-  +MMMM-  +MMs  `MMMd+-   :mMMs  `MMMMh   NMMMMo` .+s+   MMMs  `MMMMd   mM+  .MMMMd   mMy   MMMM`  sMMMMMMMs  `hhdmMMMMMm-  :os.  oMN   hMMMN   hMy   .......sMM
#MMMs  `MMMm   hMN`  hMMMMMMMMo  `dMMd`  +MMs  `MMMMMMN/  :MMs  `NMMMh   NMMMd   mMMy   MMMy  `NMMMd   mMh   hMMM/  .MMy   MMMM`  sMMMMMMMs  `MMMMMMMMM:  /MMM-  oMM-  -NMMy   hMN`  hMMMMMMMMM
#MMMs  `MMMM:  -MMd-  .:::-+MMMo`  `.``  +MMs  `MMs.:/:` `hMMm`  `-sMh   NMMMN-  ./:`   NMMm`  `-sMd   mMMy.  -/.  :mMMy   MMMM`  sMMMMMMMs  `MMMMMMMMMy   :/.`  +MMN/   .`.   hMMd-  .:::-+MMM
#MMMdsssMMMMmsssNMMMdso++osdMMMMNhyyhN.  sMMdsssMMdso++ohNMMMMNyo+odMmsssNMMMMMho+oyNsssNMMMNyo+odMNsssNMMMMhs++oymMMMMmsssMMMMsssdMMMMMMMdsssMMMMMMMMMMms++sdmsshMMMMNhsydm   dMMMMdso++osdMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdshddy:  .NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMyshdds.  /MMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo`    `-oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:`    `:yMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMM


#-------------###### Student Address ######----------------#
    
class studentDetails(tk.Frame):
    """This class creates the student details entry page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/studentDetails.png')
        main_window = tk.Label(self,image=self.bg)
        main_window.grid(pady=0,padx=0)



        
        title = ['Mr', 'Mrs', 'Miss', 'Ms'] #list containing titles for drop down menu
        
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

        
        postode = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        postode.place(x=550, y=350)

        
        phoneNum = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        phoneNum.place(x=550, y=400)

        
        email = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        email.place(x=550, y=450)

        Message = ''

        def confirmNext():
            """This function checks all data entries for input errors, mistakes or
                #empty feilds"""
            
            for i in fName.get():
                # checks to see if numbers or non-alphabetical characters are in the first name entry 
                if i not in ('abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                     Message = "First Name can only contain letters within the alphabet and should not contain spaces"
                     break
                    

            for i in sName.get():
                # checks to see if numbers or non-alphabetical characters are in the surname name entry 
                if i not in ('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                     Message = "Surname can only contain letters within the alphabet"
                     break

            for i in phoneNum.get():
                # checks to see if phone number letters or other characters
                if i not in ('1234567890'):
                     Message = "Phone Number is incorrect"
                     break

            
            else:
                controller.show_frame(coursePage)
                   
                
        #creates next to course page
        self.next = tk.PhotoImage(file='Icons/Buttons/next.png')
        next_to_course = tk.Button(self,image=self.next,command=lambda:confirmNext())
        next_to_course.place(x=950, y=220)
        


#------------------------------------------------------------------------------------------------------------------#   

        #quit button to back to Main Page
        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#including quit
        quit_r.place(x=1295, y=415)

                
            
        def prompt_signout():
            """Function incharge of quitting (back to Main page)"""
            quit_r.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
            popup_window.wm_title("Are you sure?")

            def quit():
                quit_r.config(state='normal')
                controller.show_frame(Main_menu)
                popup_window.destroy()
            
            def close_popup():
                quit_r.config(state='normal')
                popup_window.destroy()

            
                
            label = ttk.Label(popup_window, text="Are you sure you want to quit",font=("bold",12))
            label.grid(row=0, column=0,padx=70,pady=13)

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:quit())
            Okay.grid(row=1, column=0,pady=0, padx=0,)
            
            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.grid(row=2, column=0,pady=0, padx=0,)


            

#-------------###### course Page ######----------------#

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
            dat = [(tree.set(children, column), children) for children in tree.get_children('')]
            # numeric data changed to a float for sorting
            # now we sort the data into order
            dat.sort(reverse=descend)
            for i, info in enumerate(dat):
                tree.move(info[1], '', i)
            # now sort the data in the opposite order
            tree.heading(column, command=lambda column=column: sort(tree, column, int(not descend)))
            
        def getselected(treeview):
            """Function that gets/returns the selected course from the course table"""
            print(self.treeviewCourses.selection())

        #only allows one course to be selected and returned
        self.treeviewCourses.config(selectmode='browse')
        self.treeviewCourses.bind('<<TreeviewSelect>>', getselected)
        

#------------------------------------------------------------------------------------------------------------------#   
        
        #creates next to student id/password and previous buttons for student address detail page
        self.next = tk.PhotoImage(file='Icons/Buttons/next.png')
        next_to_id = tk.Button(self,image=self.next,command=lambda:controller.show_frame(studentUnique))
        next_to_id.place(x=1050, y=220)

        self.prev = tk.PhotoImage(file='Icons/Buttons/previous.png')
        prev_to_id = tk.Button(self,image=self.prev,command=lambda:controller.show_frame(studentDetails))
        prev_to_id.place(x=90, y=220)



        #quit button to back to Main Page
        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#including quit
        quit_r.place(x=1295, y=415)

                
            
        def prompt_signout():
            """Function incharge of quitting (back to Main page)"""
            quit_r.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
            popup_window.wm_title("Are you sure?")

            def quit():
                quit_r.config(state='normal')
                controller.show_frame(Main_menu)
                popup_window.destroy()
            
            def close_popup():
                quit_r.config(state='normal')
                popup_window.destroy()

            
                
            label = ttk.Label(popup_window, text="Are you sure you want to quit",font=("bold",12))
            label.grid(row=0, column=0,padx=70,pady=13)

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:quit())
            Okay.grid(row=1, column=0,pady=0, padx=0,)
            
            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.grid(row=2, column=0,pady=0, padx=0,)





#-------------###### Student username/password ######----------------#
    
class studentUnique(tk.Frame):
    """This class creates the student unique username/password entry page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/userpass.png')
        main_window = tk.Label(self,image=self.bg)
        main_window.grid(pady=0,padx=0)

                    
        uName = tk.StringVar() #first name variable
        uName = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        uName.place(x=550, y=100)
                    
        pWord = tk.StringVar() #first name variable
        pWord = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        pWord.place(x=550, y=150)
                    
        pWord2 = tk.StringVar() #first name variable
        pWord2 = tk.Entry(self, width=24,font=("Helvetica", 12, "bold") )
        pWord2.place(x=550, y=200)
        
#-----------------------------------------------------------------------------------------------------------

#creates next to confirmation Notification and previous buttons for course selection page
        self.finish = tk.PhotoImage(file='Icons/Buttons/complete.png')
        complete = tk.Button(self,image=self.finish,command=lambda:controller.show_frame(studentUnique))
        complete.place(x=1050, y=220)

        self.prev = tk.PhotoImage(file='Icons/Buttons/previous.png')
        prev_to_id = tk.Button(self,image=self.prev,command=lambda:controller.show_frame(coursePage))
        prev_to_id.place(x=90, y=220)



        #quit button to back to Main Page
        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#including quit
        quit_r.place(x=1295, y=415)

                
            
        def prompt_signout():
            """Function incharge of quitting (back to Main page)"""
            quit_r.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
            popup_window.wm_title("Are you sure?")

            def quit():
                quit_r.config(state='normal')
                controller.show_frame(Main_menu)
                popup_window.destroy()
            
            def close_popup():
                quit_r.config(state='normal')
                popup_window.destroy()

            
                
            label = ttk.Label(popup_window, text="Are you sure you want to quit",font=("bold",12))
            label.grid(row=0, column=0,padx=70,pady=13)

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:quit())
            Okay.grid(row=1, column=0,pady=0, padx=0,)
            
            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.grid(row=2, column=0,pady=0, padx=0,)



        
app = ECR()
app.mainloop()
        
