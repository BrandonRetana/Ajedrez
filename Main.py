
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


    def dibujarTablero(self):
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 ==0: #->dibuja los arios XD
                    self.window.create_rectangle(i*self.L_CUADRADO, j*self.L_CUADRADO, (i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="#ffffff")
                else: #->dibuja los morenos XD
                    self.window.create_rectangle(i*self.L_CUADRADO, j*self.L_CUADRADO, (i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="#162B4E")   

    def caragarImagenes(self):
        fichas = ["alfil-blanco","alfil-negro","caballo-blanco", "caballo-negro","peon-blanco","peon-negro","reina-blanca","reina-negra","rey-blanco","rey-negro","torre-blanca","torre-negra"]
        for ficha in fichas:
                self.imagenes[ficha]= tk.PhotoImage(file="./imagenes/" + ficha + ".png")
                self.imagenes[ficha] = self.imagenes[ficha].subsample(33) #ajusta el tamano

    def mostrarFichas(self):
        for indice_i, i in enumerate(self.gs.piezas):
            for indice_j, j in enumerate(i):
                if j!= "--":
                    self.window.create_image(indice_j*self.L_CUADRADO,indice_i*self.L_CUADRADO, image=self.imagenes[j.getName()], anchor="nw", )
                    

interfaz = Interfaz(70)
interfaz.dibujarTablero()
interfaz.caragarImagenes()
interfaz.mostrarFichas()
interfaz()