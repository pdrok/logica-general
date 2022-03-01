# Calcular e imprimir la suma y el producto de los numeros enteros que
# pertenecen al intervalo abierto (M...N)

print "--- Intervalo ---"
print "Ingrese un valor para M: ",
M = int(raw_input())

print "Ingrese un valor para N, que sea mayor que M: ",
N = int(raw_input())

while N <= M:
    N = int(raw_input())

producto = 1
sumatoria = 0
c = M + 1

while c < N:
    sumatoria = sumatoria + c
    producto = producto * c
    c += 1

print "La sumatoria es : %d, el producto es: %d" % (sumatoria, producto)
