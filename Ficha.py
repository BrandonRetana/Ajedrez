from turtle import pos, position

class ficha():
    def __init__(self,name,movementXY,movementV,X,Y):
        self.name = name
        self.movementXY = movementXY
        self.movementV = movementV
        self.posX = X
        self.posY = Y
        self.stillAlive = True

    def moveXY(self,X,Y):
        #----Verifica si el movimiento es posible----#
        if((X != self.posX and Y == self.posY)or(X == self.posX and Y != self.posY)and self.movementXY == True):
            #----Verifica si el campo no esta ocupado por otra ficha----#
            if(self.verification(X,Y)):
                print("New position: " + str(X) + ", " + str(Y))
                self.posX = X
                self.posY = Y
                return True
        print("Movement not allowed")
        return False

    def moveZ(self,X,Y):
        #----Verifica si el movimiento es posible----#

        if(X != self.posX and Y!= self.posY):
            if(abs(self.posX-X)*abs(self.posY-Y) == abs(self.posX-X) ** 2):
                if(self.verification(X,Y)):
                    print("New position: " + str(X) + ", " + str(Y))
                    self.posX = X
                    self.posY = Y
                    return True
        print("Movement not allowed")
        return False

    def moveXYZ(self,X,Y):
        if(self.moveXY(X,Y)):
            return True
        else:
            if(self.moveZ(X,Y)):
                return True
        return False


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


    def simpleVerification(self,x,y):
        '''
        Esta fucnion deberia dar un booleano si la casilla esta vacio o no.
        '''
        return True

    #---- Esta funcion saca el moviento que puede tener el caballo ----#
    def moveL(self,i,j):
        validPosition = []
        positions = [[self.posX+1, self.posY+2] ,[self.posX+2, self.posY+1] ,[self.posX+1, self.posY-2] ,[self.posX+2,self.posY-1] ,[self.posX-1,self.posY-2],[self.posX-2,self.posY-1],[self.posX-2,self.posY+1],[self.posX-1,self.posY+2]]
        for couple in positions:
            if (self.simpleVerification(couple[0],couple[1])):
                validPosition.append(couple)
        for valid in validPosition:
            if (valid == [i,j]):
                print("New position ("+str(i)+', '+str(j)+')')
                self.posX = i
                self.posY = j
                return True
        print("Position not allowed")
        return False
    
    #---- Esta funcion saca el moviento que puede tener el rey ----#
    def kingMove(self,i,j):
        validPosition = []
        positions = [[self.posX+1, self.posY-1] ,[self.posX+1,self.posY],[self.posX+1,self.posY+1] ,[self.posX, self.posY-1] ,[self.posX,self.posY+1],[self.posX-1, self.posY-1],[self.posX-1,self.posY],[self.posX-1, self.posY+1]]
        for couple in positions:
            if (self.simpleVerification(couple[0],couple[1])):
                validPosition.append(couple)
        for valid in validPosition:
            if (valid == [i,j]):
                print("New position ("+str(i)+', '+str(j)+')')
                self.posX = i
                self.posY = j
                return True
        print("Position not allowed")
        return False


    #---- Esta funcion saca el moviento que puede tener el peon ----#
    def pawnMove(self,i,j):
        validPosition = []
        if (self.posX == 2 or self.posX == 7):
            positions = [[self.posX, self.posY+1],[self.posX, self.posY+2],[self.posX+1, self.posY+1],[self.posX-1, self.posY+1]]
        else :
            positions= [[self.posX, self.posY+1],[self.posX+1, self.posY+1],[self.posX-1, self.posY+1]]
        for couple in positions:
            if (self.simpleVerification(couple[0],couple[1])):
                validPosition.append(couple)
        for valid in validPosition:
            if (valid == [i,j]):
                print("New position ("+str(i)+', '+str(j)+')')
                self.posX = i
                self.posY = j
                return True
        print("Position not allowed")
        return False

    def getName(self):
        return self.name

    def move(self,X,Y):
        if(self.movementXY == True and self.movementV == True):
            print("case")
            return self.moveXYZ(X,Y)
        elif(self.movementXY == True):
            return self.moveXY(X,Y)
        elif(self.movementV == True):
            return self.moveZ(X,Y)
        else:
            if(self.name == "peon-negro" or self.name == "peon-blanco"):
                return self.pawnMove(X+1,Y+1)
            elif(self.name == "caballo-negro" or self.name == "caballo-blanco"):
                return self.moveL(X+1,Y+1)
            else:
                return self.kingMove(X+1,Y+1)
                



    