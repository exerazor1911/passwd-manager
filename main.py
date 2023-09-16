import tkinter
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    password_list = [random.choice(letters) for letter in range(nr_letters)]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)

    password_list += [random.choice(symbols) for symbol in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list += [random.choice(numbers) for number in range(nr_numbers)]

    random.shuffle(password_list)

    password = ''.join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    input_passwd.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input_website.get()
    email = input_email.get()
    password = input_passwd.get()

    if website == '' or email == '' or password == '':
        messagebox.showerror(title='Oops', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \nPassword:{password} \nIs it ok to save?")
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f'\n{website} | {email} | {password}')
                input_website.delete(0, 'end')
                input_passwd.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = tkinter.Label()
label_website.config(text='Website:')
label_website.grid(column=0, row=1)

label_email = tkinter.Label()
label_email.config(text='Email/Username:')
label_email.grid(column=0, row=2)

label_passwd = tkinter.Label()
label_passwd.config(text='Password:')
label_passwd.grid(column=0, row=3)

input_website = tkinter.Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email = tkinter.Entry(width=35)
input_email.insert(index=0, string='exe_cien@hotmail.com')
input_email.grid(column=1, row=2, columnspan=2)

input_passwd = tkinter.Entry(width=21)
input_passwd.grid(column=1, row=3)

button_add = tkinter.Button(text='Add', width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

button_gen_passwd = tkinter.Button(text='Generate Password', command=generate_password)
button_gen_passwd.grid(column=2, row=3)

window.mainloop()
