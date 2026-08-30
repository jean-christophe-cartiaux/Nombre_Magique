import random


#Création de fonction Ddemander_nombre
def demander_nombre(nb_min, nb_max):
    nombre_int=0
    #création de la boucle pour gérer les erreurs
    while nombre_int ==0:
        nombre_str=input(f"Quelle est le nombre Magique entre {nb_min} et {nb_max} ? ")
        try:
            nombre_int=int(nombre_str)
        except:
            print("Erreur: Vous devez rentrer un nombre. Réessayer ! ")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"Erreur : Le nombre doit être compris entre {nb_min} et {nb_max}")
                nombre_int=0
    return nombre_int
#def boucle_nombre_magique(nombre):
    while nombre== NOMBRE_MAGIQUE:
        if  nombre > NOMBRE_MAGIQUE:
            "Le nombre Magique est plus petit"
        elif nombre < NOMBRE_MAGIQUE:
            "Le nombre Magique est plus grand"
        else:
            "Bravo vous avez trouvez"
    #return(nombre)
#définition des Variables "Pseudo Constante"
NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_VIES=4
vies= NB_VIES
# ajout d'un nombre random compris entre min max
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)


nombre=0
# while not nombre== NOMBRE_MAGIQUE and vies > 0:
#     print(f"Il vous rest {vies} vies")
#     nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
#     if  nombre > NOMBRE_MAGIQUE:
#             print("Le nombre Magique est plus petit")
#             vies-=1
#     elif nombre < NOMBRE_MAGIQUE:
#             print("Le nombre Magique est plus grand")
#             vies-=1
#     else:
#             print("Bravo vous avez trouvez")
# if vies == 0:
#     print(f"Vous avez perdu ! Le nombre magique était : {NOMBRE_MAGIQUE}")
gagne = False
for i in range(0, NB_VIES):
    vies = NB_VIES -i
    print(f"Il vous rest {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre > NOMBRE_MAGIQUE:
            print("Le nombre Magique est plus petit")

    elif nombre < NOMBRE_MAGIQUE:
            print("Le nombre Magique est plus grand")

    else:
        print("Bravo vous avez trouvez")
        gagne = True
        break
if not gagne:
    print(f"Vous avez perdu ! Le nombre magique était : {NOMBRE_MAGIQUE}")