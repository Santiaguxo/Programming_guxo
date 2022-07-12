# Listas
list_vehicles = ["bmw", "mercedes", "audi", "toyota"]
list_numbers = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]
print(list_vehicles)
print()
#Encontrar la longitud de la lista
print(len(list_vehicles))

# Acceder elementos de una lista
print(list_vehicles[0])
print(list_vehicles[0].upper())
print()

# Las listas se pueden concatenar
print("Yo concateneo " + list_vehicles[0] + " este texto")
print()

# Cambiar, Añadir y remover elementos de una lista
# Cambiar elementos de una lista (en este el primero)
list_vehicles[0] = "Nissan"
print(list_vehicles)
print()

# Añadir elementos a una lista  (en este el ultimo)
list_vehicles.append("Honda")
print(list_vehicles)
print()

# Insertar elementos de uan lista (parametro de : (posicion,"texto deseado"))
list_vehicles.insert(0, "Nissan")
print(list_vehicles)
print()

# Eliminar Remover Pop
# Remover elementos de una lista (Solo elimina la primera) puede ser numero o string
list_numbers.remove(5)
print(list_numbers)
print()
# Eliminar elementos de una lista (El que esta en la posicion)
del list_numbers[0]
print(list_numbers)
# Eliminar mediante pop
print(list_numbers.pop(0))

# Organizacion de listas
