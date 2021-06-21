'''
Desarrollar un algoritmo que reciba dos cadenas de caracteres y
determine si la primera está incluida en la segunda.

Se dice que una cadena está incluida en otra si todos los caracteres
con repeticiones de la cadena esta en la segunda cadena sin tener en cuenta
el orden de los caracteres.

Ejemplo:
    -"prosa" esta incluida en la cadena "la profesora de idiomas"
    -"pepito" no esta incluido en "un pedazo de tierra" falta una p
    -"pepito" si esta incluido en "tijeras o papel"
'''

'''
Invertir una cadena y decir si es palindroma
'''

cadena = "hola" #aloh

def invertirCadena(palabra) -> str:
    invertida = ""
    for i in range ((len(palabra)-1),-1,-1):
        invertida += palabra[i]
    return invertida

def palindromo(palabra):
    if invertirCadena(palabra).upper() == palabra.upper():
        print(palabra,"Es palindroma")
    else:
        print(palabra,"No es palindroma")

palindromo("hola")
palindromo("Arepera")
palindromo("Sábado")
palindromo("Amor a Roma")




