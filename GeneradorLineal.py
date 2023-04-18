# Taller 1 Simulacion
# Johan Muñoz       201958383-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

import numpy as np
from tabulate import tabulate


class GeneradorLineal:

    # ----- Constructor -----
    def genLinCongruente(xo, a, c, m):
        xn = 0
        i = 0
        guardados = np.array([])
        salida = []
        temp = []
        quebrador = False

        while quebrador != True:
            if xo in temp:
                quebrador = True
            rn = xo / m
            salida.append([i, xo, rn])
            temp.append(xo)
            xn = (a * xo + c) % m
            xo = xn
            guardados = np.append(guardados, [rn])
            i += 1

        return guardados

    def paraTabla(xo, a, c, m):

        xn = 0
        i = 0
        rn = xo / m
        guardados = np.array([])
        salida = []
        temp = []
        quebrador = False

        while quebrador != True:
            if xo in temp:
                quebrador = True
            rn = xo / m
            salida.append([i, xo, rn])
            temp.append(xo)
            xn = (a * xo + c) % m
            xo = xn
            guardados = np.append(guardados, [rn])
            i += 1

        return "Datos Generados:" + str(i) + "\n" + str(tabulate(salida, headers=["index", "Xn", "Rn"], tablefmt='grid', stralign='center'))
