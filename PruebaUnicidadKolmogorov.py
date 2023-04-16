import numpy as np
from tabulate import tabulate


class PruebaUnicidadKolmogorov:
    def pruebaKolmogorov(arr):

        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x10 = 0
        nDatos = len(arr)

        for x in arr:
            if (x >= 0 and x < 0.1):
                x1 += 1

            if (x >= 0.1 and x < 0.2):
                x2 += 1

            if (x >= 0.2 and x < 0.3):
                x3 += 1

            if (x >= 0.3 and x < 0.4):
                x4 += 1

            if (x >= 0.4 and x < 0.5):
                x5 += 1

            if (x >= 0.5 and x < 0.6):
                x6 += 1

            if (x >= 0.6 and x < 0.7):
                x7 += 1

            if (x >= 0.7 and x < 0.8):
                x8 += 1

            if (x >= 0.8 and x < 0.9):
                x9 += 1

            if (x >= 0.9 and x < 1):
                x10 += 1

        FO = np.array([['0-0.1', x1]])
        FO = np.vstack([FO, ['0.1-0.2', x2]])
        FO = np.vstack([FO, ['0.2-0.3', x3]])
        FO = np.vstack([FO, ['0.3-0.4', x4]])
        FO = np.vstack([FO, ['0.4-0.5', x5]])
        FO = np.vstack([FO, ['0.5-0.6', x6]])
        FO = np.vstack([FO, ['0.6-0.7', x7]])
        FO = np.vstack([FO, ['0.7-0.8', x8]])
        FO = np.vstack([FO, ['0.8-0.9', x9]])
        FO = np.vstack([FO, ['0.9-1.0', x10]])

        freAcu = 0
        FOA = np.array([])
        POA = np.array([])
        PEA = np.array([])
        res = np.array([])

        for x in range(len(FO)):
            freAcu += int(FO[x, 1])
            FOA = np.append(FOA, freAcu)
            POA = np.append(POA, freAcu / nDatos)
            PEA = np.append(PEA, (x + 1) / 10)
            res = np.append(res, PEA[x] - POA[x])

        FO = np.insert(FO, 2, FOA, axis=1)
        FO = np.insert(FO, 3, POA, axis=1)
        FO = np.insert(FO, 4, PEA, axis=1)
        FO = np.insert(FO, 5, abs(res), axis=1)

        var = np.max(abs(res))

        if (np.max(abs(res)) <= 0.043):
            return "Prueba de Unicidad de Kolmogorov - Smirnov (K-S)" + "\n\n" + str(tabulate(FO, headers=["rango", "FO", "FOA", "POA", "PEA", "|PEA-POA|"], tablefmt='grid',
                                                                                              stralign='center')) + "\n\n" + "Calculado :" + str(var) + "\n\n" + "Los datos tienen distribucion U(0,1), \npor lo que el generador es bueno en cuanto a uniformidad"
        else:
            return "Prueba de Unicidad de Kolmogorov - Smirnov (K-S)" + "\n\n" + str(tabulate(FO, headers=["rango", "FO", "FOA", "POA", "PEA", "|PEA-POA|"], tablefmt='grid',
                                                                                              stralign='center')) + "\n\n" + "Calculado :" + str(var) + "\n\n" + "No pasó la prueba de Unicidad de Kolmogorov"
