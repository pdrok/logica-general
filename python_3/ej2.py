# Dados 3 numeros, verificar si pueden o no ser las longitudes de los lados de un triangulo.
# Teniendo en cuenta que ninguno de los lados puede ser mayor o igual que la suma de los
# otros dos lados

print("Ingrese lado a: ")
a = int(input())
print("Ingrese lado b:")
b = int(input())
print("Ingrese lado c:")
c = int(input())
if a < (b + c) and b < (a + c) and c < (a + b):
    print("Pueden ser lados de un triangulo")
else:
    print("No pueden ser lados de un triangulo")
