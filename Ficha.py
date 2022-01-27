class ficha():
    def __init__(self,name,movementXY,movementV,X,Y):
        self.name = name
        self.movementXY = movementXY
        self.movementV = movementV
        self.posX = X
        self.posY = Y
 
    def nombre(self):
        print(self.__name)

    def moveXY(self,X,Y):
        if((X != self.posX and Y == self.posY)or(X == self.posX and Y != self.posY)and self.movementXY == True):
            posX = X
            posY = Y
            print("New position: " + str(X) + ", " + str(Y))
            return True
        else:
            print("Movement not allowed")
            return False

    def moveZ(self,X,Y):
        if(X != self.posX and Y!= self.posY):
            if(abs(self.posX-X)*abs(self.posY-Y) == abs(self.posX-X) ** 2):
                posX = X
                posY = Y
                print("New position: " + str(X) + ", " + str(Y))
                return True
            else:
                print("Movement not allowed")
                return False
        else:
            print("Movement not allowed")
            return False

    def moveXYZ(self,X,Y):
        if(self.moveXY(X,Y)):
            return True
        else:
            self.moveZ(X,Y)


    