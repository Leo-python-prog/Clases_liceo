"""Características de las Tuplas
1. Inmutables: A diferencia de las listas, una vez que una tupla es creada, no se pueden cambiar sus elementos. 
Esto significa que no puedes agregar, eliminar o modificar elementos después de la creación de la tupla.

2. Ordenadas: Al igual que las listas, los elementos en una tupla tienen un orden definido que se mantiene 
durante la vida de la tupla.

3. Heterogéneas: Una tupla puede contener elementos de diferentes tipos de datos 
(números, cadenas, listas, etc.).

4. Acceso rápido: Las tuplas permiten el acceso rápido a sus elementos debido a su inmutabilidad, 
lo que las hace más eficientes en términos de tiempo de ejecución comparado con las listas en 
ciertas situaciones."""

# Creación de Tuplas
# Puedes crear una tupla usando paréntesis () y separando los elementos por comas.

# Tupla vacía
mi_tupla = ()

# Tupla con un solo elemento (nota la coma al final)
mi_tupla_uno = (5,)

# Tupla con varios elementos
mi_tupla = (1, 2, 3, "hola", True)

# Acceso a Elementos
# Accedes a los elementos de una tupla usando índices, comenzando desde 0 para el primer elemento.

mi_tupla = (1, 2, 3, "hola", True)
print(mi_tupla[0])  # Resultado: 1
print(mi_tupla[3])  # Resultado: "hola"

# Operaciones con Tuplas
# Aunque no puedes modificar los elementos de una tupla, puedes realizar varias operaciones útiles con ellas.

# Concatenación: Puedes concatenar dos o más tuplas usando el operador +.

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Resultado: (1, 2, 3, 4, 5, 6)

# Repetición: Puedes repetir una tupla usando el operador *.

mi_tupla = (1, 2, 3)
tupla_repetida = mi_tupla * 2
print(tupla_repetida)  # Resultado: (1, 2, 3, 1, 2, 3)

# Desempaquetado: Puedes desempaquetar los elementos de una tupla en variables.

mi_tupla = (1, 2, 3)
a, b, c = mi_tupla
print(a)  # Resultado: 1
print(b)  # Resultado: 2
print(c)  # Resultado: 3

# Métodos de Tuplas
# Las tuplas tienen algunos métodos incorporados que puedes usar:

# count(): Cuenta el número de veces que un elemento aparece en la tupla.

mi_tupla = (1, 2, 2, 3, 2)
print(mi_tupla.count(2))  # Resultado: 3

# index(): Devuelve el índice del primer elemento igual al valor dado.

mi_tupla = (1, 2, 3, "hola", True)
print(mi_tupla.index("hola"))  # Resultado: 3

# Ejemplo Práctico
# Este ejemplo que utiliza varios conceptos de tuplas:

# Creación de una tupla
mi_tupla = (10, 20, 30, 40, 50)

# Acceso a elementos
print(mi_tupla[1])  # Resultado: 20

# Concatenación
otra_tupla = (60, 70)
tupla_concatenada = mi_tupla + otra_tupla
print(tupla_concatenada)  # Resultado: (10, 20, 30, 40, 50, 60, 70)

# Repetición
tupla_repetida = mi_tupla * 2
print(tupla_repetida)  # Resultado: (10, 20, 30, 40, 50, 10, 20, 30, 40, 50)

# Desempaquetado
a, b, c, d, e = mi_tupla
print(a, b, c, d, e)  # Resultado: 10 20 30 40 50

# Métodos de tuplas
print(mi_tupla.count(20))  # Resultado: 1
print(mi_tupla.index(30))  # Resultado: 2