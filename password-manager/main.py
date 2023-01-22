from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")  # extract from file system
canvas.create_image(100, 100, image=logo)
canvas.pack()

window.mainloop()
