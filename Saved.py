import os.path

class Saved:

    def __init__(self):
        if os.path.exists("saved.txt"):
            self.first_time = False
        else:
            self.first_time = True

        if self.first_time:
            self.makefile()

    def makefile(self):
        f = open("saved.txt","w+")
        f.write("Name:\n\nGoals:\nHabits:\n\n")

    def savename(self,text):
        f = open("saved.txt","r")
        data = f.readlines()
        for i in range(len(data)):
            if 'Name:' in data[i]:
                data[i+1] = text+'\n'

        f = open("saved.txt","w")
        f.writelines(data)

    def loadname(self):
        f = open("saved.txt","r")
        data = f.readlines()
        for i in range(len(data)):
            if 'Name:' in data[i]:
                name = data[i+1][0:len(data[i+1])-1]
                return name

    def savegoal(self,goal):
        f = open("saved.txt", "r")
        data = f.readlines()
        goal_line = 0  # save the line number of where the goal starts to get listed
        goalcount = 1  # this is used as number to be written in front of the goal

        for i in range(len(data)):
            if 'Goals:' in data[i]:
                goal_line = i + 1

        while data[goal_line] != 'Habits:\n':
            goalcount += 1
            goal_line += 1

        data.insert(goal_line,(str(goalcount) + '. ' + goal + '\n'))  # example output : 1. insert goal here (newline)

        f = open("saved.txt", "w")
        f.writelines(data)

    def loadgoal(self):
        f = open("saved.txt","r")
        data = f.readlines()
        goal_line = 0  # save the line number of where the goal starts to get listed
        goals = []

        for i in range(len(data)):
            if 'Goals:' in data[i]:
                goal_line = i+1

        while data[goal_line] != 'Habits:\n':
            goals.append(data[goal_line])
            goal_line += 1

        return goals