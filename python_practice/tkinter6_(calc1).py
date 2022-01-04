from tkinter import *

window = Tk()
window.title("Calculator")
display = Entry(window, width = 50, bg = "white", fg = "black")
display.grid(row = 0, column = 0, columnspan = 5)

button_list = ["7", "8", "9", "/", "C", "4", "5", "6", "*", " ", "1", "2", "3", "-", " ", "0", ".", "=", "+", " "]

def click(key):
    if key == "=":
        result = eval(display.get())
        number = str(result)
        display.delete(0, END)
        display.insert(0, number)

    elif key == "C":
        display.get()
        display.delete(0, END)

    else:
        display.insert(END, key)

row_index = 1
col_index = 0

for button_text in button_list:
    Button(window, text = button_text, width = 10, command = lambda t = button_text: click(t)).grid(row = row_index, column = col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0

window.mainloop()
