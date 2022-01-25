import time
import math
import sys

#loading animation :

def loading():
    for i in range(10):
        sys.stdout.write('\r|')
        time.sleep(0.1)
        sys.stdout.write('\r/')
        time.sleep(0.1)
        sys.stdout.write('\r-')
        time.sleep(0.1)
        sys.stdout.write('\r\\')
        time.sleep(0.1)

#func => total area

def total_area():
    return unique_area * 6

#func => spheric volume

def spheric_volume():
    pi = math.pi
    radius_at_cube = cube(radius)
    result = 4 * pi * radius_at_cube / 3
    return result

#func => volumic mass

def volumic_mass(mass, volume):
    return mass / volume


#func => power elec by hour

def elec(power, time):
    return power * time


#func => cube

def cube(num):
    return num * num * num

print("+=========================+")
print("|CALCULATRICE SCIENTIFIQUE|")
print("+=========================+")

print("1. Masse volumique")
print("2. Cube")
print("3. Racine carré")
print("4. Puissance")
print("5. Puissance éléctrique par heure (kWh)")
print("6. Volume (plusieurs options...)")


choix = input("Quelle opération veut-tu faire ?(1/2/3/4/5/6)\n")

while True:
    
    if choix in '6':
        loading()
        break
    
    elif choix in '1':
        print("Calcul de la masse volumique séléctionné.")
        
        mass = float(input("Masse :"))
        volume = float(input("Volume :"))
            
        print("OK. Calcul en cours...")
            
        time.sleep(0.3)
            
        print("La masse volumique est ", volumic_mass(mass, volume))
        
    elif choix in '2':
        print("Calcul d'un cube séléctionné.")
        
        num = float(input("Nombre à mettre au cube :"))
        
        print("OK. Calcul en cours...")
        
        time.sleep(0.1)
        
        print(f"Le cube de {num} est ", cube(num))
        
    elif choix in '3':
        print("Calcul de la racine carré selctionné.")

        num = float(input("Entrez un nombre :"))

        print("OK. Calcul en cours...")

        time.sleep(0.4)

        print(f"La racine carré de {num} est :", math.sqrt(num))
        
    elif choix in '4':
        print("Calcul d'une puissance séléctionné")
        base = float(input("Base :"))
        exponent = float(input("Puissance :"))
        print("OK. Calcul en cous...")
        time.sleep(0.8)
        print(f"{base} puissance {exponent} =", math.pow(base, exponent))

    elif choix in '5':
        print("Calcul de la puissance électrique par heure séléctionné (kWh)")

        print("Préparation en cours...")

        # time.sleep(0.4)

        power = float(input("Puissance :"))

        time = float(input("Temps :"))

        print("OK. Calcul en cours...")

        print(f"La puissance électrique par heure est de ", elec(power, time))

    else:
        print("ERROR Invalid input")

while True:
    print("1. Sphère")
    print("2. Cube")
    print("3. Pavé Droit")
    print("4. Prisme")
    print("5. Cylindre")
    
    volume_choix = input("Quelle objet (1/2/3/4/5)")

    if volume_choix in '1':
        print("Sphère sélectionnée")
        
        print("Récupérations des fonctions...")

        loading()

        print("Récuperation terminée")

        time.sleep(0.1)

        radius = float(input("Rayon :\n"))
        
        time.sleep(0.1)
        print("Calcul en cours...")
        loading()

        print("Calcul terminé")
        print("Le volume de cette sphère est de ENVIRON", spheric_volume(), "3")
        time.sleep(1)
        continue

    elif volume_choix in '2':
        global_area_known = input("Connais-tu l'aire totale de ton cube ? (oui/non)")

        if global_area_known in 'oui':
            volume_cube = float(input("Volume :\n"))

            print("OK. Calcul en cours...")
            
            loading()
            
            print("Le volume de ce cube est ", cube(volume_cube), "3")
            time.sleep(1)
            continue

        elif global_area_known in 'non':
            print("OK. Je vais la calculer pour toi...")
            
            unique_area = float(input("Il me faut seulement l'aire d'un seul côté :\n"))
            
            print("OK. Calcul de l'aire totale...")
            
            loading()
            
            print("Aire totale", total_area())
            print("Tu n'as plus qu'a refaire le même procédé...")
            print("En donnant la valeur totale.")
            time.sleep(1)

        else:
            print("ERROR Invalid input")
            time.sleep(1)
            continue
    
    elif volume_choix in '3':
        print("Calcul du pavé droit séléctionné")
        print("Si tu veux calculer le volume de ton pavé droit, il me faut :")
        
        longueure = float(input(">>>La longueure"))
        largeure = float(input(">>>La largeure"))
        hauteur = float(input(">>>La hauteure"))

        print("OK. Calcul en cours...")

        loading()

        print("Le volume de ce pavé droit est de ", longueure * largeure * hauteur)
        time.sleep(1)
        continue
    
    elif volume_choix in '4':
        print("Calcul d'un prisme sélectionné")
        
        base_area = float(input("Aire de la base :\n"))
        height = float(input("Hauteur :\n"))

        loading()

        print("Le volume du prisme est de ", base_area * height)
        time.sleep(1)
        continue

    elif volume_choix in '5':
        print("Calcul d'un prisme sélectonné")
        pi = math.pi
        radius = float(input("Rayon :\n"))
        height = float(input("Hauteur :\n"))
        print("OK. Calcul en cours...")

        loading()

        print("Le volume de ce cylindre est de ", pi * math.pow(radius, 2) * height)

        time.sleep(1)

        continue