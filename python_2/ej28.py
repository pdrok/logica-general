# Desarrollar un algoritmo para sumar dos numeros A y B de 4 digitos cada uno,
# almacenando cada digito en un posicion separada, Los digitos de A se ubicaran
# en D4,D3,D2,D1 y los de B en W4,W3,W2,W1. Larespuesta se debe dar en las
# posiciones A5,A4,A3,A2,A1 respectivamente.

"--- Dos valores de 4 digitos ---"
print "Ingrese un valor de 4 digitos para A:",
A = int(raw_input())

while A < 1000 or A > 9999:
    A = int(raw_input())

print "Ingrese un valor de 4 digitos para B:",
B = int(raw_input())

while B < 1000 or B > 9999:
    B = int(raw_input())

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
print "El valor de A es: %d" % A
print "D4=%d, D3=%d, D2=%d, D1=%d" %(D4,D3,D2,D1)
print "El valor de B es: %d" % B
print "W4=%d, W3=%d, W2=%d, W1=%d" %(W4,W3,W2,W1)
print "La suma de %d + %d es: %d" % (A,B,C)
print "A5=%d, A4=%d, A3=%d, A2=%d, A1=%d" %(A5,A4,A3,A2,A1)
