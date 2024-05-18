"""""

Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.

"""""

def fibonacci_series(limite):
    fibonacci = []
    a, b = 0, 1
    
    while a <= limite:
        fibonacci.append(a)
        a, b = b, a + b
    
    return fibonacci

limite = 50

serie_fibonacci = fibonacci_series(limite)

# Imprimir la serie de Fibonacci
print("Serie de Fibonacci entre 0 y 50:")
print(serie_fibonacci)