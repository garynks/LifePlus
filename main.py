from tkinter import *
from saved import Saved

saving = Saved()    # Saved is a class by Mari to store goals and habits

"""Each class is divided so that each class stores the contents of each frame"""

"""Main window that controls the framing"""
class LifePlusApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


"""First frame that the user sees"""
class StartPage(Frame):
    def __init__(self, master):
        self.name_str = StringVar()
        self.name = None

        Frame.__init__(self, master)
        Label(self, text = "lifeplus", font = ("Helevetica", 30)).pack(side="top", padx = 10)
        Label(self, text = "What is your name?", font = ("Calibri", 20)).pack(pady = 10, padx = 10)
        Label(text = " ").pack()
        Entry(self, width = 20, textvariable = self.name_str).pack(pady = 10)
        Label(text = " ").pack()
        Button(self, text = "Enter", command = self.store_name).pack(pady = 20)
        Label(text = " ").pack()

    def store_name(self):
        self.name = self.name_str.get()
        self.master.switch_frame(GoalEntry)


"""Prompts the user to enter their first goal"""
class GoalEntry(Frame):

    def __init__(self, master):
        self.master = master
        self.goal_str = StringVar()
        self.goal = None

        Frame.__init__(self, master)
        Label(self, text = "What is your goal?", font = ("Calibri", 20)).pack(side="top", pady = 10)
        Entry(self, width = 30, textvariable = self.goal_str).pack(pady = 10)
        Label(text=" ").pack()
        Button(self, text = "Plan your goal!", command = self.store_goal).pack(pady = 20)

    def store_goal(self):
        self.goal = self.goal_str.get()
        saving.savegoal(self.goal)
        self.master.switch_frame(HabitEntry)


"""Prompts the user to enter a habit to build towards their goal"""
class HabitEntry(Frame):
    def __init__(self, master):
        self.master = master
        self.habit = None

        Frame.__init__(self, master)
        Label(self, text="How would you like to achieve it?", font=("Calibri", 20)).pack(side="top", pady=5)
        self.add_habit()
        Button(self, text = "Add another habit", command = self.add_habit).pack(side = "bottom", pady=10)

    def store_habit(self):
        self.habit = self.habit_str.get()
        saving.savehabits(self.habit)
        self.master.switch_frame(DisplayGoalAndHabits) # temporarily direct user to the StartPage

    # def add_another(self):
    #     self.habit_str = StringVar()
    #     Entry(self, width=50, textvariable = self.habit_str).pack(pady=10)
    #     self.habit = self.habit_str.get()

    def add_habit(self):
        self.habit_str = StringVar()
        Entry(self, width=50, textvariable = self.habit_str).pack(side = "right", pady=10)
        Label(text=" ").pack()
        Button(self, text = "Add habit", command = self.store_habit).pack(side="left", padx = 10, pady=10)




"""Displays the saved goals and habits from the saved file"""
class DisplayGoalAndHabits(Frame):
    def __init__(self, master):
        self.master = master
        with open("saved.txt", "r") as f:
            Label(self, text = f.read()).pack()

        # while the end of file is not reached
        # print the goals and habits as labels
        #   Read from file and display the content
        #  Saved().loadgoals() return list of all the goals
        #  Saved().loadhabits(goal) goal = int indicating the goal; returns list of habits for that goal
        #  Saved().loadprgrs(goal,lastten) lastten is the last 10 char of habit -> could be written as habit[len(habit)-10:]
        #       this will return a string fraction (eg '2/3') to indicate progress for that habit
"""STILL IN PROGRESS"""
    def print_goal(self):
        Label(self, text = saving.loadgoal(), font = ("Calibri", 15)).pack(side = "left")

    def print_habits(self):
        Label (self, text = saving.loadhabits(), font = ("Calibri", 15)).pack(side = "right")

    def print_everything(self):



if __name__ == "__main__":
    app = LifePlusApp()
    app.mainloop()


