# Solicitar al usuario que ingrese datos por teclado

# Para lograr esto, debemos habilitar el teclado para que los usuarios puedan escribir, veamos como...

# El teclado se activa con la palabra input, veamos un ejemplo

variable = input()

# Con esta línea, se puede habilitar el uso del teclado y lo que el usuario escriba, se guardará en una variable.

# Dentro de los paréntesis, se puede escribir una cadena de texto, que indique al usuario lo que 
# debe escribir, es decir, el tipo de dato que debe escribir.
# Veamos como sería el comando para solicitar el nombre a continuación

nombre = input("Ingresa tu nombre: ")

# Lo que vimos anteriormente, sólo sirve en caso de que el tipo de dato ingresado, sea una cadena de texto,
# ya que si el usuario pone otro tipo de dato, el código lo transforma en una cadena, para solucionar esto,
# debemos hacer lo siguiente:

# Tipo de dato ENTERO
edad = int(input("Ingresa tu edad: ")) # int significa entero, es decir todo lo que esté dentro 
# de los paréntesis será transformado en entero.

# Tipo de dato FLOTANTE
precio = float(input("Ingrese el precio del producto: "))

# Ejercicio práctico

"""Deberás crear un programa que solicite al usuario el precio de un producto en dólares
y que nuestro programa devuelva el precio en pesos uruguayos"""

# Solución

dolar = 45

precio_usd = float(input("Ingrese el precio del producto en dólares: "))
precio_uy = precio_usd * dolar

print(precio_uy)

# Si quieres agregar más información a lo que se muestra por pantalla, po ejemplo "El precio en pesos es..."
# debemos hacer lo siguiente:

print(f"El precio en pesos es {precio_uy}") # la letra f antes de la cadena de texto indica que pondremos una
# variable dentro de las llaves, asi nos mostrará el contenido de la misma.