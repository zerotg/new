import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

window = tk.Tk()
window.title("Friendship Calculator")
window.geometry("600x600")
window["bg"] = "gainsboro"

# ----Functions----


def on_button():
    percentage = random.randint(40, 100)
    name1 = entry1.get()
    name2 = entry2.get()

    if percentage > 80:
        answer.set("You guys got a {0}%! {1}, and {2}, are great friends!".format(percentage, name1, name2))

    elif 79 > percentage > 65:
        answer.set("Not bad, you got a {0}%! {1}, and {2}, are good friends.".format(percentage, name1, name2))

    elif 64 >= percentage > 43:
        answer.set("Woah you got a {0}%. {1}, and {2},  are uhhh, friends?".format(percentage, name1, name2))

    elif percentage < 42:
        answer.set("{0}%, are you guys really friends?".format(percentage))


# ----label-----

word = tk.Label(text="Hello There", bg="gainsboro", font=("Times New Roman", 12))
word.grid(column=0, row=0)

word2 = tk.Label(text="What is your name?", bg="gainsboro", font=("Times New Roman", 12))
word2.grid(column=0, row=1)

word3 = tk.Label(text="What is your friends name?", bg="gainsboro", font=("Times New Roman", 12))
word3.grid(column=0, row=2)

word4 = tk.Label(text="CLICK ME!", bg="gainsboro", font=("Times New Roman", 12))
word4.grid(column=0, row=3)

# ----Entry-----

entry1 = tk.Entry(bg="pink")
entry1.grid(column=1, row=1)

entry2 = tk.Entry(bg="pink")
entry2.grid(column=1, row=2)

# ----Button----
photo = PhotoImage(file=r"C:\Users\misael.bello\PycharmProjects\new\70caa5bbf3812b479e0763f963e3a4441565111441_large"
                        r".png")
photoimage = photo.subsample(3, 3)

button1 = tk.Button(text="CLICK ME", command=on_button, bg="pink", font=("Times New Roman", 12), image=photoimage)
button1.grid(column=0, row=4)

# -----Answer-----

answer = tk.StringVar()
answer.set('')
answer_box = tk.Label(window, textvariable=answer, bg="pink", font=("Times New Roman", 12))
answer_box.grid(columnspan=5, row=5)

window.mainloop()