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
fond=pygame.image.load("Images/fond.jpg").convert_alpha()
rip_bozo=pygame.image.load("Images/rip.jpg").convert_alpha()
gg_bozo=pygame.image.load("Images\Happy.jpg").convert_alpha()
hello_bozo=pygame.image.load("Images/Babac.jpg").convert_alpha()

# musique
mixer.init()
mixer.music.load("Sons\Super_Idol.mp3")
mixer.music.play(10)

#HEE HEE HAW
augh = mixer.Sound("Sons/augh.mp3")

# creation du joueur et des entités
player = Classes.Joueur()
pygame.mouse.set_visible(False)
patient = Classes.Patient()
veines = Classes.Veines()
poubelle_c= Classes.Poubelle_C()
poubelle_b= Classes.Poubelle_B()

# creation des burgers et des cocas
liste_coca = pygame.sprite.Group()
liste_burger = pygame.sprite.Group()

# dessin des cocas
for i in range(5):
    coca = Classes.Coca(random.randint(100,800),random.randint(257,600))
    burger = Classes.Burger(random.randint(100,700),random.randint(251,600))
    # regroupement des cocas et burgers dans une liste et uniquement dans les veines
    if pygame.sprite.collide_mask(coca, veines):
        liste_coca.add([coca])
    if pygame.sprite.collide_mask(burger, veines):
        liste_burger.add([burger])

### START ###
start= True
running = True # variable pour laisser la fenêtre ouverte
victoire = False

while start:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                pygame.mouse.set_pos(50,50)
                start=False
    debut_text=player.font.render(f"Yo Akhy, Appuie sur Espace pour commencer...",1,(255,0,0))
    screen.blit(hello_bozo,(0,0))
    hello_bozo.blit(debut_text,(180,550))
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
    player.score -= 2

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
        if victoire:
            mixer.music.stop()
            mixer.music.unload()
            mixer.music.load("Sons/bamba.mp3")
            mixer.music.play() 

    # ENLEVE L'ELEMENT

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            player.etat="Attrape" # Si on clique (gauche), on est en mesure d'attraper un objet
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            player.etat="Relâche" # Si on clique (droit), on initialise player.sac comme une liste vide
            player.sac = []
    
        boissons = pygame.sprite.spritecollide(player, liste_coca, False)
        for boisson in boissons:
            if player.etat == "Attrape":
                player.attraper(boisson)
            # Marque    
            if pygame.sprite.collide_mask(boisson, poubelle_c): 
                if player.etat == "Relâche":
                    boissons = pygame.sprite.spritecollide(player, liste_coca, True) 
                    player.marquer()
                    boissons.remove(boisson)


        burgers = pygame.sprite.spritecollide(player, liste_burger, False)
        for bouffe in burgers:
            if player.etat == "Attrape":
                player.attraper(bouffe)
            # Marque    
            if pygame.sprite.collide_mask(bouffe, poubelle_b): 
                if player.etat == "Relâche":
                    burgers = pygame.sprite.spritecollide(player, liste_burger, True) 
                    player.marquer()
                    burgers.remove(bouffe)
            


         # MOURIR
    if pygame.sprite.collide_mask(player, patient) and not  pygame.sprite.collide_mask(player, veines):
        player.mourir()               
           
        
    ### Actualisation de la scene ###
    
    # dessin 
    screen.blit(patient.image,patient.rect) # appel de la fonction qui dessine le patient
    screen.blit(veines.image,veines.rect) # appel de la fonction qui dessine les veines
    screen.blit(poubelle_c.image,poubelle_c.rect) # appel de la fonction qui dessine les poubelles
    screen.blit(poubelle_b.image,poubelle_b.rect) # appel de la fonction qui dessine les poubelles
    liste_burger.draw(screen)
    liste_coca.draw(screen)
    # joueur
    player.rect.center = pygame.mouse.get_pos() 
    screen.blit(player.image,player.rect) # appel de la fonction qui dessine le joueur
    

    ### Fin de jeu ###
    if len(liste_coca) == 0 and len(liste_burger) == 0:
        victoire = True

        gg_bro = player.font.render(f"GG Akhy, Appuie sur Echap pour prendre ta douche...",1,(255,255,255))

        screen.blit(gg_bozo,(0,0))
        gg_bozo.blit(gg_bro,(190,550))

    if player.score == 0:
        player.health = 0

    if player.health == 0:
        mixer.music.stop()
        mixer.music.unload()
        augh.play()

        fin_text = player.font.render(f"R.I.P Bozo, Appuie sur Echap pour en finir...",1,(255,255,255))
        screen.blit(rip_bozo,(0,0))
        rip_bozo.blit(fin_text,(200,550))
    pygame.display.update() # pour ajouter tout changement à l'écran
    clock.tick(FPS)