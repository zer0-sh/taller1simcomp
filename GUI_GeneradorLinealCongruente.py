# Taller 1 Simulacion
# Johan Muñoz       201958380-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

from tkinter import *
from PIL import ImageTk
from GeneradorLineal import *
from PruebaIndependenciaPoker import *
from PruebaUniChi import *
from PruebaUnicidadKolmogorov import *
from pruebaCorrido import *
from pruebaUnicidadSerie import *

# ----- Clase GUI_GeneradorLinealCongruente -----


class GUI_GeneradorLinealCongruente:

    def __init__(self, root_GUIGLC):
        self.root_GUIGLC = root_GUIGLC
        self.root_GUIGLC.title("Generador lineal congruente")
        self.root_GUIGLC.resizable(False, False)
        ancho_ventana = 1200
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
        self.frameGLC = Frame(self.root_GUIGLC, bg="gray18")
        self.frameGLC.place(x=0, y=0)

        x_frame = (ancho_ventana // 2) - (1100 // 2)
        y_frame = (alto_ventana // 2) - (600 // 2)
        self.frameGLC.place(x=x_frame, y=y_frame, width=1100, height=600)

        # ----- Titulo -----
        Label(self.frameGLC, text="Generador Lineal Congruente", font=(
            "times", 18, "bold"), bg="gray18", fg="navajowhite4").place(x=45, y=30)

        # ----- Entradas Xn, a, c, m -----
        Label(self.frameGLC, text="a", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=30, y=80)
        self.a = Entry(self.frameGLC, font=("times", 16), width=9)
        self.a.place(x=55, y=82)

        Label(self.frameGLC, text="Xn", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=185, y=80)
        self.xn = Entry(self.frameGLC, font=("times", 16), width=9)
        self.xn.place(x=225, y=82)

        Label(self.frameGLC, text="c", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=350, y=80)
        self.c = Entry(self.frameGLC, font=("times", 16), width=9)
        self.c.place(x=375, y=82)

        Label(self.frameGLC, text="m", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=495, y=80)
        self.m = Entry(self.frameGLC, font=("times", 16), width=9)
        self.m.place(x=525, y=82)

        # ----- Boton generar (OK) -----
        BotonOk = Button(self.frameGLC, text="Ok", command=self.generadorLineal, font=(
            "times", 13), bg="navajowhite4", fg="white", bd=5, cursor="hand2")
        BotonOk.place(x=660, y=75, width=50)

        # ----- Pruebas de uniformidad -----
        Label(self.frameGLC, text="Pruebas de uniformidad:", font=(
            "times", 13, ), bg="gray18", fg="white").place(x=50, y=140)

        # ----- Boton prueba de chi_cuadrado -----
        BotonChi = Button(self.frameGLC, text="Chi χ²", font=(
            "times", 13), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pruebaChiCuadrado)
        BotonChi.place(x=90, y=180, width=150)

        # ----- Boton prueba de kolmogorov -----
        BotonKo = Button(self.frameGLC, text="Kolmogorov", font=(
            "times", 13), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pKolmo)
        BotonKo.place(x=90, y=240, width=150)

        # ----- Pruebas de independencia -----
        Label(self.frameGLC, text="Pruebas de independencia:", font=(
            "times", 13, ), bg="gray18", fg="white").place(x=50, y=300)

        # ----- Boton prueba de corridas -----
        BotonCo = Button(self.frameGLC, text="Corridas", font=(
            "times", 13), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pruebaCorridas)
        BotonCo.place(x=90, y=340, width=150)

        # ----- Boton Prueba Series -----
        BotonSe = Button(self.frameGLC, text="Series", font=(
            "times", 13), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pruebaSeries)
        BotonSe.place(x=90, y=400, width=150)

        # ----- Boton Prueba Poker -----
        BotonPo = Button(self.frameGLC, text="Poker", font=(
            "times", 13), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pruebaPoker)
        BotonPo.place(x=60, y=460, width=120)
        opcions = ["3", "4", "5"]
        self.variable = StringVar(self.frameGLC)
        self.variable.set(opcions[0])
        w = OptionMenu(self.frameGLC, self.variable, *opcions)
        w.config(width=5)
        w.place(x=200, y=460)

        # ----- Boton Estandar Minimo -----
        BotonVolv = Button(self.frameGLC, text="Estandar Mínimo", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.abrirEM)
        BotonVolv.place(x=25, y=530, width=170)

        # ----- Botón Menú Principal -----
        BotonInfo = Button(self.frameGLC, text="Menú", font=(
            "times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.abrirMenu)
        BotonInfo.place(x=283, y=530, width=67)

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
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

    def pKolmo(self):
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
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

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
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

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
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

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
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)

    def abrirEM(self):
        self.root_GUIGLC.destroy()
        import GUIEstandarMinimo as GEM
        GEM.iniciar()

    def abrirMenu(self):
        self.root_GUIGLC.destroy()
        import GUI_Inicio as GIN
        GIN.iniciar()

    def abrirPruebas(self):
        self.root_GUIGLC.destroy()
        import GUIPruebasLC as GP
        GP.iniciar()

    def generadorLineal(self):
        self.text = Text(self.frameGLC)
        a = int(self.a.get())
        xn = int(self.xn.get())
        c = int(self.c.get())
        m = int(self.m.get())
        arreglo = GeneradorLineal.paraTabla(xn, xn, a, c, m)
        self.text.insert(INSERT, arreglo)
        self.text.config(width=35, height=25, state="disable",
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=600, y=250)


def iniciar():
    root_GUIGLC = Tk()
    obj = GUI_GeneradorLinealCongruente(root_GUIGLC)
    root_GUIGLC.mainloop()
