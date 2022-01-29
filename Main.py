
from email.policy import default
from pydoc import text
import tkinter as tk

import AppAjedrez  
class Interfaz():

    #esta funcion incia la ventana, recibe el size de cada cuadrado
    def __init__(self, L_CUADRADO):
        self.gs = AppAjedrez.EstadoDeJuego()
        self.L_CUADRADO = L_CUADRADO
        self.ventana = tk.Tk()
        self.imagenes = {}
        self.ventana.title("interfaz de ajedrez")

        #ventana.iconbitmap("gg.jpg") icono no sirve
        self.ventana.geometry(f"{str(L_CUADRADO *8)}x{str(L_CUADRADO * 8)}")
        self.ventana.resizable(0,0)

        self.window = tk.Canvas(self.ventana)
        self.window.pack(fill="both", expand=True)


    def __call__(self):
        self.ventana.mainloop()  


    def caragarImagenes(self):
        fichas = ["alfil-blanco","alfil-negro","caballo-blanco", "caballo-negro","peon-blanco","peon-negro","reina-blanca","reina-negra","rey-blanco","rey-negro","torre-blanca","torre-negra"]
        for ficha in fichas:
                self.imagenes[ficha]= tk.PhotoImage(file="./imagenes/" + ficha + ".png")
                self.imagenes[ficha] = self.imagenes[ficha].subsample(31) #ajusta el tamano

    def prueba(self):
        print("prueba")
    

    def mostrarFichas(self):
        color = "#ffffff"
        for indice_i, i in enumerate(self.gs.piezas):
            if(color == "#162B4E"):
                color = "#ffffff"
            else:
                color = "#162B4E"
            for indice_j, j in enumerate(i):
                if(color == "#162B4E"):
                    color = "#ffffff"
                else:
                    color = "#162B4E"
                if j!= "--":
                    ficha = tk.Button(image=self.imagenes[j.getName()],borderwidth=0,bg = color,activebackground="#69F7AB",command=lambda:self.prueba())
                    ficha.place(x = indice_j*self.L_CUADRADO+1,y =indice_i*self.L_CUADRADO+1)
                else:
                    ficha = tk.Button(width=10,height=5, borderwidth=0,bg = color,activebackground="#77D5F3")
                    ficha.place(x = indice_j*self.L_CUADRADO+1,y =indice_i*self.L_CUADRADO+1)
                    
                    

interfaz = Interfaz(70)
interfaz.caragarImagenes()
interfaz.mostrarFichas()
interfaz()