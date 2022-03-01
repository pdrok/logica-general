# Construir un algoritmo que permita obterner el factorial de un numero dado.
# El factorial de un numero es el resultado de multiplicar dicho numero por los
# valores inferiores al mismo hasta la unidad. El factorial de 0 es igual a 1

print "--- Calcular Factorial ---"
print "Ingrese un valor: ",
n = int(raw_input())

f = 1 # definimos como 1, para que pueda aumenta la suma y cumpla la condicion de 0! = 1
c = n

while c > 1:
    f = f * c
    c = c - 1

print "El factorial de %d es: %d" % (n,f)
