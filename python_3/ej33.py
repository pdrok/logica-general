# Calcular e imprimir la suma y el producto de los numeros enteros que
# pertenecen al intervalo abierto (M...N)

print("--- Intervalo ---")
print(
    "Ingrese un valor para M: ",
)
M = int(input())

print(
    "Ingrese un valor para N, que sea mayor que M: ",
)
N = int(input())

while N <= M:
    N = int(input())

producto = 1
sumatoria = 0
c = M + 1

while c < N:
    sumatoria = sumatoria + c
    producto = producto * c
    c += 1

print("La sumatoria es : {sumatoria}, el producto es: {producto}")
