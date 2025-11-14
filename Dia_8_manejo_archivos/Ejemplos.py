with open('robot.txt', 'w') as archivo: #escribe archivos el with hace que se cierra el archivo
    archivo.write("Nombre: Explorador\n")
    archivo.write("Batería: 80%\n")

with open('robot.txt', 'r') as archivo: #lee el contenido del archivo
    mostrar = archivo.read()
    print(mostrar)
