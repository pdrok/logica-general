# Se tiene un archivo, con N registro; cada uno de ellos con una varible
# numerica X. Imprimir el rango del archivo. Rango = numero mayor - numero menor
def calcular_rango_archivo(nombre_archivo):
    mayor = None
    menor = None

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            try:
                # Convertir la línea a número
                numero = float(linea.strip())

                # Actualizar el mayor y el menor
                if mayor is None or numero > mayor:
                    mayor = numero
                if menor is None or numero < menor:
                    menor = numero
            except ValueError:
                # En caso de que alguna línea no contenga un número válido
                print(f"Error al procesar la línea: {linea}")
                continue

    if mayor is not None and menor is not None:
        rango = mayor - menor
        print(f"El rango del archivo es: {rango}")
    else:
        print("El archivo no contiene números válidos o está vacío.")


# Supongamos que los registros están en un archivo llamado 'numeros.txt'
nombre_archivo = "numeros.txt"
calcular_rango_archivo(nombre_archivo)
