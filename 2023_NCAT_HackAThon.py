from tkinter import*
import tkinter as tk
from tkinter import Button,Label


def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()

def fridge_one_screen():
    clear_frame()
    button_1 = Button(window, text="Fridge Menu", command=lambda: screen_three())
    button_1.grid(row=350, column=3, pady=10)

    #Change temp button
    button_1 = Button(window, text="Change Temperature", command=lambda: screen_three())
    button_1.grid(row=300, column=3, pady=10)

    # Temperature Label
    label_1 = Label(window, text="Temperature", font=40)
    label_1.grid(row=0, column=0, pady=10)

    # Door status
    label_2 = Label(window, text="Location : ", font=40)
    label_2.grid(row=0, column=50, pady=10)

    # Fridge Location
    label_3 = Label(window, text="Door Status : ", font=40)
    label_3.grid(row=25, column=0, pady=10)

    # Fridge Contents
    label_3 = Label(window, text="Fridge Inventory : ", font=40)
    label_3.grid(row=100, column=0, pady=10)
def screen_three():
    clear_frame()
    label_1 = Label(window, text="Select a fridge : ", font=40)
    label_1.grid(row=0, column=0, pady=10)
    def on_enter(e):
        mybutton['background'] = "#ffcc66"
        mybutton['foreground'] = '#141414'

    def on_leave(e):
        mybutton['background'] = '#141414'
        mybutton['foreground'] = "#ffcc66"

    #First Fridge Button
    mybutton = Button(window, width=42, height=2, text="Fridge 1", fg="#ffcc66",
                          bg='#141414', border=0, activeforeground='#141414', activebackground="#ffcc66", command= lambda : fridge_one_screen(), )

    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)

    mybutton.place(x=200, y=0)

    #Second Fridge Button
    mybutton2 = Button(window, width=42, height=2, text="Fridge 2", fg="#ffcc66",
                      bg='#141414', border=0, activeforeground='#141414', activebackground="#ffcc66", command=None, )

    mybutton2.bind("<Enter>", on_enter)
    mybutton2.bind("<Leave>", on_leave)

    mybutton2.place(x=200, y=40)

    # Third Fridge Buttton
    mybutton3 = Button(window, width=42, height=2, text="Fridge 3", fg="#ffcc66",
                      bg='#141414', border=0, activeforeground='#141414', activebackground="#ffcc66", command=None, )

    mybutton3.bind("<Enter>", on_enter)
    mybutton3.bind("<Leave>", on_leave)

    mybutton3.place(x=200, y=80)

    # Fourth Fridge Button
    mybutton4 = Button(window, width=42, height=2, text="Fridge 4", fg="#ffcc66",
                      bg='#141414', border=0, activeforeground='#141414', activebackground="#ffcc66", command=None, )

    mybutton4.bind("<Enter>", on_enter)
    mybutton4.bind("<Leave>", on_leave)

    mybutton4.place(x=200, y=120)



def screen_two():
    clear_frame()
    button_1 = Button(window, text="Go to screen two", command=lambda: screen_three())
    button_1.grid(row=10, column=3, pady=10)
    label_1 = Label(window, text="Enter your password: ", font=40)
    label_1.grid(row=0, column=0, pady=10)
    E1 = Entry(window)
    E1.grid(row=2, column=1)


def screen_one():
    clear_frame()
    button_1 = Button(window, text="Go to screen two", command=lambda: screen_two())
    button_1.grid(row=10, column=3,pady=10)
    label_1 = Label(window, text="Enter your employee username: ", font = 40)
    label_1.grid(row=0, column=0, pady=10)
    E1 = Entry(window)
    E1.grid(row=2, column=1)


window = tk.Tk()
window.title("Test")
window.geometry('300x500')
window.configure(bg="#141414")

screen_one()
window.mainloop()
