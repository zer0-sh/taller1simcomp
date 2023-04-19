# Taller 1 Simulacion
# Johan Muñoz       201958380-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

from tabulate import tabulate

import numpy as np


class PruebaUniChi:

    def pruChi(arr):
        datos = len(arr)
        fe = datos / 10
        tabla = np.array([['0-0.1'],
                          ['0.1-0.2'],
                          ['0.2-0.3'],
                          ['0.3-0.4'],
                          ['0.4-0.5'],
                          ['0.5-0.6'],
                          ['0.6-0.7'],
                          ['0.7-0.8'],
                          ['0.8-0.9'],
                          ['0.9-1.0']])
        FO = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        for x in arr:
            if (x >= 0 and x < 0.1):
                FO[0] += 1
            if (x >= 0.1 and x < 0.2):
                FO[1] += 1
            if (x >= 0.2 and x < 0.3):
                FO[2] += 1
            if (x >= 0.3 and x < 0.4):
                FO[3] += 1
            if (x >= 0.4 and x < 0.5):
                FO[4] += 1
            if (x >= 0.5 and x < 0.6):
                FO[5] += 1
            if (x >= 0.6 and x < 0.7):
                FO[6] += 1
            if (x >= 0.7 and x < 0.8):
                FO[7] += 1
            if (x >= 0.8 and x < 0.9):
                FO[8] += 1
            if (x >= 0.9 and x < 1):
                FO[9] += 1

        res = np.array([])
        for x in range(len(FO)):
            res = np.append(res, (fe-FO[x])**2 / fe)

        tabla = np.insert(tabla, 1, FO, axis=1)
        tabla = np.insert(tabla, 2, fe, axis=1)
        tabla = np.insert(tabla, 3, res, axis=1)

        xCalc = 0
        for i in range(len(tabla)):
            xCalc += float(tabla[i][3])

        if (xCalc <= 16.92):

            return "Prueba de Unicidad de Chi Cuadrado (χ²)" + "\n\n" + \
                str(tabulate(tabla, headers=["rango", "FO", "FE", "(FE - FO)^2/FE"], tablefmt='grid', stralign='center')) \
                   + "\n\n" + "Calculado :" + str(xCalc) + "\n\n" + "Los datos tienen distribucion U(0,1)" + \
                "\nPor lo que el generador es bueno en cuanto a uniformidad"
        else:
            return "Prueba de Unicidad de Chi Cuadrado (χ²)" + "\n\n" + str(
                tabulate(tabla, headers=["rango", "FO", "FE", "(FE - FO)^2/FE"], tablefmt='grid', stralign='center')) \
                + "\n\n" + "Calculado :" + \
                str(xCalc) + "\n\n" + "No pasó la prueba de Unicidad de χ²"
