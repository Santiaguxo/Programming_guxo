#Strings ("Texto")
var_string = "Hello World"
print(var_string)
print()

# Modificaciones a Strings

# Mayusculas y minusculas
print("Mayusculas y minusculas")
name = "juan valdez"
print("Texto sin modificar", name)
print(name.title())
print(name.upper())
print(name.lower())
print()

# concatenacion de textos
print("Concantenacion de texto")
first_name = "Juan"
last_name = "Valdez"
full_name = first_name + " " + last_name
print(full_name)
print()

# Agregar saltos de linea a un string
print("Agregar saltos de linea a un string")
print("Hola\nMundo")

# Quitar texto en blanco a una variable
print()
lenguaje_x = ' Texto '
# Remuever espacios en blanco de la derecha
print(lenguaje_x.rstrip())
# Remuever espacios en blanco de la izquierda
print(lenguaje_x.lstrip())
# Remuever espacios en blanco de la derecha e izquierda
print(lenguaje_x.strip())
