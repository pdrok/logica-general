# -*- coding: utf-8 -*-
# Desarrollar un algoritmo que introduzca dos Numeros, e indique la relacion entre ellos.
# Señalar el mayor, el menor o especificar si son iguales
print "Ingrese un valor: ",
a = raw_input()
print "Ingrese otro valor: ",
b = raw_input()

if a > b:
    print "%s es mayor que %s" % (a, b)
elif b > a:
    print "%s es mayor que %s" % (b, a)
else:
    print "%s es igual a %s" % (a,b)
