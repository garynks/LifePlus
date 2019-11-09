from tkinter import *

def change_frame(arg = None):

    a = e.get()
    print(a)  # change this code to pass this value to next frame

name = ""

screen = Tk()
screen.geometry("550x300")
screen.title("title_page")
Label(text=" ").pack()
Label(text="What is your name?", font=("Calibri", 30)).pack()
Label(text=" ").pack()

e = Entry(screen, width = 15, font = ("Calibri", 20))
e.pack()
e.focus()

Label(text=" ").pack()

screen.bind('<Return>', change_frame)

screen.mainloop()
