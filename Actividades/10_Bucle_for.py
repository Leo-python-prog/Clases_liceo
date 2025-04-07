# Veamos el bucle for

"""
El bucle for en Python es una herramienta poderosa que permite iterar sobre una secuencia 
(como una lista, una tupla, un diccionario, un conjunto o una cadena de caracteres) y 
ejecutar un bloque de código en cada iteración. Se utiliza cuando sabemos cuantas veces vamos a iterar.

Veamos algunos ejemplos.
"""

# Sintaxis Básica
# La sintaxis básica de un bucle for en Python es la siguiente:

#for elemento in secuencia:
    # hacer algo con el elemento
    
for i in range(5):
    print(i)
    
"""
En el anterior ejemplo, vemos una estructura básica del bucle for, lo que hace es imprimir números
empezando por el 0 (cero), ya que éste es la primera posición del rango y finalizando en el 4 (cuatro)
"""

# Veamos más ejemplos

# Quiero que me muestre el 1 y finalice en el 5

for i in range(1, 6):
    print(i)
    
# ¿Qué más podemos hacer con for?

lista = ["manzana", "pera", "frutilla", "banana"]

for elemento in lista:
    print(elemento)
    
"""
Vamos a incrementar la dificultad, vamos a hacer un algoritmo que determine si un elemento de la lista
es "igual" a "manzana" y en función de eso, haremos algo
"""

for elemento in lista:
    if elemento == "manzana":
        print(f"La {elemento} es muy rica")
    else:
        print(elemento)

# Ejercicio

"""
Te propongo un reto, haciendo algo similar al ejercicio anterior, deberás crear una lista de números al azar,
luego deberás crear un algoritmo que determine qué números de la lista son pares, el mensaje que debería
devolver tendría que ser "El número x es par", de lo contrario, debe mostrar el número solo.
"""

numero = [10, 15, 26, 35, 100, 125]

for x in numero:
    if x % 2 == 0:
        print(f"El número {x} es par")
    else:
        print(x)