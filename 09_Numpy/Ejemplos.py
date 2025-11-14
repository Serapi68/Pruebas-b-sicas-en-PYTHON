import numpy as np 
#Array es una lista pero mas eficientee para calculos
calculos = np.array([10,20,15])
lista = [10,20,15]
suma = sum(lista)
print(calculos)
print(lista)
print(calculos * 2)
print(lista * 2) #no multiplica los valores, si no clona su contenido
print(np.mean(calculos))#imprime el promedio
print(suma/len(lista))#toca añadir una variable anterior para que funcione como numpy