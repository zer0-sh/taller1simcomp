import numpy as np
from tabulate import tabulate

class pyRandom:
    def arreglo(self):

        salida = []
        datos = np.array([])

        for i in range(self):
            no = np.random.rand()
            datos = np.append(datos,no)
            salida.append([i,no])
            i +=1

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