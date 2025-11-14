lista = [0, 2, 4]
lista.append (lista[1] * lista[2])
for i in range(len(lista)):
    print ( i * lista[i])
print(lista)