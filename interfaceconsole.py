from random import *
import pickle
from collections import Counter
from SameGame import *

class Samegame(object):
    def __init__(self):
        self.noyau = Noyau()
        self.score = 0
        height = give_number("hauteur")      #rentrer la taille de la grille et le nombre de couleurs 
        width = give_number("largeur")
        nb_colors = give_number("nombre de couleur")
        self.noyau.__init__(height, width, nb_colors)
        self.noyau.init_grid()
        

    def __str__(self):
        """Affiche la grille de jeu avec des numéros pour les cotés """
        r = f"nb_moves : {self.noyau.nb_moves}\n"
        r += f"score : {self.noyau.score}\n"
        r += str([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) + "\n"
        for j, i in enumerate(self.noyau.mat):
            r += str(j)
            r += str(i)
            r += "\n"
        return r

    def game_play_one_move(self):
        """Prend la case à toucher et remove la grille"""
        x = give_number("x à toucher")
        y = give_number("y à toucher")
        if self.noyau.game_play_noyau(x, y) == False:
            print('Choisis une case de la grille!!')
            self.game_play_one_move()
        self.noyau.game_play_noyau(x, y)

    def play(self):
        """permet de jouer """
        
        while True:
            print(self)
            self.game_play_one_move()
            if self.noyau.has_win() == True:#vérifie si la grille est vide donc si c'est gagné                
                print("Bravo")
                Score.add_score(input("Nom : "),self.score)
                print(self.score)
                return self.replay()
            if self.noyau.has_lost() == True:       #regarde si il reste des possibilités pour gagner 
                print("Perdu")
                return self.replay()
               
    def replay(self):
        p = str()
        p = str(input("Voulez-vous rejouer ?"))
        if p == "oui" :
            S = Samegame()
            S.play()
# ---------------------------------------------------------------------------------------
if __name__ == '__main__':
    S = Samegame()
    S.play()
