"""""

Problema 3:
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.

"""""

numeros = []

while True:
    desea_ingresar = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    
    if desea_ingresar == 'SI':
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif desea_ingresar == 'NO':
        break
    else:
        print("Por favor, responda con 'SI' o 'NO'.")

cantidad_pares = 0
cantidad_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {cantidad_pares}")
print(f"Cantidad de números impares: {cantidad_impares}")