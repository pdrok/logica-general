// Teniendo dos variables numericas A y B, intercambiar sus contenidos sus contenidos
// sin untilizar ningun campo auxiliar
Proceso ej4
	A = 0
	B = 0
	Imprimir "Ingrese un valor para A: "
	Leer A
	Imprimir "Ingrese un valor para B: "
	Leer B
	
	Imprimir "El valor de A es: ", A
	Imprimir "El valor de B es: ", B
	
	A = A + B
	B = A - B
	A = A - B
	
	Imprimir "Despues de intercambiar"
	Imprimir "El valor de A es: ", A
	Imprimir "El valor de B es: ", B
FinProceso
