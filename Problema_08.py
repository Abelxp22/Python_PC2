"""""

Problema 8:
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.

"""""

def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    
    if n == 0:
        return 1
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

numero = int(input("Ingrese un número entero no negativo: "))
print(f"El factorial de {numero} es {factorial(numero)}")