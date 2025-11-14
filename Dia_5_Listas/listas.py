#Una lista es una colección ordenada de elementos (números, texto, etc.) que se almacenan en una sola variable.


sensores = [10, 20, 15, 30]  # Lista de lecturas de un sensor
print(sensores)  # Imprime: [10, 20, 15, 30]

sensores.append(sensores[1] * sensores[0])  # Añade 40 al final
sensores.insert(0, 5)  # Añade 5 al inicio
print(sensores)

print(sensores[0])  # Imprime: 10 (primer elemento)
print(sensores[-1]) # Imprime: 30 (último elemento)

sensores[1] = (25) # Cambia el segundo elemento a 25
print(sensores)   # Imprime: [10, 25, 15, 30]

sensores.pop()      # Elimina el último elemento
sensores.remove(25) # Elimina el valor 25
print(sensores)

for valor in sensores:
    print(valor)  # Imprime cada elemento

for i in range(len(sensores)):
    print("Sensor", i, ":", sensores[i]) #La i es el numero de la posicion 