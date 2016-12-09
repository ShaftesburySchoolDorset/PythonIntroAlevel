from tkinter import *

class Tkmaxx:
    
    def __init__(self, master):
        self.master = master
        
        self.button1 = Button(master, text="Quit", command=master.quit)
        self.button1.pack(side=LEFT)
        
        self.button2 = Button(master, text="Hello", command=self.say_hi)
        self.button2.pack(side=LEFT)
        
    def say_hi(self):
        print("Hi there!")


root = Tk() # Creates a new Tkinter app
app = Tkmaxx(root) # Creates our app
root.mainloop() # Run our app