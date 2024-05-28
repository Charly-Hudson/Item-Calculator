from tkinter import *
import os
import json
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import pyperclip
import subprocess
from tkinter import Toplevel

main_geometry = "543x361"

# Main Window Spec
main = Tk()
main.title('Item Calculators')
main.iconbitmap('Images/icon/cha0scharly.ico')
main.geometry(main_geometry)
main.geometry("+0+0")
main.configure(bg="#11161d")
main.overrideredirect(True)

# Menu Buttons Frame
menu_frame = Frame(main, bg="#11161d")
menu_frame.grid(row=0, column=0, columnspan=2, sticky=W)

# Menu Items
# Need to switch File and Edit to Option Menus
# Go back to Lessons and run the Option Menu Lesson

def file_window(event):
    # Destroy the current window
    main.withdraw()

    file_window = Toplevel()
    file_window.title('File')
    file_window.iconbitmap('Images/icon/cha0scharly.ico')
    file_window.geometry("200x400")

    label = Label(file_window, text="File Menu")
    label.pack()

    def back_funct():
        file_window.destroy()
        main.deiconify()

    back_button = Button(file_window, text="Back", command=back_funct)
    back_button.config(bg="#11161d", fg="#b5dfff", width=7)
    back_button.pack()
    file_window.mainloop()

def edit_window(event):
    # Destroy the current window
    main.withdraw()

    edit_window = Toplevel()
    edit_window.title('Edit')
    edit_window.iconbitmap('Images/icon/cha0scharly.ico')
    edit_window.geometry("200x400")

    label = Label(edit_window, text="Edit Menu")
    label.pack()
    edit_window.mainloop()

def view_window(event):
    # Destroy the current window
    main.withdraw()
    view_window = Toplevel()
    view_window.title('View')
    view_window.iconbitmap('Images/icon/cha0scharly.ico')
    view_window.geometry("200x400")
    label = Label(view_window, text="View Menu")
    label.pack()
    view_window.mainloop()

menu_options = [
    "File",
    "Edit",
    "View",
]

def handler(options_menu):
    if options_menu.get() == "File":
        file_window(None)
    elif options_menu.get() == "Edit":
        edit_window(None)
    else:
        view_window(None)


clicked = StringVar()

#options menu
options_menu = OptionMenu(menu_frame, clicked, *menu_options)
options_menu.config(bg="#11161d", fg="#b5dfff", width=6, text="Options")
options_menu.grid(row=0, column=0, padx=5,)
options_menu.children["menu"].config(bg="#11161d", fg="#b5dfff")

if clicked.get() == "File":
    file_window()   


# Exit
quit_button = Button(menu_frame, text="Exit", command=main.destroy, width=7, bg="#11161d", fg="#b5dfff")
quit_button.grid(row=0, column=1, pady=5)

# Run button Frame for different Calculators
run_button_frame = LabelFrame(main, text="Item Calculators",borderwidth=3, relief="groove", bg="#11161d", fg="#b5dfff", font="bold")
run_button_frame.grid(row=1, column=0, sticky=N) 
# Run button Frame for different Calculators
coming_soon = LabelFrame(main, text="Coming Soon",borderwidth=3, relief="groove", bg="#821e1e", fg="#e49245", font="bold")
coming_soon.grid(row=2, column=0, sticky=N)

# Note Filler Frame
filler_frame = LabelFrame(main, width=100, height=100, text="Patch Notes", borderwidth=3, relief="groove", bg="#11161d", fg="#b5dfff", font="bold")
filler_frame.grid(row=1, column=1,  rowspan=2, sticky=N)
patch_0_0_1_title = Label(filler_frame, text="Patch 0.0.1", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body1 = Label(filler_frame, text="- Creation of main window and second window interface", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body2 = Label(filler_frame, text="- Satisfactory Calculator added with item and normal calculator with notes", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body3 = Label(filler_frame, text="- Implementation of the item and normal calculator not finished yet.", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body4 = Label(filler_frame, text="- Addition of coming soon", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body5 = Label(filler_frame, text="- Factorio, Dyson Sphere, Starfeild, Infinifactory and ??? added", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body6 = Label(filler_frame, text="- Change to colour scheme in the Main Window", bg="#11161d", fg="#b5dfff").pack()
patch_0_0_1_body7 = Label(filler_frame, text="- Change to colour scheme in the Satisfactory Window", bg="#11161d", fg="#b5dfff").pack()


def satisfactory():
    # Open Satisfactory Calculator

    main.destroy()
    subprocess.run(["python", "Satisfactory-Calc.py"])


#Buttons Implemented
# open Satifactory calc and withdraw main window

sat_open = Button(run_button_frame, text="Satisfactory Calculator", width=17, command=satisfactory, bg="#11161d", fg="#b5dfff")
sat_open.grid(row=0, column=0)

# Buttons coming soon
factorio_open = Button(coming_soon, text="Factorio", state=DISABLED, width=17, bg="#11161d", fg="#b5dfff")
factorio_open.grid(row=0, column=0)
dysonSphere_open = Button(coming_soon, text="Dyson Sphere", state=DISABLED, width=17, bg="#11161d", fg="#b5dfff")
dysonSphere_open.grid(row=1, column=0)
question_open = Button(coming_soon, text="???", state=DISABLED, width=17, bg="#11161d", fg="#b5dfff")
question_open.grid(row=4, column=0)

# clickable Images frame for ads? Maybe?
image_frame = Frame(main)
image_frame.grid(row=4, column=0, columnspan=2)

# Image in main window
# Image Define
coming_soon_image = ImageTk.PhotoImage(Image.open("Images/main/main_images/coming_soon.png"))
# Image Label
coming_soon_label = Label(image_frame, image=coming_soon_image,)
coming_soon_label.pack()
coming_soon_label.config(border=FALSE)

def disable_event():
   pass
main.protocol("WM_DELETE_WINDOW", disable_event)
mainloop()