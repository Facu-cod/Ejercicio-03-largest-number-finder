"""Desarrollar un programa que solicite tres números enteros desde teclado al usuario, posteriormente, el programa deberá determinar e indicar a traves de un mensaje en pantalla, cual de los tres números es el mas grande.

Requerimientos indispensables:
El mensaje en pantalla deberá mostrar el numero que resulto ser el mas grande de los tres."""

numero1 = int(
    input("Introduce el primer número: ")
)
numero2 = int(
    input("Introduce el segundo número: ")
)
numero3 = int(
    input("Introduce el ultimo número: ")
)

if numero1 >= numero2 and numero1 >= numero3:
    print(f"El numero mas grande es {numero1}.")
elif numero2 >= numero1 and numero2 >= numero3:
    print(f"El numero mas grande es {numero2}.")
else:
    print(f"El número más grande es {numero3}.")
