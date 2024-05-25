from tkinter import *
import os
import json
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import filedialog
import pyperclip
import subprocess
from tkinter import Toplevel

sat_calc = Tk()
sat_calc.title('Satisfactory Calculator')
sat_calc.iconbitmap('Images/icon/satisfactory_img.ico')
sat_calc.geometry("408x990")
sat_calc.geometry("+0+0")
sat_calc.config(bg="#26363a")

# Set window location

# Menu Frame
sat_menu_frame = Frame(sat_calc, bg="#26363a")
sat_menu_frame.grid(row=0, column=0, columnspan=2, sticky=W)

# Menu Items: 
# Need to switch File and Edit to Option Menus

# Bring back main window
def open_main_window():
    # Destroy the current window
    sat_calc.destroy()

    # Get the path of the Python file
    file_path = "main.py"

    # Run the Python file
    subprocess.run(["python", file_path])



# Save funcation
def sat_save():
    file_path = filedialog.asksaveasfilename(initialdir="Testing_Grounds_PY/Item Calculator/sat_saves", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                text_content = sat_notes.get("1.0", "end-1c")
                file.write(text_content)
            sys_notes.config(text=f"File saved: {file_path}")
        except Exception as e:
            sys_notes.config(text=f"Error saving file: {str(e)}")
# save Button
sat_save_button = Button(sat_menu_frame, text="Save", command=sat_save, bg="#26363a", fg="#e49245", width=5)
sat_save_button.grid(row=0, column=2, pady=5)
# Load

def sat_open():
    notes_import = filedialog.askopenfilename(initialdir="sat_saves", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    notes_import = open(notes_import, 'r')
    sat_import = notes_import.read()
    sat_notes.delete('1.0', END)
    sat_notes.insert(END, sat_import)
    notes_import.close
sat_load_button = Button(sat_menu_frame, text="load", command=sat_open, bg="#26363a", fg="#e49245", width=5)
sat_load_button.grid(row=0, column=3, pady=5)

# Exit Calculator
sat_exit_menu = Button(sat_menu_frame, text="Exit Calc", command=open_main_window, bg="#26363a", fg="#e49245", width=7)
sat_exit_menu.grid(row=0, column=4, pady=5)

# Quit
sat_quit_menu = Button(sat_menu_frame, text="Quit", command=sat_calc.destroy, bg="#26363a", fg="#e49245", width=5)
sat_quit_menu.grid(row=0, column=5, pady=5)

# System Notes
sys_notes = LabelFrame(sat_calc, text="", padx=20, pady=1)
sys_notes.grid(row=1, column=0, columnspan=2)
# Item Calc frame
sat_item_frame = LabelFrame(sat_calc, text="Item Calculator", bg="#26363a", fg="#e49245")
sat_item_frame.grid(row=2, column=0, sticky=N)
#Item Calculator

# Item Calculator Function
def calculate_ingredients():
    try:
        item_name = item_var.get()
        required_amount = float(input_var.get())
        #Build the full path to the Item Data folder
        item_data_folder = os.path.join(os.path.dirname(__file__), "item_data/sat_items")
        with open(os.path.join(item_data_folder, f'{item_name}.json')) as file:
            item_data = json.load(file)
        result = item_data[item_name]["Result"]
        ingredients = item_data[item_name]["Ingredients"]
        required_ingredients = {ingredient: required_amount / result * amount for ingredient, amount in ingredients.items()}
        formatted_output = "\n".join([f"{ingredient}: {amount}" for ingredient, amount in required_ingredients.items()])
        ingredient_output.config(text=formatted_output)
    except (ValueError, FileNotFoundError, KeyError):
        result_label.config(text="Invalid item or input.", fg="#ae1b1c", font="bold")
    else:
        result_label.config(text="Calculation Complete", fg="#00e300", font="bold")
# Load the item names from the item_data directory
item_data_folder = os.path.join(os.path.dirname(__file__), "item_data/sat_items")
item_files = [file.split(".")[0] for file in os.listdir(item_data_folder)]
item_var = StringVar()
item_var.set(item_files[0])
# Item Dropdown
item_label = Label(sat_item_frame, text="Select Item:", fg="#e49245", bg="#26363a", padx=10, pady=1)
item_dropdown = OptionMenu(sat_item_frame, item_var, *item_files)
item_label.pack()
item_dropdown.pack()
item_dropdown.config(fg="#e49245", bg="#26363a", width=21)
item_dropdown["menu"].config(fg="#e49245", bg="#26363a")
# Input for the Required amount/m
input_label = Label(sat_item_frame, text="Enter Required Amount:", fg="#e49245", bg="#26363a", padx=10, pady=1)
input_var = Entry(sat_item_frame, fg="#e49245", bg="#26363a", width=28)
input_label.pack()
input_var.pack()
# Calculate Results Button
calculate_button = Button(sat_item_frame, padx=10, pady=1, text="🔻Calculate Ingredients /m🔻", command=calculate_ingredients, fg="#e49245", bg="#26363a",width=21)
calculate_button.pack()
# Labels for the results
result_label = Label(sat_item_frame, text="", fg="#e49245", bg="#26363a", padx=10, pady=1)
result_label.pack()
ingredient_output = Label(sat_item_frame, text="", fg="#e49245", bg="#26363a", padx=10, pady=1)
ingredient_output.pack()
#Export to notes
def sat_export():
    item_name = item_var.get()
    required_amount = float(input_var.get())
    #Build the full path to the Item Data folder
    item_data_folder = os.path.join(os.path.dirname(__file__), "item_data/sat_items")
    with open(os.path.join(item_data_folder, f'{item_name}.json')) as file:
        item_data = json.load(file)
    result = item_data[item_name]["Result"]
    ingredients = item_data[item_name]["Ingredients"]
    required_ingredients = {ingredient: required_amount / result * amount for ingredient, amount in ingredients.items()}
    formatted_output = "\n".join([f"{ingredient}: {amount}" for ingredient, amount in required_ingredients.items()])
    sat_notes.insert(END, formatted_output)
notes_export = Button(sat_item_frame, text="🔻Export to Notes🔻", command=sat_export, width=21,padx=10, pady=1, bg="#26363a", fg="#e49245")
notes_export.pack()
# Function Buttons
sat_function_buttons = LabelFrame(sat_calc, text="Clear Notes", bg="#26363a", fg="#e49245")
sat_function_buttons.grid(row=3, column=0, sticky=N)
def sat_notes_clear():
    sat_notes.delete('1.0', END)
sat_clear_btn = Button(sat_function_buttons, text="Clear", width=21,padx=10, pady=1, bg="#26363a", fg="#e49245", command=sat_notes_clear)
sat_clear_btn.grid(row=0 , column=0)
# Normal Calculator Frame
sat_calc_frame = LabelFrame(sat_calc, text="Calculator", bg="#26363a", fg="#e49245")
sat_calc_frame.grid(row=2, column=1, rowspan=2, sticky=N)

'''
BREAK
'''
# Standard Calculator
e = Entry(sat_calc_frame, width=30, borderwidth=5, fg="#e49245", bg="#26363a")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Number Functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
# Clear Entry
def button_ce():
    e.delete(0, END)
# Addition Function
def button_plus():
    first_number = e.get()
    global f_num 
    global math 
    math = "plus"
    f_num = int(first_number)
    e.delete(0, END)
# Subtraction Function
def button_minus():
    first_number = e.get()
    global f_num 
    global math 
    math = "minus"
    f_num = int(first_number)
    e.delete(0, END)
# Muntiplcation Function
def button_times():
    first_number = e.get()
    global f_num 
    global math 
    math = "times"
    f_num = int(first_number)
    e.delete(0, END)
#Divition Function
def button_divide():
    first_number = e.get()
    global f_num 
    global math 
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)
# Output Result
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "plus":
        e.insert(0, f_num + int(second_number))
    if math == "minus":
        e.insert(0, f_num - int(second_number))
    if math == "times":
        e.insert(0, f_num * int(second_number))
    if math == "divide":
        e.insert(0, f_num / int(second_number))
# Define layout
button_1 = Button(sat_calc_frame, text="1", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(1))
button_2 = Button(sat_calc_frame, text="2", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(2))
button_3 = Button(sat_calc_frame, text="3", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(3))
button_4 = Button(sat_calc_frame, text="4", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(4))
button_5 = Button(sat_calc_frame, text="5", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(5))
button_6 = Button(sat_calc_frame, text="6", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(6))
button_7 = Button(sat_calc_frame, text="7", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(7))
button_8 = Button(sat_calc_frame, text="8", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(8))
button_9 = Button(sat_calc_frame, text="9", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(9))
button_0 = Button(sat_calc_frame, text="0", padx=20, pady=10, fg="#e49245", bg="#26363a", command=lambda: button_click(0))
button_plus = Button(sat_calc_frame, text="+", padx=17, pady=10, fg="#e49245", bg="#26363a", command= button_plus)
button_equal = Button(sat_calc_frame, text="=", padx=100, pady=10, fg="#e49245", bg="#26363a", command=button_equal)
button_clear = Button(sat_calc_frame, text="Clear", padx=37, pady=10, fg="#e49245", bg="#26363a", command=button_ce)
button_minus = Button(sat_calc_frame, text="-", padx=19, pady=10, fg="#e49245", bg="#26363a", command= button_minus)
button_times = Button(sat_calc_frame, text="*", padx=19, pady=10, fg="#e49245", bg="#26363a", command= button_times)
button_divide = Button(sat_calc_frame, text="/", padx=19, pady=10, fg="#e49245", bg="#26363a", command= button_divide)
# Button Layout
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0,)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=0, columnspan=4)
button_plus.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_times.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
# Notes Frame
sat_notes_frame = LabelFrame(sat_calc, text="Notes", bg="#26363a", fg="#e49245")
sat_notes_frame.grid(row=4, column=0, columnspan=2)
sat_notes = Text(sat_notes_frame, bg="#26363a", fg="#e49245", width=50, height=40)
sat_notes.grid(row=0, column=0, columnspan=2)

def disable_event():
   pass
sat_calc.protocol("WM_DELETE_WINDOW", disable_event)

mainloop()