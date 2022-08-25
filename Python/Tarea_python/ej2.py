from random import randint
n = 1
menoredad = 0
mayoredad = 0
while n <= 30:  # TOPE DE PERSONAS
    n = n+1
    edadranndom = randint(1, 100)  # EDAD DE PERSONAS DE 1 A 100
    print("Tu edad generada es", edadranndom)
    if edadranndom > 10:
        print("Ingresas tranquilo ")
        print("-----------")
        mayoredad = mayoredad+1
    else:
        print("MENOR DE EDAD DETECTADO")
        n = n
        print("-----------")
        menoredad = menoredad+1

print("TERMINO EL LOOP")
print("-----------")
print("MAYOR DE EDAD", mayoredad)
print("MENOR EDAD", menoredad)
