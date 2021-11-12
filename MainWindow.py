import tkinter
from tkinter import *
from tkinter import messagebox

from CredRepo import CredRepo
from Credentials import Credentials
from PasswordGenerator import PasswordGenerator


class MainWindow(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        PINK = "#e2979c"
        RED = "#e7305b"
        GREEN = "#9bdeac"
        YELLOW = "#f7f5dd"
        FONT_NAME = "Courier"
        WORK_MIN = 25
        SHORT_BREAK_MIN = 5
        LONG_BREAK_MIN = 20
        reps = 0
        timer = None
        self.passwd = StringVar()
        self.email = StringVar()
        self.web = StringVar()
        self.title("Password Manager")
        self.config(padx=100, pady=50, bg=YELLOW)
        self.passwd.set("-----")
        self.title_label = Label(text="Password Manager", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
        self.title_label.grid(column=1, row=0)

        self.canvas = Canvas(width=350, height=224, bg=YELLOW, highlightthickness=0)
        tomato_img = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 112, image=tomato_img)
        self.canvas.grid(column=1, row=1)

        self.title_label_website = Label(text="Website", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 11))
        self.title_label_website.grid(column=0, row=2)
        self.entry_website = Entry(textvariable=self.web, width=50)
        self.entry_website.grid(column=1, row=2)

        self.title_label_email = Label(text="email", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 11))
        self.title_label_email.grid(column=0, row=3)
        self.entry_email = Entry(textvariable=self.email, width=50)

        self.entry_email.grid(column=1, row=3)

        self.title_label_password = Label(text="Password", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 11))
        self.title_label_password.grid(column=0, row=4)
        self.entry_password = Entry(self, textvariable=self.passwd, width=25)
        self.entry_password.config(text="---")
        self.entry_password.grid(column=1, row=4)

        self.start_button = Button(text="Generate", highlightthickness=0, command=lambda:self.generate())
        self.start_button.grid(column=1, row=6)

        self.add_button = Button(text="Add", highlightthickness=0, command=lambda:self.add())
        self.add_button.grid(column=2, row=6)

        def evaluate(event):
            self.title_label_website.configure(text="Result: " + str(eval(self.title_label_website.get())))

        self.mainloop()

    def generate(self):
        pwd = PasswordGenerator.generate_password()
        self.passwd.set(pwd)
        self.update_idletasks()

    def add(self):
        cred = Credentials(url=self.web, user_email=self.email, passw=self.passwd)
        if CredRepo.save(credentials=cred):
            self.passwd = StringVar()
            self.email = StringVar()
            self.web = StringVar()
            messagebox.showinfo(title="Saving", message='Saved')
        else:
            messagebox.showerror(title="bad", message="error saving")
