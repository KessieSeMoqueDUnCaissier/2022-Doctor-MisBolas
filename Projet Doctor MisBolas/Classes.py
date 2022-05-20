import pygame  # necessaire pour charger les images et les sons
import random

class Joueur() : # classe pour créer le joueur
    def __init__(self) :
        self.font = font=pygame.font.Font("Oswald.ttf",25)
        self.font2 = font=pygame.font.Font("Koulen.ttf",50)
        self.image = pygame.image.load("Images\Moi.png").convert_alpha()
        self.score = 3500
        self.health = 100
        self.rect = self.image.get_rect() # dessine un rectangle autour du joueur
        self.mask = pygame.mask.from_surface(self.image) # créer un masque de pixels sur le joueur

        self.etat="Normal" # l'état varie entre "attrape" et "relâche"
        self.sac = [] # liste pour attraper


    def attraper(self, objet):
        """
        Prend en paramètres un objet, si la liste sac est vide, 
        Alors on ajoute cet objet à la liste,
        L'objet dans la liste prend les coordonnées du joueur
        """
        if len(self.sac) == 0:
            self.sac.append(objet)
        for element in self.sac:
            element.rect.x = self.rect.x
            element.rect.y = self.rect.y


    def mourir(self):
        """
        Initialise la vie du joueur à 0
        """
        self.health = 0

    def marquer(self):
        """
        Accumule 250 points à chaque appel
        """
        self.score+= 250

    def update(self,screen):
        """
        Renvoie le score à l'écran de jeu
        """
        score_text=self.font2.render(f"{self.score}%",1,(255,255,255))
        screen.blit(score_text,(682,0))


class Patient():
    def __init__(self):
        self.image = pygame.image.load("Images\Patient.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = 100
        self.mask = pygame.mask.from_surface(self.image)
        self.etat = "Normal"

class Veines():
    def __init__(self):
        self.image = pygame.image.load("Images\Veines.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = 100
        
class Poubelle_C():
    def __init__(self):
        self.image = pygame.image.load("Images\Poubelle_Coca.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -220
        self.rect.y = -172

class Coca(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images\-Coca.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class Poubelle_B():
    def __init__(self):
        self.image = pygame.image.load("Images\Poubelle_Burger.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -350
        self.rect.y = -172

class Burger(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images\-Burger.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
