import tkinter as tk
from tkinter import *
from tkinter import Menu, ttk

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


        frame1 = registrationPage(window, self) #each page is a frame
        frame2 = welcome_page(window, self)
        frame3 = Main_menu(window, self)
        
        self.frames[registrationPage] = frame1
        self.frames[welcome_page] = frame2
        self.frames[Main_menu] = frame3

        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=0, sticky="nsew")
        frame3.grid(row=0, column=0, sticky="nsew")
        
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
            """This function produces a welcome back pop when the user details are correct
                & displays the user image for that specific user"""

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
                controller.show_frame(registrationPage)

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

    
class registrationPage(tk.Frame):
    """This class creates the Booking page"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.bg = tk.PhotoImage(file='Icons/Backgrounds/RegistrationPage.png')
        main_window = tk.Label(self,image=self.bg)
        main_window.grid(pady=0,padx=0)



        self.quit_img = tk.PhotoImage(file='Icons/Buttons/quit.png')
        quit_r = tk.Button(self,image=self.quit_img, command=lambda:prompt_signout())#including quit
        quit_r.place(x=1295, y=415)


        #creates the treeview table which contains the course columns

        
        self.treeviewCourses = ttk.Treeview(main_window)
        self.treeviewCourses.place(x=95, y=215)
        self.dataColumns = ('country', 'capital', 'currency')
        self.treeviewCourses.config(columns = ('type'))
        self.treeviewCourses.column('#0',width = 200, anchor = 'n')#department column
        self.treeviewCourses.column('type',width = 150, anchor = 'n')#course type column
        #self.treeviewCourses.column('code',width = 150, anchor = 'n')#course code column
        #self.treeviewCourses.column('start',width = 150, anchor = 'n')#start date column
        #self.treeviewCourses.column('end',width = 150, anchor = 'n')#end date column
        #self.treeviewCourses.column('hours',width = 150, anchor = 'n')#hours perweek column
        #self.treeviewCourses.column('AvSpace',width = 150, anchor = 'n')#Available spaces column


        
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
        
