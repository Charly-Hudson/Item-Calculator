from tkinter import *
import json


main = Tk()
main.title('Testing Stuff')
main.geometry('500x500')
main.configure(bg="blue")

# Menu Frame affixed to West (left) Side 
# row=0 Col=0
menu = LabelFrame(main)
menu.grid(row=0, column=0, columnspan=3, sticky=W)

def fg_def():
    fg="blue"
def bg_def():
    bg="red"

def edit_win():
    edit_win_def = Tk()

    #selector frame
    selector = LabelFrame(edit_win_def)
    selector.grid(row=0, column=0, columnspan=2)

    def standard_colour():
        if standard_var == "PY_VAR0":(main.configure(bg="red"))
        else:
            print("CHARLY NO")
            print(standard_var)

    standard_var = StringVar()
    standard = Checkbutton(selector, text="Standard",variable=standard_var, onvalue="On", offvalue="Off")
    standard.grid(row=0, column=0)


    opt1 = Radiobutton(selector, text="Light Mode")
    opt1.grid(row=0, column=1)
    opt1_var = StringVar

    opt2 = Radiobutton(selector, text="Get oudda here")
    opt2.grid(row=0, column=2)

    #Colour 1 Frame
    colour1 = LabelFrame(edit_win_def)
    colour1.grid(row=1,column=0)

    #Colour 2 Frame
    colour2 = LabelFrame(edit_win_def)
    colour2.grid(row=1,column=1) 

    #Ok button
    buttons = LabelFrame(edit_win_def)
    buttons.grid(row=2, column=0, columnspan=2)

    ok_button = Button(buttons, text="Ok", command=edit_win_def.destroy)
    ok_button.grid(row=0, column=0)

    test_button = Button(buttons, text="Test", command=standard_colour)
    test_button.grid(row=0, column=1)


    edit_win_def.mainloop()


file = Button(menu, text="File")
file.grid(row=0, column=0)
edit = Button(menu, text="Edit", command=edit_win)
edit.grid(row=0, column=1)
exit = Button(menu, text="Exit", command=main.destroy)
exit.grid(row=0, column=2)

main_frame = LabelFrame(main)
main_frame.grid(row=1, column=0)




main.mainloop()