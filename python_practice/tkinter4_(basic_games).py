# 1부터 100까지 숫자 추측하기

from tkinter import * 
import random

answer = random.randint(1, 100)

def guess_process():
    guess = int(guess_entry.get())

    if guess > answer:
        msg = "Too High!"
    elif guess < answer:
        msg = "Too Low!"
    else:
        msg = "Your answer is Correct!"
    
    resultLabel["text"] = msg 
    guess_entry.delete(0, END)

def reset():
    global answer
    answer = random.randint(1, 100)
    resultLabel["text"] = "Try one more time!"

window = Tk()
window.configure(bg = "white")
window.title("Number guessing game")
window.geometry("600x70")

titleLabel = Label(window, text = "Let's play Number guessing game!", fg = "black", bg = "white", font = "Gothic 18 bold")
titleLabel.pack()

guess_entry = Entry(window)
guess_entry.pack(side = LEFT)
guess_button = Button(window, text = "Guess", fg = "red", bg = "white", command = guess_process)
guess_button.pack(side = LEFT)
reset_button = Button(window, text = "Reset", fg = "blue", bg = "white", command = reset)
reset_button.pack(side = LEFT)

resultLabel = Label(window, text = "Enter number between 1 to 100", fg = "black", bg = "white", font = "Gothic 15 bold")
resultLabel.pack(side = LEFT)

window.mainloop()

# Rock, Paper, Scissors!

from tkinter import * 
import random 

def choice(user):
    computer = random.choice(["rock", "paper", "scissors"])
    if computer == "rock":
        computer_image["image"] = rock_image 
    elif computer == "paper":
        computer_image["image"] = paper_image 
    else:
        computer_image["image"] = scissors_image 
    
    if (computer == "rock" and user == "paper") or (computer == "paper" and user == "scissors") or (computer == "scissors" and user == "rock"):
        result = "User wins!"
    elif computer == user:
        result = "Draw!"
    else:
        result = "Computer wins!"
    output.config(text = "User: " + user + "    Computer: " + computer + "  " + result)

def choose_rock():
    choice("rock")
def choose_paper():
    choice("paper")
def choose_scissors():
    choice("scissors")

window = Tk()
window.configure(bg = "white")
window.title("Rock, Paper, Scissors!")
window.geometry("600x600")
Label(window, text = "User: Rock, Paper, Scissors!", fg = "black", bg = "white", font = ("Helvetica", "16")).pack()
frame = Frame(window)

rock_image = PhotoImage(file = "rock.png")
paper_image = PhotoImage(file = "paper.png")
scissors_image = PhotoImage(file = "scissors.png")

rock = Button(window, image = rock_image, commannd = choose_rock)
rock.pack(side = "left")
paper = Button(window, image = paper_image, commannd = choose_paper)
paper.pack(side = "left")
scissors = Button(window, image = scissors_image, commannd = choose_scissors)
scissors.pack(side = "left")

frame.pack()
Label(window, text = "Computer's Choice", fg = "black", bg = "white", font = ("Helvetica", "16")).pack()
computer_image = Label(window, image = rock_image)
computer_image.pack()
output = Label(window, text='', font = ("Helvetica", "16"))
output.pack()

window.mainloop()

# Tic-Tac-Toe game
from tkinter import * 
import random

window = Tk()
window.title("Tic Tac Toe!")
window.geometry("220x90")
player = "X"
list = []

for i in range(9):
    b = Button(window, text = "          ", command = lambda k = i: checked(k))
    b.grid(row=i//3, column=i%3)
    list.append(b)

def checked(i):
    global player 
    button = list[i]
    if button["text"] != "          ":
        return
    button["text"] = "    " + player + "    "
    button["bg"] = "blue"
    if player == "X":
        player = "0"
        button["bg"] = "blue"
    else:
        player = "X"
        button["bg"] = "yellow"

window.mainloop()
