# Taller 1 Simulacion
# Johan Muñoz       201958380-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

import numpy as np
from tabulate import tabulate


class pyRandom:
    def arreglo(self):

        salida = []
        datos = np.array([])

        for i in range(self):
            no = np.random.rand()
            datos = np.append(datos, no)
            salida.append([i, no])
            i += 1

        return datos

    def tabla(self):

        salida = []
        datos = np.array([])

        for i in range(self):
            no = np.random.rand()
            datos = np.append(datos, no)
            salida.append([i, no])
            i += 1

        return "Datos Generados" + "\n" + str(tabulate(salida, headers=["index", "No"], tablefmt='grid', stralign='center'))
