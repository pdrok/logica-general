# Leer A,B y C, ordenarlas en forma ascendente usando como auxiliar el campo D, suponiendo
# que se desconocen los contenidos de A,B y C. Imprimir las variables ordenadas


use std::io;

fn main() {
    // Solicita al usuario ingresar tres valores.
    println!("Introduce el valor de A:");
    let mut a = leer_numero();
    println!("Introduce el valor de B:");
    let mut b = leer_numero();
    println!("Introduce el valor de C:");
    let mut c = leer_numero();

    // Variable auxiliar D para ayudar en el intercambio.
    let mut d: f32;

    // Comparaciones e intercambios para ordenar A, B, y C.
    if a > b {
        d = a;
        a = b;
        b = d;
    }
    if a > c {
        d = a;
        a = c;
        c = d;
    }
    if b > c {
        d = b;
        b = c;
        c = d;
    }

    // Imprimir los valores ordenados.
    println!("Valores ordenados: A = {}, B = {}, C = {}", a, b, c);
}

// Función para leer un número del usuario y convertirlo a f32.
fn leer_numero() -> f32 {
    let mut numero_str = String::new();
    io::stdin()
        .read_line(&mut numero_str)
        .expect("Fallo al leer la línea");
    let numero: f32 = numero_str
        .trim()
        .parse()
        .expect("Entrada inválida");
    numero
}
