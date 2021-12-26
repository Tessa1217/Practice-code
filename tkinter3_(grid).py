# 위젯 속성 변경 
from tkinter import *
window = Tk()
label = Label(window, text = "This is how tkinter displays a label.", fg = "red", font = "Times 18 bold")
label.pack()
label['text'] = "This is a label."
label['fg'] = "blue"
label['font'] = "Gothic 32"
label.config(text = "THIS IS A LABEL")
label.config(fg = "#FF00AA")
window.mainloop()

# Gridspan

from tkinter import * 

window = Tk()

Label(window, text = "Width").grid(row = 0, column = 0)
Label(window, text = "Height").grid(row = 1, column = 0)

Entry(window).grid(row = 0, column = 1)
Entry(window).grid(row = 1, column = 1)

Button(window, text = "Save Image").grid(row = 2, column  = 1, sticky = W + E + N + S)
Button(window, text = "Zoom in").grid(row = 2, column = 2)
Button(window, text = "Zoom out").grid(row = 2, column = 3)

Label(window, text = "Image").grid(row = 0, column = 2, columnspan = 2, rowspan = 2)

window.mainloop()

# Event Driven Programming - 1
from tkinter import * 

def process():
    print("You clicked the button!") # define process() function

window = Tk()
button = Button(window, text = "Click!", command = process).pack() # call process() func 

window.mainloop()

# EDP - 2
from tkinter import * 

cnt = 0

window = Tk()

def process():
    global cnt
    cnt += 1
    label['text'] = "버튼 클릭 횟수: " + str(cnt)

def reset():
    global cnt 
    cnt = 0
    label['text'] = "버튼 클릭 횟수: " + str(cnt)

label = Label(window, text = "버튼 클릭 횟수 없음")
label.pack()
button_increase = Button(window, text = "증가", command = process).pack()
button_reset = Button(window, text = "리셋", command = reset).pack()

window.mainloop()

# Temperature F -> C, C -> F
from tkinter import * 

window = Tk()
Label(window, text="F").grid(row = 0, column = 0)
Label(window, text = "C").grid(row = 1, column = 0)

def FtoC():
    tf = float(e1.get())
    tc = round((tf - 32.0) * 5.0/9.0, 3)
    e2.delete(0, END)
    e2.insert(0, str(tc))

def CtoF():
    tc = float(e2.get())
    tf = round((tc * 9.0/5.0) + 32, 3)
    e1.delete(0, END)
    e1.insert(0, str(tf))

e1 = Entry(window)
e1.grid(row = 0, column = 1)
e2 = Entry(window)
e2.grid(row = 1, column = 1)

Button(window, text = "F -> C", command = FtoC).grid(row = 2, column = 1, sticky = W + E + N + S)
Button(window, text = "C -> F", command = CtoF).grid(row = 3, column = 1, sticky = W + E + N + S)
window.mainloop()