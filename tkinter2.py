# Frame.py
from tkinter import * 

window = Tk()
f = Frame(window)

box1 = Button(f, text = "Box 1", bg = "red", fg = "white")
box2 = Button(f, text = "Box 2", bg = "blue", fg = "white")
box3 = Button(f, text = "Box 3", bg = "green", fg = "white")
box4 = Button(f, text = "Box 4", bg = "yellow", fg = "white")
box1.pack(side = LEFT)
box2.pack(side = LEFT)
box3.pack(side = LEFT)
box4.pack(side = LEFT)

l = Label(window, text = "Box numbers")
l.pack()
f.pack()

window.mainloop()

# Window size.py 
from tkinter import * 
window = Tk()
window.geometry("300x300") # "x" instead of "*"
Label(window, text = "Window size: 300 x 300").pack()
Button(window, text = "Box1", width = 10, height = 3).pack()
Button(window, text = "Box2", width = 10, height = 3).pack()
Button(window, text = "Box3", width = 10, height = 3).pack()
Button(window, text = "Box4", width = 10, height = 3).pack()
window.mainloop()
