from tkinter import *

class Window(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.goal_entry()
        
    # Creation of init window
    def init_window(self):
        
        # changing the title of our master widget 
        self.master.title("Lifeplus")
        
        # allowing the widget to take the full space of the root window 
        self.pack()
    
    def goal_entry(self):
        Label(text="What is your goal?", font=("Calibri", 24)).pack()
        Label(text=" ").pack()
        
        goal = Entry(self.master, width = 40, font=("Calibri", 20))
        goal.pack()
        
        Button(self.master, text="Ok", font=("Calibri", 15)).pack()
        
    def client_exit(self):
        exit()
        
root = Tk()

# size of window 
root.geometry("550x300")

app = Window(root)
root.mainloop()