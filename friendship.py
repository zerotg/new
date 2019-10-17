import tkinter as tk

window = tk.Tk()

window.title("Friendship")

window.geometry("400x400")

title = tk.Label(text="HELLO THERE", font=("Times New Roman", 20))
title.grid(column=0, row=0)

button1 = tk.Button(text="Click Me", bg="red")
button1.grid(column=0, row=1)

entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

window.mainloop()
