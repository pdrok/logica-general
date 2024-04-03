# Se tiene un conjunto de registro, cada uno con una varible X, que contiene un numero.
# Desarrollar un algoritmo para verificar si los registros estan ordenados en forma ascendente
# El ultimo registro no procesable, tiene 0. Realizar la prueba de escritorio con 10 valores.
def estan_ordenados(registros):
    # Comprobar si la lista está vacía o tiene un solo elemento
    if len(registros) < 2:
        return True

    for i in range(1, len(registros)):
        # Si encontramos el valor 0, detenemos el proceso
        if registros[i] == 0:
            return True
        # Si el valor actual es menor que el anterior, la lista no está ordenada
        if registros[i] < registros[i - 1]:
            return False
    return True


# Lista de prueba con 10 valores terminando en 0
registros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Verificar si los registros están ordenados de forma ascendente
ordenados = estan_ordenados(registros)
print(f"Los registros están ordenados de forma ascendente: {ordenados}")
