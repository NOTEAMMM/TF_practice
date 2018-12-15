import pyautogui as pag
import numpy as np
import tkinter as tk
from  tkinter import messagebox
import time

COUNT = 0
class Gobang(tk.Tk,object):
    def __init__(self):
        super(Gobang,self).__init__()
        self.GridSize = 30
        self.ChessSize = 12
        self.Units_num = 18
        self.title('Gobang')
        self.geometry('{0}x{1}'.format(self.Units_num*self.GridSize+10,self.Units_num*self.GridSize+10))
        self.resizable(width=False,height=False)
        self._build_Gobang()
        self.BlackTurn = True
        self.chess_state_black = []
        self.chess_state_white = []
        self.WIN = False
    def _build_Gobang(self):
        self.canvas = tk.Canvas(self, bg = 'Bisque', height = self.Units_num*self.GridSize+10,
                                width = self.Units_num*self.GridSize+10)

        for c in range(5, (self.Units_num+1)*self.GridSize+5,self.GridSize):
            x0,y0,x1,y1 = c,5,c,self.Units_num*self.GridSize+5
            self.canvas.create_line(x0,y0,x1,y1)

        for c in range(5, (self.Units_num+1)*self.GridSize+5,self.GridSize):
            x0,y0,x1,y1 = 5,c,self.Units_num*self.GridSize+5,c
            self.canvas.create_line(x0,y0,x1,y1)

        self.canvas.bind(sequence='<Button-1>', func=self.add_chess)
        self.canvas.pack()
    def change_turn(self):
        if self.BlackTurn == True:
            self.BlackTurn = False
        else:
            self.BlackTurn = True
        return self.BlackTurn
    def add_chess(self,me):
        chess_x_position = (me.x+10)//self.GridSize
        chess_y_position = (me.y+10)//self.GridSize
        black = 1 if self.BlackTurn==1 else 0
        if [chess_x_position,chess_y_position] in self.chess_state_black+self.chess_state_white:
            pass
        else:
            self.store_chess(chess_x_position, chess_y_position, black)
            self.draw_chess()

            self.row_check()
            self.column_check()
            if self.WIN == True:
                if tk.messagebox.askyesno('WIN','WINNER!\nyes to quit,no to again?'):
                    exit(0)
                else:
                    self.canvas.destroy()
                    self.reset()
            self.change_turn()
    def draw_chess(self):
        wmouse_x = [x[0] for x in (self.chess_state_white)]
        wmouse_y = [x[1] for x in (self.chess_state_white)]
        bmouse_x = [x[0] for x in (self.chess_state_black)]
        bmouse_y = [x[1] for x in (self.chess_state_black)]
        for x,y in zip(bmouse_x,bmouse_y):
            self.canvas.create_oval(x*self.GridSize-7,y*self.GridSize-7,
                                    x*self.GridSize+17,y*self.GridSize+17,fill='black')
        for x,y in zip(wmouse_x,wmouse_y):
            self.canvas.create_oval(x*self.GridSize-7,y*self.GridSize-7,
                                    x*self.GridSize+17,y*self.GridSize+17,fill='white')
    def row_check(self,):
        BLACKFIVE = 0
        WHITEFIVE = 0
        for y in range(1,self.Units_num+1):
            for x in range(1,self.Units_num+1):
                if [x, y] in self.chess_state_black:
                    BLACKFIVE += 1
                else:
                    BLACKFIVE = 0
                if [x, y] in self.chess_state_white:
                    WHITEFIVE += 1
                else:
                    WHITEFIVE = 0

                if WHITEFIVE == 5:
                    self.WIN = True
                if BLACKFIVE == 5:
                    self.WIN = True
            BLACKFIVE = 0
            WHITEFIVE = 0
    def reset(self):
        self._build_Gobang()
        self.BlackTurn = True
        self.chess_state_black = []
        self.chess_state_white = []
        self.draw_chess()
        self.WIN = False
    def column_check(self):
        BLACKFIVE = 0
        WHITEFIVE = 0
        for x in range(1, self.Units_num+1):
            for y in range(1, self.Units_num+1):
                if [x, y] in self.chess_state_black:
                    BLACKFIVE += 1
                else:
                    BLACKFIVE = 0
                if [x, y] in self.chess_state_white:
                    WHITEFIVE += 1
                else:
                    WHITEFIVE = 0

                if WHITEFIVE == 5:
                    self.WIN = True
                if BLACKFIVE == 5:
                    self.WIN = True
            BLACKFIVE = 0
            WHITEFIVE = 0
    def store_chess(self,x,y,black):
        if black == 1:
            self.chess_state_black.append([x,y])
        else:
            self.chess_state_white.append([x,y])

GOBANG = Gobang()
GOBANG.mainloop()
