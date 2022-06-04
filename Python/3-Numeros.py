# Interger
x = 1
print(x)
# Float
y = 1.5
print(y)

# Orden de operations
# 1. Parenthisis
# 2. Exponent
# 3. Multiplication
# 4. Division
# 5. Modulo (Resto division)
# 6. Addition (Suma)
# 7. Subtraction (Resta)
print()
print("Evitar erros numericos con str()")

# Evitar errores numericos con str()
age = 23
# BIEN
print("Usando ,")
print("Tenes", age, "años ")
print()
# MAL
#print(age, ("Tenes" + age + "años "))

# FIX (convierte ing numero a string para poder concatenar))
print("Usando concatenacion")
print("Tenes " + str(age) + " años ")
print()
