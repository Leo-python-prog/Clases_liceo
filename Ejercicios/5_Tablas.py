# Le preguntamos al usuario qué tabla quiere que le mostremos

print("¿Qué tabla te gustaría ver? ")
tabla = int(input("Respuesta: "))

for i in range(11):
    respuesta = i * tabla
    print(f"{tabla} x {i} = {respuesta}")
    i += 1