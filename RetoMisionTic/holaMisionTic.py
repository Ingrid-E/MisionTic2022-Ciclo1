#El reto consiste en escribir en  un programa en el lenguaje de programación Python 
#que utilice variables y operadores el siguiente mensaje: 
#"Hola Misión TIC 2022... soy <nombre del estudiante>"

#Funcion que imprime el saludo de mision tic
def saludoMisionTic(nombre):
    print("Hola Misión TIC 2022, Yo soy", nombre)
    if nombre == "Ingrid":
        universidad = [
           "██╗░░░██╗███╗░░██╗██╗██╗░░░██╗███████╗██████╗░░██████╗██╗██████╗░░█████╗░██████╗░",
            "██║░░░██║████╗░██║██║██║░░░██║██╔════╝██╔══██╗██╔════╝██║██╔══██╗██╔══██╗██╔══██╗",
            "██║░░░██║██╔██╗██║██║╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║██║░░██║███████║██║░░██║",
            "██║░░░██║██║╚████║██║░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║██║░░██║██╔══██║██║░░██║",
            "╚██████╔╝██║░╚███║██║░░╚██╔╝░░███████╗██║░░██║██████╔╝██║██████╔╝██║░░██║██████╔╝",
            "░╚═════╝░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░",

           "███╗░░██╗░█████╗░░█████╗░██╗░█████╗░███╗░░██╗░█████╗░██╗░░░░░",
            "████╗░██║██╔══██╗██╔══██╗██║██╔══██╗████╗░██║██╔══██╗██║░░░░░",
            "██╔██╗██║███████║██║░░╚═╝██║██║░░██║██╔██╗██║███████║██║░░░░░",
            "██║╚████║██╔══██║██║░░██╗██║██║░░██║██║╚████║██╔══██║██║░░░░░",
            "██║░╚███║██║░░██║╚█████╔╝██║╚█████╔╝██║░╚███║██║░░██║███████╗",
            "╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝"
        ]
        for x in universidad:
            print(x)

if __name__ == "__main__":
    name = input("Cual es tu nombre: ")
    saludoMisionTic(name)
