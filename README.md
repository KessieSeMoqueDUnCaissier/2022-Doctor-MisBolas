# Doctor-MisBolas 😳
Bienvenue amigo! Je suis señor MisBolas, docteur diplômé d'Etat et je te présente mon jeu! Ton but? Aide-moi à opérer Nickocado! L'opération est cependant très dure...  
Ce jeu est codé à l'aide du module Pygame sur Python, et en majorité avec de la P.O.O.

----------------------------------------------------------

## Présentation 🤡
Premièrement, à l'aide de votre souris (qui vous sert d'outil), enlevez l'élément ciblé par le jeu!
En effet, notre patient, un peu trop gourmand sur les bords, se voit avec des cochonneries dans le corps! 
J'ai oublié de l'anesthésier et ma pause café est bientôt proche...  

Deuxièmement, vous avez un temps imparti pour enlever l'élément, c'est-à-dire: le prendre en cliquant et le poser sur un récipient spécifique.  
**Ne touchez que la partie rouge du patient avec votre outil, sinon c'est fini!**

#### Pour résumer, enlevez l'élément ciblé, ne blessez pas le patient, et mettez le dans le bon récipient, LE TOUT DANS UN TEMPS IMPARTI !!! Si l'opération est un franc succès, vous gagnez l'équivalent du PIB comorien. L'argent est accumulé lorsque vous réussissez à effectuer la bonne tâche, sinon le patient meurt et vous finissez au chomâge!  

![jhonny-sins-winkgif](https://user-images.githubusercontent.com/90514084/161158727-7d1e21ba-f898-4595-8a37-3239ca759431.gif)

-----------------------------------------------------------

## Problèmes??? 😞
Ce projet est certes amusant mais les problèmes se dessinent déjà:
  * L'aspect graphique 
  * La spécificité du récipient 
  * L'élément ciblé
  * La partie rouge du patient (donc hitbox)
  * Le temps par élément donné (doit être réinitialisé lorsque la tâche est réussie)
  * Si le jeu est trop dur, alors on imposera un système à 3 vies  

![angryspeed](https://user-images.githubusercontent.com/90514084/161158995-27ada36e-3d0b-4487-a9b1-fc8a7eb07b96.gif)

----------------------------------------------------------

## Minimum Viable Product 🧠  
Le joueur doit pouvoir enlever tous les éléments se trouvant dans le corps du patient pour gagner. Si il touche autre chose que la zone rouge (dans laquelle restent les éléments), alors il perd et la partie recommence. Aucune autre contrainte dans cette version: temps imparti, types d'éléments, système de points...  
Il y a un écran de début et de fin. Voici une image illustrant la version de notre jeu, de manière simple:  

![MisBolasDemo](https://user-images.githubusercontent.com/90514084/162639710-7791ffe3-f980-4c29-a83f-c59fbb3a4e8c.png)  

----------------------------------------------------------

## Fonctions et prototypage 🤔  
class Joueur() :
  
    def attraper(self, objet):
        """
        Prend en paramètres un objet, si la liste sac est vide, 
        Alors on ajoute cet objet à la liste,
        L'objet dans la liste prend les coordonnées du joueur
        """  
    def mourir(self):
        """
        Initialise la vie du joueur à 0
        """  
    def marquer(self):
        """
        Accumule 250 points à chaque appel
        """  
    def update(self,screen):
        """
        Renvoie le score à l'écran de jeu
        """  
  


class Patient():
   
class Veines():
    
class Poubelle_C():
    
class Coca(pygame.sprite.Sprite):
   
class Poubelle_B():
     
class Burger(pygame.sprite.Sprite):
    
