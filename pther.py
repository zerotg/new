from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()
img = PhotoImage(file=r"C:\Users\misael.bello\PycharmProjects\new\70caa5bbf3812b479e0763f963e3a4441565111441_large"
                      r".png")
canvas.create_image(20, 20, anchor=NW, image=img)
mainloop()
