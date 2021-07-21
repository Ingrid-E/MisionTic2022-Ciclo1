'''
Modele mediante una función matemática y diseñe un
programa recursivo que calcule la suma de los primeros
n cuadrados de los números naturales
'''

def alCuadrado(n):
    if(n == 0):
        return 0
    return n**2 + alCuadrado(n-1)

#print(alCuadrado(2))

'''
Modele mediante una funcion matematica y disene un programa
recursivo sin cadenas, tuplas o listas que determine la cantidad de
dıgitos que componen un n ́umero natural n. Por ejemplo,
longitud(1230321) = 7.
'''

def longitud(numero):
    if(numero/10 == 0):
        return 0
    return 1 + longitud(int(numero/10))

print(longitud(1356))

'''
Modele mediante una funcion matematica y disene un programa sin
cadenas, tuplas o listas que retorne el  ́ultimo dıgito de un numero
natural n (le ́ıdo de izquierda a derecha). Por ejemplo,
ultimo(13579) = 9.
'''

def ultimo(numero):
    size = longitud(numero)-1 #Len para numeros
    eliminar = 10**size
    if size == 0:
        return numero
    else:
        return ultimo(numero-eliminar)

print(ultimo(4569))

'''
Modele mediante una funcion matematica y disene un programa
recursivo sin cadenas, tuplas o listas que dado un numero natural
nelimine el  ́ultimo dıgito del numero. Por ejemplo,
elimina ult(654321) = 65432.
'''

def eliminaUlt(numero):
    if(numero == 0):
        return 0
    size = 10**(longitud(numero)-2)#Len para numeros
    sumar = int(numero/(size*10))*size
    if(sumar == 0):
        return 0
    restar = int(numero/(size*10))*(size*10)
    return int(int(numero/(size*10))*size + eliminaUlt(numero-restar))

print(eliminaUlt(10))

'''
Modele mediante una funcion matematica y disene un programa
recursivo sin cadenas, tuplas o listas que calcule la suma de los dıgitos
que componen un n ́umero natural n. Por ejemplo,
suma digitos(123456) = 21.
'''

def sumaDigitos(numero):
    size = 10**(longitud(numero)-1)
    if(size == 1):
        return numero
    resta = int(numero/size)*size
    return int(numero/size) + sumaDigitos(numero-resta)

print(sumaDigitos(4545))

'''
Modele mediante una funcion matematica y disene un programa
recursivo sin cadenas, tuplas o listas que retorne el primer dıgito de
un numero natural n (le ́ıdo de izquierda a derecha). Por ejemplo,
primero(86420) = 8.
'''

def primerNumero(numero):
    size = 10**(longitud(numero)-1)
    return int(numero/size)

print(primerNumero(4))

'''
Modele mediante una funcion matematica y disene un programa
recursivo sin cadenas, tuplas o listas que dado un numero natural n
elimine el primer dıgito del n ́umero. Por ejemplo,
elimina pri(654321) = 54321.
'''

def eliminaPrimero(numero):
    size = 10**(longitud(numero)-1)
    eliminar = (int(numero/size))*size
    return numero - eliminar

print(eliminaPrimero(654321))

'''
Modele mediante una funcion matematica y disene un programa
recursivo sin cadenas, tuplas o listas que dado un n ́umero natural n
inserte un dıgito al comienzo del numero. Por ejemplo,
inserta(7, 654321)
'''

def insertar(n, numero):
    size = 10**(longitud(numero))
    sumar = n * size
    return sumar + numero

print(insertar(7, 654321))

'''
Modele mediante una funcion matematica y disene un programa
recursivo sin cadenas, tuplas o listas que invierta la cifras de un
numero n dado. Por ejemplo, inversa(654321) = 123456.
'''

def inversa(numero, n=0):
    if(longitud(numero) == 0):
        return 0
    size = 10**(longitud(numero)-1)
    eliminar = int(numero/size)*size
    return  int(numero/size)*(10**n) + inversa((numero-eliminar), n+1)

print(inversa(654321))

'''
Modele mediante una funcion matematica y disene un programa
recursivo sin cadenas, tuplas o listas que determine si un numero es
capicua. Un numero se dice palındromo si al leerlo de izquierda a
derecha es lo mismo que leerlo de derecha a izquierda. Por ejemplo,
capicua(1) = V, capicua(1234321) = V, capicua(123421) = F.
'''

def capicua(numero):
    if(numero == inversa(numero)):
        return True
    else:
        return False

print(capicua(123421))