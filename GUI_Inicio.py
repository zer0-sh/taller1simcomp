# Taller 1 Simulacion
# Johan Muñoz       201958***-3743
# Camilo Azcarate   201958932-3743
# Valentina Hurtado 201958542-3743
# Estefany Castro   201958552-3743

from tkinter import CENTER, Frame, Label, Button, Tk, messagebox
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

        label_texto = Label(frameInicio, text="NÚMEROS \n PSEUDOALEATORIOS", font=("Agency FB", 35, "bold"), bg="gray1", fg="darkgoldenrod1")
        label_texto.place(relx=0.5, rely=0.2, anchor=CENTER)      

        # ----- Label seleccion -----
        Label(frameInicio, text="-Por favor seleccione un generador:",
              font=("Agency FB", 20, ""), bg="gray1", fg="white").place(x=50, y=190)

        # ----- Boton generador lineal congruente -----
        BotonLC = Button(frameInicio, text="Lineal congruente", cursor="hand2", command=self.abrirLC, font=(
            "Agency FB", 20), bg="darkgoldenrod1", fg="white")
        BotonLC.place(x=162, y=253, width=200)

        # ----- Boton generador de estandar minimo -----
        BotonEM = Button(frameInicio, text="Estandar Mínimo", cursor="hand2", relief= "flat", command=self.abrirEM, font=(
            "Agency FB", 20), bg="darkgoldenrod1", fg="white")
        BotonEM.place(x=162, y=323, width=200)

        # ----- Boton generador random de python -----
        BotonSalir = Button(frameInicio, text="Python Random", cursor="hand2", command=self.abrirRandom, font=(
            "Agency FB", 20), bg="darkgoldenrod1", fg="white")
        BotonSalir.place(x=162, y=393, width=200)

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
