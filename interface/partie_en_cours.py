import pygame
pygame.init()

from ..moteur.partie import Partie
from ..utils import largeur_fenetre, hauteur_fenetre, afficher_texte, dict_couleurs, souris_est_dans_zone, \
    chemin_absolu_dossier
from . import menu_pause, boutton

decalage = 50
arriere_plan = pygame.image.load(chemin_absolu_dossier+"assets/images/menu_arrière_plan.jpg")
arriere_plan = pygame.transform.scale(arriere_plan, (largeur_fenetre, hauteur_fenetre))


def dessiner_cases(fenetre, grille_couleurs, grille_progrès, ligne_actuelle, case_selectionnee):

    largeur_case = 80
    hauteur_case = 80
    espacement_horizontal = 5
    espacement_vertical = 20

    x_initial = (largeur_fenetre - (4 * largeur_case + 4 * espacement_horizontal)) // 2
    y_initial = 100

    for ligne in range(6):
        for colonne in range(4):
            x = x_initial + colonne * (largeur_case + espacement_horizontal)
            y = y_initial + ligne * (hauteur_case + espacement_vertical)

            if ligne == ligne_actuelle:
                couleur_interieur = dict_couleurs["blanc"]
            else:
                couleur_interieur = dict_couleurs["gris clair"]

            pygame.draw.rect(fenetre, couleur_interieur, (x, y, largeur_case, hauteur_case))

            epaisseur_bordure = 6 if (ligne == ligne_actuelle and colonne == case_selectionnee) else 5
            couleur_bordure = dict_couleurs["bleu marin"] if (ligne == ligne_actuelle and colonne == case_selectionnee) else dict_couleurs["gris"]

            pygame.draw.rect(fenetre, couleur_bordure, (x, y, largeur_case, hauteur_case), epaisseur_bordure)

            if grille_couleurs[ligne][colonne] != "":
                pygame.draw.circle(fenetre, dict_couleurs[grille_couleurs[ligne][colonne]], (x + largeur_case // 2, y + hauteur_case // 2), 30)
        corrects = grille_progrès[ligne].count(2)
        presque_corrects = grille_progrès[ligne].count(1)
        for i in range(corrects):
            pygame.draw.circle(fenetre, dict_couleurs["vert"], (x + largeur_case + decalage + i * 30, y + hauteur_case // 2), 10)
        for j in range(presque_corrects):
            pygame.draw.circle(fenetre, dict_couleurs["jaune"], (x + largeur_case + decalage + (corrects+j) * 30, y + hauteur_case // 2), 10)
    grille_coordonnées_cases = []
    for ligne in range(6):
        ligne_coordonnées_cases = []
        for colonne in range(4):
            x = x_initial + colonne * (largeur_case + espacement_horizontal)
            y = y_initial + ligne * (hauteur_case + espacement_vertical)
            ligne_coordonnées_cases.append((x, y, largeur_case, hauteur_case))
        grille_coordonnées_cases.append(ligne_coordonnées_cases)

    return grille_coordonnées_cases


def main():
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Mastermind")
    horloge = pygame.time.Clock()
    partie = Partie()

    ligne_actuelle = 0
    case_selectionnee = None
    grille_couleurs = [["" for _ in range(4)] for _ in range(6)]
    grille_progrès = [[0 for _ in range(4)] for _ in range(6)]
    est_victoire = False
    est_perdu = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if menu_pause.main():
                        return
                    else:
                        fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

                if case_selectionnee is not None and not est_victoire and not est_perdu:
                    if event.key == pygame.K_RETURN:
                        toutes_cases_remplies = True
                        for colonne in range(4):
                            if grille_couleurs[ligne_actuelle][colonne] == "":
                                toutes_cases_remplies = False
                                break
                        if toutes_cases_remplies:
                            couleurs_choisies = grille_couleurs[ligne_actuelle]
                            if partie.tester_combinaison(couleurs_choisies):
                                est_victoire = True
                                for colonne in range(4):
                                    grille_progrès[ligne_actuelle][colonne] = 2
                            else:
                                for colonne in range(4):
                                    grille_progrès[ligne_actuelle][colonne] = partie.progrès[colonne]

                                ligne_actuelle += 1
                                case_selectionnee = None

                                if ligne_actuelle >= 6:
                                    est_perdu = True

                    elif event.key == pygame.K_BACKSPACE:
                        grille_couleurs[ligne_actuelle][case_selectionnee] = ""

                    elif event.unicode.isnumeric():
                        nombre = int(event.unicode)
                        if 0 < nombre < 7:
                            if nombre == 1:
                                grille_couleurs[ligne_actuelle][case_selectionnee] = "rouge"
                            elif nombre == 2:
                                grille_couleurs[ligne_actuelle][case_selectionnee] = "vert"
                            elif nombre == 3:
                                grille_couleurs[ligne_actuelle][case_selectionnee] = "bleu"
                            elif nombre == 4:
                                grille_couleurs[ligne_actuelle][case_selectionnee] = "jaune"
                            elif nombre == 5:
                                grille_couleurs[ligne_actuelle][case_selectionnee] = "orange"
                            elif nombre == 6:
                                grille_couleurs[ligne_actuelle][case_selectionnee] = "rose"

            if event.type == pygame.MOUSEBUTTONDOWN and not est_victoire and not est_perdu:
                pos_souris = pygame.mouse.get_pos()
                cases = dessiner_cases(fenetre, grille_couleurs, grille_progrès, ligne_actuelle, case_selectionnee)

                for colonne in range(4):
                    if souris_est_dans_zone(pos_souris, cases[ligne_actuelle][colonne]):
                        case_selectionnee = colonne
                        break
                    else:
                        case_selectionnee = None

        fenetre.blit(arriere_plan, (0, 0))
        afficher_texte(fenetre, largeur_fenetre//2, 50, "Mastermind", 75, couleur=dict_couleurs["bleu marin"])
        dessiner_cases(fenetre, grille_couleurs, grille_progrès, ligne_actuelle, case_selectionnee)

        if est_victoire:
            afficher_texte(fenetre, largeur_fenetre // 2, hauteur_fenetre - 70, "Bravo! Vous avez trouvé le combo!", 36, dict_couleurs["vert"])
        elif est_perdu:
            afficher_texte(fenetre, largeur_fenetre // 2, hauteur_fenetre - 80, f"Dommage! Le combo était:", 36, dict_couleurs["rouge"])
            afficher_texte(fenetre, largeur_fenetre // 2, hauteur_fenetre - 30, " ".join(partie.combinaison), 36, dict_couleurs["rouge"])
        else:
            afficher_texte(fenetre, largeur_fenetre // 2, hauteur_fenetre - 80, "1: rouge | 2: vert | 3: bleu", 36, dict_couleurs["bleu marin"])
            afficher_texte(fenetre, largeur_fenetre // 2, hauteur_fenetre - 30,"4: jaune | 5: orange | 6: rose", 36, dict_couleurs["bleu marin"])

        pygame.display.flip()
        horloge.tick(60)