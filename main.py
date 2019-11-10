from tkinter import *

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
        print(self.goal, "is the goal!")
        self.master.switch_frame(HabitEntry)


"""Prompts the user to enter a habit to build towards their goal"""
class HabitEntry(Frame):
    def __init__(self, master):
        self.master = master
        self.habit_str = StringVar()
        self.habit = None

        Frame.__init__(self, master)
        Label(self, text="How would you like to achieve it?", font=("Calibri", 20)).pack(side="top", fill="x", pady=5)
        Entry(self, width=50, textvariable = self.habit_str).pack(pady=10)
        Label(text=" ").pack()
        Button(self, text = "Add habit", command = self.store_habit).pack(side="left", padx = 10, pady=10)   # Bind a function to command
        Button(self, text = "Add another habit", command = self.add_another).pack(pady=10)

    def store_habit(self):
        self.habit = self.habit_str.get()
        self.master.switch_frame(StartPage) # temporarily direct user to the StartPage

    def add_another(self):
        self.habit_str = StringVar()
        Entry(self, width=50, textvariable = self.habit_str).pack(pady=10)
        self.habit = self.habit_str.get()


"""Displays the saved goals and habits from the saved file"""
class DisplayGoalAndHabits(Frame):
    def __init__(self, master):
        self.master = master
        #   Read from file and display the content




if __name__ == "__main__":
    app = LifePlusApp()
    app.mainloop()


