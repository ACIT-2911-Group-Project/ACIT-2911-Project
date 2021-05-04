from tkinter import *
from ui.main_frame import MainFrame

    
if __name__ == "__main__":
    root = Tk()         
    root.title('Movie Reviews')
    root.geometry('800x650')

    MainFrame(root)
    
    root.mainloop()  