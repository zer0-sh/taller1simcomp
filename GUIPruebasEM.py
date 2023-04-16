from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

import GeneradorEstandarMinimo
import PruebaIndependenciaPoker
import PruebaUniChi
import PruebaUnicidadKolmogorov
import pruebaCorrido
import pruebaUnicidadSerie


#----- ClaseGUIP -----
class GUIPEM:

    def __init__(self, rootGUIPEM):
        self.rootGUIPEM = rootGUIPEM
        self.rootGUIPEM.title("Generador de Números Pseaudoleatorios")
        self.rootGUIPEM.geometry("1366x768")
        self.rootGUIPEM.resizable(1, 1)

# ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo01.jpg")
        Label(self.rootGUIPEM, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

# ****** Frame 1 GUI Pruebas ******
        self.framePEM1 = Frame(self.rootGUIPEM, bg="gray18")
        self.framePEM1.place(x=50, y=80, width=340, height=490)

# ***** Labels *****
        Label(self.framePEM1, text="Pruebas", font=("times", 18, "bold"), bg="gray18",fg="navajowhite4").place(x=45, y=30)

# ****** Boton Salir ****** #
        BotonSalir = Button(self.framePEM1, text="Salir", command=self.rootGUIPEM.destroy, font=("times", 15), bg="firebrick4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=250, y=425, width=70)

# ***** Boton Info *****
        BotonInfo = Button(self.framePEM1, text="i", font=("times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2",command=self.info3)
        BotonInfo.place(x=20, y=425, width=50)

# ***** Botón Menú Principal *****
        BotonInfo = Button(self.framePEM1, text="Menú", font=("times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2",command=self.abrirMenu)
        BotonInfo.place(x=173, y=425, width=67)

# ***** Boton Prueba Chi *****
        BotonChi = Button(self.framePEM1, text="Chi χ²", font=("times", 15), bg="navajowhite4", fg="white", bd=5,cursor="hand2", command=self.pChiCu)
        BotonChi.place(x=90, y=100, width=170)

# ***** Boton Prueba Kolmogorov *****
        BotonKo = Button(self.framePEM1, text="Kolmogorov", font=("times", 15), bg="navajowhite4", fg="white", bd=5,cursor="hand2", command=self.pKolmo)
        BotonKo.place(x=90, y=160, width=170)

# ***** Boton Prueba Corridas *****
        BotonCo = Button(self.framePEM1, text="Corridas", font=("times", 15), bg="navajowhite4", fg="white", bd=5,cursor="hand2", command=self.pCorridas)
        BotonCo.place(x=90, y=220, width=170)

# ***** Boton Prueba Series *****
        BotonSe = Button(self.framePEM1, text="Series", font=("times", 15), bg="navajowhite4", fg="white", bd=5,cursor="hand2", command=self.pSeries)
        BotonSe.place(x=90, y=280, width=170)

# ***** Boton Prueba Poker *****
        BotonPoker = Button(self.framePEM1, text="Poker", font=("times", 15), bg="navajowhite4", fg="white", bd=5,cursor="hand2", command=self.pPoker)
        BotonPoker.place(x=90, y=340, width=80)
        opcions = ["3", "5"]
        self.variable = StringVar(self.frameP1)
        self.variable.set(opcions[0])
        w = OptionMenu(self.framePEM1, self.variable, *opcions)
        w.config(width=5)
        w.place(x=180, y=345)

 # ****** Frame 2 GUI Pruebas ******
        self.framePEM2 = Frame(self.rootGUIPEM, bg="gray18")
        self.framePEM2.place(x=520, y=75, width=750, height=560)
        Label(self.framePEM2, text="Ingrese los datos para la prueba", font=("times", 17, "bold"), bg="gray18",fg="navajowhite4").place(x=50, y=30)

        # ****** Frame 2 GUI Pruebas ******
        self.framePEM2 = Frame(self.rootGUIPEM, bg="gray18")
        self.framePEM2.place(x=520, y=75, width=750, height=560)
        Label(self.framePEM2, text="Ingrese los datos para la prueba", font=("times", 17, "bold"), bg="gray18",
              fg="navajowhite4").place(x=50, y=30)

        # ***** Campo a *****
        Label(self.framePEM2, text="a", font=("times", 16, "bold"), bg="gray18", fg="white").place(x=100, y=77)
        self.a = Entry(self.framePEM2, font=("times", 16), width=9)
        self.a.place(x=135, y=77)

        # ***** Campo Xn *****
        Label(self.framePEM2, text="Xn", font=("times", 16, "bold"), bg="gray18", fg="white").place(x=240, y=77)
        self.xn = Entry(self.framePEM2, font=("times", 16), width=9)
        self.xn.place(x=275, y=77)

        # ***** Campo M *****
        Label(self.framePEM2, text="M", font=("times", 16, "bold"), bg="gray18", fg="white").place(x=365, y=77)
        self.m = Entry(self.framePEM2, font=("times", 16), width=9)
        self.m.place(x=400, y=77)

    def info3(self):
       messagebox.showinfo("Información", "Para las pruebas ingresa los datos usados para generar los numeros Pseaudoleatorios")

    def abrirMenu(self):
        self.rootGUIPEM.destroy()
        import GUIInicio as GIN
        GIN.iniciar()

    def pChiCu(self):

        self.text = Text(self.framePEM2)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(xn,xn,a,m)
        datos = PruebaUniChi.PruebaUniChi.pruChi(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable", bg="gray18",bd=0,fg="white")
        self.text.pack()
        self.text.place(x=115, y=115)

    def pKolmo(self):

        self.text = Text(self.framePEM2)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(xn,xn,a,m)
        datos = PruebaUnicidadKolmogorov.PruebaUnicidadKolmogorov.pruebaKolmogorov(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable", bg="gray18",bd=0,fg="white")
        self.text.pack()
        self.text.place(x=115, y=115)

    def pCorridas(self):

        self.text = Text(self.framePEM2)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(xn,xn,a,m)
        datos = pruebaCorrido.pruebaCorrido.corrido(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable", bg="gray18",bd=0,fg="white")
        self.text.pack()
        self.text.place(x=115, y=115)

    def pSeries(self):

        self.text = Text(self.framePEM2)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(xn,xn,a,m)
        datos = pruebaUnicidadSerie.pruebaUnicidadSerie.pruebaSerie(arreglo)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable", bg="gray18",bd=0,fg="white")
        self.text.pack()
        self.text.place(x=115, y=115)

    def pPoker(self):

        self.text = Text(self.framePEM2)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        k = int(self.variable.get())
        arreglo = GeneradorEstandarMinimo.GeneradorEstandar.generador(xn,xn,a,m)
        datos = PruebaIndependenciaPoker.PruebaIndependenciaPoker.pruebaPoker(arreglo,k)
        self.text.insert(INSERT, datos)
        self.text.config(width=70, height=25, state="disable", bg="gray18",bd=0,fg="white")
        self.text.pack()
        self.text.place(x=115, y=115)

def iniciar():
    rootGUIPEM = Tk()
    obj = GUIPEM(rootGUIPEM)
    rootGUIPEM.mainloop()