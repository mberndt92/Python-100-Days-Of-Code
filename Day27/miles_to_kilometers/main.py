
# Miles to KM converter

from tkinter import *


def calculate():
    miles_value = int(entry.get())
    km_value = round(miles_value * 1.60934)
    km_value_label.config(text=f"{km_value}")


window = Tk()
window.title("Miles to KM converter")
window.wm_minsize(width=300, height=200)
window.config(padx=50, pady=50)

entry = Entry(width=10)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_value_label = Label(text="0")
km_value_label.grid(column=1, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)


window.mainloop()