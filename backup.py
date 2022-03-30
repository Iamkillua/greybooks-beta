from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import os
import sys
import random
import webbrowser



def callback(url):
    webbrowser.open_new(url)
    link1 = Label(root, text="Visit-thegreybooks.herokuapp.com ", fg="purple", cursor="hand2", font='Garamond 15')
    link1.grid(row=4, column=0, padx=15, pady=40)
    link1.bind("<Button-1>", lambda e: callback("https://thegreybooks.herokuapp.com"))

# function to deal with id and password
def login_control(id,password):
    if  password == 'GHAtkt777':
        login = Button(frame1, text="Login", state=DISABLED,padx=15, borderwidth=5, cursor='hand2', command=lambda: login_control(off_entryuser.get(), off_entrypass.get()))
        login.grid(row=2, column=1, pady=18)
        text = open('C:/Grey_book_beta/lprk/ugrk/dont touch this.txt', 'w')
        text.write(id)
        text.close()

        g = open('C:/Grey_book_beta/lprk/ugrk/variable_thk.txt', 'r')
        k = g.read()
        if k != '1':
            os.system('C:/Grey_book_beta/support/gots/2nd_page_beta.py')
        else:
            os.system('C:/Grey_book_beta/support/gots/page_3.py')

    else:
        messagebox.showerror('Login Info', 'Password dose not match with username')


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def about():
    messagebox.showinfo('About us', 'Grey Books is a result of bunch of college students getting together trying to find a solution to a very common problem that even they face, and actually learn some skills. It is a platform by the students for the students which aims to provide handwritten notes, books, PDFs and everything in between. This is a pilot project and we are still learning. Hoping for a positive response from you guys.')

def ver():
    messagebox.showinfo('Version Info', 'Currently You are using V-0.1.0-Beta')

# defining frame
root = Tk()
root.iconbitmap('grey book icon2.ico')
root.title('Grey Book')
root.geometry('700x500')

# added a head image
head_image = ImageTk.PhotoImage(Image.open('label final.png'))
head_label = Label(image=head_image, relief=SUNKEN)
head_label.grid(row=0, column=0, columnspan=8, pady=5, padx=3)

# adding a menubar
menubar = Menu(root)

helpmenu = Menu(menubar, tearoff=0, activebackground='light blue', activeforeground='black')
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about)
helpmenu.add_command(label="Version Info", command=ver)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

# frame
frame1 = LabelFrame(root, text='Offline Login', padx=10, pady=10, font='Helvetica 15')
frame1.grid(row=2, column=0, padx=10, pady=30)

# adding login mode(offline)
# adding labels
off_user = Label(frame1, text='User Name', borderwidth=2, font='Helvetica 10', border='5', anchor=W)
off_user.grid(row=0, column=0)

off_password = Label(frame1, text='Password', borderwidth=2, font='Helvetica 10', border='5', anchor=W)
off_password.grid(row=1, column=0)

# adding entrybox(offline)
off_entryuser = Entry(frame1, width=20, borderwidth=1)
off_entryuser.grid(row=0, column=1)

off_entrypass = Entry(frame1, width=20, borderwidth=1,show='*')
off_entrypass.grid(row=1, column=1)


# adding login button
login = Button(frame1, text="Login", padx=15, borderwidth=5, cursor='hand2', command=lambda: login_control(off_entryuser.get(), off_entrypass.get()))
login.grid(row=2, column=1, pady=18)

# Exit button
Exit = Button(root, text='Exit', borderwidth=5, padx=20, command=sys.exit)
Exit.grid(row=5, column=7)

# adding quotes
quote = [
    'Either you run the day or the day runs you.',
    'Start where you are. Use what you have. Do what you can.',
    'If you think education is expensive, try ignorance.',
    'The only person who is educated is the one who has learned how to learn …and change.',
    'Education is a progressive discovery of our own ignorance.',
    'Do not let what you cannot do interfere with what you can do.',
    'Education is what remains after one has forgotten what one has learned in school. ',
    'Live as if you were to die tomorrow. Learn as if you were to live forever.'
]

ra = random.randint(0, 7)
quotelabel = Label(root, text='\"'+quote[ra]+'\"', wraplength=285, font='Garamond 24')
quotelabel.grid(row=2, column=5)

# website link
link1 = Label(root, text="Visit-thegreybooks.herokuapp.com ", fg="blue", cursor="hand2", font='Garamond 15')
link1.grid(row=4, column=0, padx=15, pady=40)
link1.bind("<Button-1>", lambda e: callback("https://thegreybooks.herokuapp.com"))

# version info label
info = Label(root, text="V-0.1.0-Beta", font='Ariel 7')
info.grid(row=5, column=0)

root.mainloop()
