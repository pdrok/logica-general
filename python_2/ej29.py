# Leer un numero de 5 cifras e imprimir el digito de la centena
print "--- Numero de 5 digitos ---"
print "Ingrese un valor de 5 digitos :",
n = int(raw_input())

while n < 10000 or n > 99999:
    n = int(raw_input())

x = (n / 100) % 10

print "El numero ingresado es: %d y el digito de la centena es: %d" % (n,x)
