"""Características de las Listas:
1- Ordenadas: Los elementos en una lista tienen un orden definido que se mantiene durante la vida de la lista. 
Esto significa que puedes acceder a los elementos usando índices.

2- Mutables: Puedes modificar los elementos de una lista después de haberla creado. Puedes agregar, 
eliminar o cambiar elementos.

3- Heterogéneas: Una lista puede contener elementos de diferentes tipos de datos.

4- Dinámicas: El tamaño de una lista puede cambiar de forma dinámica conforme agregas o eliminas elementos."""

# Lista vacía
mi_lista = []

# Lista con números
numeros = [1, 2, 3, 4, 5]

# Lista con diferentes tipos de datos
mezclada = [1, "hola", 3.14, True]

# Mostrar el contenido específico de una lista, según su posición.
numeros = [1, 2, 3, 4, 5]
print(numeros[0])  # Resultado: 1
print(numeros[2])  # Resultado: 3

# Se pueden sumar elementos de una lista
print(numeros[1] + numeros[3])

# Puedes cambiar los valores de los elementos en una lista
numeros = [1, 2, 3, 4, 5]
numeros[1] = 10
print(numeros)  # Resultado: [1, 10, 3, 4, 5]

# Agregar y Eliminar Elementos

# Agregar elementos:
# append() agrega un elemento al final de la lista.
# insert() inserta un elemento en una posición específica.
# extend() agrega elementos de otra lista al final.

mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)  # Resultado: [1, 2, 3, 4]

mi_lista.insert(1, 10)
print(mi_lista)  # Resultado: [1, 10, 2, 3, 4]

otra_lista = [5, 6, 7]
mi_lista.extend(otra_lista)
print(mi_lista)  # Resultado: [1, 10, 2, 3, 4, 5, 6, 7]

# Eliminar elementos
# remove() elimina la primera aparición de un valor específico.
# pop() elimina el elemento en una posición específica y lo devuelve.
# del elimina un elemento o una porción de la lista.

mi_lista = [1, 2, 3, 4, 5]
mi_lista.remove(3)
print(mi_lista)  # Resultado: [1, 2, 4, 5]

mi_lista.pop(1)
print(mi_lista)  # Resultado: [1, 4, 5]

del mi_lista[0]
print(mi_lista)  # Resultado: [4, 5]

# Iterar sobre una Lista
# Puedes usar bucles para iterar sobre los elementos de una lista.

mi_lista = [1, 2, 3, 4, 5]
for elemento in mi_lista:
    print(elemento)

# Slicing
# El slicing permite acceder a una porción de la lista.

mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[1:4])  # Resultado: [2, 3, 4]
print(mi_lista[:3])   # Resultado: [1, 2, 3]
print(mi_lista[2:])   # Resultado: [3, 4, 5]
print(mi_lista[-1])   # Resultado: 5 (último elemento)
