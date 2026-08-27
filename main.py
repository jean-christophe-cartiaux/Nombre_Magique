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
NOMBRE_MAGIQUE = 5
nombre=0
while not nombre== NOMBRE_MAGIQUE:
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if  nombre > NOMBRE_MAGIQUE:
            print("Le nombre Magique est plus petit")
    elif nombre < NOMBRE_MAGIQUE:
            print("Le nombre Magique est plus grand")
    else:
            print("Bravo vous avez trouvez")
#boucle_nombre_magique(nombre)