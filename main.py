# pip install pygame

import pygame
import sys


pygame.init()


BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)


largeur_fenetre = 1440
hauteur_fenetre = 960


fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Ping Pong avec Bot")


largeur_raquette = 10
hauteur_raquette = 100
vitesse_raquette = 5


x_joueur = 20
y_joueur = hauteur_fenetre // 2 - hauteur_raquette // 2


x_bot = largeur_fenetre - 30
y_bot = hauteur_fenetre // 2 - hauteur_raquette // 2


x_balle = largeur_fenetre // 2
y_balle = hauteur_fenetre // 2
taille_balle = 10
vitesse_balle_x = -5
vitesse_balle_y = 5


score_joueur = 0
score_bot = 0


police = pygame.font.SysFont("Arial", 30)


def menu():
    while True:
        fenetre.fill(NOIR)
        titre = police.render("Ping Pong avec Bot", True, BLANC)
        instruction = police.render("Appuyez sur ESPACE pour commencer", True, BLANC)
        fenetre.blit(titre, (largeur_fenetre // 2 - titre.get_width() // 2, hauteur_fenetre // 3))
        fenetre.blit(instruction, (largeur_fenetre // 2 - instruction.get_width() // 2, hauteur_fenetre // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    jeu()

        pygame.display.flip()


def jeu():
    global x_balle, y_balle, vitesse_balle_x, vitesse_balle_y, score_joueur, score_bot, y_joueur, y_bot

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        touches = pygame.key.get_pressed()
        if touches[pygame.K_UP] and y_joueur > 0:
            y_joueur -= vitesse_raquette
        if touches[pygame.K_DOWN] and y_joueur < hauteur_fenetre - hauteur_raquette:
            y_joueur += vitesse_raquette

        if y_balle < y_bot + hauteur_raquette // 2:
            y_bot -= vitesse_raquette
        if y_balle > y_bot + hauteur_raquette // 2:
            y_bot += vitesse_raquette

 
        if y_bot < 0:
            y_bot = 0
        if y_bot > hauteur_fenetre - hauteur_raquette:
            y_bot = hauteur_fenetre - hauteur_raquette


        x_balle += vitesse_balle_x
        y_balle += vitesse_balle_y

    
        if y_balle <= 0 or y_balle >= hauteur_fenetre - taille_balle:
            vitesse_balle_y *= -1

 
        if (x_balle <= x_joueur + largeur_raquette and y_joueur <= y_balle <= y_joueur + hauteur_raquette):
            vitesse_balle_x *= -1
        if (x_balle >= x_bot - largeur_raquette and y_bot <= y_balle <= y_bot + hauteur_raquette):
            vitesse_balle_x *= -1

    
        if x_balle <= 0:
            score_bot += 1
            x_balle = largeur_fenetre // 2
            y_balle = hauteur_fenetre // 2
            vitesse_balle_x = -vitesse_balle_x

        if x_balle >= largeur_fenetre - taille_balle:
            score_joueur += 1
            x_balle = largeur_fenetre // 2
            y_balle = hauteur_fenetre // 2
            vitesse_balle_x = -vitesse_balle_x


        fenetre.fill(NOIR)

   
        pygame.draw.rect(fenetre, BLANC, (x_joueur, y_joueur, largeur_raquette, hauteur_raquette))
        pygame.draw.rect(fenetre, BLANC, (x_bot, y_bot, largeur_raquette, hauteur_raquette))
        pygame.draw.ellipse(fenetre, BLANC, (x_balle, y_balle, taille_balle, taille_balle))
        pygame.draw.line(fenetre, BLANC, (largeur_fenetre // 2, 0), (largeur_fenetre // 2, hauteur_fenetre), 5)

        score_texte = police.render(f"{score_joueur}  -  {score_bot}", True, BLANC)
        fenetre.blit(score_texte, (largeur_fenetre // 2 - score_texte.get_width() // 2, 20))

        pygame.display.flip()
        clock.tick(60)


menu()
