Emma Marqueton 
Marine Troadec 

La class Noyaux : 

Intinie : 
	la hauteur de la grille
	la largeur de la grille 
	le nombre de couleur 
	le nombre de déplacement 
	le score 
	la grille

init_grid : 
	la grille est remplie au hasard avec des chiffres 

aux_grid : 
	regarde les cases adjacentes jusqu'à ne plus trouver de couleur identique à la couleur du premier clic
	les cases de la coeleur du début sont remplacé par 0
	ajout du score pour que case remplacé par 0
	
actu_grid : 
	regarde les cases adjacentes à la case touchée pour comparer la couleur 
	si la couleur est identique à la case touchée appel à aux_grid afin de  parcourir les cases autour de celle ci 
	

lower_aux : 
	Renvoie à lower la couleur présente au-dessus du zéro
	
lower : 
	regarde tous les zéros de la grille
        remplace le zéro par la couleur du dessus renvoyée par lower_aux

left_aux :
	renvoie à left la couleur présente à gauche du zéro

left : 
	si il existe une colonne de zéro, la méthode décale sur cette colonne tout le bloc de couleur à droite

game_play_noyau : 
	fait les étapes d'actualisation de la grille dans l'ordre

has_win : 
	verifie que la grille est remplie de zéro
 
has_lost : 
	verifie que plus aucune possibilité n'existe 



give_number : 
	rend l'interface python jouable 

class Samegame : 

intie : 
	noyaux 
	score 
	hauteur de la grille 
	largeur de la grille 
	nombre de couleur 
	intie dans le noyaux 
	intie la grille dans le noyau

str : 
	affiche la grille du jeu avec les indices des lignes et colonnes sur les cotés 

game_play_on_move : 
	associe x et y à la position de touche 
	lance le jeu dans le noyau 
	verifie que la case soit dans la grille 

play : 
	vérifie si le jeu est gagné ou perdu 
	donne le score 


class SameGameInt :

intie : 
	une fenetre de configuration (hauteur et largeur de la grille, nombre de couleurs)
	une liste de couleur 

on_click : 
	verifie que le click est dans une des cases de la grille 
	recupere l'indice de la case 
	joue dans le noyau
	appel à show pour affiher la nouvelle grille 
	verifie si le jeu est gagné ou perdu et propose une nouvelle partie en appelant reset

reset : 
	efface toutes les fenetres precedement ouvertes 
	propose une nouvelle configurationd de jeu  

show : 
	associe l'indice de la couleur avec l'indice de la matrice de jeu du noyau 
	met à jour la grille 	

start : 
	intie la grille
	utilise la matrice du noyau pour placer les couleurs 
	affiche le score à 0 
	
