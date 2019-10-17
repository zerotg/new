from tkinter import *
from tkinter.ttk import *

root = Tk()

Label(root, text='GeeksforGeeks', font=('verdana', 15)).pack(side=TOP, pady=10)
photo = PhotoImage(file=r"C:\Users\misael.bello\PycharmProjects\new\70caa5bbf3812b479e0763f963e3a4441565111441_large"
                        r".png")
photoimage = photo.subsample(3, 3)

Button(root, text='Click Me!', image=photoimage, compound=LEFT).pack(side=TOP)

mainloop()