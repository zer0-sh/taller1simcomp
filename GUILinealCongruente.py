from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

from GeneradorLineal import *

# ----- Clase GUILC -----
class GUILC:

    def __init__(self, rootGUILC):
        self.rootGUILC = rootGUILC
        self.rootGUILC.title("Generador de Números Pseaudoleatorios")
        self.rootGUILC.geometry("1366x768")
        self.rootGUILC.resizable(1, 1)

# ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo01.jpg")
        Label(self.rootGUILC, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

# ****** Frame 1 GUI Lineal Congruente ******
        self.frameLC1 = Frame(self.rootGUILC, bg="gray18")
        self.frameLC1.place(x=50, y=80, width=450, height=450)

        Label(self.frameLC1, text="Generador Lineal Congruente", font=("times", 18, "bold"), bg="gray18",fg="navajowhite4").place(x=45, y=30)
        Label(self.frameLC1, text="Definido por la relación de recurrencia:", font=("times", 13, ), bg="gray18", fg="white").place(x=45, y=100)
        Label(self.frameLC1, text="Xn+1 = (a . Xn + C)mod m; X0: Semilla", font=("times", 14, "bold"), bg="gray18", fg="navajowhite4").place(x=45, y=165)
        Label(self.frameLC1, text="Rn = Xn/m", font=("times", 14,), bg="gray18", fg="navajowhite4").place(x=160, y=195)
        Label(self.frameLC1, text="a: Multiplicador", font=("times", 13, "bold"), bg="gray18", fg="white").place(x=25, y=250)
        Label(self.frameLC1, text="c: Incremento", font=("times", 13, "bold"), bg="gray18", fg="white").place(x=25, y=275)
        Label(self.frameLC1, text="m: Módulo", font=("times", 13, "bold"), bg="gray18", fg="white").place(x=25, y=300)
        Label(self.frameLC1, text="Se tiene 0 <= Xn < m, por eso Rn < 1", font=("times", 13, "bold"), bg="gray18", fg="white").place(x=25, y=330)


# ****** Boton Salir ****** #
        BotonSalir = Button(self.frameLC1, text="Salir", command=self.rootGUILC.destroy, font=("times", 15), bg="firebrick4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=360, y=385, width=70)

# ***** Boton Info *****
        BotonInfo = Button(self.frameLC1, text="i", font=("times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2",command=self.info1)
        BotonInfo.place(x=222, y=385, width=50)

# ***** Boton Estandar Minimo *****
        BotonVolv = Button(self.frameLC1, text="Estandar Mínimo", font=("times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2",command=self.abrirEM)
        BotonVolv.place(x=25, y=385, width=170)

# ***** Botón Menú Principal *****
        BotonInfo = Button(self.frameLC1, text="Menú", font=("times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.abrirMenu)
        BotonInfo.place(x=283, y=385, width=67)

# ****** Frame 2 GUI Lineal Congruente ******
        self.frameLC2 = Frame(self.rootGUILC, bg="gray18")
        self.frameLC2.place(x=560, y=75, width=750, height=560)
        Label(self.frameLC2, text="Ingrese los datos del generador", font=("times", 17, "bold"), bg="gray18",fg="navajowhite4").place(x=50, y=30)

# ***** Campo a *****
        Label(self.frameLC2, text="a", font=("times", 16, "bold"), bg="gray18",fg="white").place(x=30, y=70)
        self.a = Entry(self.frameLC2, font=("times", 16),width=9)
        self.a.place(x=55, y=72)

# ***** Campo Xn *****
        Label(self.frameLC2, text="Xn", font=("times", 16, "bold"), bg="gray18", fg="white").place(x=185, y=70)
        self.xn = Entry(self.frameLC2, font=("times", 16), width=9)
        self.xn.place(x=225, y=72)

# ***** Campo C *****
        Label(self.frameLC2, text="C", font=("times", 16, "bold"), bg="gray18", fg="white").place(x=350, y=70)
        self.c = Entry(self.frameLC2, font=("times", 16), width=9)
        self.c.place(x=375, y=72)

# ***** Campo M *****
        Label(self.frameLC2, text="M", font=("times", 16, "bold"), bg="gray18", fg="white").place(x=495, y=70)
        self.m = Entry(self.frameLC2, font=("times", 16), width=9)
        self.m.place(x=525, y=72)

# ***** Boton generar (OK) *****
        BotonSalir = Button(self.frameLC2, text="Ok", command=self.generadorLineal, font=("times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=660, y=65, width=50)

        # ****** Frame 3 GUI Lineal Congruente ******
        frameLC3 = Frame(self.rootGUILC, bg="gray18")
        frameLC3.place(x=50, y=545, width=450, height=100)

        # ***** Boton Pruebas *****
        BotonPr = Button(frameLC3, text="Pruebas", font=("times", 15), bg="navajowhite4", fg="white", bd=5,cursor="hand2", command=self.abrirPruebas)
        BotonPr.place(x=145, y=30, width=170)

    def info1(self):
       messagebox.showinfo("Información", "Selecciona un m grande, selecciona C tal que \n "
                                     "C y m son primos relativos. \n "
                                     "Utilice estos datos de prueba para el generador: \n\n"
                                     "X0: 5, a: 106, C: 1283, m: 6075")

    def abrirEM(self):
        self.rootGUILC.destroy()
        import GUIEstandarMinimo as GEM
        GEM.iniciar()

    def abrirMenu(self):
        self.rootGUILC.destroy()
        import GUIInicio as GIN
        GIN.iniciar()

    def abrirPruebas(self):
        self.rootGUILC.destroy()
        import GUIPruebasLC as GP
        GP.iniciar()
        
    def generadorLineal(self):

        self.text = Text(self.frameLC2)
        a = int(self.a.get())
        xn = int(self.xn.get())
        c = int(self.c.get())
        m = int(self.m.get())
        arreglo = GeneradorLineal.paraTabla(xn, xn, a, c, m)
        self.text.insert(INSERT, arreglo)
        self.text.config(width=35, height=25, state="disable", bg="gray18",bd=0,fg="white")
        self.text.pack()
        self.text.place(x=250, y=110)


def iniciar():
    rootGUILC = Tk()
    obj = GUILC(rootGUILC)
    rootGUILC.mainloop()