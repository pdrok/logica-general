// Dados 3 numeros, verificar si pueden o no ser las longitudes de los lados de un triangulo.
// Teniendo en cuenta que ninguno de los lados puede ser mayor o igual que la suma de los
// otros dos lados

use std::io;

fn main() {
    let mut lado1 = String::new();
    let mut lado2 = String::new();
    let mut lado3 = String::new();

    println!("Introduce la longitud del primer lado:");
    io::stdin()
        .read_line(&mut lado1)
        .expect("Fallo al leer la línea");

    println!("Introduce la longitud del segundo lado:");
    io::stdin()
        .read_line(&mut lado2)
        .expect("Fallo al leer la línea");

    println!("Introduce la longitud del tercer lado:");
    io::stdin()
        .read_line(&mut lado3)
        .expect("Fallo al leer la línea");

    // Convertimos las entradas a números flotantes
    let lado1: f32 = lado1.trim().parse().expect("Entrada inválida");
    let lado2: f32 = lado2.trim().parse().expect("Entrada inválida");
    let lado3: f32 = lado3.trim().parse().expect("Entrada inválida");

    if es_triangulo(lado1, lado2, lado3) {
        println!("Los números pueden ser las longitudes de los lados de un triángulo.");
    } else {
        println!("Los números NO pueden ser las longitudes de los lados de un triángulo.");
    }
}

fn es_triangulo(lado1: f32, lado2: f32, lado3: f32) -> bool {
    // Verificamos la desigualdad triangular para cada combinación de lados
    lado1 < lado2 + lado3 && lado2 < lado1 + lado3 && lado3 < lado1 + lado2
}
