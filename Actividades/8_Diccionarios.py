"""Características de los Diccionarios

1. Desordenados: A diferencia de las listas y las tuplas, los diccionarios no mantienen un 
   orden fijo de los elementos.

2. Mutables: Puedes cambiar los valores, agregar y eliminar elementos después de crear el diccionario.

3. Claves Únicas: Cada clave en un diccionario debe ser única. No puede haber dos claves iguales.

4. Par Clave-Valor: Cada elemento en un diccionario se almacena como un par clave-valor."""

"""Creación de Diccionarios
Puedes crear un diccionario usando llaves {} y separando las claves y valores con dos puntos :, 
las claves suelen ser cadenas, pero también pueden ser de otros tipos de datos inmutables, 
como números o tuplas."""

# Diccionario vacío
mi_diccionario = {}

# Diccionario con pares clave-valor
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceso a Elementos
# Accedes a los valores de un diccionario usando sus claves.

print(mi_diccionario["nombre"])  # Resultado: Juan
print(mi_diccionario["edad"])    # Resultado: 30

# Modificación de Valores
# Puedes cambiar el valor asociado a una clave existente o agregar nuevos pares clave-valor.

mi_diccionario["edad"] = 31  # Cambiar el valor de una clave existente
print(mi_diccionario["edad"])  # Resultado: 31

mi_diccionario["profesión"] = "Ingeniero"  # Agregar un nuevo par clave-valor
print(mi_diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 31, 'ciudad': 'Madrid', 'profesión': 'Ingeniero'}

# Eliminación de Elementos
# Puedes eliminar pares clave-valor utilizando la palabra clave del o el método pop().

del mi_diccionario["ciudad"]
print(mi_diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 31, 'profesión': 'Ingeniero'}

profesion = mi_diccionario.pop("profesión")
print(profesion)        # Resultado: Ingeniero
print(mi_diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 31}

# Iterar sobre un Diccionario
# Puedes iterar sobre las claves, los valores o los pares clave-valor de un diccionario.

# Iterar sobre las claves
for clave in mi_diccionario:
    print(clave)

# Iterar sobre los valores
for valor in mi_diccionario.values():
    print(valor)

# Iterar sobre los pares clave-valor
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")

""" Métodos Útiles
1. keys(): Devuelve una vista de las claves del diccionario.

2. values(): Devuelve una vista de los valores del diccionario.

3. items(): Devuelve una vista de los pares clave-valor del diccionario.

4. get(): Devuelve el valor de una clave. Si la clave no existe, devuelve un valor predeterminado.

5. update(): Actualiza el diccionario con los pares clave-valor de otro diccionario o iterable. """

print(mi_diccionario.keys())    # Resultado: dict_keys(['nombre', 'edad'])
print(mi_diccionario.values())  # Resultado: dict_values(['Juan', 31])
print(mi_diccionario.items())   # Resultado: dict_items([('nombre', 'Juan'), ('edad', 31)])

# Uso de get()
print(mi_diccionario.get("ciudad", "No especificado"))  # Resultado: No especificado

# Uso de update()
mi_diccionario.update({"ciudad": "Barcelona", "edad": 32})
print(mi_diccionario)  # Resultado: {'nombre': 'Juan', 'edad': 32, 'ciudad': 'Barcelona'}
