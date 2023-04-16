import math as mt

class pruebaCorrido:

    def corrido(arr):
        n=len(arr)
        simbolos = []
        # El numero minimo de corridas es 1
        cantCorridas = 1

        tamanio = 0
        tamanio2 = 0
        tamanioCorridas = []

        # Si la x es igual a cero (primera posicion) de los datos,
        # se pone un asterisco para iniciar a contar las corridas

        for x in range(len(arr)):
            if (x == 0):
                simbolos.append("*")

            else:
                if (arr[x - 1] <= arr[x]):
                    simbolos.append("+")
                    if (tamanio2 != 0):
                        tamanioCorridas.append(tamanio2)
                    tamanio2 = 0
                    tamanio +=1
                else:
                    simbolos.append("-")
                    if (tamanio != 0):
                        tamanioCorridas.append(tamanio)
                    tamanio = 0
                    tamanio2 +=1

            if (simbolos[x] != simbolos[x - 1] and x != 1):
                cantCorridas += 1

        print("Tamaño de corridas :")
        print (tamanioCorridas)
        arreglo = []
        arreglo.append(pruebaCorrido.contar(tamanioCorridas))


        #Calculo de la media
        media =  (2*n-1)/3

        # Calculo de la varianza
        varianza = (16*n-29)/90

        #Calculo del Z obtenido
        zObs = (cantCorridas-media)/mt.sqrt(varianza)

        #Comparar el Z obtenido con el Z Critico para comprobar si pasa la prueba
        # de corridas
        if(zObs>= -1.96 and zObs<= 1.96 ):

            return "Prueba de Independencia Corridas" + "\n\n" + "\n\nLa cantidad de corridas es: " + str(
                cantCorridas) + "\n" + "\nLa media es: " + str(media) + "\nLa varianza es: " + str(varianza) + "\nEl Z obtenido es: " + str(zObs) + "\nNo hay evidencia para rechazar la hipotesis de independencia." + "\n" +"Simbolos de la corrida :\n\n" + str(simbolos)

        else:

            return "Prueba de independecia Corridas" + "\n\n" + "\nLa cantidad de corridas es: " + str(
                cantCorridas) + "\n" + "\nLa media es: " + str(media) + "\nLa varianza es: " + str(
                varianza) + "\nEl Z obtenido es: " + str(zObs) + "\nNo pasa la prueba de independencia." + "\nSimbolos de la corrida :\n" + str(simbolos)

    def contar(arr):
        arr = list(arr)
        a = {x: arr.count(x) for x in arr}

        for x in a:
            print("Cadenas de tamaño ", x ,": ", a[x])

    print("")