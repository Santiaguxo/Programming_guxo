#Hacer loop a la totalidad de una lista
import numbers


amigos = ['juan', 'pedro', 'maria', 'jose']
for amigo in amigos: #Recibe el primer valor de amigos y lo guarda en amigo hasta que se acabe la lista
    print(amigo)
    print("Hola "+ amigo.title() +' a veces eres medio weon' + "!")
print("Se termino el loop felizmente")

#Crear listas numericas
print()
for value in range(1,11):
    print(value)

#Crear variables con range()
numbers = list(range(1,11))
print(numbers)

#Crear variables con range salteando ciertos numeros()
print()
#Los dos primeros parametros son el valor inicial y el final y el tercero es el salto
even_numbers = list(range(2,11,2))
print(even_numbers)
print(min(even_numbers))
print(max(even_numbers))
print(sum(even_numbers))

#Ejemplos de compresiones de listas (listas de listas)
print()
#En este caso se imprime cada valor de la lista siempre al exponente 2
#1 **2 = 1 2 **2 = 4 3 **2 = 9 4 **2 = 16 .etc
squares = [value **2 for value in range(1,11)]
print(squares)