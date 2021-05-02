from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

# initialize tkinter
root = Tk()
app = Window(root)
b1 = Button(root, text ="OK")

# set window title
root.wm_title("Tkinter window")

# show window
b1.pack()
root.mainloop()