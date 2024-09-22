class Estado():
    def __init__(self,x,y,g,h,padre=None):
        self.pos = x,y
        self.g = g
        self.h = 0
        self.f = g + h
        self.padre = padre
    def getF(self):
        return self.f
    def getG(self):
        return self.g
    def getPos(self):
        return self.pos

    def setPadre(self, padre):
        self.padre = padre
    def getPadre(self):
        return self.padre
    def setF(self,f):
        self.f=f

    def setG(self,g):
        self.g=g


    def __lt__(self, other):
        return self.f < other.f
