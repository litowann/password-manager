from tkinter import *
from tkinter import messagebox
from password import Password
import pyperclip


class Content:

    def __init__(self):
        # Labels config
        self.website_label = Label(text="Website:")
        self.website_label.grid(column=0, row=1)

        self.email_label = Label(text="Email/Username:")
        self.email_label.grid(column=0, row=2)

        self.password_label = Label(text="Password:")
        self.password_label.grid(column=0, row=3)

        # Inputs config
        self.website_input = Entry(width=50)
        self.website_input.grid(column=1, row=1, columnspan=2)

        self.email_input = Entry(width=50)
        self.email_input.grid(column=1, row=2, columnspan=2)

        self.password_input = Entry(width=26)
        self.password_input.grid(column=1, row=3)

        # Buttons config
        self.generate_password_btn = Button(text="Generate Password", width=20, command=self.generate_password)
        self.generate_password_btn.grid(column=2, row=3)

        self.save_btn = Button(text="Save", width=47, command=self.save)
        self.save_btn.grid(column=1, row=4, columnspan=2)

        # Password instance
        self.password_instance = Password()

    def generate_password(self):
        generated_password = self.password_instance.generate_password()

        pyperclip.copy(generated_password)
        self.password_input.delete(0, END)
        self.password_input.insert(0, generated_password)

    def save(self):
        website_data = self.website_input.get()
        email_data = self.email_input.get()
        password_data = self.password_input.get()

        if not len(website_data) or not len(email_data) or not len(password_data):
            messagebox.showwarning(title="Fields validation warning", message="All fields are required!")

        else:
            is_okay = messagebox.askokcancel(
                title="Generated data",
                message=f"These data will be entered:\n"
                        f"Website: {website_data}\n"
                        f"Email/Username: {email_data}\n"
                        f"Password: {password_data}\n"
                        f"Do you want to save it?",
            )

            if is_okay:
                with open("data.txt", "a") as data:
                    data.write(f"{website_data} | {email_data} | {password_data}\n")

                    self.website_input.delete(0, END)
                    self.email_input.delete(0, END)
                    self.password_input.delete(0, END)
