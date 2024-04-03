# Hacer un algoritmo que describa el proceso siguiente. Se leen dos valores de
# 4 digitos a la vez. Calcular e imprimir un nuevo numero que consiste en los
# dos digitos de mayor de la primera cantidad y los dos de menor orden de la
# segunda cantidad colocados uno a continuacion del otro.
# ejemplo: num1=1234 num2=5423  Resultado=1223
print("--- Unir dos valores ---")

print("Ingrese un valor de 4 digitos: ")
num1 = int(input())

while num1 < 1000 or num1 > 9999:
    num1 = int(input())

print("Ingrese otro valor de 4 digitos: ")
num2 = int(input())

while num2 < 1000 or num2 > 9999:
    num2 = int(input())

Resultado = ((num1 / 100) * 100) + (num2 % 100)

print(f"El resultado es: {Resultado}")
