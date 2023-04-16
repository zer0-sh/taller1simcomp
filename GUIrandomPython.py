from tkinter import *
from tkinter import messagebox

from PIL import ImageTk
import PruebaIndependenciaPoker
import PruebaUniChi
import PruebaUnicidadKolmogorov
import pruebaCorrido
import pruebaUnicidadSerie
import pythonRandom


# ----- Clase GUIRAND -----
class GUIRAND:

    def __init__(self, rootGUIRAND):
        self.rootGUIRAND = rootGUIRAND
        self.rootGUIRAND.title("Generador de Números Pseaudoleatorios")
        self.rootGUIRAND.geometry("1366x768")
        self.rootGUIRAND.resizable(1, 1)

# ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo01.jpg")
        Label(self.rootGUIRAND, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

# ****** Frame 1 GUI Randoms ******
        self.frameRAND1 = Frame(self.rootGUIRAND, bg="gray18")
        self.frameRAND1.place(x=50, y=50, width=450, height=600)

        Label(self.frameRAND1, text="Generadores ", font=("times", 18,
              "bold"), bg="gray18", fg="navajowhite4").place(x=45, y=30)
        Label(self.frameRAND1, text="Con entradas aleatorias ", font=(
            "times", 14, "bold"), bg="gray18", fg="navajowhite4").place(x=45, y=56)
        Label(self.frameRAND1, text="Implementando la función numpy.random.rand :", font=(
            "times", 13, ), bg="gray18", fg="white").place(x=45, y=100)
        Label(self.frameRAND1, text="propia del lenguaje python.", font=(
            "times", 13, ), bg="gray18", fg="white").place(x=45, y=123)

# ***** Campo entrada *****
        Label(self.frameRAND1, text="Entrada", font=("times", 14,
              "bold"), bg="gray18", fg="white").place(x=44, y=178)
        self.cuadro = Entry(self.frameRAND1, font=("times", 16), width=15)
        self.cuadro.place(x=132, y=180)

        # ***** Boton generar (OK) *****
        BotonSalir = Button(self.frameRAND1, text="Ok", command=self.randoms, font=(
            "times", 14), bg="navajowhite4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=335, y=180, width=40, height=35)

        Label(self.frameRAND1, text="Pruebas", font=("times", 17, "bold"),
              bg="gray18", fg="navajowhite4").place(x=160, y=255)


# ***** Boton Prueba Chi *****
        BotonChi = Button(self.frameRAND1, text="Chi X", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pChiCu)
        BotonChi.place(x=55, y=320, width=150, height=40)

# ***** Boton Prueba Kolmogorov *****
        BotonKolm = Button(self.frameRAND1, text="Kolmogorov", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pKolmo)
        BotonKolm.place(x=230, y=320, width=150, height=40)

# ***** Boton Prueba Corridas *****
        BotonCor = Button(self.frameRAND1, text="Corridas", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pCorridas)
        BotonCor.place(x=55, y=375, width=150, height=40)

# ***** Boton Prueba Series *****
        BotonKolm = Button(self.frameRAND1, text="Series", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pSeries)
        BotonKolm.place(x=230, y=375, width=150, height=40)

# ***** Boton Prueba Poker *****
        BotonPok = Button(self.frameRAND1, text="Poker", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.pPoker)
        BotonPok.place(x=55, y=430, width=150, height=40)
        opcions = ["3", "5"]
        self.variable = StringVar(self.frameRAND1)
        self.variable.set(opcions[0])
        w = OptionMenu(self.frameRAND1, self.variable, *opcions)
        w.config(width=5)
        w.place(x=230, y=435)


# ****** Boton Salir ****** #
        BotonSalir = Button(self.frameRAND1, text="Salir", command=self.rootGUIRAND.destroy, font=(
            "times", 15), bg="firebrick4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=360, y=535, width=70)

# ***** Boton Info *****
        BotonInfo = Button(self.frameRAND1, text="i", font=(
            "times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.info4)
        BotonInfo.place(x=25, y=535, width=50)

# ***** Botón Menú Principal *****
        BotonInfo = Button(self.frameRAND1, text="Menú", font=(
            "times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.abrirMenu)
        BotonInfo.place(x=283, y=535, width=67)


# ****** Frame 2 GUI Randoms ******
        self.frameRAND2 = Frame(self.rootGUIRAND, bg="gray18")
        self.frameRAND2.place(x=560, y=75, width=750, height=560)
        Label(self.frameRAND2, text="Resultados del generador", font=(
            "times", 17, "bold"), bg="gray18", fg="navajowhite4").place(x=50, y=30)

    def info4(self):
        messagebox.showinfo("Información", "Las entradas: a, Xn, C y m; se llenan de forma aleatoria con \n "
                            "numpy.random.rand: \n "
                            "Esta función genera un array NumPy conteniendo números aleatorios  \n\n"
                            "con distribución uniforme.")

    def abrirMenu(self):
        self.rootGUIRAND.destroy()
        import GUI_Inicio as GIN
        GIN.iniciar()

    def randoms(self):

        self.text = Text(self.frameRAND2)
        x = int(self.cuadro.get())
        mostrar = (pythonRandom.pyRandom.tabla(x))
        self.text.insert(INSERT, mostrar)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=115, y=80)

    def pChiCu(self):

        self.text = Text(self.frameRAND2)
        x = int(self.cuadro.get())
        arreglo = pythonRandom.pyRandom.arreglo(x)
        datos = PruebaUniChi.PruebaUniChi.pruChi(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=115, y=80)

    def pKolmo(self):

        self.text = Text(self.frameRAND2)
        x = int(self.cuadro.get())
        arreglo = pythonRandom.pyRandom.arreglo(x)
        datos = PruebaUnicidadKolmogorov.PruebaUnicidadKolmogorov.pruebaKolmogorov(
            arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=115, y=80)

    def pCorridas(self):

        self.text = Text(self.frameRAND2)
        x = int(self.cuadro.get())
        arreglo = pythonRandom.pyRandom.arreglo(x)
        nc = pruebaCorrido.pruebaCorrido.contar(arreglo)
        print(nc)
        datos = pruebaCorrido.pruebaCorrido.corrido(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=115, y=80)

    def pSeries(self):

        self.text = Text(self.frameRAND2)
        x = int(self.cuadro.get())
        arreglo = pythonRandom.pyRandom.arreglo(x)
        datos = pruebaUnicidadSerie.pruebaUnicidadSerie.pruebaSerie(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=115, y=80)

    def pPoker(self):

        self.text = Text(self.frameRAND2)
        x = int(self.cuadro.get())
        arreglo = pythonRandom.pyRandom.arreglo(x)
        k = int(self.variable.get())
        datos = PruebaIndependenciaPoker.PruebaIndependenciaPoker.pruebaPoker(
            arreglo, k)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable",
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=115, y=80)


def iniciar():
    rootGUIRAND = Tk()
    obj = GUIRAND(rootGUIRAND)
    rootGUIRAND.mainloop()
