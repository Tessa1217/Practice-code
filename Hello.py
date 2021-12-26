# tkinter basic 
'''from tkinter import *
window = Tk()
label = Label(window, text = "Hello tkinter")
button = Button(window, text="클릭하세요!", bg = "yellow", fg = "blue", width=6, height = 2)
entry = Entry(window, fg = "black", bg = "yellow", width = 80)
label.pack()
button.pack()
entry.pack()
window.mainloop()'''

# pack.py
'''from tkinter import *
window = Tk() 
Button(window, text = "Box 1", bg = "red", fg = "white").pack(side = LEFT)
Button(window, text = "Box 2", bg = "blue", fg = "white").pack(side = RIGHT)
Button(window, text = "Box 3", bg = "black", fg = "white").pack() # side = LEFT, RIGHT, TOP, BOTTOM
window.mainloop()'''

# grid.py
'''from tkinter import * 
window = Tk() 
box1 = Button(window, text = "Box 1", bg = "red", fg = "white")
box2 = Button(window, text = "Box 2", bg = "blue", fg = "white")
box3 = Button(window, text = "Box 3", bg = "black", fg = "white")
box4 = Button(window, text = "Box 4", bg = "green", fg = "white")
box1.grid(row = 0, column = 0)
box2.grid(row = 0, column = 1)
box3.grid(row = 1, column = 0)
box4.grid(row = 1, column = 1)
window.mainloop()'''

# place.py
from tkinter import * 
window = Tk()
box1 = Button(window, text = "Box 1", bg = "red", fg = "white")
box2 = Button(window, text = "Box 2", bg = "blue", fg = "white")
box3 = Button(window, text = "Box 3", bg = "black", fg = "white")
box4 = Button(window, text = "Box 4", bg = "green", fg = "white")
box1.place(x = 0, y = 0)
box2.place(x = 20, y = 40)
box3.place(x = 40, y = 80)
box4.place(x = 60, y = 120)
window.mainloop()