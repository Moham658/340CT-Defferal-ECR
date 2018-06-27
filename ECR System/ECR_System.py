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


#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMssssdMMMMMMdssssMMMMMMMMMMMMMMMMMy/+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMmssssNMMMMMMysssyMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm    .NMMMMN.    NMMMMMMMMMMMMMMMM-``+MMMMMMMMMMMMMMMMMMMMMMMMMMMMs    /MMMMMd    .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh  .  oMMMM+ ``  dMMMMNmmmmmNMMMMMmhhNMMMNNNMNmmmNMMMMMMMMMMMMMMMM+  .  hMMMM- .  `MMMMMMNmmmmNMMMMMNNNMNmmmNMMMMMNNNNMMMMNNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs  +. `mMMd  o.  yMMM+-..```-sNMMM-``+MMd..-s-```./mMMMMMMMMMMMMMM:  s  -MMMo  y   NMMMm+-`.``-oNMMd..-s-```./dMMM+``-MMMM-``+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+  ss  /MM- .N-  sMMMhydmdh`  +MMM`  /MMd   .shy.  .MMMMMMMMMMMMMM.  d/  sMm` :N   dMMh` .ymdo  -NMm   `shy.  .NMM/  `MMMM.  /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:  yN.  dy  yM:  +MMMNho/:-`  .MMM`  /MMd   sMMMs   mMMMMMMMMMMMMM`  Nm` .N+ `mM`  hMM.  :oooo`  hMm   sMMMy   dMM/  `MMMM.  /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.  hMh  /- :MM/  /MMy. `/sh/  .MMM`  /MMd   yMMMy   dMMMMMMMMMMMMm   MM+  o` oMM.  sMM`  .:::::::hMm   yMMMh   dMM/  `MMMM.  /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   mMM:   `mMMo  -MM.  :MMN:  .MMM`  /MMd   yMMMy   dMMMMMMMMMMMMh  `MMN`   -NMM-  +MM/  -dMMMMNMMMm   yMMMh   dMMo   hMNh   /MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm   NMMd   oMMMs  `MMs`  -:..  `MMM`  /MMd   yMMMy   dMMMMMMMMMMMMs  -MMMs   dMMM:  /MMNo` `.---.sMMm   yMMMh   dMMN-  `...-  :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNsssMMMMdhhMMMMmsssMMMmyoosdmsssMMMysshMMNsssmMMMmsssNMMMMMMMMMMMMdsshMMMMhhdMMMMhsshMMMMNhsooosymMMNsssmMMMmsssNMMMNhsooymmsshMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM



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


#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMms+/::/+dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo```MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh+//////osdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm:-/mMMo```MMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMN/  `-::-`dMMMdo/:MMMMMMMMMMMMMMMMMMMMMMMMMMMo   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMdo/:MMMMMMMMMMo   :/:-`  .oNMMMMMMMMMMMMMMMMMs+:yMMMMMMMMMMMMMMMMMd.`.dMM+   MMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMo   mMMMMNMMNd/   ddmMMmddNMMMMdddNMMMMNmhhdNo   MMMMMNmhhhmNMMMMmmmNNmhhdmMMMNd+   ddmMMMMMMMo   MMMMNy`  -NMMMMNmhhhmNMMMmd   +ddNMMNmdhhhmNMMMMNdhdNMM+   MMMMNmhhhdNMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMy`  /ymNMMMMd``   ``.MM`  +MMMd   yMMNs-  ``..   MMMNo.`..` .sMMM/  /-``  `/NMd``   ``.MMMMMMMo   MMMMMMh   oMMNo-`..` .oNM/`   ```yMN.....  .sMMMh   hMM+   MMMs. `..`oMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMh:`  `-+hMMNm+   mmmMM`  +MMMd   yMM+  `smmy.   MMN:  sNNm:  oMM/   oddy   +MMm+   mmmMMMMMMMo   MMMMMMM   :MN:  omNm/  +Mmm   +mmNMMdmNmds   hMMh   hMM+   MMd   yNNmNMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMmho-   /NMMo   MMMMM`  +MMMd   yMN   +MMMM+   MMy   ////-  .MM/  `MMMM-  :MMMo   MMMMMMMMMMo   MMMMMMm   +My   ////-  `MMM   oMMMMNh+:-.-   oMMh   hMM+   MMN:` `:+hNMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMs   hMMo   MMMMM`  /MMMd   yMN   oMMMM+   MMs   +++++++oMM/  `MMMM-  :MMMo   MMMMMMMMMMo   MMMMMN/  `dMy   +++++++oMMM   oMMMN:  :ydm`  oMMh   hMM+   MMMMds/.  -NMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMdshdmdh:  `mMMs   ymmMM-  `hmd/   yMM/  `ymmh.   MMN.  +dNNNmmMMM/  `MMMM-  :MMMs   ymmMMMMMMMo   mmmhs-  .hMMN.  +dNNNmmMMMM`  :mmNd   sMNh   oMMh   hMM+   MMMdmNNh   hMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMM+  ```  .+mMMMN:   `/MMd-   ``:.  yMMNo`  ``.+   NMMm+. `...`.NMM/  `MMMM-  :MMMN:   `:MMMMMMMo   ``` `.:sNMMMMm+. `...``NMMMs`  ``dM+` `..-.  +MMh   hMM+   MMy``..` .oMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMNmdhyyhmNMMMMMMNmhyhdMMMNdhyhmMmddNMMMMNdyydNMdddMMMMMNmhyyhdmMMMmdddMMMMmddmMMMMNmhyhdMMMMMMMNdhhhhhdmNMMMMMMMMMNmhyyhdmMMMMMNdyyhNMMmhyhdNmddmMMNdddNMMmdddMMNmhyyhmNMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM


#-------------###### Student Address ######----------------#
    
class studentDetails(tk.Frame):
    """This class creates the student details entry page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/studentDetails.png')
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

        self.message = '' #pre prepared message for invalid inputs will be stored here and displayed insie the invalid pop up window below

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

            ok = ttk.Button(popup_window, text="OK", width = 23, command = lambda:canc_close_popup())#remains in to Main_menu frame
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

            ok = ttk.Button(popup_window, text="OK", width = 23, command = lambda:canc_close_popup())#remains in to Main_menu frame
            ok.place(x=330,y=185)

            popup_window.mainloop()





        def valid_pop():
            
            """This function produces an valid message on a pop when all inputs are invalid"""

            getdata = (select_title.get(), DoB.get(), fName.get(), sName.get(), \
                       address1.get(), address2.get(), county.get(), postcode.get(), phoneNum.get(),email.get())

            if studentProcess.checkExists(getdata) == True:
                #if student is already registered gets details for message
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
                
            next_to_course.config(state='disabled')
            quit_r.config(state='disabled')
            popup_window= tk.Toplevel()
            popup_window.attributes('-alpha', 0.86)
            popup_window.wm_title("invalid details")
            imageLabel = tk.Label(popup_window, text="Congratulations all fields are correct your ready "+"\n"+"to progress to the next stage to select your "+"\n" + "course")
            imageLabel.pack(padx=185, pady=45)



            
            def proc_close_popup():
                
                """This function closes valid pop-up message and stores student
                    details in temporary table and moves to course selection stage"""
                
                next_to_course.config(state='active')
                quit_r.config(state='active')
                studentProcess.TempStudDet(getdata)
                controller.show_frame(coursePage)
                popup_window.destroy()
                


            def canc_close_popup():
                
                """This function closes pop-up and remains in student details page"""
                
                next_to_course.config(state='active')
                quit_r.config(state='active')
                popup_window.destroy()

            ok = ttk.Button(popup_window, text="OK", width = 13, command = lambda:proc_close_popup())#remains in to Main_menu frame
            ok.place(x=230,y=107)

            cancel = ttk.Button(popup_window, text="Cancel", width = 13, command = lambda:canc_close_popup())#remains in to Main_menu frame
            cancel.place(x=320,y=107)
            
            popup_window.mainloop()


        def check_empty():
            """ This Function checks to see if any mandetory fields are empty, if so creates an error message for pop else it moves on to the
                next error check"""
            if fName.get() == '' or sName.get() == '' or address1.get() == ''or address2.get() == ''\
               or postcode.get() == ''or phoneNum.get() == ''or email.get() == ''or DoB.get() =='':
                
                self.message="Please Enusre all mandetory fields are filled in" #all check functions contain a message update for invalid pop up
                invalid_pop() #all check finctions run the pop up with the matching invalid message 
            
            else:
                check_DoB()#all check functions if succesful runs the next check function

        def check_DoB():
            """This function uses regular expression patterns to validate the date of birth inputed by the student"""
            
            re_pattern = "^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$" #regular expression for UK first line address
    
            if re.match(re_pattern,DoB.get()):
                check_fName()

            else:
               self.message = "You have inputted an incorrect date of birth. "+"\n"+"Please input correct date of birth"
               invalid_pop()

                
        def check_fName():
            """This function checks to see if the first name is a valid name"""
            
            for i in fName.get():
                # checks to see if phone number letters or other 
                if i not in ('abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXYZ-'):
                     self.message = "First Name can only contain letters within "+"\n"+"the alphabet and should not contain spaces"
                     invalid_pop()
                    
            else:
                confirm_sName()

            
        def confirm_sName():
            """This function checks to see if the surname name is a valid name/s"""
            for i in sName.get():
                # checks to see if numbers or non-alphabetical characters are in the first name entry 
                if i not in 'abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ-':
                     self.message = "Surname can only contain letters within the alphabet"
                     invalid_pop()
                    
            else:
                check_address1()

        def check_address1():
            """This function uses regular expression patterns to validate the Address line 1 inputed by the student"""
            
            re_pattern = "(\d+).*?\s+(.+)" #regular expression for UK first line address
    
            if re.match(re_pattern,address1.get()):
                check_address2()

            else:
               self.message = "Address line 1 is incorrect, please check and re-enter"
               invalid_pop()

        def check_address2():
            """This function checks if address line 2 is Valid i.e. town,city"""
            
            count = 0
            
            if len(address2.get().split())>2 or len(address2.get().split())<2:
                self.message = "Address line 2 is incorrect, please check and re-enter"
                invalid_pop()
                

            else:
               check_postcode()
        

        def check_postcode():
            """This function uses regular expression patterns to validate the postcode inputed by the student"""
            
            re_pattern = "^([A-Z]{1,2}\d{1,2}|d[A-Z]{1,2}\d[A-Z])\d[A-Z]{2}$" #regular expression for UK postcodes
    
            if re.match(re_pattern,postcode.get()):
                check_phoneNum()

            else:
               self.message = "postcode is incorrect, please check and re-enter"
               invalid_pop()
            

            
        def check_phoneNum():
            """This function uses regular expression patterns to validate the mobile number inputed by the student"""
            
            re_pattern = "^(07\d{8,12}|447\d{7,11})$" # regular expression for UK mobile numbers
            re_pattern2 = "^(01\d{8,12}|447\d{7,11})$" # regular expression for UK landlines
            
            if re.match(re_pattern,phoneNum.get()) or re.match(re_pattern2,phoneNum.get()): 
                check_email()

            else:
               self.message = "PhoneNumber is incorrect, please check and re-enter"
               invalid_pop()

            

        def check_email():
            """This function uses regular expression patterns to validate the email address inputed by the student"""
            re_pattern = "[^@]+@[^@]+\.[^@]+"  # regular expression for emails
            
            if re.match(re_pattern,email.get()):
                valid_pop()

            else:
               self.message = "email is not valid please enter valid email address"
               invalid_pop()
               
            
        #creates next to course page
        self.next = tk.PhotoImage(file='Icons/Buttons/next.png')
        next_to_course = tk.Button(self,image=self.next,command=lambda:check_empty())
        next_to_course.place(x=950, y=220)
        


#------------------------------------------------------------------------------------------------------------------#   

        #quit button to back to Main Page
        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#including quit
        quit_r.place(x=1295, y=415)

                
            
        def prompt_signout():
            """Function incharge of quitting (back to Main page)"""
            quit_r.config(state='disabled')
            next_to_course.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
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


            

#-------------###### course Page ######----------------#


#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMNds+/::/+hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo+/////+sdMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMNo.  `-::-.hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM`  .//-`  :mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMm.  .yNMMMMMMMMMMNdhhhdNMMMMMmddmMMMMdddNMMNddmMmhhMMMNdhhhmNMMMMNmdhhdNMMMMMMMMMM`  +MMMm.  :MMNmmhhhdmNMMMMMMNmhhdNNmmmMMMMMNdhhdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMM-  `mMMMMMMMMMMd/. `.` .+mMMM.  /MMMm   sMMs  :/` `MN+. ...`hMMMy-``.. ./NMMMMMMMM`  +MMMN.  :MMy..... `:dMMMNo.  ``.:  :MMMd/.`..``:hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMN   /MMMMMMMMMMd`  +mNd:  .mMM.  /MMMm   sMMy   `oyhMo  `dNNdMMMo  /mNNo  -MMMMMMMM`  :yso-  -dMMNdmNmd/  `NMM:  .ymms   /MMd` .hNNd` `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMN   :MMMMMMMMMM:  .MMMMN   oMM.  /MMMm   sMMy   yMMMMd-  .:odMMN   :////   mMMMMMMM`  `..--/yNMMMms/---.   mMd   yMMMM.  /MM:  .////`  oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMM/   yMMMMMMMMM:  .MMMMN   oMM.  :MMMm   sMMy   mMMMMMNho:` `/Mm   /+++++++NMMMMMMM`  +NNNMMMMMMd.  +hdy   dMd   yMMMM.  /MM-  .+++++++hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMN:   :yddddhNMh`  omNm/  .mMM:  `hmd+   sMMy   mMMMMmdNNNo  `NM/  -hmNNmdMMMMMMMMM`  +MMMMMMMMM+  `mMN+   dMM:  .yddo   /MMy  `smNNNmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMNh/.  ```` hMMd:` `.` ./mMMMm-   ``:-  oMMy   mMMMM+`...` -yMMNs-  `..``hMMMMMMMM`  +MMMMMMMMMm:  `..:`  dMMNo-  `./.  /MMMh:` `...`/MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhhyhhmNMMMMNdyyhdNMMMMMMNmhyhmMmddmMMNdddNMMMMNdhyyhmNMMMMMNmhhyhdmNMMMMMMMMdddmMMMMMMMMMMNmhyhmMdddNMMMMNmmmNm`  oMMMMMNdhyyhdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM++sss+.  :NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/-....-+hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

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
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
            popup_window.wm_title("Course Full")
            #message with course name and course type
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
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
            popup_window.wm_title("Are you sure?")
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
                studentProcess.TempStudCourse(getselected(self.treeviewCourses)[1])
                popup_window.destroy()
                controller.show_frame(studentUnique)
                

            Okay = ttk.Button(popup_window, text="Okay", command = lambda:choose())
            Okay.place(x=270,y=245)

            cancel = ttk.Button(popup_window, text="Cancel", command = lambda:close_popup())
            cancel.place(x=350,y=245)

            
            

        
        def check_course_free():
                
            if getselected(self.treeviewCourses)[6] == 0:
                prompt_full()

            else:
                prompt_choose()
                
        

#------------------------------------------------------------------------------------------------------------------#   
        
        #creates next to student id/password and previous buttons for student address detail page
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




#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMNNNNMMMMMNNNNMMMMMMMMMMMMMMMMMdhmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmdmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMhssyMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMNNNmmmNNNMMMMMMMMMMMM
#MMMMMMM`  sMMMMM-  +MMMMMMMMMMMMMMMMy  `MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+-` `` .mMMMNmdmMMMMMMMMMMMMMMMMMMMMMMMMM+  -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhMMMMM   yMMm`  `````-/hNMMMMMMMMM
#MMMMMMM`  sMMMMM-  +MMMMMMMMNNNMMMMMNyshMMMMMMNNNMMMMMMMMMMMMMMMMMMMMMMMMMNNNMMMMMMMMMMm`  +hddhyMMMM.` yMMMMMMMMMMMMMMMMMMMMMNNNM+  -MMMMMMNNNMMMMMMMMMMMMNNMMMMMMh`  MMMMM   yMMd   yddho.  -dMMMMMMMM
#MMMMMMM`  sMMMMM-  +MMm::oh/---/dMMMh:::MMMNy/---+y::/MMm:::mMMM+::sMMMNs/---:omMMMMMMMh   yNMMMMMMs:   .::NM/::yMMMy::/MMMNy/---+/  -MMMNy/---:+dMMM+::ho:--:sNMM:-   ::+MM   yMMd   mMMMMN:  .MMMMMMMM
#MMMMMMM`  sMMMMM-  +MMd   .+s/  `hMMy   MMN:  -os/`  .MMm   mMMM-  +MMd. .yhy. .dMMMMMMMo.  .:sdNMMhs   /ssNM.  oMMMo  .MMm-  -os/   -MMm: `shy- `yMM:  `:oo.  :MMs/   sshMM   yMMd   mMMMMMh   dMMMMMMM
#MMMMMMM`  sMMMMM-  +MMd   hMMM-  +MMy   MMo  .NMMM/  .MMm   mMMM-  +MM.  oyyy/  /MMMMMMMMmy+-`  -hMMM`  yMMMM.  oMMMo  .MM+  -NMMM/  -MM/  /yyyo  .MM:  :MMMy   NMMy   MMMMM   yMMd   mMMMMMh   dMMMMMMM
#MMMMMMM.  oMMMMM.  oMMd   mMMM:  +MMy   MM/  :MMMMo  .MMm   dMMM-  +MN   -::::::+MMMMMMMMMMMMm/  `MMM`  yMMMM.  oMMMo  .MM:  /MMMM+  -MM-  .:::::::MM:  /MMMd   NMMy   MMMMM   yMMd   mMMMMN:  .MMMMMMMM
#MMMMMMMs  `hNNmo  `mMMd   mMMM:  +MMy   MMy  `yNMm-  .MMN   oNNh`  +MM:  +mNMMNNMMMMMMMMhmNNNm/  .MMM`  oNNMM:  -mNm-  .MMs  `hNMd.  -MMo  :dNMMNNMMM:  /MMMd   NMMh   dNMMM   yMMd   mMNmy:  .dMMMMMMMM
#MMMMMMMMs.  ..` `:dMMMd   mMMM:  +MMy   MMMs.  ....  .MMMs`  ...-  +MMN+. `.--.-MMMMMMMy `...` `/mMMMo   .-MMd.  `..:  `MMMo`  ...:  -MMMs. `.--..mMM:  /MMMd   NMMN-  `.oMM   yMMd   ...` `:sNMMMMMMMMM
#MMMMMMMMMNdyssyhmMMMMMNhhhNMMMdhhdMMmhhhMMMMNhsshmo  .MMMMmysshNmhhdMMMMNdyssyhdMMMMMMMNdhyssydNMMMMMMmyssyMMMNhssymMhhhMMMMNhssymNhhhMMMMNdyssyydMMMdhhdMMMNhhhMMMMNdysydMMhhhmMMNhyyyyyhmNMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo  .MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy::/MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    
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

                    
        pWord_ = tk.StringVar() #first name variable
        pWord = tk.Entry(self, width=24,font=("Helvetica", 12, "bold"),textvariable= pWord_, show='*')
        pWord.place(x=550, y=150)
                    
        pWord2_ = tk.StringVar() #first name variable
        pWord2 = tk.Entry(self, width=24,font=("Helvetica", 12, "bold"),textvariable= pWord2_, show='*' )
        pWord2.place(x=550, y=200)
        
#-----------------------------------------------------------------------------------------------------------

#creates next to confirmation Notification and previous buttons for course selection page
        self.finish = tk.PhotoImage(file='Icons/Buttons/complete.png')
        self.complete = tk.Button(self,image=self.finish,command=lambda: complete_details()) 
        self.complete.place(x=1050, y=220)

        self.prev = tk.PhotoImage(file='Icons/Buttons/previous.png')
        prev_to_id = tk.Button(self,image=self.prev,command=lambda:controller.show_frame(coursePage))
        prev_to_id.place(x=90, y=220)

        
        
        def prompt_incomplete():
            """Function that prompts a display message for registration completion (notification page)"""
            quit_r.config(state='disabled')
            self.complete.config(state='disabled')
            prev_to_id.config(state='disabled')
            uName.config(state='disabled')
            pWord.config(state='disabled')
            pWord2.config(state='disabled')
            
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
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
            """Function that prompts a display message for registration completion (notification page)"""
            quit_r.config(state='disabled')
            self.complete.config(state='disabled')
            prev_to_id.config(state='disabled')
            uName.config(state='disabled')
            pWord.config(state='disabled')
            pWord2.config(state='disabled')
            
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
            popup_window.wm_title("Are you sure?")
            imageLabel = tk.Label(popup_window, text="You have chosen to the username"+ "\n"*2 +\
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
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
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



#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MM+//+mMMMMMs//hMMMMMMMMMMMMMMMMMMMMMMMMMMs--oMMMMh:`   yh:-+MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/-:mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm+//////oymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MM`   `dMMMM:  oMMMMMMMMMMMMMMMMMmo+:mMMMMo../MMMd   +hhNy.`-NMMMMMMMMMMMMMMMMMMMMMMMMMMMho/+MMMMm-`.dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh   ://-  `oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#MM`  . `hMMM:  oMMMMMNdhhhmNMMMMds   yddMMmddmMNd+   ddmMNdddMMMMMMmdhhhdMMMNmdhhdmNMMMNd.  -ddmMMdhdNMMMMNmdhhdmNMMMMNmmmMmdhhmNMMMMMMMMMh   dMMMy   yMMNmdhhhdNMMMMMMMmdhhmNmmmNMMMMNmdhhdNMMMMMMMMMMM
#MM`  y. `yMM:  oMMMd/. `.` .+mMN``   ```NM:  -Mh``   ``+Mo   NMMNy:` ````NMm.....  -yMMs`    ``+Md   yMMMy-` .. `-sMMMh  ./.`   -dMMMMMMMMh   dMMMh   yMM/....` .+NMMMm/` ```:.  yMMMy-``.. ./NMMMMMMMMM
#MM`  dd` `yM/  oMMh`  omNd:  .NMms   hmmMM:  -MNm+   mmNMo   NMN:  .sdmmmMMMhmNmdo   dMNm-  -mmNMd   yMM+  `hNNy`  +MMh   -hmh-  .MMMMMMMMh   oys/`  /NMMmdmmmh`  /MMm`  /dmd/   hMMo  /mNNo  -MMMMMMMMM
#MM`  hMd. `y+  oMM:  .MMMMm   sMMy   dMMMM:  -MMMo   MMMMo   NMy   hMMMMMMMNy+:---   sMMM-  :MMMMd   yMm   oMMMMo   NMh   hMMMs   NMMMMMMMh   ...-:odMMMMdo:-.-`  -MM+  `NMMMd   hMN   :////   mMMMMMMMM
#MM`  hMMm. `:  oMM-  .MMMMm   sMMy   dMMMM:  -MMMo   MMMMo   NMs   hMMMMMMN-  :hdd   sMMM-  :MMMMd   yMm   oMMMMo   NMh   hMMMs   NMMMMMMMh   hNNNMMMMMMo` .sdd/  .MM+  `NMMMd   hMm   /+++++++NMMMMMMMM
#MM`  hMMMm-    oMMy   omNm:  .NMMd   ommMM:  -MMMo   MMMMo   NMN.  .ymmmmMh   yMNy   sMMM:  .dmNMd   yMM/  .hNNh`  +MMh   hMMMs   NMMMMMMMh   dMMMMMMMMM`  /NMm-  .MMd`  :hdh:   hMM/  -hmNNmdMMMMMMMMMM
#MM`  hMMMMN-   oMMMh:` `.` .+mMMMM/   `.MM:  -MMMo   MMMMo   NMMm+.  ````NN/` `..-.  oMMMd.  ``sMd   yMMNs- `..  -sMMMh   hMMMs   NMMMMMMMh   dMMMMMMMMMy.  ...-  .MMMd/.  `-/   hMMNs-  `..``hMMMMMMMMM
#MMdddNMMMMMNdddNMMMMMmdyyhmNMMMMMMMmhyydMMmdddMMMmdddMMMMmdddMMMMMNmhyyhdMMMmhyhmNmddmMMMMNdhyhNMNdddNMMMMNmhyyhmNMMMMNdddNMMMNdddMMMMMMMMNdddNMMMMMMMMMMNdyydNNdddMMMMMNmmmNs   mMMMMNmhhyhdmNMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm:+sss/`  oMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh:-....:omMMMMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM            
    
class NotificationPage(tk.Frame):
    """This class creates the student unique username/password entry page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/notification.png')
        main_window = tk.Label(self,image=self.bg)
        main_window.grid(pady=0,padx=0)


        def Notification_message():
            
            Message1 = Text(self, width=54, height= 22,font=("Helvetica", 9, "bold"))
            Message1.place(x=240,y=108)
            with open("notification_message.txt", 'r') as f:
                Message1.insert(INSERT, f.read())
                Message1.config(state="disabled")


            Message2 = Text(self, wrap=WORD, width=65, height= 22,font=("Helvetica", 9, "bold"))
            Message2.place(x=680,y=108)
            with open("notification_message2.txt", 'r') as f:
                Message2.insert(INSERT, f.read())
            self.after(1000, Notification_message)
        Notification_message()

        self.print_pic = tk.PhotoImage(file='Icons/Buttons/print.png')
        self.print_button = tk.Button(self,image=self.print_pic)
        self.print_button.place(x=1222, y=123)

        def prompt_signout():
            """Function incharge of completing registration and temporary table and goes back to startup page"""
            self.exit_button.config(state='disabled')
            self.print_button.config(state='disabled')
            popup_window= tk.Tk()
            popup_window.attributes('-alpha', 0.96)#opacity to all pop-ups for professional look
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
        
