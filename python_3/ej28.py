# Desarrollar un algoritmo para sumar dos numeros A y B de 4 digitos cada uno,
# almacenando cada digito en un posicion separada, Los digitos de A se ubicaran
# en D4,D3,D2,D1 y los de B en W4,W3,W2,W1. Larespuesta se debe dar en las
# posiciones A5,A4,A3,A2,A1 respectivamente.

print("--- Dos valores de 4 digitos ---")
print("Ingrese un valor de 4 digitos para A:")
A = int(input())

while A < 1000 or A > 9999:
    A = int(input())

print("Ingrese un valor de 4 digitos para B:")
B = int(input())

while B < 1000 or B > 9999:
    B = int(input())

C = A + B

D1 = A % 10
D2 = (A % 100) / 10
D3 = (A / 100) % 10
D4 = A / 1000

W1 = B % 10
W2 = (B % 100) / 10
W3 = (B / 100) % 10
W4 = B / 1000
A5 = 0
A1 = C % 10
A2 = (C % 100) / 10
A3 = (C / 100) % 10
A4 = (C / 1000) % 10
if C > 9999:
    A5 = C / 10000
print(f"El valor de A es: {A}" % A)
print(f"D4={D4}, D3={D3}, D2={D2}, D1={D1}")
print(f"El valor de B es: {B}")
print(f"W4={W4}, W3={W3}, W2={W2}, W1={W1}")
print(f"La suma de {A} + {B} es: {C}")
print(f"A5={A5}, A4={A4}, A3={A3}, A2={A2}, A1={A1}")
