# ==============================================================================
"""SAME GAME : interface """
# ==============================================================================
__author__  = "Marine Troadec"
__version__ = "1.0"
__date__    = "2019-11-15"
# ==============================================================================
from ezTK import *
from SameGame import Noyau
from random import randint,random 
# ------------------------------------------------------------------------------
class SameGameInt(Win):

    def __init__(self):
        
        Win.__init__(self, title='SamGame', op=5, click = self.on_click)
        # --------------------------------------------------------------------------
        self.config = Frame(self, flow='S', op=0)
        Label(self.config, text='CONFIGURATION', font='Arial 18 bold italic')
        Scale(self.config, scale=(4,15), length=200)
        Label(self.config, text='Number of rows and cols')
        Scale(self.config, scale=(2,8), length=200) 
        Label(self.config, text='Number of colors')
        Button(self.config, text='START GAME', command=self.start)
        # --------------------------------------------------------------------------
        self.colors = ['white','#44F', '#4AF', '#4FF', '#4FA', '#4F4','#AF4', '#FF4', '#FA4' ,'#F44', '#F4A', '#F4F' ,'#A4F'] # combine values and colors
        self.loop()
 # ----------------------------------------------------------------------------
    def on_click(self, widget, code, mods):
        if widget.master != self.grid: pass
        else:
            print(widget.index)
            y = widget.index[0]
            x = widget.index[1]
            self.game.game_play_noyau(x, y)
            for y in range(self.game.height) :
                print(self.game.mat[y])
            self.show()
            if self.game.has_win() :
                self.l = Label(self, text='YOU WIN')
                self. b = Button(self, text='REPLAY', command=self.reset)
            if self.game.has_lost() :
                self.l = Label(self, text='YOU LOST')
                self.b = Button(self, text='REPLAY', command=self.reset)

    def reset(self) :
        self.grid.destroy()
        self.b.destroy()
        self.l.destroy()
        self.score.destroy()
        self.config = Frame(self, flow='S', op=0)
        Label(self.config, text='CONFIGURATION', font='Arial 18 bold italic')
        Scale(self.config, scale=(4,20), length=200)
        Label(self.config, text='Number of rows and cols')
        Scale(self.config, scale=(2,8), length=200) 
        Label(self.config, text='Number of colors')
        Button(self.config, text='START GAME', command=self.start)
        
              

    def show(self) :
        for y in range (self.game.height) :
            for x in range (self.game.width) :
                cell = self.grid[y][x]
                cell['bg'] = self.colors[self.game.mat[y][x]]
        self.score['text'] = "Score = " + str(self.game.score)
        
            
            
    def start(self):
        size, seed = self.config[1].state, self.config[3].state # get slider values
        self.config.destroy() # remove configuration frame
        self.game = Noyau(size,size,seed)
        self.game.init_grid()
        self.grid = Frame(self, fold=size, op=2)
        for y in range(self.game.height) :
                print(self.game.mat[y])
        self.matgrid = []
        for y in range(size):
            self.matgrid.append([])
            for x in range(size) :
                self.matgrid[y].append(Label(self.grid, width=6, height=3, border=1, bg = self.colors[self.game.mat[y][x]]))
        self.score = Label(self, text = 'Score = 0')                               
if __name__ == "__main__" :
  SameGameInt()

# ==============================================================================
