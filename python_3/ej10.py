# Dados N numeros hallar el mayor y el menor. Imprimiendo ambos con los mensajes
# identificacion respectivos


def encontrar_maximo_minimo(numeros):
    if not numeros:  # Comprobar si la lista está vacía
        print("La lista está vacía.")
        return

    # Encontrar el valor máximo y mínimo en la lista de números
    maximo = max(numeros)
    minimo = min(numeros)

    # Imprimir los resultados
    print(f"El número mayor es: {maximo}")
    print(f"El número menor es: {minimo}")


# Ejemplo de uso con una lista de N números
numeros = [5, 1, 8, 7, 2, -3, 9, 4, 0, -1]
encontrar_maximo_minimo(numeros)
