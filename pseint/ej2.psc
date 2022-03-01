// Dado 3 numeros, verificar si pueden o no ser las longitudes de los lados de un triangulo
// Teneniedo en cuenta que ninguno de los lados puede ser mayor o igual que la sumade de los
// otros dos lados
Proceso ej2
	a=0
	b=0 
	c=0
	Imprimir "Ingrese el lado a del triangulo"
	leer a
	Imprimir "Ingrese el lado b del triangulo"
	leer b
	Imprimir "Ingrese el lado c del triangulo"
	leer c
	
	Si a <= (b+c) & b <= (a+c) & c <= (a+b) Entonces
		imprimir "Pueden ser lados de un triangulo"
	SiNo
		imprimir "No pueden ser lados de un triangulo"
	FinSi
	
FinProceso
