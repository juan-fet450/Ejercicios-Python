def edad(x,y):
    respuesta=x+(2070-y)
    return respuesta

def parOimpar(num):
    respuesta = " "
    if num % 2 != 1:
        respuesta = "par"
    else:
        respuesta = "impar"

    return respuesta

def indicepalabra(palabra):
    inicial = palabra[0]
    final = palabra[len(palabra)-1]
    return inicial+final

