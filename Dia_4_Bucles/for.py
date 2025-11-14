
# se usa cuando se sabe cuantas veces se repite
for i in range(1, 6):
    if i == 3:
        print('Me salte el 3')
        continue # Salta el 3
        
    print(i) # Imprime 1, 2, 4, 5