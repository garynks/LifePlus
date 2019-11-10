from tkinter import *


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


class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text = "lifeplus", font = ("Helevetica", 30)).pack(side="top", fill="x", pady=5)
        Button(self, text="What is your name?", command = lambda: master.switch_frame(GoalEntry)).pack()


class GoalEntry(Frame):

    def __init__(self, master):
        self.master = master
        self.goal_str = StringVar()
        self.goal = None

        Frame.__init__(self, master)
        Label(self, text = "What is your goal?", font = ("Calibri", 20)).pack(side="top", fill="x", pady=5)
        Entry(self, width = 50, textvariable = self.goal_str).pack()
        Label(text=" ").pack()
        Button(self, text = "Plan your goal!", command = self.store_goal).pack()

    def store_goal(self):
        self.goal = self.goal_str.get()
        print(self.goal, "is the goal!")
        self.master.switch_frame(HabitEntry)


class HabitEntry(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="How would you like to achieve it?", font=("Calibri", 20)).pack(side="top", fill="x", pady=5)
        #
        # habit = StringVar()
        # global habit

        Entry(self, width=50).pack()
        Label(text=" ").pack()
        Button(self, text = "Add habit", command = lambda: master.switch_frame(StartPage)).pack()   # Bind a function to command



if __name__ == "__main__":
    app = LifePlusApp()
    app.mainloop()


