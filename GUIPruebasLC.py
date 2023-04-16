import tkinter.ttk
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

import GeneradorLineal
import PruebaIndependenciaPoker
import PruebaUniChi
import PruebaUnicidadKolmogorov
import pruebaCorrido
import pruebaUnicidadSerie


# ----- ClaseGUIP -----
class GUIP:

    def __init__(self, rootGUIP):
        self.rootGUIP = rootGUIP
        self.rootGUIP.title("Generador de Números Pseaudoleatorios")
        self.rootGUIP.geometry("1366x768")
        self.rootGUIP.resizable(1, 1)

# ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo01.jpg")
        Label(self.rootGUIP, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

# ****** Frame 1 GUI Pruebas ******
        self.frameP1 = Frame(self.rootGUIP, bg="gray18")
        self.frameP1.place(x=50, y=80, width=340, height=490)

# ***** Labels *****
        Label(self.frameP1, text="Pruebas", font=("times", 18, "bold"),
              bg="gray18", fg="navajowhite4").place(x=45, y=30)


# ****** Boton Salir ****** #
        BotonSalir = Button(self.frameP1, text="Salir", command=self.rootGUIP.destroy, font=(
            "times", 15), bg="firebrick4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=250, y=425, width=70)

# ***** Boton Info *****
        BotonInfo = Button(self.frameP1, text="i", font=(
            "times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.info3)
        BotonInfo.place(x=20, y=425, width=50)

# ***** Botón Menú Principal *****
        BotonInfo = Button(self.frameP1, text="Menú", font=(
            "times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.abrirMenu)
        BotonInfo.place(x=173, y=425, width=67)

# ***** Boton Prueba Chi *****
        BotonChi = Button(self.frameP1, text="Chi χ²", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pChiCu)
        BotonChi.place(x=90, y=100, width=170)

# ***** Boton Prueba Kolmogorov *****
        BotonKo = Button(self.frameP1, text="Kolmogorov", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pKolmo)
        BotonKo.place(x=90, y=160, width=170)

# ***** Boton Prueba Corridas *****
        BotonCo = Button(self.frameP1, text="Corridas", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pCorridas)
        BotonCo.place(x=90, y=220, width=170)

# ***** Boton Prueba Series *****
        BotonSe = Button(self.frameP1, text="Series", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pSeries)
        BotonSe.place(x=90, y=280, width=170)

# ***** Boton Prueba Poker *****
        BotonPoker = Button(self.frameP1, text="Poker", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pPoker)
        BotonPoker.place(x=90, y=340, width=80)
        opcions = ["3", "5"]
        self.variable = StringVar(self.frameP1)
        self.variable.set(opcions[0])
        w = OptionMenu(self.frameP1, self.variable, *opcions)
        w.config(width=5)
        w.place(x=180, y=345)

 # ****** Frame 2 GUI Pruebas ******
        self.frameP2 = Frame(self.rootGUIP, bg="gray18")
        self.frameP2.place(x=520, y=75, width=750, height=560)
        Label(self.frameP2, text="Ingrese los datos para la prueba", font=(
            "times", 17, "bold"), bg="gray18", fg="navajowhite4").place(x=50, y=30)

        # ****** Frame 2 GUI Pruebas ******
        self.frameP2 = Frame(self.rootGUIP, bg="gray18")
        self.frameP2.place(x=520, y=75, width=750, height=560)
        Label(self.frameP2, text="Ingrese los datos para la prueba", font=("times", 17, "bold"), bg="gray18",
              fg="navajowhite4").place(x=50, y=30)

        # ***** Campo a *****
        Label(self.frameP2, text="a", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=50, y=77)
        self.a = Entry(self.frameP2, font=("times", 16), width=9)
        self.a.place(x=85, y=77)

        # ***** Campo Xn *****
        Label(self.frameP2, text="Xn", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=220, y=77)
        self.xn = Entry(self.frameP2, font=("times", 16), width=9)
        self.xn.place(x=255, y=77)

        # ***** Campo C *****
        Label(self.frameP2, text="C", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=370, y=77)
        self.c = Entry(self.frameP2, font=("times", 16), width=9)
        self.c.place(x=405, y=77)

        # ***** Campo M *****
        Label(self.frameP2, text="M", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=520, y=77)
        self.m = Entry(self.frameP2, font=("times", 16), width=9)
        self.m.place(x=555, y=77)

    def info3(self):
        messagebox.showinfo(
            "Información", "Para las pruebas ingresa los datos usados para generar los numeros Pseaudoleatorios")

    def abrirMenu(self):
        self.rootGUIP.destroy()
        import GUI_Inicio as GIN
        GIN.iniciar()

    def pChiCu(self):

        self.text = Text(self.frameP2)
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
        self.text.place(x=115, y=115)

    def pKolmo(self):

        self.text = Text(self.frameP2)
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
        self.text.place(x=115, y=115)

    def pCorridas(self):

        self.text = Text(self.frameP2)
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
        self.text.place(x=115, y=115)

    def pSeries(self):

        self.text = Text(self.frameP2)
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
        self.text.place(x=115, y=115)

    def pPoker(self):

        self.text = Text(self.frameP2)
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
        self.text.place(x=115, y=115)


def iniciar():
    rootGUIP = Tk()
    obj = GUIP(rootGUIP)
    rootGUIP.mainloop()
