import numpy as np
from tabulate import tabulate


class GeneradorLineal:
    ## Constructor##
    def genLinCongruente(xo, x, a, c, m):

        xn = 0
        i = 0
        guardados = np.array([])
        salida = []

        while xn != x:
            rn = xo / m
            salida.append([i, xo, rn])
            xn = (a * xo + c) % m
            xo = xn
            guardados = np.append(guardados, [rn])
            i += 1

        return guardados

    def paraTabla(xo, x, a, c, m):

        xn = 0
        i = 0
        guardados = np.array([])
        salida = []

        while xn != x:
            rn = xo / m
            salida.append([i, xo, rn])
            xn = (a * xo + c) % m
            xo = xn
            guardados = np.append(guardados, [rn])
            i += 1

        return "Datos Generados" + "\n" + str(tabulate(salida, headers=["index", "Xn", "Rn"], tablefmt='grid', stralign='center'))
