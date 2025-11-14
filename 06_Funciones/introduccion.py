def saludar():
    print("¡Hola, robot!")
saludar()  # Llama a la función, imprime: ¡Hola, robot!

#Funciones con parametros

def saludar_persona(nombre):
    print("Hola,", nombre)
saludar_persona("Juan")  # Imprime: Hola, Juan

#Devuelve un resultado

def sumar(a, b):
    return a + b
resultado = sumar(3, 5)
print(resultado)  # Imprime: 8

#Con listas

def promedio_lista(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)
sensores = [10, 20, 30]
print(promedio_lista(sensores))  # Imprime: 20.0

def decision_robot(distancia):
    if distancia < 10:
        return "Detener"
    return "Avanzar"
print(decision_robot(int(input('Defina la distancia del obstaculo: '))))  # Imprime: Detener