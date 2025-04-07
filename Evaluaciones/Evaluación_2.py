"""
Primer ejercicio:

Trabajamos con operadores de comparación

1. Crea dos variables y asígnales valores de tipo entero a cada una
2. Realiza la comparación de ambas variables para saber si son:
    a. Iguales
    b. Diferentes
    c. Si la primera variable es mayor que la segunda
    d. Si la primera variable es menor que la segunda
    e. Si la primera variable es mayor o igual a la segunda
    f. Si la primera variable es menor o igual a la segunda
    
Segundo ejercicio

Trabajamos con if

1. Siguiendo con lo que hiciste en el primer ejercicio, deberás realizar lo siguiente:
    a. Si el contenido de las variables son iguales, el mensaje debe ser "Los valores son iguales"
    b. Realiza las comprobaciones y devuelve el mensaje correspondiente para cada caso

"""

# Ejercicios resueltos

# Primer ejercicio

a = 5
b = 10
resultado = (a == b)
print(resultado)

a = 5
b = 10
resultado = (a != b)
print(resultado)

a = 5
b = 10
resultado = (a > b)
print(resultado)

a = 5
b = 10
resultado = (a < b)
print(resultado)

a = 5
b = 10
resultado = (a >= b)
print(resultado)

a = 5
b = 10
resultado = (a <= b)
print(resultado)

# Ejercicio 2

if (a == b):
    print("Los valores son iguales")
else:
    print("Los valores son diferentes")
    
if (a != b):
    print("Los valores son diferentes")
else:
    print("Los valores son iguales")
    
if (a > b):
    print("El primer valor es mayor que el segundo")

if (a < b):
    print("El segundo valor es mayor que el primero")