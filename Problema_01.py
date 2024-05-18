"""""

Problema 1:
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).

"""""

start = 1500
end = 2700

result = []

for number in range(start, end + 1):
    if number % 7 == 0 and number % 5 == 0:
        result.append(number)

print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:", result)