import math
from tabulate import tabulate


class GeneradorEstandar:

    def generador(xo, x, a, m):
        xn = 0
        i = 0
        salida = []
        q = math.floor(m / a)
        r = m % a
        mn = (a * q) + r
        guardados = []

        while xn != x:
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

        return guardados

    def paraTablas(xo, x, a, m):
        xn = 0
        i = 0
        salida = []
        q = math.floor(m / a)
        r = m % a
        mn = (a * q) + r
        guardados = []

        while xn != x:
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

        return "Datos Generados" + "\n" + str(tabulate(salida, headers=["index", "Xn", "Rn"], tablefmt='grid', stralign='center'))
