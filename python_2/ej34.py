# Desarrollar un algoritmo que imprima la suma de 100 + 98 + 96 + 94 + .. 40

print "--- Sumatoria ---"
sumatoria = 0
n = 100
while n >= 40:
    sumatoria = sumatoria + n
    n = n - 2

print "la sumatoria es: %d" % sumatoria
