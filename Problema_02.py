"""""

Problema 2:
Escriba un programa en Python para construir el siguiente patrón.

"""""

max_rows = 5

for i in range(1, max_rows + 1):
    print('* ' * i)

for i in range(max_rows - 1, 0, -1):
    print('* ' * i)