// Desarrollar un algoritmo que introduzca dos Numeros, e indique la relacion entre ellos.
// Señalar el mayor, el menor o especificar si son iguales
Proceso eje1
	Imprimir "ingrese un valor:"
	leer a
	Imprimir "ingrese otro valor:"
	leer b
	
	Si a > b Entonces
		Imprimir a, " es mayor que ", b
	SiNo
		Si b > a Entonces
			Imprimir b, " es mayor que ", a
		SiNo
			Imprimir  a , " igual a ", b
		Fin Si
	Fin Si
FinProceso
