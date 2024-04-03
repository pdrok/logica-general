# Se tiene un archivo en el que cada registro tiene una variable numerica X,
# escribir un algoritmos que permita controlar la secuencia correlativa
# ascendente de las mismas. Imprimir los registro fuera de secuencia,
# ignorandolos para el control. El primero no necesariamente comienza con 1
def controlar_secuencia(nombre_archivo):
    ultimo_valido = None

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            try:
                valor_actual = int(linea.strip())
                # Si es el primer valor leído o sigue correctamente la secuencia
                if ultimo_valido is None or valor_actual == ultimo_valido + 1:
                    ultimo_valido = valor_actual
                else:
                    # El registro no sigue la secuencia, se imprime pero se ignora para el control
                    print(f"Registro fuera de secuencia: {valor_actual}")
            except ValueError:
                # Manejar el caso de líneas que no puedan convertirse a entero
                print(f"Error al procesar la línea: {linea}")
                continue


# Suponiendo que los registros están en un archivo llamado 'secuencia.txt'
nombre_archivo = "secuencia.txt"
controlar_secuencia(nombre_archivo)
