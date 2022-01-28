class ficha():
    def __init__(self,name,movementXY,movementV,X,Y):
        self.name = name
        self.movementXY = movementXY
        self.movementV = movementV
        self.posX = X
        self.posY = Y

    def moveXY(self,X,Y):
        #----Verifica si el movimiento es posible----#
        if((X != self.posX and Y == self.posY)or(X == self.posX and Y != self.posY)and self.movementXY == True):
            #----Verifica si el campo no esta ocupado por otra ficha----#
            if(self.verification(X,Y)):
                print("New position: " + str(X) + ", " + str(Y))
                return True
        print("Movement not allowed")
        return False

    def moveZ(self,X,Y):
        #----Verifica si el movimiento es posible----#

        if(X != self.posX and Y!= self.posY):
            if(abs(self.posX-X)*abs(self.posY-Y) == abs(self.posX-X) ** 2):
                if(self.verification(X,Y)):
                    print("New position: " + str(X) + ", " + str(Y))
                    return True
        print("Movement not allowed")
        return False

    def moveXYZ(self,X,Y):
        if(self.moveXY(X,Y)):
            return True
        else:
            self.moveZ(X,Y)


    #----Verifica si las casillas no son ocupadas por otras fichas----#        
    def verification(self,newX,newY):
        #----Asignación de cuadrante-----#
        if(self.posX < newX):
            valueX = 1
        elif(self.posX == newX):
            valueX = 0 
        else:
            valueX = -1

        if(self.posY < newY):
            valueY = 1
        elif(self.posY == newY):
            valueY = 0
        else:
            valueY = -1

        #----Asignacion de pares ordenados----#
        x = self.posX
        y = self.posY
        print("imprimiendo")
        while(x != newX or y != newY):
            x+=valueX
            y+=valueY
            print("("+str(x)+","+str(y)+")")
            
            '''
                Espacio para alguna funcion que compruebe si
                los espacios no estan ocupados por otras fichas
            '''
        return True







    