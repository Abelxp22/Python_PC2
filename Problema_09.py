"""""

Problema 9:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.

"""""

def omitir_vocales(cadena):
    vocales = "aeiouAEIOU"
    
    resultado = ''.join([caracter for caracter in cadena if caracter not in vocales])
    
    return resultado

texto_ingresado = input("Ingrese una cadena de texto: ")

texto_sin_vocales = omitir_vocales(texto_ingresado)

print(f"Texto sin vocales: {texto_sin_vocales}")
