// Desarrollar un algoritmo que introduzca dos Numeros, e indique la relacion entre ellos.
// Señalar el mayor, el menor o especificar si son iguales

use std::io; // Importamos la biblioteca de entrada/salida para interactuar con la consola.

fn main() {
    // Inicializamos un String vacío para almacenar la entrada del usuario.
    let mut numero1 = String::new();
    let mut numero2 = String::new();

    // Solicitamos al usuario el primer número.
    println!("Introduce el primer número: ");
    io::stdin()
        .read_line(&mut numero1)
        .expect("Fallo al leer la línea");

    // Convertimos el String a un número flotante.
    let numero1: f32 = numero1.trim().parse().expect("Entrada inválida");

    // Repetimos el proceso para el segundo número.
    println!("Introduce el segundo número: ");
    io::stdin()
        .read_line(&mut numero2)
        .expect("Fallo al leer la línea");

    let numero2: f32 = numero2.trim().parse().expect("Entrada inválida");

    // Comparamos los números e imprimimos la relación entre ellos.
    if numero1 > numero2 {
        println!(
            "El primer número ({}) es mayor que el segundo número ({}).",
            numero1, numero2
        );
    } else if numero1 < numero2 {
        println!(
            "El segundo número ({}) es mayor que el primer número ({}).",
            numero2, numero1
        );
    } else {
        println!("Ambos números son iguales.");
    }
}
