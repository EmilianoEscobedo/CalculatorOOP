from tkinter import *
from calc import *

root = Tk()
root.title('Calculator OOP')
root.geometry('400x400')

view = View(root)
screen = Screen(view.top)
Create_Btns().create(view.bottom, screen)

root.mainloop()
