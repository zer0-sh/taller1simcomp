from tkinter import Frame, Label,Button, Tk
from tkinter import messagebox
from PIL import ImageTk

# ----- Clase GUIINICIO -----
class GUIInicio:

    def __init__(self, rootInicio):
        self.rootInicio = rootInicio
        self.rootInicio.title("Generador de Números Pseaudoleatorios")
        self.rootInicio.geometry("1366x768")
        self.rootInicio.resizable(1, 1)

# ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo01.jpg")
        Label(self.rootInicio, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ****** Frame Login ****** #
        frameInicio = Frame(self.rootInicio, bg="gray18")
        frameInicio.place(x=427, y=90, width=510, height=480)
        Label(frameInicio, text="NÚMEROS PSEUDOALEATORIOS", font=("times", 19, "bold"), bg="gray18",fg="navajowhite4").place(x=50, y=30)

        # ****** Label Info Inicial ****** #
        Label(frameInicio, text="Diseñados con el fin de generar números con un", font=("times", 13, ""), bg="gray18", fg="white").place( x=43, y=100)
        Label(frameInicio, text="comportamiento similar al aleatorio.", font=("times", 13, ""), bg="gray18", fg="white").place( x=43, y=122)

        # ----- icono info -----
        Label(frameInicio, text=" ✅", font=("", 35, ""), bg="gray18", fg="white").place(x=400, y=95)

        # ****** Label Selección ****** #
        Label(frameInicio, text="Seleccione el generador que desea emplear:", font=("times", 14, ""), bg="gray18", fg="white").place( x=43, y=205)

        # ----- Boton Generador Lineal Congruente -----
        BotonLC = Button(frameInicio, text="Lineal Congruente", command=self.abrirLC,font=("times", 15), bg="navajowhite4", fg="white", bd=5,cursor="hand2")
        BotonLC.place(x=162, y=253, width=200)

        # ----- Boton Generador de Estandar Mínimo -----
        BotonEM = Button(frameInicio, text="Estandar Mínimo", command=self.abrirEM,font=("times", 15), bg="navajowhite4", fg="white", bd=5,cursor="hand2")
        BotonEM.place(x=162, y=323, width=200)

        # ----- Boton Generador Random de Python ----- #
        BotonSalir = Button(frameInicio, text="Python Random", command=self.abrirRandom, font=("times", 15),bg="navajowhite4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=162, y=393, width=200)

        # ****** Boton Salir ****** #
        BotonSalir = Button(frameInicio, text="Salir", command=self.rootInicio.destroy,font=("times", 15), bg="firebrick4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=410, y=410, width=70)

        # ****** Boton Info Integrantes ****** #
        BotonSalir = Button(frameInicio, text="i", command=self.infoGrupo, font=("times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=30, y=410, width=50)


    def infoGrupo(self):
       messagebox.showinfo("Simulación Computacional UV", "Desarrollado por:\n\n "
                           "* John Edward Correa Ramírez    201958557-3743\n"
                           "* Stephania Martinez Rodriguez  201958884-3743\n"
                           "* Miguel Ángel Paz velasco           201958444-3743\n"
                           "* Jaime Alberto Lopez Restrepo    201958379-3743")

    def abrirLC(self):
        self.rootInicio.destroy()
        import GUILinealCongruente as LC
        LC.iniciar()

    def abrirEM(self):
        self.rootInicio.destroy()
        import GUIEstandarMinimo as EM
        EM.iniciar()

    def abrirRandom(self):
        self.rootInicio.destroy()
        import GUIrandomPython as PR
        PR.iniciar()


def iniciar():

    rootInicio = Tk()
    obj = GUIInicio(rootInicio)
    rootInicio.mainloop()

rootInicio = Tk()
obj = GUIInicio(rootInicio)
rootInicio.mainloop()


