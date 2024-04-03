# Leer las variables A, B, C, D. Verificar que A pertenezca al intervalo
# Abierto (C,D) y que B no pertenezca al mismo. Si se cumplen las dos
# condiciones, sumar A y B, sino restar A de B. Imprimir A, B y el resultado.

print("Ingrese un valor para A :")
A = int(input())
print("Ingrese un valor para B :")
B = int(input())
print("Ingrese un valor para C :")
C = int(input())
print("Ingrese un valor para D :")
D = int(input())

if A > C and A < D:
    if B < C or B > D:
        result = A + B
        print(f"{A} pertenece al intervalo de {C} y {D}, y {B} no pertence")
        print(f"El resultado es: {result}")
else:
    result = B - A
    print(f"No {A} y {B} no cumplen las condiciones")
    print(f"el resultado es: {result}")
