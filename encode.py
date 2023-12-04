import tkinter
from tkinter import *
from random import randint, choice
import string

root = tkinter.Tk()
root.title("PASSWORD GENERATOR")
root.config(background='aquamarine')
root.geometry('800x600')

def generate_password():
    pw_length = int(pass_entry.get())
    uppercases = uppercase_var.get()
    lowercases = lowercase_var.get()
    numbers = numbers_var.get()
    special_chars = special_chars_var.get()

    characters = ''
    if uppercases:
        characters += string.ascii_uppercase
    if lowercases:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        tkinter.messagebox.showinfo("Error", "Please select at least one character set.")
        return

    my_password = ''.join(choice(characters) for _ in range(pw_length))
    Password_enter.delete(0, END)
    Password_enter.insert(0, my_password)

def clip():
    root.clipboard_clear()
    root.clipboard_append(Password_enter.get())

Password = tkinter.Label(root, text='How many characters do you want for your password?', bg='aquamarine')
Password.config(font=("Times New Roman", 20))
Password.pack(pady=20)

pass_entry = Entry(root, text='', font=('Helvetica', 20))
pass_entry.pack(pady=20)

uppercase_var = IntVar()
uppercase_checkbox = Checkbutton(root, text="Uppercase Letters", variable=uppercase_var, bg='aquamarine', font=('Helvica',20))
uppercase_checkbox.pack()

lowercase_var = IntVar()
lowercase_checkbox = Checkbutton(root, text="Lowercase Letters", variable=lowercase_var, bg='aquamarine',font=('Helvica',20))
lowercase_checkbox.pack()

numbers_var = IntVar()
numbers_checkbox = Checkbutton(root, text="Numbers", variable=numbers_var, bg='aquamarine', font=('Helvica',20))
numbers_checkbox.pack()

special_chars_var = IntVar()
special_chars_checkbox = Checkbutton(root, text="Special Characters", variable=special_chars_var, bg='aquamarine', font=('Helvica',20))
special_chars_checkbox.pack()

Password_enter = Entry(root, text='')
Password_enter.pack(pady=20)
Password_enter.config(font=("Times New Roman", 20))

generate_button = Button(root, text="Generate Strong Password", command=generate_password, bg='light pink')
generate_button.pack(pady=10)

copy_button = Button(root, text="Copy to Clipboard", command=clip, bg='light pink')
copy_button.pack(pady=10)

root.mainloop()