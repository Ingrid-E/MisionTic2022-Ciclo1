'''
	Twitter: @g1_alexander
	Github: @g1alexander
'''
import random

def main():
    pd = {
        "LAMBETAZO": ["QUERIDOS","APRECIADOS","DISTINGUIDOS","HONORABLES","ESTIMADOS","RESPETADOS"], 
        "POTENCIALES": ["COMPATRIOTAS","CONCIUDADANOS","AMIGOS","COTERRANEOS","COPARTIDARIOS","ELECTORES"],
        "CONDICIÓN": ["EN MI GOBIERNO","CON SU APOYO","SIENDO ELEGIDO","CON SU AYUDA","SI ME SIGUEN","DURANTE MI MANDATO"],
        "COMPROMISO": ["VOY A DERROTAR","VENCERÉ","ELIMINARÉ","ACABARÉ","LUCHARÉ CONTRA","COMBATIRÉ"],
        "ILUSIÓN": ["LA VIOLENCIA Y","LA DELINCUENCIA Y","LA CORRUPCIÓN Y","LA INFLACIÓN Y","LA POBREZA Y","EL DESPLAZAMIENTO Y"],
        "PROMESA": ["TRABAJARÉ POR","GARANTIZARÉ","PROTEGERÉ","VELARÉ POR", "PROMOVERÉ","DEFENDERÉ"],
        "BENEFICIO": ["LA EDUCACIÓN","EL EMPLEO","LA SEGURIDAD","LA LAZ","LA IGUALDAD","LA SALUD"],
        "DEPENDIENDO": ["DEL PAÍS","DE LA CIUDAD","DE LA COMUNIDAD","DE LA POBLACIÓN","PARA TODA LA GENTE","DE CADA COLOMBIANO"],
    }
    d = {
        "LAM": random.choice(pd["LAMBETAZO"]),
        "POT": random.choice(pd["POTENCIALES"]),
        "CON": random.choice(pd["CONDICIÓN"]),
        "COM": random.choice(pd["COMPROMISO"]),
        "ILU": random.choice(pd["ILUSIÓN"]),
        "PRO": random.choice(pd["PROMESA"]),
        "BEN": random.choice(pd["BENEFICIO"]),
        "DEP": random.choice(pd["DEPENDIENDO"])
    }

    print(F"discurso: {d['LAM']} {d['POT']} {d['CON']} {d['COM']} {d['ILU']} {d['PRO']} {d['BEN']} {d['DEP']}")


if __name__ == "__main__":
    main()


