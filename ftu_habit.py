from tkinter import *

# Initializing the habits 2d array
habits = list()


def habit_entry():
    # Initializing the window
    habit_screen = Tk()
    habit_screen.geometry("600x300")
    habit_screen.title("New Habit Entry")
    Label(text="How would you like to achieve it?", font=("Calibri", 30)).pack()
    Label(text=" ").pack()

    # Getting user input
    global habit
    habit = StringVar()

    # Add an entry box for user input
    Entry(habit_screen, width = 50, font = ("Calibri", 15), textvariable = habit).pack()
    Label(text=" ").pack()

    # Adding buttons for user to proceed to next step
    Button(habit_screen, text = "Add another habit", font=("Calibri", 15), command = habit_storage).pack()
    Label(text=" ").pack()
    Button(habit_screen, text = "Finish adding", font=("Calibri", 15), command = display).pack()

    habit_screen.mainloop()


def habit_storage():
    # Retrieving the user habit entry and add to 2-d array
    habit_str = habit.get()
    index = 1
    habits.insert(index, habit_str)


def display():
    return



habit_entry()

