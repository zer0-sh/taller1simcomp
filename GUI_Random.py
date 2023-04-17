# Taller 1 Simulacion
# Johan Muñoz       201958380-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

from tkinter import *
from PIL import ImageTk

import GeneradorRandom
import PruebaPoker
import PruebaChiCuadrado
import PruebaKolmogorov
import PruebaCorrido
import PruebaSeries


# ----- Clase GUI_Random -----


class GUI_Random:

    def __init__(self, root_GUIPR):
        self.root_GUIPR = root_GUIPR
        self.root_GUIPR.title("Generador de Numeros Random")
        self.root_GUIPR.resizable(False, False)
        ancho_ventana = 1100
        alto_ventana = 650
        ancho_pantalla = root_GUIPR.winfo_screenwidth()
        alto_pantalla = root_GUIPR.winfo_screenheight()
        x_ventana = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y_ventana = (alto_pantalla // 2) - (alto_ventana // 2)
        self.root_GUIPR.geometry(
            f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

        # ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo02.jpg")
        Label(self.root_GUIPR, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # ----- Frame -----
        self.framePR = Frame(self.root_GUIPR, bg="gray1")
        self.framePR.place(x=0, y=0)

        x_frame = (ancho_ventana // 2) - (1000 // 2)
        y_frame = (alto_ventana // 2) - (600 // 2)
        self.framePR.place(x=x_frame, y=y_frame, width=1000, height=600)

        # ----- Titulo -----
        Titulo = Label(self.framePR, text="Generador Random", font=(
            "Agency FB", 30, "bold"), bg="gray1", fg="darkgoldenrod1")
        Titulo.place(relx=0.5, rely=0.08, anchor=CENTER)

        # ----- Campo entrada -----
        Label(self.framePR, text="Entrada", font=("times", 14,
              "bold"), bg="gray1", fg="white").place(x=80, y=83)
        self.cuadro = Entry(self.framePR, font=("times", 16), width=15)
        self.cuadro.place(x=200, y=85)

        # ----- Boton Ok -----
        BotonOk = Button(self.framePR, text="Ok", command=self.randoms, font=(
            "Agency FB", 12, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2")
        BotonOk.place(x=650, y=85, width=40)

        # ----- Pruebas de uniformidad -----
        Label(self.framePR, text="Pruebas de uniformidad:", font=(
            "Agency FB", 15, "bold"), bg="gray1", fg="white").place(x=50, y=140)

        # ----- Boton prueba de chi_cuadrado -----
        BotonChi = Button(self.framePR, text="Chi χ²", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaChiCuadrado)
        BotonChi.place(x=90, y=183, width=150)

        # ----- Boton prueba de kolmogorov -----
        BotonKo = Button(self.framePR, text="Kolmogorov", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaKolmogorov)
        BotonKo.place(x=90, y=240, width=150)

        # ----- Pruebas de independencia -----
        Label(self.framePR, text="Pruebas de independencia:", font=(
            "Agency FB", 15, "bold"), bg="gray1", fg="white").place(x=50, y=300)

        # ----- Boton prueba de corridas -----
        BotonCo = Button(self.framePR, text="Corridas", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaCorridas)
        BotonCo.place(x=90, y=340, width=150)

        # ----- Boton prueba series -----
        BotonSe = Button(self.framePR, text="Series", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaSeries)
        BotonSe.place(x=90, y=400, width=150)

        # ----- Boton prueba poker -----
        BotonPo = Button(self.framePR, text="Poker", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaPoker)
        BotonPo.place(x=60, y=460, width=120)
        opcions = ["3", "4", "5"]
        self.variable = StringVar(self.framePR)
        self.variable.set(opcions[0])
        w = OptionMenu(self.framePR, self.variable, *opcions)
        w.config(width=5)
        w.place(x=200, y=460)

        # ----- Boton estandar minimo -----
        BotonVolv = Button(self.framePR, text="Estandar Minimo", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.abrirEM)
        BotonVolv.place(x=25, y=530, width=120)

        # ----- Boton lineal congruente -----
        BotonVolv = Button(self.framePR, text="Lineal congruente", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.abrirLC)
        BotonVolv.place(x=150, y=530, width=120)

        # ----- Botón Menú Principal -----
        BotonInfo = Button(self.framePR, text="Menú", font=(
            "times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.abrirMenu)
        BotonInfo.place(x=275, y=530, width=90)

    def abrirMenu(self):
        self.root_GUIPR.destroy()
        import GUI_Inicio as GIN
        GIN.iniciar()

    def abrirEM(self):
        self.root_GUIPR.destroy()
        import GUI_EstandarMinimo as GEM
        GEM.iniciar()

    def abrirLC(self):
        self.root_GUIPR.destroy()
        import GUI_GeneradorLinealCongruente as LC
        LC.iniciar()

    def randoms(self):
        self.text = Text(self.framePR)
        x = int(self.cuadro.get())
        mostrar = (GeneradorRandom.pyRandom.tabla(x))
        self.text.insert(INSERT, mostrar)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=450, y=150)

    def pruebaChiCuadrado(self):
        self.text = Text(self.framePR)
        x = int(self.cuadro.get())
        arreglo = GeneradorRandom.pyRandom.arreglo(x)
        datos = PruebaChiCuadrado.PruebaUniChi.pruChi(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)

    def pruebaKolmogorov(self):
        self.text = Text(self.framePR)
        x = int(self.cuadro.get())
        arreglo = GeneradorRandom.pyRandom.arreglo(x)
        datos = PruebaKolmogorov.PruebaUnicidadKolmogorov.pruebaKolmogorov(
            arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)

    def pruebaCorridas(self):
        self.text = Text(self.framePR)
        x = int(self.cuadro.get())
        arreglo = GeneradorRandom.pyRandom.arreglo(x)
        nc = PruebaCorrido.pruebaCorrido.contar(arreglo)
        print(nc)
        datos = PruebaCorrido.pruebaCorrido.corrido(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)

    def pruebaSeries(self):
        self.text = Text(self.framePR)
        x = int(self.cuadro.get())
        arreglo = GeneradorRandom.pyRandom.arreglo(x)
        datos = PruebaSeries.pruebaUnicidadSerie.pruebaSerie(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)

    def pruebaPoker(self):
        self.text = Text(self.framePR)
        x = int(self.cuadro.get())
        arreglo = GeneradorRandom.pyRandom.arreglo(x)
        k = int(self.variable.get())
        datos = PruebaPoker.PruebaIndependenciaPoker.pruebaPoker(
            arreglo, k)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)


def iniciar():
    root_GUIPR = Tk()
    obj = GUI_Random(root_GUIPR)
    root_GUIPR.mainloop()
