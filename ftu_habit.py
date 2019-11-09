from tkinter import *
import os


def habit_entry():

    habit_screen = Tk()
    habit_screen.geometry("550x300")
    habit_screen.title("New Habit Entry")
    Label(text="How would you like to achieve it?", font=("Calibri", 30)).pack()
    Label(text=" ").pack()

    habit = Entry(habit_screen, width = 50)
    habit.pack()
    Label(text=" ").pack()

    Button(habit_screen, text = "Add another habit", font=("Calibri", 15), command = habit_storage).pack()
    Label(text=" ").pack()
    Button(habit_screen, text = "Finish adding", font=("Calibri", 15), command = display).pack()


    habit_screen.mainloop()


def habit_storage():
    habits_list = list()


def display():
    return



habit_entry()

