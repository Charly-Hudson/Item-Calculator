from tkinter import *
import subprocess

splash = Tk()
splash.title("Splash Screen")
splash.geometry("500x500")
splash.geometry("+700+240")
splash.configure(bg="black")
splash.resizable(0,0)
splash.iconbitmap("Images/main/main_images/cha0scharly.png")
splash.attributes("-topmost", True)
splash.overrideredirect(True)
splash.call('wm', 'iconphoto', splash._w, PhotoImage(file="Images/main/main_images/cha0scharly.png"))

def open_main_window():
    splash.destroy()
    subprocess.Popen(["python", "main.py"])

loading = Label(splash, text="Loading...", font=("Arial", 20), bg="black", fg="white")
loading.pack(pady=20)

loading_progress_bar = Label(splash, text="0%", font=("Arial", 10), bg="black", fg="white")
loading_progress_bar.pack(pady=10)

# Load the image
charly = PhotoImage(file="Images/main/main_images/cha0scharly.png")
# Create a label to display the image
splash_image = Label(splash, image=charly)
splash_image.pack(pady=20)
splash_image.configure(bg="black")  

def checks(i):
    if i < 50:
        subprocess.run(["pip", "install", "tk"])
        subprocess.run(["pip", "install", "pillow"])
        subprocess.run(["pip", "install", "pyperclip"])
        subprocess.run(["pip", "install", "filedialog"])
        subprocess.run(["pip", "install", "messagebox"])
        i = 100

for i in range(100):
    loading_progress_bar.config(text=f"{i}%")
    splash.update()
    checks
    splash.after(50)
    if i == 10:
        subprocess.run(["pip", "install", "tk"])
        subprocess.run(["pip", "install", "--upgrade", "tk"])
    elif i == 20:
        subprocess.run(["pip", "install", "pillow"])
        subprocess.run(["pip", "install", "--upgrade", "pillow"])
    elif i == 40:
        subprocess.run(["pip", "install", "pyperclip"])
        subprocess.run(["pip", "install", "--upgrade", "pyperclip"])
    elif i == 60:
        subprocess.run(["pip", "install", "tkfilebrowser"])
        subprocess.run(["pip", "install", "--upgrade", "tkfilebrowser"])
    elif i == 80:
        subprocess.run(["pip", "install", "--upgrade", "messagebox"])
        subprocess.run(["pip", "install", "messagebox"])
    else:
        if i == 99:
            open_main_window()
    
splash.mainloop()