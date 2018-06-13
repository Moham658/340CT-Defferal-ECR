import tkinter as tk
from tkinter import *


class ECR(tk.Tk):
    """Class that inherits other classes (pages) and stores each class as frames to allow program
        to switch between frames or pages.i.e. login page to main menu page within the same window"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) #initialising tkinter 

        window = tk.Frame(self)
        window.pack(side="top", expand = False)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        self.frames = {} # container that holds all of the frames/pages that we create


        frame1 = registrationPage(window, self) #each page is a frame
        frame2 = main_page(window, self)
        frame3 = Main_menu(window, self)
        
        self.frames[registrationPage] = frame1
        self.frames[main_page] = frame2
        self.frames[Main_menu] = frame3

        frame1.grid(row=0, column=0, sticky="nsew")
        frame2.grid(row=0, column=0, sticky="nsew")
        frame3.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(main_page)


        
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

app = ECR()
app.mainloop()
        
