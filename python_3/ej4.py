# Teniendo dos variables numericas A y B, intercambiar sus contenidos sus contenidos
# sin utilizar ningun campo auxiliar

print(
    "Ingrese un valor para A:",
)
a = int(input())  # para poder realizar las operaciones hay que ingresar como int()
print(
    "Ingrese un valor para B:",
)
b = int(input())

print(f"El valor de A es: {a}")
print(f"El valor de B es: {b}")

a = a + b
b = a - b
a = a - b
print("Despues de intercambiar")
print(f"El valor de A es: {a}")
print(f"El valor de B es: {b}")
