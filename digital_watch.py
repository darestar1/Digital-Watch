import time
import tkinter as tk

window = tk.Tk()
window.title("My Watch")

time_1 = ""
tik_tak = tk.Label(window, font=("bold", 200, "bold"), bg="white")
tik_tak.grid()

def watch():
    global time_1
    time_2 = time.strftime("%H:%M:%S")
    if time_1 != time_2:
        time_1 = time_2
        tik_tak.config(text=time_2)
    window.after(1000, watch)  # every 1000 milliseconds (1 second)

watch()
window.mainloop()
