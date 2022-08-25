lista = [2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4]
contador1 = 0
contador2 = 0
for numero in lista:
    if (numero % 2) == 0:
        print("{0} es par".format(numero))
        contador1 = contador1+1
    else:
        contador2 = contador2+1
print()
print("Son ", contador2, " impares ")
