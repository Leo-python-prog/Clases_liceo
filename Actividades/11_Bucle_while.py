"""
El bucle while en Python es una estructura de control que permite ejecutar repetidamente un bloque 
de código mientras una condición sea verdadera. Se utiliza cuando no sabemos cuántas veces se va a
iterar en un código, veamos ejemplos:
"""

# Primero vemos la sintaxis 


# while condición:
    # Código que se ejecutará
    
# Ejemplo 1: Contador simple

contador = 1 # variable

while contador <= 5: # La condición para que el bucle while termine, es que la variable sea menor o igual a 5
    print(contador) # Mostramos el valor de la variable
    contador += 1 # Sumamos de a uno
    
# Ejemplo 2: Verificar contraseña

password = "python123"
entrada = ""

while entrada != password:
    entrada = input("Ingrese su contraseña: ")
    
print("¡Contraseña correcta!")