import pygame # importation de la librairie pygame
from pygame.locals import *
from pygame import mixer
import Classes
from Classes import*
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 
# définir une clock
clock=pygame.time.Clock()
FPS=400

# création d'une fenêtre de 800 par 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Doctor MisBolas") 

# chargement de l'image de fond
fond=pygame.image.load("Images\-Amogus.png").convert_alpha()
rip_bozo=pygame.image.load("Images\-Nick-Avocado.png").convert_alpha()
gg_bozo=pygame.image.load("Images\Happy.jpg").convert_alpha()
hello_bozo=pygame.image.load("Images\-Kanye_Feast.png").convert_alpha()

# musique
mixer.init()
mixer.music.load("Sons\Super_Idol.mp3")
mixer.music.play(10)

#HEE HEE HAW
oof = mixer.Sound("Sons\HeeHeeHaw.mp3")
sus = mixer.Sound("Sons\Vine_Boom.mp3")
augh = mixer.Sound("Sons/augh.mp3")

# creation du joueur et des ennemis
player = Classes.Joueur()
pygame.mouse.set_visible(False)
patient = Classes.Patient()
veines = Classes.Veines()

# creation des burgers et des cocas
liste_coca = pygame.sprite.Group()

# dessin des cocas
coca = Classes.Coca(89,210)
coca2 = Classes.Coca(681,210)

# regroupement des cocas et burgers dans une liste
liste_coca.add([coca,coca2])

### START ###
start= True
running = True # variable pour laisser la fenêtre ouverte

while start:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                start=False
    debut_text=player.font.render(f"Hello Bozo, Appuie sur Espace pour commencer...",1,(0,0,0))
    screen.blit(hello_bozo,(0,0))
    hello_bozo.blit(debut_text,(170,550))
    pygame.display.flip()
mixer.music.stop()
mixer.music.unload()
mixer.music.load("Sons\MissTheRage.mp3")
mixer.music.play(10)

### BOUCLE DE JEU  ###
while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    player.update(screen)

    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
        # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
    # R.I.P
            if event.key == pygame.K_ESCAPE:
                running = False # running est sur False 
                sys.exit()
                
    # DEDICACE A LEO ROI SOLEIL ET DANIIL LE RACISTE
            if event.key == pygame.K_j:
                mixer.music.load("Sons\Giorno_JJBA.mp3")
                mixer.music.play()

    # MOURIR
    #if player.rect.colliderect(patient.rect):
        #player.mourir()

    # ENLEVE L'ELEMENT
        miam = pygame.sprite.spritecollide(player, liste_coca, False)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.etat="Attrape"
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            player.etat="Relâche"
        for graille in miam:
            if player.etat == "Attrape":
                player.attraper(graille)
        
                
        
    ### Actualisation de la scene ###
    
    # dessin 
    screen.blit(patient.image,patient.rect) # appel de la fonction qui dessine le patient
    screen.blit(veines.image,veines.rect) # appel de la fonction qui dessine les veines
    liste_coca.draw(screen)
    # joueur
    player.rect.center = pygame.mouse.get_pos() 
    screen.blit(player.image,player.rect) # appel de la fonction qui dessine le joueur
    

    ### Fin de jeu ###
    if len(liste_coca) == 0:
        augh.play()

        score_fin = player.font.render(f"PIB actuel:{player.score}",1,(234,31,31))
        gg_bro = player.font.render(f"GG Bozo, Appuie sur Echap pour prendre ta douche...",1,(255,255,255))

        screen.blit(gg_bozo,(0,0))
        gg_bozo.blit(gg_bro,(222,550))
        gg_bozo.blit(score_fin,(0,150))

    if player.health == 0:
        oof.play()

        score_fin = player.font.render(f"PIB actuel:{player.score}",1,(234,31,31))
        fin_text = player.font.render(f"R.I.P Bozo, Appuie sur Echap pour en finir...",1,(255,255,255))

        screen.blit(rip_bozo,(0,0))
        rip_bozo.blit(fin_text,(222,550))
        rip_bozo.blit(score_fin,(0,150))
    pygame.display.update() # pour ajouter tout changement à l'écran
    clock.tick(FPS)