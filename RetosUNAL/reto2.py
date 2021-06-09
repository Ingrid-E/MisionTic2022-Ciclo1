# Reto 2: Grupo P2
# Límite de entrega: Monday, 14 de June de 2021, 23:59
# Número máximo de ficheros: 1
# Tipo de trabajo: Individual

# Felipe y su amigo francés, Chandler, están recorriendo la ciudad de Rolotá conociendo 
# las calles más famosas.  Ellos fueron recorriendo las calles e iban adivinando 
# la primera letra de la placa en las direcciones que veían por los sitios. Para ello, 
# cada uno definió las letras con las que jugaría. Al ver la dirección, miraban si esta 
# empezaba con una letra que ellos habían seleccionado, y anotaban un punto en su agenda. 
# Cada que veían una nueva dirección, veían quien acumulaba más puntos, si Felipe llevaba 
# más puntos se escribía un 'F', si por el contrario Chandler tenía más puntos, se escribía 
# una ‘C’, pero si había igualdad de puntos se escribía una ‘J’

# Aquí necesitan de su ayuda como programador, para realizar un programa que reciba las 
# letras con los que participan Felipe y Chandler y una cadena de caracteres con las letras 
# de las direcciones vistas en la ciudad y les muestre como iba el resultado cada vez que 
# llegaban a un nuevo sitio.


#################
#   Input       #
#################

#Felipe 
felipe = input()


#Chandler 
chandler = input()

#Calles
calles = input()

#Output

#String salida
salida = ""

#0:Felipe 1:Chandler
puntos = [0, 0]

#Para cada letra de calles
for i in calles:

    #Si la letra está en las que adivina felipe sumarle un punto
    if i in felipe:
        puntos[0] += 1 
    #Si la letra está en las que adivina chandler sumarle un punto
    if i in chandler:
        puntos[1] += 1 


    #Si Chandler tiene mas puntos que Felipe añadir la letra a salida
    if puntos[0] < puntos[1]:
        salida += "C"
    #Si Felipe tiene mas puntos que Chandler añadir la letra a salida
    elif puntos[0] > puntos[1]:
        salida += "F"
    #Si están empatados sumar la letra J 
    else:
        salida += "J"

    
#############
#   Salida  #
#############

print(salida)
    