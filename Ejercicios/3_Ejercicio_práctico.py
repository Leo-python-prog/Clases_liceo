# Área de un cuadrado
lado = int(input("Ingrese el lado del cuadrado: "))
area = lado ** 2
print(f" El área del cuadrado es: {area}")

# Área de un círculo
PI = 3.1416
r = int(input("Ingrese el radio del círculo: "))
area = PI * r ** 2

print(f"El área del círculo es: {area:.2f}")

# Área de un triángulo
base = int(input("Ingrese la base del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))
area = (base * altura)/2

print(f"El área del triángulo es: {area:.2f}")