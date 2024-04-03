# Desarrollar un algoritmo que introduzca dos Numeros, e indique la relacion entre ellos.
# Señalar el mayor, el menor o especificar si son iguales
print("Ingrese un valor: ")
a = input()
print("Ingrese otro valor: ")
b = input()

if a > b:
    print(f"{a} es mayor que {b}")
elif b > a:
    print(f"{a} es mayor que {b}")
else:
    print(f"{a} es igual a {b}")
