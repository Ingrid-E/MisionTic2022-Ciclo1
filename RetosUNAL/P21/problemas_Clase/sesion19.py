'''
Para el JSON con la estructura mostrada
'''
import json
from os import sep

with open('files/EstructuraJSON.Json', 'r', encoding='utf-8') as archivo:
    estructuraJSON = json.load(archivo)

def practicanDeporte(deporte):
    personas = []
    for persona in estructuraJSON:
        if deporte.title() in estructuraJSON[persona]['deportes']:
            personas.append(persona)
    return personas

#deporte = input('Deporte: ')
#print(*practicanDeporte(deporte), sep="\n")

def rangoDeEdades(rango):
    personas = []
    for persona in estructuraJSON:
        edad = estructuraJSON[persona]['edad']
        if edad >= int(rango[0]) and edad <= int(rango[1]):
            personas.append(persona)
    return personas
        
#rangoEdad = input("Rango de edad, escribirlo como: 0 10\n").split()
#print(*rangoDeEdades(rangoEdad))

def deportePersona():
    deportes = {}
    for persona in estructuraJSON:
        personas = []
        deporte = estructuraJSON[persona]['deportes']
        for x in deporte:
            if x not in deportes.keys():
                deportes[x] = []
            deportes[x].append(persona)
    
    
    with open('files/newJSON.Json', 'w', encoding="utf-8") as newArchive:
        json.dump(deportes, newArchive, indent= 4)

deportePersona()


