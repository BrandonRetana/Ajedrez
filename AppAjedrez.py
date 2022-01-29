from Ficha import *
class EstadoDeJuego():
    #aqui si maneja el estado del juego

    def __init__(self):
        self.piezas = [
            [ficha("torre-negra",True,False,1,1),ficha("caballo-negro",False,False,1,2),ficha("alfil-negro",False,True,1,3),ficha("reina-negra",True,True,1,4),ficha("rey-negro",False,False,1,5),ficha("alfil-negro",False,True,1,6),ficha("caballo-negro",False,False,1,7),ficha("torre-negra",True,False,1,8)],
            [ficha("peon-negro",False,False,2,1),ficha("peon-negro",False,False,2,2),ficha("peon-negro",False,False,2,3),ficha("peon-negro",False,False,2,4),ficha("peon-negro",False,False,2,5),ficha("peon-negro",False,False,2,6),ficha("peon-negro",False,False,2,7),ficha("peon-negro",False,False,2,8)],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            [ficha("peon-blanco",False,False,7,1),ficha("peon-blanco",False,False,7,2),ficha("peon-blanco",False,False,7,3),ficha("peon-blanco",False,False,7,4),ficha("peon-blanco",False,False,7,5),ficha("peon-blanco",False,False,7,6),ficha("peon-blanco",False,False,7,7),ficha("peon-blanco",False,False,7,8)],
            [ficha("torre-blanca",True,False,8,1),ficha("caballo-blanco",False,False,8,2),ficha("alfil-blanco",False,True,8,3),ficha("reina-blanca",True,True,8,4),ficha("rey-blanco",False,False,8,5),ficha("alfil-blanco",False,True,8,6),ficha("caballo-blanco",False,False,8,7),ficha("torre-blanca",True,False,8,8)]
        ]




        