import random
import os
import pygame


def récupérer_combinaison_aléatoire():
    couleurs = ["rouge", "vert", "bleu", "jaune", "orange", "rose"]
    combinaison = []
    for i in range(4):
        combinaison.append(random.choice(couleurs))
    return combinaison
largeur_fenetre = 700
hauteur_fenetre = 800

def souris_est_dans_zone(souris, zone):
    x, y, largeur, hauteur = zone
    return x < souris[0] < x + largeur and y < souris[1] < y + hauteur

def afficher_texte(fenetre, x, y, texte, taille, couleur=(0, 0, 0), font="freesansbold.ttf"):
    font = pygame.font.Font(font, taille)
    texte = font.render(texte, True, couleur)
    text_rect = texte.get_rect(center=(x, y))
    fenetre.blit(texte, text_rect)

dict_couleurs = {
    "rouge": (255, 0, 0),
    "vert": (0, 255, 0),
    "bleu": (0, 0, 255),
    "jaune": (255, 255, 0),
    "noir": (0, 0, 0),
    "blanc": (255, 255, 255),
    "gris": (128, 128, 128),
    "gris clair": (200, 200, 200),
    "marron": (139, 69, 19),
    "rose": (255, 105, 180),
    "violet": (128, 0, 128),
    "cyan": (0, 255, 255),
    "orange": (255, 165, 0),
    "bleu marin": (20, 40, 70),
    "bleu boutton": (100, 150, 255)
}
chemin_absolu_dossier = os.path.dirname(os.path.abspath(__file__))