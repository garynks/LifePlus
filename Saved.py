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
        f.write("Name:\n\nGoals:\nHabits:\n")

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

        for i in range(len(goals)):
            goals[i] = goals[i][:-1]

        return goals

    def savehabits(self,goal,habit):  # variable for single integer
        f = open("saved.txt", "r")
        data = f.readlines()
        repeats = 10  # assume each habits are repeated 10 times
        habit_line = 0  # saves which line I should write the habit on
        numberthehab = True # True or False depending on whether i need to number the habit to its goal or not

        for i in range(len(data)):
            if 'Habits:' in data[i]:
                habit_line = i + 1

        lineafter = habit_line # where I need to insert

        while lineafter < len(data):
            lineafter += 1  # lineafter then indicates the last index in data + 1 (out of index without adjustment)

        for i in range(habit_line-1, lineafter-1):  ##fix this
            if data[i] == str(goal)+'\n':  # if habit is already numbered
                numberthehab = False  # don't need to make another one

        if numberthehab:
            data.insert(lineafter, str(goal)+'\n')
            lineafter += 1

        data.insert(lineafter,('\t' + habit + ' x ' + str(repeats) +'\n'))  # example output : 1. insert goal here (newline)

        f = open("saved.txt", "w")
        f.writelines(data)

    def loadhabits(self,goal):
        f = open("saved.txt", "r")
        data = f.readlines()
        habit_line = 0  # the habits I need to return
        return_list = []

        for i in range(len(data)):
            if data[i] == str(goal)+'\n':
                habit_line = i + 1

        return_list.append(data[habit_line])  # first one always exist so append
        while habit_line+1 < len(data) and data[habit_line+1][0] == '\t':
            habit_line += 1
            if data[habit_line][1] != '\t':
                return_list.append(data[habit_line])

        for i in range(len(return_list)):
            return_list[i] = return_list[i][1:-1]

        return return_list

    def saveprgrs(self,goal,lastfive,progress):
        f = open("saved.txt", "r")
        data = f.readlines()
        prog_line = 0  # saves which line I should write the progress on
        start = 0 # where to search the start from

        for i in range(len(data)):
            if (str(goal) + '\n') in data[i]:
                start = i + 1

        next_goal = start

        while next_goal+1 < len(data) and data[next_goal+1][0] == '\t':
            next_goal += 1  # at the end it should give the line to stop the search at

        for i in range(start, next_goal+1):
            if lastfive in data[i]:
                prog_line = i + 1

        if data[prog_line][1] != '\t':  # if progress doesn't already exist
            data.insert(prog_line,('\t\t' +'Progress: ' + str(progress)+'\n'))
            # example output : (double tab)Progress: 20
        else:
            data[prog_line] = ('\t\t' +'Progress: ' + str(progress)+'\n')  # just replace the progress part

        f = open("saved.txt", "w")
        f.writelines(data)

    def loadprgrs(self,goal,lastfive):
        f = open("saved.txt", "r")
        data = f.readlines()
        prog_line = 0  # saves which line I should write the progress on
        start = 0 # where to search the start from

        for i in range(len(data)):
            if (str(goal) + '\n') in data[i]:
                start = i + 1

        next_goal = start

        while next_goal+1 < len(data) and data[next_goal+1][0] == '\t':
            next_goal += 1  # at the end it should give the line to stop the search at

        for i in range(start, next_goal+1):
            if lastfive in data[i]:  # if i find the habit
                prog_line = i + 1  # line after that is where the progress is written

        progress = data[prog_line][12:-1]  # this is after Progress:

        return int(progress)
