import numpy as np

sensores = np.array([12, 18, 25])
if np.any(sensores < 15): #compara cualquiera de los sensores
    print("Obstáculo cerca.")
print("Promedio:", np.mean(sensores))