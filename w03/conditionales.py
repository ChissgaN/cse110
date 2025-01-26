temperatura = float(input("Ingrese temperatura: "))
if temperatura > 40.5:
    print("La temperatura es muy alta")
elif temperatura > 35.5:
    print("La temperatura es alta")
else:
    print("La temperatura es normal")
    
# comparing strings
animal = input("Ingrese el animal: ")
animal_lc = animal.lower()
if animal == "cat" or animal == "Car" or animal == "CAT": #this is a bag idea
    print("Meow")
elif animal_lc == "dog": #this is a good idea
    print("Woof")
else:
    print("No se reconoce el animal")
    
    
# Booleans and comparisons 

men = int(input("Ingrese el numero de hombres: "))
women = int(input("Ingrese el numero de mujeres: "))

total = men + women

has_enough_players = total >= 7
has_enough_women = women >= 4

if has_enough_players and has_enough_women:
    print("Hay suficientes personas para jugar")
else:
    print("Hay suficientes personas para jugar")
    
if not has_enough_players:
    print("No hay suficientes personas para jugar pueden entrenar.")
    