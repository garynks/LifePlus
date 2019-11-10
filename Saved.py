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
        f.write("Name:\n\nGoals:\n\nHabits:\n\n")

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
