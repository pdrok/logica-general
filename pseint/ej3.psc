// Leer A,B y C, ordenarlas en forma ascendente usando como auxiliar el campo D,
// suponiendo que se desconocen los contenidos de A, B y C. Imprimir las variables ordenadas.
Proceso ej3
	A = 0
	B = 0
	C = 0
	D = 0
	Imprimir "Ingrese un valor para A: "
	leer A
	Imprimir "Ingrese un valor para B: "
	leer B
	Imprimir "Ingrese un valor para C: "
	leer C
	
	Si A > B Entonces
		D = A
		A = B
		B = D
	FinSi
	Si B > C Entonces
		D = C
		C = B
		B = D
	FinSi
	Si A > B Entonces
		D = A
		A = B
		B = D
	FinSi
	Imprimir "Los valores ordenados son: ", A, " ", B, " ", C 
FinProceso
