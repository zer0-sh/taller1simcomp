from tkinter import *
from PIL import ImageTk
import GeneradorEstandarMinimo
# ----- ClaseGUIEM -----


class GUIEM:

    def __init__(self, rootGUIEM):
        self.rootGUIEM = rootGUIEM
        self.rootGUIEM.title("Generador de Números Pseaudoleatorios")
        self.rootGUIEM.geometry("1366x768")
        self.rootGUIEM.resizable(1, 1)

# ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo01.jpg")
        Label(self.rootGUIEM, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

# ****** Frame 1 GUI Estandar Mínimo ******
        frameEM1 = Frame(self.rootGUIEM, bg="gray18")
        frameEM1.place(x=50, y=80, width=450, height=450)

        Label(frameEM1, text="Generador de Estandar Mínimo", font=(
            "times", 18, "bold"), bg="gray18", fg="navajowhite4").place(x=45, y=30)
        Label(frameEM1, text="Aplicando la factorización aproximada y cálculo", font=(
            "times", 13, ), bg="gray18", fg="white").place(x=45, y=110)
        Label(frameEM1, text="modular se obtiene la recurrencia:", font=(
            "times", 13, ), bg="gray18", fg="white").place(x=45, y=135)
        Label(frameEM1, text="Xn+1 = (a . Xn)mod m; X0: Semilla", font=("times",
              14, "bold"), bg="gray18", fg="navajowhite4").place(x=55, y=183)
        Label(frameEM1, text="Por:", font=("times", 13, ),
              bg="gray18", fg="white").place(x=45, y=230)
        Label(frameEM1, text="(a . Xn)mod m =", font=("times", 13, "bold"),
              bg="gray18", fg="navajowhite4").place(x=25, y=280)
        Label(frameEM1, text="{", font=("times", 45,),
              bg="gray18", fg="navajowhite4").place(x=145, y=250)
        Label(frameEM1, text="a.(Xn mod q)-r.⌊Xn/q⌋, ", font=("times",
              13,), bg="gray18", fg="navajowhite4").place(x=175, y=265)
        Label(frameEM1, text="si es >= 0", font=("times", 13,),
              bg="gray18", fg="white").place(x=345, y=265)
        Label(frameEM1, text="a.(Xn mod q)-r.⌊Xn/q⌋ + m, ", font=("times",
              13,), bg="gray18", fg="navajowhite4").place(x=175, y=290)
        Label(frameEM1, text="si no", font=("times", 13,),
              bg="gray18", fg="white").place(x=380, y=290)

# ****** Boton Salir ****** #
        BotonSalir = Button(frameEM1, text="Salir", command=self.rootGUIEM.destroy, font=(
            "times", 15), bg="firebrick4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=360, y=385, width=70)

# ***** Boton Info *****
        BotonInfo = Button(frameEM1, text="i", font=(
            "times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.info2)
        BotonInfo.place(x=222, y=385, width=50)

# ***** Botón Menú Principal *****
        BotonInfo = Button(frameEM1, text="Menú", font=(
            "times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2", command=self.abrirMenu)
        BotonInfo.place(x=283, y=385, width=67)

# ***** Boton Lineal Congruente *****
        BotonVolv = Button(frameEM1, text="Lineal Congruente", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.abrirLC)
        BotonVolv.place(x=25, y=385, width=170)

# ****** Frame 2 GUI Estandar Mínimo ******
        self.frameEM2 = Frame(self.rootGUIEM, bg="gray18")
        self.frameEM2.place(x=560, y=75, width=750, height=560)
        Label(self.frameEM2, text="Ingrese los datos del generador", font=(
            "times", 17, "bold"), bg="gray18", fg="navajowhite4").place(x=50, y=30)

# ***** Campo a *****
        Label(self.frameEM2, text="a", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=30, y=70)
        self.a = Entry(self.frameEM2, font=("times", 16), width=9)
        self.a.place(x=55, y=72)

# ***** Campo Xn *****
        Label(self.frameEM2, text="Xn", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=185, y=70)
        self.xn = Entry(self.frameEM2, font=("times", 16), width=9)
        self.xn.place(x=225, y=72)

# ***** Campo M *****
        Label(self.frameEM2, text="M", font=("times", 16, "bold"),
              bg="gray18", fg="white").place(x=350, y=70)
        self.m = Entry(self.frameEM2, font=("times", 16), width=9)
        self.m.place(x=375, y=72)

# ***** Boton generar (OK) *****
        BotonOk = Button(self.frameEM2, text="Ok", command=self.generadorEM, font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2")
        BotonOk.place(x=660, y=65, width=50)


# ****** Frame 3 GUI Lineal Congruente ******
        self.frameEM3 = Frame(self.rootGUIEM, bg="gray18")
        self.frameEM3.place(x=50, y=545, width=450, height=100)


# ***** Boton Pruebas *****
        BotonPr = Button(self.frameEM3, text="Pruebas", font=(
            "times", 15), bg="navajowhite4", fg="white", bd=5, cursor="hand2", command=self.abrirPruebas)
        BotonPr.place(x=145, y=30, width=170)

    def info2(self):
        messagebox.showinfo("Información", "Se evita overflow si se utiliza una factorización aproximada de m.\n\n"
                                           "m ≈ a.q+r\n"
                                           "donde q=⌊m/a⌋; r=m mod \n\n"
                                           "Datos de Ejemplo:\n"
                                           "a=10; m=73  →  q=7; r=3; a.q+r=73")

    def abrirLC(self):
        self.rootGUIEM.destroy()
        import GUILinealCongruente as LC
        LC.iniciar()

    def abrirMenu(self):
        self.rootGUIEM.destroy()
        import GUI_Inicio as GIN
        GIN.iniciar()

    def abrirPruebas(self):
        self.rootGUIEM.destroy()
        import GUIPruebasEM as GP
        GP.iniciar()

    def generadorEM(self):
        self.text = Text(self.frameEM2)
        a = int(self.a.get())
        xn = int(self.xn.get())
        m = int(self.m.get())
        arreglo = (
            GeneradorEstandarMinimo.GeneradorEstandar.paraTablas(xn, xn, a, m))
        self.text.insert(INSERT, arreglo)
        self.text.config(width=35, height=25, state="disable",
                         bg="gray18", bd=0, fg="white")
        self.text.pack()
        self.text.place(x=250, y=110)


def iniciar():
    rootGUIEM = Tk()
    obj = GUIEM(rootGUIEM)
    rootGUIEM.mainloop()
