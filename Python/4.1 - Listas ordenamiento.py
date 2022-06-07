#Ordenar Permanentemente (alfabeticamente)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#Inverso
cars.sort(reverse=True)
print(cars)

#Da vuelta la lista
print()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

#Ordenar Lista Temporalmente
print()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))