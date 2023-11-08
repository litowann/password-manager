from tkinter import *

# Window config
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50)

# Canvas config
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png", width=200, height=200)
canvas.create_image(135, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels config
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Inputs config
website_input = Entry(width=50)
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=26)
password_input.grid(column=1, row=3)


# Buttons config
def generate_password():
    print("Password has been generated.")


def add():
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()

    with open("data.txt", "w") as data:
        data.write(f"{website_data} | {email_data} | {password_data}")

    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)


generate_password_btn = Button(text="Generate Password", width=20, command=generate_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=47, command=add)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()