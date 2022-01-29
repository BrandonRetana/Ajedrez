from Ficha import *
class EstadoDeJuego():
    #aqui si maneja el estado del juego

    def __init__(self):
        self.piezas = [
            ["torre-negra","caballo-negro","alfil-negro","reina-negra","rey-negro","alfil-negro","caballo-negro","torre-negra"],
            ["peon-negro","peon-negro","peon-negro","peon-negro","peon-negro","peon-negro","peon-negro","peon-negro"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["peon-blanco","peon-blanco","peon-blanco","peon-blanco","peon-blanco","peon-blanco","peon-blanco","peon-blanco"],
            ["torre-blanca","caballo-blanco","alfil-blanco","reina-blanca","rey-blanco","alfil-blanco","caballo-blanco","torre-blanca"]
        ]

        self.pieceReal = [["--","--","--","--","--","--","--","--"],
                          ["--","--","--","--","--","--","--","--"],
                          ["--","--","--","--","--","--","--","--"],
                          ["--","--","--","--","--","--","--","--"],
                          ["--","--","--","--","--","--","--","--"],
                          ["--","--","--","--","--","--","--","--"],
                          ["--","--","--","--","--","--","--","--"],
                          ["--","--","--","--","--","--","--","--"],]

        
    
    def simpleCheck(self, x,y):
        if (self.piezas[x][y] != "--"):
            return True
        return False

    def printMatrix(self):
        for i in range(0,7):
            for j in range(0,7):
                print(self.pieceReal[i][j])


    def charger(self):
        for x in range(0,7):
            for y in range(0,7):
                piece = self.piezas[x][y]
                if (piece == "torre-negra"):
                        self.pieceReal[x][y] = ficha("torre-negra",True,False,x,y)

                elif (piece == "torre-blanco"):
                        self.pieceReal[x][y] = ficha("torre-blanco",True,False,x,y)
                
                elif (piece == "caballo-negro"):
                        self.pieceReal[x][y] = ficha("caballo-negro",False,False,x,y)

                elif (piece == "caballo-blanco"):
                        self.pieceReal[x][y] = ficha("caballo-blanco",False,False,x,y)

                elif (piece == "alfil-negro"):
                        self.pieceReal[x][y] = ficha("alfil-negro",False,True,x,y)

                elif (piece == "alfil-blanco"):
                        self.pieceReal[x][y] = ficha("alfil-blanco",False,True,x,y)

                elif (piece == "reina-blanca"):
                        self.pieceReal[x][y] = ficha("reina-blanca",True,True,x,y)

                elif (piece == "reina-negra"):
                        self.pieceReal[x][y] = ficha("reino-negra",True,True,x,y)

                elif (piece == "rey-blanco"):
                        self.pieceReal[x][y] = ficha("rey-blanco",False,False,x,y)
                
                elif (piece == "rey-negro"):
                        self.pieceReal[x][y] = ficha("rey-negro",False,False,x,y)

                elif (piece == "peon-blanco"):
                        self.pieceReal[x][y] = ficha("peon-blanco",False,False,x,y)

                elif (piece == "peon-negro"):
                        self.pieceReal[x][y] = ficha("peon-negro",False,False,x,y)


        self.charger()
        self.printMatrix()
        