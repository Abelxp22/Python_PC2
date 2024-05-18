"""""

Problema 5:
Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.

"""""

def contar_digito(numero, digito):
    numero_str = str(numero)
    digito_str = str(digito)
    
    cantidad = numero_str.count(digito_str)
    
    return cantidad

numero_ingresado = int(input("Ingrese un número entero: "))
digito_ingresado = int(input("Ingrese un dígito: "))

cantidad_veces = contar_digito(numero_ingresado, digito_ingresado)
print(f"Cantidad de veces {digito_ingresado} en el número {numero_ingresado}: {cantidad_veces}")