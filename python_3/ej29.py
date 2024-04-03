# Leer un numero de 5 cifras e imprimir el digito de la centena
print("--- Numero de 5 digitos ---")
print("Ingrese un valor de 5 digitos :")
n = int(input())

while n < 10000 or n > 99999:
    n = int(input())

x = (n / 100) % 10

print(f"El numero ingresado es: {n} y el digito de la centena es: {x}")
