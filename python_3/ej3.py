# Leer A,B y C, ordenarlas en forma ascendente usando como auxiliar el campo D, suponiendo
# que se desconocen los contenidos de A,B y C. Imprimir las variables ordenadas

print("Ingrese un valor para a:")
a = int(input())
print("Ingrese un valor para b:")
b = int(input())
print("Ingrese un valor para c:")
c = int(input())

if a > b:
    d = a
    a = b
    b = d

if b > c:
    d = b
    b = c
    c = d

if a > b:
    d = a
    a = b
    b = d
print(f"los valores ondenados: {a}, {b}, {c}")
