from tkinter import *

class View():
    # A view can only contain and show elements
    def __init__(self, body):
        self.top = Frame(body)
        self.bottom = Frame(body)
        self.top.pack()
        self.bottom.pack()

class Screen():
    # A screen can only show and update results
    def __init__(self, frame):
        self._result= StringVar()
        self._screen = Entry(frame, width=26, background='black',fg='green', justify='right', textvariable=self._result)
        self._screen.pack(ipady=5)

class Btn():
    # A Btn can only creates itself, and send its text values to other objects 
    def __init__(self, frame, screen, char, pos_row, pos_col):
        def __action(char_pressed):
            if screen._result.get() == 'Math error!':
                screen._result.set('')
            if char_pressed == '=':
               Calculator().solve(screen)
            elif char_pressed == '<<':
                screen._result.set(screen._result.get()[:-1])
            elif char_pressed == 'clear':
                screen._result.set('')
            else:
                screen._result.set(screen._result.get() + char_pressed)
        self._btn = Button(frame, text=char, pady=2, padx=2, width=4, height=2, command=lambda:__action(char))
        self._btn.grid(row=pos_row, column=pos_col)

class Create_Btns():
    # A Create_Btns can only create btns 
    def __init__(self):
        self._chars = ['7','8','9','*','4','5','6','/','1','2','3','-','0','.','=','+','clear','<<']
        self._pos_row=0
        self._pos_col=1
    def create(self, frame_to, screen_to):
        for i in self._chars:
            if self._chars.index(i) % 4 == 0:
                self._pos_row+=1
                self._pos_col=1
            self._pos_col+=1
            Btn(frame_to, screen_to, i, self._pos_row, self._pos_col)

class Calculator():
    # A calculator can only solve math operations
    def _solve(self, operation):
        try:
            solved = eval(operation._result.get())
            operation._result.set(solved)
        except:
            operation._result.set('Math error!')
