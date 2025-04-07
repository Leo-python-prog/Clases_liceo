"""
Ahora vamos a ver una opción que tenemos para tomar decisiones en nuestro código, habitualmente en nuestra vida
cotidiana, debemos tomar decisiones, por ejemplo, qué ropa usaré hoy, qué haré el fin de semana, entre otras.

¿Te has puesto a pensar cómo tomamos decisiones?

Lo normal para tomar decisiones, es que tengamos que considerar condiciones, veamos ejemplos:

¿Qué ropa usaré hoy?

    Las condiciones pueden ser, hace frio, hace calor, está lloviendo, me la puse ayer
    Elijamos una condición, por ejemplo "hace frío", veamos como seria la estructura
    
    Si hace frío, entonces me pongo una campera, sino la dejo en casa.
    
    Ahora veamos esto mismo, pero llevado a código de Python

"""
condincion = "Hace frío"

if condincion == "Hace frío":
    print("Me pongo la campera")
else:
    print("La dejo en casa")
    
# Veamos otro ejemplo

numero = 10

if numero % 2 == 0:
    print("Es par")
else:
    print("Es impar")
    
"""
En el ejemplo que vimos, usamos la operación aritmética de módulo, también conocida como "resto", la fórmula
sirve para saber si un número es par o impar, es decir, si el resto de la división por 2 da 0 (cero),
entonces el número es par, sino es impar.
"""

# ¿Qué pasa si tenemos mas de una posible salida?

"""
Vamos a usar "elif", esta palabra reservada, es una conjunción entre la palabra if y else y sirve para
lograr agregar una nueva "salida" según la condición.

Veamos un ejemplo
"""

condincion = "Hace frío"

if condincion == "Hace frío":
    print("Me pongo la campera")
elif condincion == "Ahora no hace frío, pero más tarde si":
    print("llevo la campera por las dudas")
else:
    print("La dejo en casa")
    
"""
El ejemplo anterior, quizás sea un poco confuso debido a que usamos un ejemplo de la vida cotidiana,
a continuación veremos un ejemplo que quizás te aclare las cosas
"""

nota = 7

if nota >= 7:
    print("Sobresaliente")
elif nota >= 5:
    print("Aceptable")
else:
    print("No aprobado")
    
