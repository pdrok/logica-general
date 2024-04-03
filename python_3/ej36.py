# Leer un numero N y asignarle a la varible C un valor 1 , si N es un cubo
# perfecto, sino asignarle a C el valor 0.
# Obs: Se dice que un numero es un cubo perfecto si existe un entero X tal que
# el cubo de X sea igual al numero. Repetir el proceso M veces.

print("--- En busca del cubo percto ---")
print("Ingrese un valor: ")
N = int(input())

x = 1
C = 0

while x < N and C == 0:
    if x**3 == N:
        C += 1

    x += 1

if C == 0:
    print(f"{N} no es cuadrado perfecto")
    print(f"el valor de C es : {C}")
else:
    print(f"{N} es cuadrado perfecto")
    print("el valor de C es : {C}")
