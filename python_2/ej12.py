# Leer las variables A, B, C, D. Verificar que A pertenezca al intervalo
# Abierto (C,D) y que B no pertenezca al mismo. Si se cumplen las dos
# condiciones, sumar A y B, sino restar A de B. Imprimir A, B y el resultado.

print "Ingrese un valor para A :",
A = int(raw_input())
print "Ingrese un valor para B :",
B = int(raw_input())
print "Ingrese un valor para C :",
C = int(raw_input())
print "Ingrese un valor para D :",
D = int(raw_input())

if A > C and A < D:
    if B < C or B > D:
        result = A + B
        print "%d pertenece al intervalo de %d y %d, y %d no pertence" %(A,C,D,B)
        print "el resultado es:", result
else:
    result = B - A
    print "No %d y %d no cumplen las condiciones" %(A,B)
    print "el resultado es:", result
