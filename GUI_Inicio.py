# Taller 1 Simulacion
# Johan Muñoz       201958***-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

from tkinter import Frame, Label, Button, Tk, messagebox
from PIL import ImageTk

# ----- Clase GUI_INICIO -----


class GUI_Inicio:

    def __init__(self, rootInicio):
        self.rootInicio = rootInicio
        self.rootInicio.title("Generador de Números Pseaudoleatorios")
        self.rootInicio.resizable(False, False)
        ancho_ventana = 900
        alto_ventana = 600
        ancho_pantalla = rootInicio.winfo_screenwidth()
        alto_pantalla = rootInicio.winfo_screenheight()
        x_ventana = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y_ventana = (alto_pantalla // 2) - (alto_ventana // 2)
        rootInicio.geometry(
            f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

# ----- Imagen Fondo -----
        self.bg = ImageTk.PhotoImage(file="Imagenes/fondo02.jpg")
        Label(self.rootInicio, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # ----- Frame Login -----
        frameInicio = Frame(self.rootInicio, bg="gray1")
        frameInicio.place(x=0, y=0)
        x_frame = (ancho_ventana // 2) - (510 // 2)
        y_frame = (alto_ventana // 2) - (480 // 2)
        frameInicio.place(x=x_frame, y=y_frame, width=510, height=480)
        Label(frameInicio, text="NÚMEROS PSEUDOALEATORIOS", font=(
            "Agency FB", 35, "bold"), bg="black", fg="darkgoldenrod1").place(x=20, y=30)

        # ----- Label informacion inicial -----
        Label(frameInicio, text="Diseñados con el fin de generar números con un", font=(
            "times", 13, ""), bg="black", fg="white").place(x=40, y=130)
        Label(frameInicio, text="comportamiento similar al aleatorio.", font=(
            "times", 13, ""), bg="black", fg="white").place(x=40, y=160)

        # ----- icono informacion -----
        Label(frameInicio, text=" ✅", font=("", 35, ""),
              bg="black", fg="white").place(x=400, y=95)

        # ----- Label seleccion -----
        Label(frameInicio, text="-Por favor seleccione un generador:",
              font=("Agency FB", 20, ""), bg="gray1", fg="white").place(x=50, y=205)

        # ----- Boton generador lineal congruente -----
        BotonLC = Button(frameInicio, text="Lineal congruente", cursor="hand2", command=self.abrirLC, font=(
            "Agency FB", 20), bg="darkgoldenrod1", fg="white", bd=5)
        BotonLC.place(x=162, y=253, width=200)

        # ----- Boton generador de estandar minimo -----
        BotonEM = Button(frameInicio, text="Estandar Mínimo", cursor="hand2", command=self.abrirEM, font=(
            "Agency FB", 20), bg="darkgoldenrod1", fg="white", bd=5)
        BotonEM.place(x=162, y=323, width=200)

        # ----- Boton generador random de python -----
        BotonSalir = Button(frameInicio, text="Python Random", cursor="hand2", command=self.abrirRandom, font=(
            "Agency FB", 20), bg="darkgoldenrod1", fg="white", bd=5)
        BotonSalir.place(x=162, y=393, width=200)

        # ----- Boton salir -----
        BotonSalir = Button(frameInicio, text="Salir", cursor="hand2", command=self.rootInicio.destroy, font=(
            "times", 20), bg="firebrick4", fg="white", bd=5)
        BotonSalir.place(x=410, y=410, width=70)

        # ----- Boton Info Integrantes -----
        BotonSalir = Button(frameInicio, text="i", command=self.infoGrupo, font=(
            "times", 15), bg="Skyblue4", fg="white", bd=5, cursor="hand2")
        BotonSalir.place(x=30, y=420, width=50)

    def infoGrupo(self):
        messagebox.showinfo("Simulación Computacional", "Desarrollado por:\n\n"
                            "* Juan Camilo Azcarate      201958932-3743\n"
                            "* Estefany Castro Agudelo   201958552-3743\n"
                            "* Valentina Hurtado Garcia  201958542-3743\n"
                            "* Johan Steven Muñoz        201958***-3743")

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
    obj = GUI_Inicio(rootInicio)
    rootInicio.mainloop()


rootInicio = Tk()
obj = GUI_Inicio(rootInicio)
rootInicio.mainloop()
