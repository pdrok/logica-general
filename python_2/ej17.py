# Hacer un algoritmo que permita hallar el producto de los numeros por el metodo
# de las sumas sucesivas. Los numeros deben ser  enteros y mayores que 0
a = 0
b = 0
c = 0
producto = 0
# calular el mod es %
print "Ingrese un valor mayor que 0:"
while a <= 0:
    a = int(raw_input())

print "Ingrese otro valor mayor que 0:"
while b <= 0:
    b = int(raw_input())

while c < b:
    producto = producto + a
    c += 1

print "El producto de %d veces %d es: %d" % (a,b,producto)
