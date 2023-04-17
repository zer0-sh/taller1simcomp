# Taller 1 Simulacion
# Johan Muñoz       201958383-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

from tkinter import *
from PIL import ImageTk

import GeneradorEstandarMinimo
import PruebaIndependenciaPoker
import PruebaUniChi
import PruebaUnicidadKolmogorov
import pruebaCorrido
import pruebaUnicidadSerie

# ----- Clase GUI_EstandarMinimo -----


class GUI_EstandarMinimo:

    def __init__(self, root_GUIEM):
        self.root_GUIEM = root_GUIEM
        self.root_GUIEM.title("Generador estandar minimo")
        self.root_GUIEM.resizable(False, False)
        ancho_ventana = 1000
        alto_ventana = 650
        ancho_pantalla = root_GUIEM.winfo_screenwidth()
        alto_pantalla = root_GUIEM.winfo_screenheight()
        x_ventana = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y_ventana = (alto_pantalla // 2) - (alto_ventana // 2)
        self.root_GUIEM.geometry(
            f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

        # ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo02.jpg")
        Label(self.root_GUIEM, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # ----- Frame -----
        self.frameEM = Frame(self.root_GUIEM, bg="gray1")
        self.frameEM.place(x=0, y=0)

        x_frame = (ancho_ventana // 2) - (900 // 2)
        y_frame = (alto_ventana // 2) - (600 // 2)
        self.frameEM.place(x=x_frame, y=y_frame, width=900, height=600)

        # ----- Titulo -----
        Titulo = Label(self.frameEM, text="Generador Estandar Minino", font=(
            "Agency FB", 30, "bold"), bg="gray1", fg="darkgoldenrod1")
        Titulo.place(relx=0.5, rely=0.08, anchor=CENTER)

        # ----- Entradas Xn, a, m -----
        Label(self.frameEM, text="a", font=("Agency FB", 16, "bold"),
              bg="gray1", fg="white").place(x=80, y=83)
        self.a = Entry(self.frameEM, font=("Agency FB", 16), width=9)
        self.a.place(x=110, y=85)

        Label(self.frameEM, text="Xn", font=("Agency FB", 16, "bold"),
              bg="gray1", fg="white").place(x=210, y=83)
        self.xn = Entry(self.frameEM, font=("Agency FB", 16), width=9)
        self.xn.place(x=240, y=85)

        Label(self.frameEM, text="m", font=("Agency FB", 16, "bold"),
              bg="gray1", fg="white").place(x=340, y=83)
        self.m = Entry(self.frameEM, font=("Agency FB", 16), width=9)
        self.m.place(x=370, y=85)

        # ----- Boton generar (OK) -----
        BotonOk = Button(self.frameEM, text="Ok", command=self.generadorEM, font=(
            "Agency FB", 12, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2")
        BotonOk.place(x=650, y=85, width=40)

        # ----- Pruebas de uniformidad -----
        Label(self.frameEM, text="Pruebas de uniformidad:", font=(
            "Agency FB", 15, "bold"), bg="gray1", fg="white").place(x=50, y=140)

        # ----- Boton prueba de chi_cuadrado -----
        BotonChi = Button(self.frameEM, text="Chi χ²", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaChiCuadrado)
        BotonChi.place(x=90, y=183, width=150)

        # ----- Boton prueba de kolmogorov -----
        BotonKo = Button(self.frameEM, text="Kolmogorov", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaKolmogorov)
        BotonKo.place(x=90, y=240, width=150)

        # ----- Pruebas de independencia -----
        Label(self.frameEM, text="Pruebas de independencia:", font=(
            "Agency FB", 15, "bold"), bg="gray1", fg="white").place(x=50, y=300)

        # ----- Boton prueba de corridas -----
        BotonCo = Button(self.frameEM, text="Corridas", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaCorridas)
        BotonCo.place(x=90, y=340, width=150)

        # ----- Boton prueba series -----
        BotonSe = Button(self.frameEM, text="Series", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaSeries)
        BotonSe.place(x=90, y=400, width=150)

        # ----- Boton prueba poker -----
        BotonPo = Button(self.frameEM, text="Poker", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.pruebaPoker)
        BotonPo.place(x=60, y=460, width=120)
        opcions = ["3", "4", "5"]
        self.variable = StringVar(self.frameEM)
        self.variable.set(opcions[0])
        w = OptionMenu(self.frameEM, self.variable, *opcions)
        w.config(width=5)
        w.place(x=200, y=460)

        # ----- Boton lineal congruente -----
        BotonVolv = Button(self.frameEM, text="Lineal congruente", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.abrirLC)
        BotonVolv.place(x=25, y=530, width=120)

        # ----- Boton random -----
        BotonVolv = Button(self.frameEM, text="Random", font=(
            "Agency FB", 13, "bold"), bg="darkgoldenrod1", fg="white", bd=5, cursor="hand2", command=self.abrirPoker)
        BotonVolv.place(x=150, y=530, width=120)

        # ----- Botón menú principal -----
        BotonInfo = Button(self.frameEM, text="Menú", font=(
            "Agency FB", 13, "bold"), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.abrirMenu)
        BotonInfo.place(x=275, y=530, width=90)

    def pruebaChiCuadrado(self):
        self.text = Text(self.frameEM)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(
            xn, xn, a, m)
        datos = PruebaUniChi.PruebaUniChi.pruChi(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

    def pruebaKolmogorov(self):
        self.text = Text(self.frameEM)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(
            xn, xn, a, m)
        datos = PruebaUnicidadKolmogorov.PruebaUnicidadKolmogorov.pruebaKolmogorov(
            arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

    def pruebaCorridas(self):
        self.text = Text(self.frameEM)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(
            xn, xn, a, m)
        datos = pruebaCorrido.pruebaCorrido.corrido(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

    def pruebaSeries(self):
        self.text = Text(self.frameEM)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(
            xn, xn, a, m)
        datos = pruebaUnicidadSerie.pruebaUnicidadSerie.pruebaSerie(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

    def pruebaPoker(self):
        self.text = Text(self.frameEM)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        k = int(self.variable.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(
            xn, xn, a, m)
        datos = PruebaIndependenciaPoker.PruebaIndependenciaPoker.pruebaPoker(
            arreglo, k)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray1", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

    def abrirLC(self):
        self.root_GUIEM.destroy()
        import GUI_GeneradorLinealCongruente as LC
        LC.iniciar()

    def abrirMenu(self):
        self.root_GUIEM.destroy()
        import GUI_Inicio as GIN
        GIN.iniciar()

    def abrirPoker(self):
        self.root_GUIEM.destroy()
        import GUIrandomPython as GR
        GR.iniciar()

    def generadorEM(self):
        self.text = Text(self.frameEM)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = (
            GeneradorEstandarMinimo.GeneradorEstandar.paraTablas(xn, xn, a, m))
        self.text.insert(INSERT, arreglo)
        self.text.config(width=35, height=25, state="disable",
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=450, y=150)


def iniciar():
    root_GUIEM = Tk()
    obj = GUI_EstandarMinimo(root_GUIEM)
    root_GUIEM.mainloop()
