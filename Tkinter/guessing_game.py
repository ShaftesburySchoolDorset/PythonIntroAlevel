from tkinter import *
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")

        self.secret_number = random.randint(1, 10)
        self.guess = None
        self.num_guesses = 0
        
        self.message = "Guess a number from 1 to 10"
        self.label_text = StringVar()
        self.label_text.set(self.message)
        self.label = Label(master, textvariable=self.label_text)

        self.entry = Entry(master)

        self.guess_button = Button(master, text="Guess", command=self.guess_number)
        self.reset_button = Button(master, text="Play again", command=self.reset, state=DISABLED)

        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.guess_button.grid(row=2, column=0)
        self.reset_button.grid(row=2, column=1)

    def guess_number(self):
        self.num_guesses += 1
        
        self.guess = int(self.entry.get())
        
        if self.guess is None:
            self.message = "Guess a number from 1 to 10"

        elif self.guess == self.secret_number:
            suffix = '' if self.num_guesses == 1 else 'es'
            self.message = "Congratulations! You guessed the number after %d guess%s." % (self.num_guesses, suffix)
            self.guess_button.configure(state=DISABLED)
            self.reset_button.configure(state=NORMAL)

        elif self.guess < self.secret_number:
            self.message = "Too low! Guess again!"
        else:
            self.message = "Too high! Guess again!"

        self.label_text.set(self.message)

    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = random.randint(1, 10)
        self.guess = 0
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 10"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

root = Tk()
my_gui = GuessingGame(root)
root.mainloop()