#!/usr/bin/env python3

# Ejercicios de la sección 2 del curso de Python Essentials

print("¡Hola, Mundo!")
print("Brayan Diaz")
# print(Hola) #NameError: name 'Hola' is not defined

print("Mi", "nombre", "es", "Monty", "Python", end=".\n")


print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

print("Programming","Essentials","in", sep="***", end="...")
print("Python")

# Original 2.1.13 Lab
print()
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print()
# Minimizar el número de invocaciones de la función print() insertando \n en las cadenas

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****\n")

# hacer que la flecha sea el doble de grande (pero mantener las proporciones)

print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
print()
# duplica la flecha, colocando ambas flechas una al lado de la otra; nota: una cadena se puede multiplicar usando el siguiente truco: "string" * 2 producirá "stringstring" (pronto contaremos más al respecto)

print("    *    " * 2)
print("   * *   " * 2)
print("  *   *  " * 2)
print(" *     * " * 2)
print("***   ***" * 2)
print("  *   *  " * 2)
print("  *   *  " * 2)
print("  *****  " * 2)
print()

# Cuestionario 
print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")

# LAB 2.2 Literales de Python - Cadenas

print('\"Estoy\"')
print('\"'*2,"aprendiendo",'\"'*2, sep='')
print('\"'*3,"python",'\"'*3, sep='')

print(0b1011)
