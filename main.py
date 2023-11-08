from tkinter import *
from content import Content

# Window config
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

# Canvas config
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png", width=200, height=200)
canvas.create_image(135, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Content config
content = Content()

window.mainloop()
