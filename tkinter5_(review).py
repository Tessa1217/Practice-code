# 1. 
'''from tkinter import * 
window = Tk()
label = Label(window, text = "Hi!")
label.pack(side = LEFT)
def click():
  label["text"] = "clicked"
button = Button(window, text = "click me", command = click)
button.pack(side = LEFT)

window.mainloop()'''

#2. 
'''from tkinter import *
window = Tk()
Label(window, text = "Hello, I'm Label", width = 50, height = 3, bg = "orange", fg = "blue").pack()
window.mainloop()'''

#3.
'''from tkinter import * 
window = Tk()
row_index = 0
col_index = 0
button_list = []
for button_row in range(0, 4):
  for button_col in range(0, 10):
    i = str(button_row) + "행" + str(button_col) + "열"
    button_list.append(i)
for button_text in button_list: 
  Button(window, text = button_text).grid(row = row_index, column = col_index)
  col_index += 1
  if col_index > 9:
    row_index += 1
    col_index = 0
window.mainloop()'''

#4. 
'''from tkinter import * 
window = Tk()

#Labels
name = Label(window, text = "이름:").grid(row = 0, column = 0)
address = Label(window, text = "주소:").grid(row = 1, column = 0)
state = Label(window, text = "주:").grid(row = 2, column = 0)
code = Label(window, text = "우편번호:").grid(row = 3, column = 0)
country = Label(window, text = "국가:").grid(row = 4, column = 0)

#Entries
e1 = Entry(window, bg = "white").grid(row = 0, column = 1, columnspan = 9)
e2 = Entry(window, bg = "white").grid(row = 1, column = 1, columnspan = 9)
e3 = Entry(window, bg = "white").grid(row = 2, column = 1, columnspan = 9)
e4 = Entry(window, bg = "white").grid(row = 3, column = 1, columnspan = 9)
e5 = Entry(window, bg = "white").grid(row = 4, column = 1, columnspan = 9)

#Buttons
clear = Button(window, text = "clear").grid(row = 5, column = 9)
submit = Button(window, text = "submit").grid(row = 5, column = 10)

window.mainloop()'''


#5. 
'''from tkinter import * 
window = Tk()

number = Label(window, text = "0")
number.grid(row = 0, column = 1)

cnt = 0
def Increase():
  global cnt
  cnt += 1
  number["text"] = str(cnt)

def Decrease():
  global cnt 
  cnt -= 1
  number["text"] = str(cnt)

def Reset():
  global cnt 
  cnt = 0
  number["text"] = str(cnt)

inc = Button(window, text = "Increase", command = Increase).grid(row = 0, column = 2)
dec = Button(window, text = "Decrease", command = Decrease).grid(row = 0, column = 0)
reset = Button(window, text = "Reset", command = Reset).grid(row = 1, column = 1) 

  
window.mainloop()'''

#6. 
'''from tkinter import * 
import random 
window = Tk()

label = Label(window, text = "Roll the dice!")
label.pack(side = "left")

def Roll():
  num = random.randint(1, 7)
  label["text"] = str(num)

button = Button(window, text = "Roll", command = Roll)
button.pack(side = "left")

window.mainloop()'''

#7. 
'''from tkinter import * 
import random 
window = Tk()

#Label
Label(window, text = "Inch: ").grid(row = 0, column = 0)
Label(window, text = "Inch to cm ").grid(row = 1, column = 0)

#Entry
inch = Entry(window)
inch.grid(row = 0, column = 1, columnspan = 8)

#Result Label
cm = Label(window, text = "Let's convert inch to cm")
cm.grid(row = 1, column = 1, columnspan = 8)

#Button Function
def ItoC():
  inch_val = float(inch.get())
  cm_val = round(inch_val * 2.54, 3)
  cm["text"] = str(cm_val) + "cm"

def Reset():
    inch.get()
    inch.delete(0, END)
    cm["text"] = "Let's convert inch to cm"

#Button
button = Button(window, text = "Convert", command = ItoC)
button.grid(row = 2, column = 5)
button2 = Button(window, text = "Reset", command = Reset)
button2.grid(row = 2, column = 6)


window.mainloop()'''

#8. 
from tkinter import *
from tkinter import messagebox 
window = Tk()

#Label
Label(window, text = "ID").grid(row = 0, column = 0)
Label(window, text = "Password").grid(row = 1, column = 0)

#Entry
id = Entry(window, bg = "white", fg = "black")
id.grid(row = 0, column = 1, columnspan = 8)
password = Entry(window, bg = "white", fg = "black")
password.grid(row = 1, column = 1, columnspan = 8)

#Button Function
def Login():
  id.get()
  password.get()
  id.delete(0, END)
  password.delete(0, END)
  messagebox.showinfo("Login", "Login successful")
  

def Reset():
  id.get()
  id.delete(0, len(id))
  password.get()
  password.delete(0, len(password))

#Button
log = Button(window, text = "Login", command = Login)
log.grid(row = 2, column = 0)
cancel = Button(window, text = "Cancel", command = Reset)
cancel.grid(row = 2, column = 1)

window.mainloop()

