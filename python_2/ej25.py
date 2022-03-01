# Sabiendo que un numero A es divisible por B si la division es entera, hacer un
# algoritmo en el que dados A y B:
# I = 2 si A divide a B (A/B)
# I = 3 si B divide a A (A/B)
# I = 4 si A divide a B y B divide a A (A = B)
# I = 5 si no cumplen ninguno de los requisitos anteriores.

print "--- Verificar si dos numeros son divisbles ---"
print "Ingrese un valor para A :",
A = int(raw_input())
print "Ingrese un valor para B :",
B = int(raw_input())
I = 0
if B > A:
    if B % A == 0:
        I = 2
        print "%d divide a %d y el valor de I es: %d" % (A,B,I)
    else:
        I = 5
        print "%d y %d no cumplen ninguno de los requisitos, el valor de I es: %d" % (A,B,I)
elif A > B:
    if A % B == 0:
        I = 3
        print "%d divide a %d y el valor de I es: %d" % (B,A,I)
    else:
        I = 5
        print "%d y %d no cumplen ninguno de los requisitos, el valor de I es: %d" % (A,B,I)
else:
    I = 4
    print "%d y %d son iguales, el valor de I es: %d" % (A,B,I)
