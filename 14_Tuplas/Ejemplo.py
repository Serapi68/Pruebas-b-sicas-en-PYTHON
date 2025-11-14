
#Tupla:

posicion = (10, 20)  # Tupla de coordenadas (x, y)
print(posicion[0])  # Imprime: 10
#posicion[0] = 15  # Error: las tuplas son inmutables

#Conjunto:

estados = {"Patrulla", "Reconocimiento", "Manual"}
estados.add("Apagado")
print(estados)  # Imprime: {'Patrulla', 'Reconocimiento', 'Manual', 'Apagado'}
if "Patrulla" in estados:
    print("Modo válido")