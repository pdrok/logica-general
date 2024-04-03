# Leer un numero N mayor que 100 y hallar e imprimir los numero de 1 hasta N,
# que sean impares pero que no sean multiplos de 5. Hallar tambien la suma, el
# producto y el promedio de los numeros encontrado e imprimir estos valores y
# ademas la cantidad de numeros que cumplieron la condicion.

print("--- Leer un numero N mayor a 100 --")
print("Ingrese un numero mayor a 100 :")
N = int(input())
sumatoria = 0
promedio = 0
producto = 1
cantidad = 0
i = 1

while N <= 100:
    N = int(input())

while i < N:
    if i % 2 != 0 and i % 5 != 0:
        cantidad += 1
        sumatoria = sumatoria + i
        producto = producto * i
        print(f" {i} es impar y no es multiplo de 5")
    i += 1


promedio = sumatoria / cantidad

print(
    "La sumatoria es: {sumatoria}, la cantida es: {cantidad}, el promedio es: {promedio}, el producto es: {producto}"
)
