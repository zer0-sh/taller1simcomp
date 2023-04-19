# Taller 1 Simulacion
# Johan Muñoz       201958380-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

from PruebaChiCuadrado import *


class pruebaUnicidadSerie:

    def pruebaSerie(arr):
        n = len(arr)
        nPares = n/2
        xCalc = 0
        # °°°°°° Bidimensional °°°°°°
        FE = nPares/25
        tablaFO = [["|=|", "0.0-0.2", "0.2-0.4", "0.4-0.6", "0.6-0.8", "0.8-1.0"],
                   ["0.0-0.2", 0, 0, 0, 0, 0],
                   ["0.2-0.4", 0, 0, 0, 0, 0],
                   ["0.4-0.6", 0, 0, 0, 0, 0],
                   ["0.6-0.8", 0, 0, 0, 0, 0],
                   ["0.8-1.0", 0, 0, 0, 0, 0]]
        tuplas = []

        for x in range(0, n-1, 2):
            auxTupla = (arr[x], arr[x+1])
            tuplas.append(auxTupla)

            # °°°°°° Comparacion de la primera fila °°°°°°
            if (arr[x] >= 0.0 and arr[x] < 0.2 and arr[x+1] >= 0.0 and arr[x+1] < 0.2):
                tablaFO[1][1] += 1
            if (arr[x] >= 0.0 and arr[x] < 0.2 and arr[x + 1] >= 0.2 and arr[x + 1] < 0.4):
                tablaFO[1][2] += 1
            if (arr[x] >= 0.0 and arr[x] < 0.2 and arr[x + 1] >= 0.4 and arr[x + 1] < 0.6):
                tablaFO[1][3] += 1
            if (arr[x] >= 0.0 and arr[x] < 0.2 and arr[x + 1] >= 0.6 and arr[x + 1] < 0.8):
                tablaFO[1][4] += 1
            if (arr[x] >= 0.0 and arr[x] < 0.2 and arr[x + 1] >= 0.8 and arr[x + 1] < 1):
                tablaFO[1][5] += 1

            # °°°°°° Comparacion de la segunda fila °°°°°°
            if (arr[x] >= 0.2 and arr[x] < 0.4 and arr[x + 1] >= 0.0 and arr[x + 1] < 0.2):
                tablaFO[2][1] += 1
            if (arr[x] >= 0.2 and arr[x] < 0.4 and arr[x + 1] >= 0.2 and arr[x + 1] < 0.4):
                tablaFO[2][2] += 1
            if (arr[x] >= 0.2 and arr[x] < 0.4 and arr[x + 1] >= 0.4 and arr[x + 1] < 0.6):
                tablaFO[2][3] += 1
            if (arr[x] >= 0.2 and arr[x] < 0.4 and arr[x + 1] >= 0.6 and arr[x + 1] < 0.8):
                tablaFO[2][4] += 1
            if (arr[x] >= 0.2 and arr[x] < 0.4 and arr[x + 1] >= 0.8 and arr[x + 1] < 1):
                tablaFO[2][5] += 1

            # °°°°°° Comparacion de la tercer fila °°°°°°
            if (arr[x] >= 0.4 and arr[x] < 0.6 and arr[x + 1] >= 0.0 and arr[x + 1] < 0.2):
                tablaFO[3][1] += 1
            if (arr[x] >= 0.4 and arr[x] < 0.6 and arr[x + 1] >= 0.2 and arr[x + 1] < 0.4):
                tablaFO[3][2] += 1
            if (arr[x] >= 0.4 and arr[x] < 0.6 and arr[x + 1] >= 0.4 and arr[x + 1] < 0.6):
                tablaFO[3][3] += 1
            if (arr[x] >= 0.4 and arr[x] < 0.6 and arr[x + 1] >= 0.6 and arr[x + 1] < 0.8):
                tablaFO[3][4] += 1
            if (arr[x] >= 0.4 and arr[x] < 0.6 and arr[x + 1] >= 0.8 and arr[x + 1] < 1):
                tablaFO[3][5] += 1

            # °°°°°° Comparacion de la cuarta fila °°°°°°
            if (arr[x] >= 0.6 and arr[x] < 0.8 and arr[x + 1] >= 0.0 and arr[x + 1] < 0.2):
                tablaFO[4][1] += 1
            if (arr[x] >= 0.6 and arr[x] < 0.8 and arr[x + 1] >= 0.2 and arr[x + 1] < 0.4):
                tablaFO[4][2] += 1
            if (arr[x] >= 0.6 and arr[x] < 0.8 and arr[x + 1] >= 0.4 and arr[x + 1] < 0.6):
                tablaFO[4][3] += 1
            if (arr[x] >= 0.6 and arr[x] < 0.8 and arr[x + 1] >= 0.6 and arr[x + 1] < 0.8):
                tablaFO[4][4] += 1
            if (arr[x] >= 0.6 and arr[x] < 0.8 and arr[x + 1] >= 0.8 and arr[x + 1] < 1):
                tablaFO[4][5] += 1

            # °°°°°° Comparacion de la quinta fila °°°°°°
            if (arr[x] >= 0.8 and arr[x] < 1 and arr[x + 1] >= 0.0 and arr[x + 1] < 0.2):
                tablaFO[5][1] += 1
            if (arr[x] >= 0.8 and arr[x] < 1 and arr[x + 1] >= 0.2 and arr[x + 1] < 0.4):
                tablaFO[5][2] += 1
            if (arr[x] >= 0.8 and arr[x] < 1 and arr[x + 1] >= 0.4 and arr[x + 1] < 0.6):
                tablaFO[5][3] += 1
            if (arr[x] >= 0.8 and arr[x] < 1 and arr[x + 1] >= 0.6 and arr[x + 1] < 0.8):
                tablaFO[5][4] += 1
            if (arr[x] >= 0.8 and arr[x] < 1 and arr[x + 1] >= 0.8 and arr[x + 1] < 1):
                tablaFO[5][5] += 1

        # °°°°°° Tabla con el valor de chi cuadrado calculado °°°°°°
        chiTab = [["|=|", "0.0-0.2", "0.2-0.4", "0.4-0.6", "0.6-0.8", "0.8-1.0"],
                  ["0.0-0.2", 0, 0, 0, 0, 0],
                  ["0.2-0.4", 0, 0, 0, 0, 0],
                  ["0.4-0.6", 0, 0, 0, 0, 0],
                  ["0.6-0.8", 0, 0, 0, 0, 0],
                  ["0.8-1.0", 0, 0, 0, 0, 0]]

        chiCalc = 0

        for f in range(1, len(tablaFO)):
            for c in range(1, len(tablaFO)):
                chiCalc += (FE-tablaFO[f][c])**2/FE
                chiTab[f][c] = round((FE-tablaFO[f][c])**2/FE, 5)

        if (chiCalc <= 36.42):
            return "Prueba de unicidad Series" + "\n\n" + str(tabulate(tablaFO,  tablefmt='grid', stralign='center')) + \
                "\n\n" + str(tabulate(chiTab, tablefmt='grid', stralign='center')) + "\n\n" + "El valor de Chi calculado es: " \
                + str(chiCalc) + "\n\n" + "Se acepta la hipotesis" + "\n" + \
                "los datos tiene una distribucion uniforme bidimensional"

        else:
            return "Prubea de unicidad Series" + "\n\n" + str(tabulate(tablaFO,  tablefmt='grid', stralign='center')) + "\n\n" \
                + str(tabulate(chiTab, tablefmt='grid', stralign='center')) + "\n\n" + "El valor de Chi calculado es: " \
                + str(chiCalc) + "\n\n" + "\033[1mNO\033[0m se acepta la hipotesis" + \
                "\n" + "los datos tiene una distribucion uniforme bidimensional"
