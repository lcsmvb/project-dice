from constantes import NB_DES, NB_FACES
from des import lancerDeDes, relancerDes
from mains import calculerScore
 
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