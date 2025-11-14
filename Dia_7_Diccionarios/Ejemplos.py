robot = {"nombre": "R2D2", "velocidad": 10, "bateria": 80}
print(robot)  # Imprime: {'nombre': 'R2D2', 'velocidad': 10, 'bateria': 80}

print(robot["nombre"])  # Imprime: R2D2
print(robot.get("bateria"))  # Imprime: 80  , son dos formas diferentes de usar

for clave in robot:
    print(clave, ":", robot[clave])  # Imprime cada clave y valor

for clave, valor in robot.items():
    print(clave, "->", valor)

robot["bateria"] = int(input('Digite valor de bateria: '))  # Cambia el valor de bateria
print(robot)  # Imprime: {'nombre': 'R2D2', 'velocidad': 10, 'bateria': 90}

del robot["velocidad"]  # Elimina la clave velocidad
robot.pop("nombre")     # Elimina la clave estado
print(robot)

for clave in robot:
    print(clave, ":", robot[clave])  # Imprime cada clave y valor