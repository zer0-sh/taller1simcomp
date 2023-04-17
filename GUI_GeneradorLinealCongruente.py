# Taller 1 Simulacion
# Johan Muñoz       201958383-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

from tkinter import *
from PIL import ImageTk

import GeneradorLineal
import PruebaIndependenciaPoker
import PruebaUniChi
import PruebaUnicidadKolmogorov
import pruebaCorrido
import pruebaUnicidadSerie

# ----- Clase GUI_GeneradorLinealCongruente -----


class GUI_GeneradorLinealCongruente:

    def __init__(self, root_GUIGLC):
        self.root_GUIGLC = root_GUIGLC
        self.root_GUIGLC.title("Generador lineal congruente")
        self.root_GUIGLC.resizable(False, False)
        ancho_ventana = 1000
        alto_ventana = 650
        ancho_pantalla = root_GUIGLC.winfo_screenwidth()
        alto_pantalla = root_GUIGLC.winfo_screenheight()
        x_ventana = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y_ventana = (alto_pantalla // 2) - (alto_ventana // 2)
        self.root_GUIGLC.geometry(
            f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

        # ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo02.jpg")
        Label(self.root_GUIGLC, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # ----- Frame -----
        self.frameGLC = Frame(self.root_GUIGLC, bg="gray1")
        self.frameGLC.place(x=0, y=0)

        x_frame = (ancho_ventana // 2) - (900 // 2)
        y_frame = (alto_ventana // 2) - (600 // 2)
        self.frameGLC.place(x=x_frame, y=y_frame, width=900, height=600)

        # ----- Titulo -----
        Titulo = Label(self.frameGLC, text="Generador Lineal Congruente", font=(
            "Agency FB", 30, "bold"), bg="gray1", fg="darkgoldenrod1")
        Titulo.place(relx=0.5, rely=0.08, anchor=CENTER)

        # ----- Entradas Xn, a, c, m -----
        Label(self.frameGLC, text="a", font=("Agency FB", 16, "bold"),
              bg="gray1", fg="white").place(x=80, y=83)
        self.a = Entry(self.frameGLC, font=("Agency FB", 16), width=9)
        self.a.place(x=110, y=85)

        Label(self.frameGLC, text="Xn", font=("Agency FB", 16, "bold"),
              bg="gray1", fg="white").place(x=210, y=83)
        self.xn = Entry(self.frameGLC, font=("Agency FB", 16), width=9)
        self.xn.place(x=240, y=85)

        Label(self.frameGLC, text="c", font=("Agency FB", 16, "bold"),
              bg="gray1", fg="white").place(x=340, y=83)
        self.c = Entry(self.frameGLC, font=("Agency FB", 16), width=9)
        self.c.place(x=370, y=85)

        Label(self.frameGLC, text="m", font=("Agency FB", 16, "bold"),
              bg="gray1", fg="white").place(x=470, y=83)
        self.m = Entry(self.frameGLC, font=("Agency FB", 16), width=9)
        self.m.place(x=500, y=85)

        # ----- Boton generar (OK) -----
        BotonOk = Button(self.frameGLC, text="Ok", command=self.generadorLineal, font=(
            "Agency FB", 12, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2")
        BotonOk.place(x=650, y=85, width=40)

        # ----- Pruebas de uniformidad -----
        Label(self.frameGLC, text="Pruebas de uniformidad:", font=(
            "Agency FB", 15, "bold"), bg="gray1", fg="white").place(x=50, y=140)

        # ----- Boton prueba de chi_cuadrado -----
        BotonChi = Button(self.frameGLC, text="Chi χ²", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaChiCuadrado)
        BotonChi.place(x=90, y=183, width=150)

        # ----- Boton prueba de kolmogorov -----
        BotonKo = Button(self.frameGLC, text="Kolmogorov", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaKolmogorov)
        BotonKo.place(x=90, y=240, width=150)

        # ----- Pruebas de independencia -----
        Label(self.frameGLC, text="Pruebas de independencia:", font=(
            "Agency FB", 15, "bold"), bg="gray1", fg="white").place(x=50, y=300)

        # ----- Boton prueba de corridas -----
        BotonCo = Button(self.frameGLC, text="Corridas", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaCorridas)
        BotonCo.place(x=90, y=340, width=150)

        # ----- Boton prueba series -----
        BotonSe = Button(self.frameGLC, text="Series", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaSeries)
        BotonSe.place(x=90, y=400, width=150)

        # ----- Boton prueba poker -----
        BotonPo = Button(self.frameGLC, text="Poker", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaPoker)
        BotonPo.place(x=60, y=460, width=120)
        opcions = ["3", "4", "5"]
        self.variable = StringVar(self.frameGLC)
        self.variable.set(opcions[0])
        w = OptionMenu(self.frameGLC, self.variable, *opcions)
        w.config(width=5)
        w.place(x=200, y=460)

        # ----- Boton estandar minimo -----
        BotonVolv = Button(self.frameGLC, text="Estandar Minimo", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.abrirEM)
        BotonVolv.place(x=25, y=530, width=120)

        # ----- Boton random -----
        BotonVolv = Button(self.frameGLC, text="Random", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.abrirPoker)
        BotonVolv.place(x=150, y=530, width=120)

        # ----- Botón menú principal -----
        BotonInfo = Button(self.frameGLC, text="Menú", font=(
            "Agency FB", 13, "bold"), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.abrirMenu)
        BotonInfo.place(x=275, y=530, width=90)

    def pruebaChiCuadrado(self):
        self.text = Text(self.frameGLC)
        a = int(self.a.get())
        xn = int(self.xn.get())
        c = int(self.c.get())
        m = int(self.m.get())
        arreglo = GeneradorLineal.GeneradorLineal.genLinCongruente(
            xn, xn, a, c, m)
        datos = PruebaUniChi.PruebaUniChi.pruChi(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)

    def pruebaKolmogorov(self):
        self.text = Text(self.frameGLC)
        a = int(self.a.get())
        xn = int(self.xn.get())
        c = int(self.c.get())
        m = int(self.m.get())
        arreglo = GeneradorLineal.GeneradorLineal.genLinCongruente(
            xn, xn, a, c, m)
        datos = PruebaUnicidadKolmogorov.PruebaUnicidadKolmogorov.pruebaKolmogorov(
            arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)

    def pruebaCorridas(self):
        self.text = Text(self.frameGLC)
        a = int(self.a.get())
        xn = int(self.xn.get())
        c = int(self.c.get())
        m = int(self.m.get())
        arreglo = GeneradorLineal.GeneradorLineal.genLinCongruente(
            xn, xn, a, c, m)
        nc = pruebaCorrido.pruebaCorrido.contar(arreglo)
        print(nc)
        datos = pruebaCorrido.pruebaCorrido.corrido(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)

    def pruebaSeries(self):
        self.text = Text(self.frameGLC)
        a = int(self.a.get())
        xn = int(self.xn.get())
        c = int(self.c.get())
        m = int(self.m.get())
        arreglo = GeneradorLineal.GeneradorLineal.genLinCongruente(
            xn, xn, a, c, m)
        datos = pruebaUnicidadSerie.pruebaUnicidadSerie.pruebaSerie(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)

    def pruebaPoker(self):
        self.text = Text(self.frameGLC)
        a = int(self.a.get())
        xn = int(self.xn.get())
        c = int(self.c.get())
        m = int(self.m.get())
        k = int(self.variable.get())
        arreglo = GeneradorLineal.GeneradorLineal.genLinCongruente(
            xn, xn, a, c, m)
        datos = PruebaIndependenciaPoker.PruebaIndependenciaPoker.pruebaPoker(
            arreglo, k)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=400, y=150)

    def abrirEM(self):
        self.root_GUIGLC.destroy()
        import GUI_EstandarMinimo as GEM
        GEM.iniciar()

    def abrirMenu(self):
        self.root_GUIGLC.destroy()
        import GUI_Inicio as GIN
        GIN.iniciar()

    def abrirPoker(self):
        self.root_GUIGLC.destroy()
        import GUIrandomPython as GR
        GR.iniciar()

    def generadorLineal(self):
        self.text = Text(self.frameGLC)
        a = int(self.a.get())
        xn = int(self.xn.get())
        c = int(self.c.get())
        m = int(self.m.get())
        arreglo = GeneradorLineal.paraTabla(xn, xn, a, c, m)
        self.text.insert(INSERT, arreglo)
        self.text.config(width=35, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=450, y=150)


def iniciar():
    root_GUIGLC = Tk()
    obj = GUI_GeneradorLinealCongruente(root_GUIGLC)
    root_GUIGLC.mainloop()
