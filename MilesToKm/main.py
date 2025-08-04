from tkinter import *

window = Tk()
window.config(padx = 30 , pady = 30)

def calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    result.config(text = f"{km}")


label1 = Label(text = "Miles")
label1.grid(row = 0 , column = 4)

label2 = Label(text = "is equal to")
label2.grid(row = 2 , column = 2)

label3 = Label(text = " Km")
label3.grid(row = 2 , column = 4)

miles_input = Entry(width = 10)
miles_input.grid(row = 0, column = 3)

result = Label(text = "0")
result.grid(row = 2, column = 3)

button = Button(text = "Calculate", command = calculate)
button.grid(row = 3 , column = 3)


window.mainloop()