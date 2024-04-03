# Se tiene un archivo de N registro, cada uno con una variable numerica A,
# seleccionar aquellos que sean mayores que 5 y sumarlos. Imprimir el resultado
# y la cantidad de registro que no cumplieron la condicion.


def procesar_registros(nombre_archivo):
    suma_valores = 0
    contador_no_validos = 0

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            try:
                valor = int(linea.strip())
                if valor > 5:
                    suma_valores += valor
                else:
                    contador_no_validos += 1
            except ValueError:
                # Manejar el caso de líneas que no puedan convertirse a entero
                print(f"Error al procesar la línea: {linea}")
                continue

    print(f"Suma de valores mayores a 5: {suma_valores}")
    print(f"Cantidad de registros no válidos (5 o menos): {contador_no_validos}")


# Llamar a la función con el nombre del archivo que contiene los registros
nombre_archivo = "registros.txt"
procesar_registros(nombre_archivo)
