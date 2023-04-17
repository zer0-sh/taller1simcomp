# Taller 1 Simulacion
# Johan Muñoz       201958380-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

from decimal import Decimal
from tabulate import tabulate


class PruebaIndependenciaPoker:
    def pruebaPoker(arr, k):
        n = len(arr)
        # tabla de frecuencias  cuando son 3 digitos
        TabF3 = [["Casos", "FO", "FE", "(FO-FE)²/FE"],
                 ["3 dig iguales", 0, n*0.01, 0],
                 ["2 dig iguales", 0, n*0.27, 0],
                 ["3 dig diferentes", 0, n*0.72, 0]]

        if (k == 3):

            for x in arr:
                numAux = round(Decimal(x), 3)

                var = list(str(numAux))
                del var[0:2]

                if (var[0] == var[1] == var[2]):
                    TabF3[1][1] += 1

                if ((var[0] == var[1] and var[0] != var[2]) or
                        var[0] == var[2] and var[0] != var[1] or
                        var[1] == var[2] and var[1] != var[0]):
                    TabF3[2][1] += 1

                if (var[0] != var[1] and var[0] != var[2] and var[1] != var[2]):
                    TabF3[3][1] += 1

            chiCalc3 = 0
            au1 = (TabF3[1][1]-TabF3[1][2])**2 / TabF3[1][2]
            TabF3[1][3] = au1

            au2 = (TabF3[2][1] - TabF3[2][2])**2 / TabF3[2][2]
            TabF3[2][3] = au2

            au3 = (TabF3[3][1] - TabF3[3][2])**2 / TabF3[3][2]
            TabF3[3][3] = au3
            chiCalc3 = au1+au2+au3

            if (chiCalc3 <= 5.99):
                return "Prueba de independecia Poker" + "\n\n" +\
                       str(tabulate(TabF3, tablefmt='grid', stralign='center')) + "\n\n" + "Pasa la prueba de independencia de poker" + "\n" +\
                       "El valor de chi calculado con la prueba de poker es : " + \
                    str(chiCalc3)
            else:
                return "Prueba de independecia Poker" + "\n\n" +\
                       str(tabulate(TabF3, tablefmt='grid', stralign='center')) + "\n\n" + "NO la prueba de independencia de poker" + "\n" +\
                       "El valor de chi calculado con la prueba de poker es : " + \
                    str(chiCalc3)

        # tabla de frecuencias  cunado son 5 digitos
        TabF5 = [["Casos", "FO", "FE", "(FO-FE)²/FE"],
                 ["Todos iguales", 0, n*0.0001, 0],  # ya
                 ["4 iguales", 0, n*0.0045, 0],  # ya
                 ["Full house", 0, n*0.009, 0],
                 ["3 iguales", 0, n*0.072, 0],
                 ["2 pares", 0, n*0.108, 0],
                 ["1 par", 0, n*0.504, 0],
                 ["Todos diferentes", 0, n*0.3024, 0]]

        if (k == 5):

            for x in arr:

                numAux = round(Decimal(x), 5)

                var = list(str(numAux))
                del var[0:2]

                # -------- todas iguales
                if (var[0] == var[1] == var[2] == var[3] == var[4]):
                    TabF5[1][1] += 1

                # -------- 4 iguaales y 1 diferente
                elif ((var[0] == var[1] == var[2] == var[3] and var[0] != var[4] and var[1] != var[4] and var[2] != var[4] and var[3] != var[4]) or
                      (var[0] == var[1] == var[2] == var[4] and var[0] != var[3] and var[1] != var[3] and var[2] != var[3] and var[4] != var[3]) or
                        (var[0] == var[1] == var[3] == var[4] and var[0] != var[2] and var[1] != var[2] and var[3] != var[2] and var[4] != var[2]) or
                        (var[0] == var[2] == var[3] == var[4] and var[0] != var[1] and var[2] != var[1] and var[3] != var[1] and var[4] != var[1]) or
                        (var[1] == var[2] == var[3] == var[4] and var[1] != var[0] and var[2] != var[0] and var[2] != var[0] and var[4] != var[0])):
                    TabF5[2][1] += 1

                # -------- 3 iguales y 2 iguales
                elif ((var[0] == var[1] == var[2] and var[3] == var[4] and var[0] != var[3]) or
                      (var[0] == var[1] == var[3] and var[2] == var[4] and var[0] != var[2]) or
                      (var[0] == var[1] == var[4] and var[2] == var[3] and var[0] != var[2]) or
                      (var[0] == var[2] == var[4] and var[1] == var[3] and var[0] != var[1]) or
                      (var[0] == var[3] == var[4] and var[1] == var[2] and var[0] != var[1]) or
                      (var[1] == var[3] == var[4] and var[0] == var[2] and var[1] != var[0]) or
                      (var[2] == var[3] == var[4] and var[0] == var[1] and var[2] != var[0]) or
                      (var[1] == var[2] == var[3] and var[0] == var[4] and var[1] != var[0]) or
                      (var[1] == var[2] == var[4] and var[0] == var[3] and var[1] != var[0]) or
                      (var[0] == var[2] == var[3] and var[1]
                       == var[4] and var[0] != var[1])
                      ):
                    TabF5[3][1] += 1

                # 3 iguales y 2 diferentes
                elif ((var[0] == var[1] == var[2] and var[3] != var[4]) or
                        (var[0] == var[1] == var[3] and var[2] != var[4]) or
                        (var[0] == var[1] == var[4] and var[2] != var[3]) or
                        (var[0] == var[2] == var[4] and var[1] != var[3]) or
                        (var[0] == var[3] == var[4] and var[1] != var[2]) or
                        (var[1] == var[3] == var[4] and var[0] != var[2]) or
                        (var[2] == var[3] == var[4] and var[0] != var[1]) or
                        (var[1] == var[2] == var[3] and var[0] != var[4]) or
                        (var[1] == var[2] == var[4] and var[0] != var[3]) or
                        (var[0] == var[2] == var[3] and var[1] != var[4])
                      ):
                    TabF5[4][1] += 1

                # 2 pares y una difernte
                elif (
                        (var[0] == var[1] and var[2] == var[3] and var[4] != var[0] != var[2]) or
                        (var[0] == var[1] and var[2] == var[4] and var[3] != var[0] != var[2]) or
                        (var[0] == var[1] and var[3] == var[4] and var[2] != var[0] != var[3]) or
                        (var[0] == var[2] and var[3] == var[4] and var[1] != var[0] != var[3]) or
                        (var[1] == var[2] and var[3] == var[4] and var[0] != var[1] != var[3]) or

                        (var[0] == var[2] and var[1] == var[3] and var[4] != var[0] != var[1]) or
                        (var[0] == var[2] and var[1] == var[4] and var[3] != var[0] != var[1]) or
                        (var[0] == var[3] and var[1] == var[4] and var[2] != var[0] != var[1]) or
                        (var[0] == var[3] and var[2] == var[4] and var[1] != var[0] != var[2]) or
                        (var[1] == var[3] and var[2] == var[4] and var[0] != var[1] != var[2]) or

                        (var[0] == var[3] and var[1] == var[2] and var[4] != var[0] != var[1]) or
                        (var[0] == var[4] and var[1] == var[2] and var[3] != var[0] != var[1]) or
                        (var[0] == var[4] and var[1] == var[3] and var[2] != var[0] != var[1]) or
                        (var[0] == var[4] and var[2] == var[3] and var[1] != var[0] != var[2]) or
                        (var[1] == var[4] and var[2] == var[3] and var[0] != var[1] != var[2]) or

                        (var[0] == var[2] and var[1] == var[3] and var[4] != var[0] != var[1]) or
                        (var[0] == var[2] and var[1] == var[4] and var[3] != var[0] != var[1]) or
                        (var[0] == var[3] and var[1] == var[4] and var[2] != var[0] != var[1]) or
                        (var[0] == var[3] and var[2] == var[4] and var[1] != var[0] != var[2]) or
                        (var[1] == var[3] and var[2] == var[4]
                         and var[0] != var[1] != var[2])
                ):

                    TabF5[5][1] += 1

                # 2 iguales y 3 diferentes
                elif ((var[0] != var[1] != var[2] and var[3] == var[4]) or
                        (var[0] != var[1] != var[3] and var[2] == var[4]) or
                        (var[0] != var[1] != var[4] and var[2] == var[3]) or
                        (var[0] != var[2] != var[4] and var[1] == var[3]) or
                        (var[0] != var[3] != var[4] and var[1] == var[2]) or
                        (var[1] != var[3] != var[4] and var[0] == var[2]) or
                        (var[2] != var[3] != var[4] and var[0] == var[1]) or
                        (var[1] != var[2] != var[3] and var[0] == var[4]) or
                        (var[1] != var[2] != var[4] and var[0] == var[3]) or
                        (var[0] != var[2] != var[3] and var[1] == var[4])
                      ):
                    TabF5[6][1] += 1

                # todas diferentes
                elif ((var[0] != var[1] and var[0] != var[2] and var[0] != var[3] and var[0] != var[4]) and
                      (var[1] != var[2] and var[1] != var[3] and var[1] != var[4]) and
                      (var[2] != var[3] and var[2] != var[4]) and
                        (var[3] != var[4])):
                    TabF5[7][1] += 1

            chiCalc5 = 0
            au4 = (TabF5[1][1] - TabF5[1][2])**2 / TabF5[1][2]
            TabF5[1][3] = au4

            au5 = (TabF5[2][1] - TabF5[2][2])**2 / TabF5[2][2]
            TabF5[2][3] = au5

            au6 = (TabF5[3][1] - TabF5[3][2])**2 / TabF5[3][2]
            TabF5[3][3] = au6

            au7 = (TabF5[4][1] - TabF5[4][2])**2 / TabF5[4][2]
            TabF5[4][3] = au7

            au8 = (TabF5[5][1] - TabF5[5][2])**2 / TabF5[5][2]
            TabF5[5][3] = au8

            au9 = (TabF5[6][1] - TabF5[6][2])**2 / TabF5[6][2]
            TabF5[6][3] = au9

            au10 = (TabF5[7][1] - TabF5[7][2])**2 / TabF5[7][2]
            TabF5[7][3] = au10

            chiCalc5 = au4 + au5 + au6 + au7 + au8 + au9 + au10

            if (chiCalc5 > 12.99):
                return "Prueba de independecia Poker" + "\n\n" +\
                       str(tabulate(TabF5, tablefmt='grid', stralign='center')) + "\n\n" + "Pasa la prueba de independencia de poker" + "\n" +\
                       "El valor de chi calculado con la prueba de poker es : " + \
                    str(chiCalc5)
            else:
                return "Prueba de independecia Poker" + "\n\n" + \
                       str(tabulate(TabF5, tablefmt='grid',
                                    stralign='center')) + "\n\n" + "Pasa la prueba de independencia de poker" + "\n" + \
                       "El valor de chi calculado con la prueba de poker es : " + \
                    str(chiCalc5)
