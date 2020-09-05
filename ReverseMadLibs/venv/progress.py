from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('Progress Bar Demo')
root.geometry("600x400")


def step():
    my_progress.start(10)


def stop():
    my_progress.stop()


my_progress = ttk.Progressbar(root, orient=HORIZONTAL,
                              length=300, mode='determinate')

step_button = Button(root, text="Progress", command=step)
step_button.pack(pady=20)

stop_button = Button(root, text="Progress", command=stop)
stop_button.pack(pady=20)

root.mainloop()
