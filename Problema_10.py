"""""

Problema 10:
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:

"""""


def obtener_fecha_en_formato_iso(fecha):
    meses = {
        "Enero": "01",
        "Febrero": "02",
        "Marzo": "03",
        "Abril": "04",
        "Mayo": "05",
        "Junio": "06",
        "Julio": "07",
        "Agosto": "08",
        "Septiembre": "09",
        "Octubre": "10",
        "Noviembre": "11",
        "Diciembre": "12"
    }

    partes = fecha.split()
    if len(partes) == 3:
        mes = partes[0]
        dia = partes[1][:-1]
        año = partes[2]
    else:
        mes, dia, año = fecha.split("/")

    mes_numero = meses.get(mes, None)
    if mes_numero:
        fecha_iso = f"{año}-{mes_numero}-{dia.zfill(2)}"
        return fecha_iso
    else:
        return "Formato de fecha incorrecto"

fecha1 = input("Ingresa una fecha (mes/día/año o Mes, día, año): ")
print("Fecha en formato AAAA-MM-DD:", obtener_fecha_en_formato_iso(fecha1))

fecha2 = input("Ingresa otra fecha (mes/día/año o Mes, día, año): ")
print("Fecha en formato AAAA-MM-DD:", obtener_fecha_en_formato_iso(fecha2))
