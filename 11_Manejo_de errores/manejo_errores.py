try:
    numero = int(input("Ingresa un número: "))
    print(f"El cuadrado es: {numero ** 2}")
except ValueError:
    print("Por favor, ingresa un número válido.")