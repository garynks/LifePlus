from tkinter import *

def  main():
    root = Tk()

    # size of the window
    root.geometry("750x500")

    app = Window(root)
    root.mainloop()


class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget
        self.master.title("LifePlus")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        

main()
