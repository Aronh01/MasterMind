import tkinter as tk
import random
import collections

class Mastermind:
    def __init__(self,parent):
        frame = tk.Frame(parent)
        frame.pack()
        self.l1 = tk.Label(frame, text="----")
        self.l1.grid(column=1, row=0)
        self.l2 = tk.Label(frame, text="----")
        self.l2.grid(column=1, row=2)
        self. l3 = tk.Label(frame, text="----")
        self.l3.grid(column=0, row=2)
        c=0
        self.current = 0
        self.attempts = 0
        self.bt1 = tk.Button(frame, text="Sprawdz",command=lambda c=c: self.check()).grid(column=0, row=1)
        self.bt2 = tk.Button(frame, text="Oszust!",command=lambda c=c: self.check2()).grid(column=1, row=1)
        self.text1 = tk.Entry(frame)
        self.text1.grid(column=0, row=0)
        self.roll()
    def roll(self):
        self.var = random.randint(1,2)
        if self.var == 1:
            self.wzor = [random.choice('123456') for _ in range(4)]
        else:
            self.wzor = [random.choice('12345689') for _ in range(4)]
        print(*self.wzor)
    def check(self,event = None):
        self.player_guess = self.text1.get()
        self.attempts += 1
        self.hint = ""
        self.hint1 = ""
        i=0
        if self.hint != "XXXX":
            for i in range(4):
                if self.player_guess[i] == self.wzor[i]:
                    self.hint+="X"
                if self.player_guess[i] != self.wzor[i] and self.player_guess[i] in self.wzor:
                    self.hint+= "O"
            self.l1.config(text= self.hint + self.hint1)
        if self.hint == "XXXX":  
            self.l3.config(text= "Wygrales!!")
        elif self.attempts > 11:
            self.l3.config(text= "Wykorzystales 12 podejsc")
    def check2(self,event = None):
        if self.var == 1:
            self.l2.config(text='Tere fere '+format(''.join(self.wzor)))
        else:
            self.l2.config(text='Zlapales mnie ;/')

root = tk.Tk()
root.geometry("300x200")
Mastermind = Mastermind(root)
root.mainloop()

