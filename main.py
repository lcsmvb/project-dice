from constantes import NB_DES, NB_FACES
from des import lancerDeDes, relancerDes
from mains import calculerScore
import pygame 

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect(300, 250, 50, 50)

run = True
while run: 
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255, 0, 0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_q] == True: #Gauche
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True: #Droite
            player.move_ip(1, 0)
    elif key[pygame.K_z] == True: #Haut 
            player.move_ip(0, -1)
    elif key[pygame.K_s] == True: #Bas
                player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    pygame.display.update()
pygame.quit()

if __name__ == "__main__":
    des = lancerDeDes(NB_DES, NB_FACES)
    print("Tes dés :", des)
 
    choix = input("Lesquels relancer ? (ex : 1 3 5, ou Entrée pour aucun) : ")
 
    if choix.strip():
        indices = [int(n) - 1 for n in choix.split()]  # le joueur tape 1 à 5, la liste va de 0 à 4
        des = relancerDes(des, indices)
 
    print("Dés finaux :", des)
    main, score = calculerScore(des)
    print(main, ":", score, "points")