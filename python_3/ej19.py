# introducir un numero y averiguar si es par o impar
print("--- Par o Impar ---")

print("Ingrese un valor: ")
a = int(input())

if a % 2 == 0:
    print(f"{a} es par")
else:
    print(f"{a} es impar")
