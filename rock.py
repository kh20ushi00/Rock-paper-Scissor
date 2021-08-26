# Import Required Library
from tkinter import *
import random
  
# Create Object
root = Tk()
  
# Set geometry
root.geometry("600x600")
  
# Set title
root.title("Rock Paper Scissor Game")
  
# Computer Value
computer_value = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}
  
# Reset The Game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    c1.config(text = "Player              ")
    c3.config(text = "Computer")
    c4.config(text = "")
  
# Disable the Button
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
  
# If player selected rock
def isrock():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    c4.config(text = match_result)
    c1.config(text = "Rock            ")
    c3.config(text = c_v)
    button_disable()
  
# If player selected paper
def ispaper():
    c_v = computer_value[str(random.randint(0, 2))]
    if c_v == "Paper":
        match_result = "Match Draw"
    elif c_v=="Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    c4.config(text = match_result)
    c1.config(text = "Paper           ")
    c3.config(text = c_v)
    button_disable()
  
# If player selected scissor
def isscissor():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Computer Win"
    elif c_v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    c4.config(text = match_result)
    c1.config(text = "Scissor         ")
    c3.config(text = c_v)
    button_disable()
  
# Add Labels, Frames and Button
Label(root,
      text = "Rock Paper Scissor",
      font = "normal 30 bold",
      fg = "red").pack(pady = 20)
  
frame = Frame(root)
frame.pack()
  
c1 = Label(frame,
           text = "User              ",
           font = 5)
  
c2 = Label(frame,
           text = "VS             ",
           font = "normal 10 bold")
  
c3 = Label(frame, text = "Computer", font = 10)
  
c1.pack(side = LEFT)
c2.pack(side = LEFT)
c3.pack()
  
c4 = Label(root,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
c4.pack(pady = 20)
  
frame1 = Frame(root)
frame1.pack()
  
b1 = Button(frame1, text = "Rock",
            font = 10, width = 7,
            command = isrock)
  
b2 = Button(frame1, text = "Paper ",
            font = 10, width = 7,
            command = ispaper)
  
b3 = Button(frame1, text = "Scissor",
            font = 10, width = 7,
            command = isscissor)
  
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)
  
Button(root, text = "Reset Game",
       font = 10, fg = "red",
       bg = "black", command = reset_game).pack(pady = 20)
  
# Excecute Tkinter
root.mainloop()
