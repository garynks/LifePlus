from tkinter import *
from Saved import Saved
from tkinter.ttk import *

# Global Variables
saving = Saved()  # Saved is a class by Mari to store goals and habits
goal_number = None


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


"""First frame that the user sees
    Prompts the user for name if they are a new user
    Jumps to the progress page if they are an existing user"""


class StartPage(Frame):
    def __init__(self, master):
        self.name_str = StringVar()
        self.name = None
        Frame.__init__(self, master)
        Label(self, text="lifeplus", font=("Helevetica", 30)).pack(side="top", padx=10)
        if saving.first_time:
            self.new_user()
        else:
            self.existing_user()

    def existing_user(self):
        Label(self, text="Welcome back!", font = ("Calibri", 15)).pack()
        Button(self, text="View progress", command=lambda: self.master.switch_frame(DisplayGoalAndHabits)).pack()

    def new_user(self):
        Label(self, text="What is your name?", font=("Calibri", 20)).pack(pady=10, padx=10)
        Label(text=" ").pack()
        Entry(self, width=20, textvariable=self.name_str).pack(pady=10)
        Label(text=" ").pack()
        Button(self, text="Enter", command=self.store_name).pack(pady=20)
        Label(text=" ").pack()

    def store_name(self):
        self.name = self.name_str.get()
        saving.savename(self.name)
        self.master.switch_frame(GoalEntry)


"""Prompts the user to enter their first goal"""


class GoalEntry(Frame):

    def __init__(self, master):
        self.master = master
        self.goal_str = StringVar()
        self.goal = None

        Frame.__init__(self, master)
        Label(self, text="What is your goal?", font=("Calibri", 20)).pack(side="top", pady=10)
        Entry(self, width=30, textvariable=self.goal_str).pack(pady=10)
        Label(text=" ").pack()
        Button(self, text="Plan your goal!", command=self.store_goal).pack(pady=20)

    def store_goal(self):
        self.goal = self.goal_str.get()
        saving.savegoal(self.goal)
        self.load_goal()
        self.master.switch_frame(HabitEntry)

    def load_goal(self):
        global goal_number
        temp = saving.loadgoal()
        goal_number = int(temp[len(temp)-1][0])


"""Prompts the user to enter a habit to build towards their goal"""


class HabitEntry(Frame):
    def __init__(self, master):
        self.master = master
        self.habit = None

        Frame.__init__(self, master)
        Label(self, text="What are some habits that you want to achieve to fulfill this goal?",
              font=("Calibri", 20)).pack(side="top", pady=5)
        self.add_habit()
        Button(self, text="Add another habit", command=self.add_habit).pack(side="bottom", pady=10)

    def store_habit(self):
        self.habit = self.habit_str.get()
        saving.savehabits(goal_number, self.habit)
        self.master.switch_frame(DisplayGoalAndHabits)  # temporarily direct user to the StartPage

    def add_habit(self):
        self.habit_str = StringVar()
        Entry(self, width=50, textvariable=self.habit_str).pack(side="right", pady=10)
        Label(text=" ").pack()
        Button(self, text="Add habit", command=self.store_habit).pack(side="left", padx=10, pady=10)


"""Displays the saved goals and habits from the saved file"""


class DisplayGoalAndHabits(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)

        with open("saved.txt", "r") as f:
            Label(self, text=f.read()).pack(side="left", fill="x")

        Button(self, text="View Progress", command=lambda: self.master.switch_frame(ProgressPage)).pack(side="right")


"""Display progress page"""


class ProgressPage(Frame):
    def __init__(self, master):
        self.master = master
        Frame.__init__(self, master)

        self.progress = 0  # stores the starting value of progress
        self.step = 10  # amount by which the progress bar increases
        self.Progressbar = Progressbar(mode="determinate", value=self.progress, variable="")
        self.Progressbar.pack(pady = 10)
        Button(self, text="+", command=self.IncrementProg).pack()
        Label(self, text = " ").pack()

    def IncrementProg(self):
        if self.progress + self.step < 100:
            self.Progressbar.step(self.step)
            self.progress += self.step

        else:
            self.Progressbar.step(99.9 - self.progress)
            self.progress = 100

        self.success_message()

    def success_message(self):
        if self.progress >= 99.9:
            Label(self, text = "Congratulations! You have successfully finished a habit!", font = ("Calibri", 13)).pack(pady = 10)


if __name__ == "__main__":
    app = LifePlusApp()
    app.mainloop()


