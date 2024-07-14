from tkinter import *
from playsound import playsound

main = Tk()
main.title('Sound test')
main.iconbitmap('Images/icon/cha0scharly.ico')
main.geometry("400x400")
main.configure(bg='black')
main.resizable(False, False)
main.attributes('-topmost', True)

def play_sound():
    playsound('assets/satisfactory/additional_pylons.mp3')

Button = Button(main, text="Play Sound", command=play_sound)
Button.pack(pady=20)

main.mainloop()

# Works now not sure why it does not work in the other file will go investigate