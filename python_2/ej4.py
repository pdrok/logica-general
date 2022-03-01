# Teniendo dos variables numericas A y B, intercambiar sus contenidos sus contenidos
# sin utilizar ningun campo auxiliar

print "Ingrese un valor para A:",
a = int(raw_input()) # para poder realizar las operaciones hay que ingresar como int()
print "Ingrese un valor para B:",
b = int(raw_input())

print "El valor de A es:",a
print "El valor de B es:",b

a = a + b
b = a - b
a = a - b
print "Despues de intercambiar"
print "el valor de A es:",a
print "El valor de B es:",b
