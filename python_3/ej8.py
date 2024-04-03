# Se tiene un archivo con 3000 regitros, cada uno de ellos con una variable X.
# Imprimir la sumatoria y el promedio de cada 3 valores consecutivos.
def calcular_sumatoria_promedio(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        # Inicializar una lista para almacenar los 3 valores consecutivos
        valores = []

        for linea in archivo:
            # Convertir la línea actual a número y añadirla a la lista de valores
            try:
                valor_actual = float(linea.strip())
                valores.append(valor_actual)

                # Cuando hay 3 valores en la lista, calcular la sumatoria y el promedio
                if len(valores) == 3:
                    sumatoria = sum(valores)
                    promedio = sumatoria / 3
                    print(f"Sumatoria: {sumatoria}, Promedio: {promedio}")
                    # Remover el primer valor de la lista para seguir con los siguientes 3 valores
                    valores.pop(0)
            except ValueError:
                print(f"Error al procesar la línea: {linea}")
                continue


# El nombre del archivo que contiene los 3000 registros
nombre_archivo = "registros_x.txt"
calcular_sumatoria_promedio(nombre_archivo)
