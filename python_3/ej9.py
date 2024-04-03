# En un laboratorio se registra ,cada hora , la temperatura de los hornos,
# medidas en grados centigrados. Cada registro contiene la siguiente informacion:
# Hora - Temperatura. Se desea convertir la temperatura a grados Farenheit, de
# acuerdo con la siguiente formula: F = 9(C +32)/5
# Por cada registro imprimir:
# Hora, Grados Centigrados y Grados Farenheit. Hay 24 registros por dia.
def convertir_temperaturas(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            # Asumiendo que cada línea tiene el formato "Hora - Temperatura"
            partes = linea.strip().split("-")
            if len(partes) == 2:
                hora, temp_celsius_str = partes
                temp_celsius = float(temp_celsius_str.strip())
                # Convertir la temperatura a Fahrenheit
                temp_fahrenheit = (9 / 5) * (temp_celsius + 32)
                print(
                    f"Hora: {hora.strip()}, Grados Centigrados: {temp_celsius}, Grados Fahrenheit: {temp_fahrenheit:.2f}"
                )
            else:
                print(f"Formato incorrecto en la línea: {linea}")


# Supongamos que los registros están en un archivo llamado 'temperaturas.txt'
nombre_archivo = "temperaturas.txt"
convertir_temperaturas(nombre_archivo)
