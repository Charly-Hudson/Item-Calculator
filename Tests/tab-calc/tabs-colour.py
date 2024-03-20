from tkinter import *
from tkinter import ttk

main = Tk()
main.geometry("502x600")
main.config(bg="#11161d")
# main.overrideredirect(1)

# #move event
# def move(event):
#     x, y = main.winfo_pointerxy()
#     main.geometry(f"+{x}+{y}")

# main.bind('<B1-Motion>',move)

# menu start
menu = ttk.Frame(main)
menu.grid(row=0, column=0, columnspan=5, sticky=W)

exit_btn = ttk.Button(menu, text="Exit", command=main.destroy)
exit_btn.grid(row=0, column=0, sticky=W)

## Style Section

# Notebook Style
style_nb = ttk.Style()
style_nb.theme_use('default')
style_nb.configure('TNotebook.Tab', background="#11161d", foreground="#b5dfff")  # Set background color for all tabs
style_nb.map('TNotebook.Tab', background=[('selected', '#11161d')], foreground=[('selected', '#b5dfff')])  # Set background and foreground color for the selected tab

# Frame Style
style_frame = ttk.Style()
style_frame.theme_use('default')
style_frame.configure("TFrame", background="#11161d", foreground="#b5dfff")

# Button Style

style_button = ttk.Style()
style_button.theme_use('default')
style_button.configure('TButton', background="#11161d", foreground="#b5dfff")
style_button.map('TButton', background=[('active', '#b5dfff')], foreground=[('active', '#11161d')])

# Menu Style

style_menu = ttk.Style()
style_menu.theme_use('default')
style_menu.configure('Tmenu', background="#11161d", foreground="#b5dfff")
style_menu.map('Tmenu', background=[('active',"#11161d")], foreground=[('active',"#b5dfff")])

# # Entry Style
# style_entry = ttk.Style()
# style_entry.theme_use('default')
# style_entry.configure('TEntry', background="#11161d", foreground="#b5dfff")

# calc functions
    
def math_funct(entry_widget):
    try:
        input_m = entry_widget.get()
        print(float(input_m) * 25)
    except Exception as e:
        print("Error:", e)

main_math = ttk.Notebook(main)
main_math.configure()
main_math.grid(row=1, column=0)

math_frame_1 = ttk.Frame(main_math, width=500, height=500)
math_frame_1.pack(fill="both", expand=1)
main_math.add(math_frame_1, text="assembler")

math_1 = ttk.Entry(math_frame_1)
math_1.pack()

math_1_btt = ttk.Button(math_frame_1, text="Calculate", command=lambda:math_funct(math_1))
math_1_btt.pack()

#test_menu = ttk.OptionMenu()

math_frame_2 = ttk.Frame(main_math, width=500, height=500)
math_frame_2.pack(fill="both", expand=1)
main_math.add(math_frame_2, text="craftor")

math_2 = ttk.Entry(math_frame_2)
math_2.pack()

math_2_btt = ttk.Button(math_frame_2, text="Calculate", command=lambda:math_funct(math_2))
math_2_btt.pack()

math_frame_3 = ttk.Frame(main_math, width=500, height=500)
math_frame_3.pack(fill="both", expand=1)
main_math.add(math_frame_3, text="bang")

math_3 = ttk.Entry(math_frame_3)
math_3.pack()

math_3_btt = ttk.Button(math_frame_3, text="Calculate", command=lambda:math_funct(math_3))
math_3_btt.pack()

math_frame_4 = ttk.Frame(main_math, width=500, height=500)
math_frame_4.pack(fill="both", expand=1)
main_math.add(math_frame_4, text="crash")

math_4 = ttk.Entry(math_frame_4)
math_4.pack()

math_4_btt = ttk.Button(math_frame_4, text="Calculate", command=lambda:math_funct(math_4))
math_4_btt.pack()

math_frame_5 = ttk.Frame(main_math, width=500, height=500)
math_frame_5.pack(fill="both", expand=1)
main_math.add(math_frame_5, text="whollop")

math_5 = ttk.Entry(math_frame_5)
math_5.pack()

math_5_btt = ttk.Button(math_frame_5, text="Calculate", command=lambda:math_funct(math_5))
math_5_btt.pack()



main.mainloop()