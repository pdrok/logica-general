# introducir un numero y averiguar si es par o impar
print "--- Par o Impar ---"

print "Ingrese un valor: ",
a = int(raw_input())

if a % 2 == 0:
    print "%d es par" % a
else:
    print "%d es impar" % a
