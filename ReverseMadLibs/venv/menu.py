from tkinter import *
from tkinter.filedialog import askopenfilename


def NewFile():
    print("New File!")


def OpenFile():
    name = askopenfilename()
    print(name)


def About():
    print("This is a simple example of a menu")

# set up main window
root = Tk()
menu = Menu(root)
root.config(menu=menu)
root.title('Reverse Mad Libs')
root.iconbitmap('William_Shakespeare.ico')
root.geometry("800x500")
root['background']='#808080'

#Set up the menu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

# set up orginal story frame
originalframe = LabelFrame(root, text="Original Story")
originalframe.pack(fill="both", expand="yes")

left = Label(originalframe, text="Inside the originalframe")
left.pack()

left.pack(fill=BOTH, expand=True)

getButton = Button(originalframe, text="Get a Story")
getButton.pack(side=LEFT)
genButton = Button(originalframe, text="Generate")
genButton.pack(side=LEFT, padx=5, pady=5)

# set up mad lib story frame
madlibsframe = LabelFrame(root, text="Madlibs Story")
madlibsframe.pack(fill="both", expand="yes")

left = Label(madlibsframe, text="Inside the madlibsframe")
left.pack()

left.pack(fill=BOTH, expand=True)

closeButton = Button(root, text="Close", command=root.quit)

closeButton.pack(side=RIGHT, padx=5, pady=5)
# okButton = Button(root, text="OK")
# okButton.pack(side=RIGHT)

mainloop()