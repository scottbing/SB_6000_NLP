""" OOP Madlib
    Mad Lib using TK
"""


import tkinter as Tkinter


class App:
    def __init__(self, master):
        self.frame = Tkinter.Frame(master)
        self.frame.grid()

        self.lblColor = Tkinter.Label(self.frame, text="Color")
        self.lblColor.grid(row=1, column=0)
        self.txtColor = Tkinter.Entry(self.frame)
        self.txtColor.grid(row=1, column=1)

        self.lblInstrument = Tkinter.Label(self.frame, text="Instrument")
        self.lblInstrument.grid(row=2, column=0)
        self.txtInstrument = Tkinter.Entry(self.frame)
        self.txtInstrument.grid(row=2, column=1)

        self.lblAnim1 = Tkinter.Label(self.frame, text="Animal")
        self.lblAnim1.grid(row=3, column=0)
        self.txtAnim1 = Tkinter.Entry(self.frame)
        self.txtAnim1.grid(row=3, column=1)

        self.lblAnim2 = Tkinter.Label(self.frame, text="Another Animal")
        self.lblAnim2.grid(row=4, column=0)
        self.txtAnim2 = Tkinter.Entry(self.frame)
        self.txtAnim2.grid(row=4, column=1)

        self.lblPlace = Tkinter.Label(self.frame, text="Place")
        self.lblPlace.grid(row=5, column=0)
        self.txtPlace = Tkinter.Entry(self.frame)
        self.txtPlace.grid(row=5, column=1)

        self.lblVegetable = Tkinter.Label(self.frame, text="Vegetable")
        self.lblVegetable.grid(row=6, column=0)
        self.txtVegetable = Tkinter.Entry(self.frame)
        self.txtVegetable.grid(row=6, column=1)

        self.btnStory = Tkinter.Button(self.frame,
                                       text="make story",
                                       command=self.makeStory)
        self.btnStory.grid(row=7, column=0, columnspan=2)

        self.lblOutput = Tkinter.Label(self.frame)
        self.lblOutput.grid(row=8, columnspan=2)

    def makeStory(self):
        color = self.txtColor.get()
        instrument = self.txtInstrument.get()
        anim1 = self.txtAnim1.get()
        anim2 = self.txtAnim2.get()
        place = self.txtPlace.get()
        vegetable = self.txtVegetable.get()

        story = """
        Little boy %(color)s, come blow your %(instrument)s.
        The %(anim1)s's in the %(place)s, 
        the %(anim2)s's in the %(vegetable)s
        """ % vars()

        self.lblOutput["text"] = story


root = Tkinter.Tk()
root.title("Mad Lib")
app = App(root)
root.mainloop()