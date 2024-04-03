# Dado dos variables M y N, hallar el cociente de M/N por restas sucesivas.
# M Puede o no ser multiplo de N, pero es siempre mayor
print("--- Division por Restas sucesivas ---")
print("Ingrese el divisor: ")
M = int(input())
Resto = M
Cociente = 0
print("Ingrese un divendo menor: ")
N = int(input())

if N >= M:
    print("Ingrese un divendo menor: ")
    N = int(input())

while Resto >= N:
    Cociente += 1
    Resto = Resto - N

print(f"{M} divido {N} es igual a: {Cociente}")
