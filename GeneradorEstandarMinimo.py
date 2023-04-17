# Taller 1 Simulacion
# Johan Muñoz       201958383-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

import math
from tabulate import tabulate


class GeneradorEstandar:

    # ----- Constructor -----
    def generador(xo, x, a, m):
        x = xo
        xn = 0
        i = 0
        salida = []
        q = math.floor(m / a)
        r = m % a
        mn = (a * q) + r
        guardados = []
        temp = []
        quebrador = False

        while quebrador != True:
            if xo in temp:
                quebrador = True
            xn = a * (xo % q) - r * math.floor(xo / q)
            temp.append(xo)
            if (xn >= 0):
                xo = xn
                rn = xn / mn
                i += 1
                salida.append([i, xo, rn])
                guardados.append(rn)
            else:
                xn = xn + mn
                xo = xn
                rn = xn / mn
                i += 1
                salida.append([i, xo, rn])
                guardados.append(rn)

        return guardados

    def paraTablas(xo, x, a, m):
        x = xo
        xn = 0
        i = 0
        salida = []
        q = math.floor(m / a)
        r = m % a
        mn = (a * q) + r
        guardados = []
        temp = []
        quebrador = False

        while quebrador != True:
            if xo in temp:
                quebrador = True
            temp.append(xo)
            xn = a * (xo % q) - r * math.floor(xo / q)
            if (xn >= 0):
                xo = xn
                rn = xn / mn
                i += 1
                salida.append([i, xo, rn])
                guardados.append(rn)
            else:
                xn = xn + mn
                xo = xn
                rn = xn / mn
                i += 1
                salida.append([i, xo, rn])
                guardados.append(rn)

        return "Datos Generados:" + str(i) + "\n" + str(tabulate(salida, headers=["index", "Xn", "Rn"], tablefmt='grid', stralign='center'))
