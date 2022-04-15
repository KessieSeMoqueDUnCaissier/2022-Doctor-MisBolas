import pygame  # necessaire pour charger les images et les sons
import random

class Joueur() : # classe pour créer le joueur
    def __init__(self) :
        self.font=font=pygame.font.Font("Oswald.ttf",25)
        self.image = pygame.image.load("Images\Moi.png").convert_alpha()
        self.score=0
        self.health = 100
        self.rect=self.image.get_rect()
        self.rect.x=10
        self.rect.y=10
        self.etat="Normal"

    def attraper(self,objet):
        objet.rect.x = self.rect.x
        objet.rect.y = self.rect.y

    def mourir(self):
        self.health = 0

    def marquer(self):
        self.score+= 250

    def update(self,screen):
        score_text=self.font.render(f"Salaire:{self.score}$",1,(255,255,255))
        screen.blit(score_text,(20,20))


class Patient():
    def __init__(self):
        self.image = pygame.image.load("Images\Patient.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = 100
        self.etat = "Normal"

class Veines():
    def __init__(self):
        self.image = pygame.image.load("Images\Veines.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = -100
        self.rect.y = 100
        self.etat = "Normal"


class Coca(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images\-Coca.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y
 

