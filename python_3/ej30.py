# -*- coding: utf-8 -*-
# Se introduce una fecha en la variable F(año,mes,dia) en una varible numerica
# N de seis digitos, imprimir en varibles separadas año, mes, dia, ejemplo
# F = 851221 Anho=85, Mes=12, Dia=21

print("--- Separar Fechas ---")
print("Ingrese una fecha en el formato AAMMDD  :")
F = int(input())

dia = F % 100
mes = (F / 100) % 100
anho = F / 10000

print(f"Año={anho}, Mes={mes}, Dia={dia}")
