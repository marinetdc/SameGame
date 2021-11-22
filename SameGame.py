from random import *
import pickle
from collections import Counter

class Noyau(object):

    def __init__(self, height=5, width=10, nb_colors=3):
        """création de 6 champs"""
        self.height = height  # hauteur du plateau
        self.width = width  # largeur du plateau
        self.nb_colors = nb_colors  # nbr de couleurs
        self.nb_moves = 0  # nbr de coups joués
        self.score = 0  # calculé avec pickler
        self.int_score = 0
        self.mat = [[0 for i in range(self.width)] for j in range(self.height)]  # création d'une matrice de zéro

    def init_grid(self):
        """ on remplis au hasard les cases de la matrice avec les couleurs"""
        """(ici les couleurs sont représentées par des chiffres"""
        for i in range(self.height):
            for j in range(self.width):
                self.mat[i][j] = randint(1, self.nb_colors)



    def aux_actu(self, x, y):
        """Méthode récursive:
        Action sur la grille:
        - remplace par un zéro les cases de la même couleur que celle choisie au départ
        - rajoute +1 au score"""
        c = self.mat[y][x]  # on stocke la couleur initiale
        self.mat[y][x] = 0  # on la remplace par zéro dans la grille (pour éviter une boucle infinie sur les voisins)
        t = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # on crée la liste (droite, gauche, haut, bas)
        for i in t:  # on parcourt la liste
            if y + i[0] >= 0 and y + i[0] < self.height and x + i[1] >= 0 and \
                    x + i[1] < self.width and self.mat[y + i[0]][x + i[1]] != 0 and \
                    self.mat[y + i[0]][x + i[
                        1]] == c:  # on vérifie de ne pas sortir de la grille et que le voisin soit de la même couleur
                self.aux_actu(x + i[1], y + i[0])# on rappelle la méthode sur un autre
                self.int_score += 1
        
        
    def actu_grid(self, x, y):
        """Actualisation de la grille:
        - fait appel à aux_actu sur la case choisie et ses voisins de même couleur
        - rajoute +1 au nombre de coups joués"""
        self.int_score = 0
        t = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # on crée une liste des positions voisines
        for i in t:  # on parcourt la liste (droite, gauche, haut, bas)
            if y + i[0] >= 0 and y + i[0] < self.height and x + i[1] >= 0 and \
                    x + i[1] < self.width and self.mat[y][x] != 0 and \
                    self.mat[y][x] == self.mat[y + i[0]][
                x + i[1]]:  # on vérifie de ne pas sortir de la grille et qu'un moins un voisin est de la même couleur
                self.nb_moves += 1
                self.int_score += 1
                self.aux_actu(x, y)  # on fait appel à aux_actu
        self.score += self.int_score*self.int_score
                
        

            
    def lower_aux(self, x, y):
        """Renvoie à lower la couleur présente au-dessus du zéro"""
        if y < 0: return 0
        if self.mat[y][x] == 0: return self.lower_aux(x, y - 1)
        c_tmp = self.mat[y][x]
        self.mat[y][x] = 0
        return c_tmp

    def lower(self):
        """Action sur la grille:
        - regarde tous les zéros de la grille
        - remplace le zéro par la couleur du dessus renvoyée par lower_aux"""

        for y in range(self.height - 1, -1, -1):  # on parcout de bas en haut et de gauche à droite la grille
            for x in range(self.width):
                if self.mat[y][x] == 0:
                    self.mat[y][x] = self.lower_aux(x, y)


    def left_aux(self, x, y):
        if x >= self.width: return -1  # on vérifie qu'on reste dns la grille
        if self.mat[y][x] == 0: return self.left_aux(x + 1,
                                                     y)  # on parcourt le bas des colonnes jusqu'à tomber sur une couleur
        return x  # donne l'indice de la première colonne sans zéro en bas

    def left(self):
        """Action sur la grille:
        - si il existe une colonne de zéro, la méthode décale sur cette colonne tout le bloc de couleur à droite"""

        for x in range(self.width):  # on parcourt les colonnes
            if self.mat[self.height - 1][
                x] == 0:  # si la grille possède un zéro sur la ligne du bas (donc une colonne de zéro après lower)
                ind = self.left_aux(x, self.height - 1)  # on appelle left_aux et on stocke sa valeur dans ind
                if ind != -1:  # on vérifie qu'on est toujours dans la grille
                    for y in range(self.height):  # on parcourt la colonne qui possède un zéro en bas
                        self.mat[y][x] = self.mat[y][
                            ind]  # on remplace toutes les valeurs de la colonne de zéro par celles de la colonne de droite
                        self.mat[y][ind] = 0  # la colonne de droite est remplie de zéros

    def game_play_noyau(self, x, y):
        """ Fait les étapes d'actualisation de la grille dans l'ordre"""
        if x < 0 or x >= self.width or y < 0 or y >= self.height: return False
        self.actu_grid(x, y)
        self.lower()
        self.left()
        return True

    def has_win(self):
        """ Vérifie que la grille est remplie de zéro"""
        for y in range(self.height):
            for x in range(self.width):
                if self.mat[y][x] != 0:
                    return False
        return True

    def has_lost(self) :
        if self.has_win() : return False
        for y in range(self.height):
            for x in range(self.width) :
                t = [(1,0),(-1,0),(0,1),(0,-1)]
                for i in t :
                    if y + i[0] >= 0 and y + i[0] < self.height and x + i[1] >= 0 and \
                            x + i[1] < self.width and self.mat[y][x] != 0 and \
                            self.mat[y][x] == self.mat[y + i[0]][x + i[1]]:
                        return False
        return True

def give_number(s) :
    booler = False
    while not booler :
        try :
            n=int(input( f"Entrez {s} :"))
        except ValueError :
            print("Entrez un nombre")
        else :
            booler = True
    return n 
# ---------------------------------------------------------------------------------------


class Score(object):

##    def add_score(score):
##        ligne = []
##        with open ("scores", "r") as f: 
##            for i in f :
##                ligne.append(f.readline)
##        print(ligne)
##        l_net = [ s.strip ("\n\r") for s in l ]
##        for i in l_net :
##            if self.score > i :
##                del l_net[-1]
##                l_net.append(self.score)
##        l_net.sort()
##        fichier = open ("scores","w")                                                 #ouvre un fichier
##        fichier.write(str(l_net))
##        fichier.close()

##    def score(self, score):
##
##        with open ("scores", "r") as f: 
##            l = f.readlines ()
##        l_net = [ s.strip ("\n\r") for s in l ]
##        for i in l_net :
##            if self.score > i :
##                del l_net[-1]
##                l_net.append(self.score)
##        l_net.sort()
##        fichier = open ("scores","w")                                                 #ouvre un fichier
##        fichier.write(str(l_net))
##        fichier.close()   
##        

        
    def readscore(cls):
        f = open("scores", "rb")
        unpickler = pickle.Unpickler(f)
        s = unpickler.load()
        f.close()
        return s

    def add_score(cls, name, score):
        try:
            s = Score.readscore()
        except FileNotFoundError:
            s = []
        s.append((name, score))
        s.sort(key=lambda x: x[1], reverse=True)
        if len(s) == 11: del s[10]
        f = open("scores", "wb")
        pickler = pickle.Pickler(f)
        pickler.dump(s)
        f.close()

    readscore = classmethod(readscore)
    add_score = classmethod(add_score)


