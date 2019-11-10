class ProgBar:
    def __init__(self):
        self.progress = 50                                                     # stores the starting value of progress
        self.step = 25                                                              # amount by which the progress bar increases
        self.Progressbar = Progressbar(mode="determinate", value = self.progress, variable="")
        self.Progressbar.pack()
        Button(self, text="+", command=self.IncrementProg).pack()
    
    def IncrementProg(self):
        if self.progress + self.step < 100:
            self.Progressbar.step(self.step)
            self.progress += self.step
            print(self.progress)
            
        else:
            self.Progressbar.step(99.9-self.progress)
            self.progress = 100    