#Funciones sin Parametros
function repetirletras()
    imprimirletras()
    imprimirletras()
end
function imprimirletras()
    println("Jueguemos en el bosque")
    println("mientras el lobo no está.")
end
repetirletras()

#Funciones con Parametros
function imprimirdosveces(juan)
    println(juan)
    println(juan)
end
# Uso de Parametros (Imprime el output con el string ya sea ingresado o de una variable)
# Test de funcion de tipo stirng
texto_x = "Frase utilizada para ejemplo"
resultado = imprimirdosveces("Correo no deseado")
#OJO NO SE PUEDE LLAMAR A UNA VARIABLE QUE ESTA DENTRO 
#UNA FUNCION YA QUE SOLO EXISTE DENTRO DE LA FUNCION
#=
function concatenar_dos(parte1, parte2)
    concat = parte1 * parte2
    imprimirdosveces(concat)
end
println(concat)
=#