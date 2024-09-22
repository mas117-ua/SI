from casilla import *

class Mapa():
    def __init__(self, archivo):        
        self.mapa=leer(archivo)         
        self.alto = len(self.mapa)
        self.ancho = len(self.mapa[0])        
        
    def __str__(self):
        salida = "" 
        for f in range(self.alto):            
            for c in range(self.ancho):               
                if self.mapa[f][c] == 0:
                    salida += "  "
                if self.mapa[f][c] == 1:
                    salida += "# "                 
                if self.mapa[f][c] == 3:
                    salida += "D "
                if self.mapa[f][c] == 4:
                    salida += "~ "
                if self.mapa[f][c] == 5:
                    salida += "* "   
            salida += "\n"
        return salida
    
    def getAlto (self):
        return self.alto
    
    def getAncho (self):
        return self.ancho
    
    def getCelda(self, y, x):
        return self.mapa[y][x]
    
    def setCelda(self, y, x, valor):
        self.mapa[y][x]=valor

    def movimientosValidos(self, posicion): #recibe una casilla
        fil, col = posicion.fila, posicion.col
        movimientos = []
        # Posibles desplazamientos (arriba, abajo, izquierda, derecha, y diagonales)
        desplazamientos = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for d in desplazamientos:
            nuevaFila = fil + d[0]
            nuevaColumna = col + d[1]
            if 0 < nuevaFila < self.getAlto() and 0 < nuevaColumna < self.getAncho():
                if self.getCelda(nuevaFila, nuevaColumna) in [0, 4, 5]:
                    movimientos.append((nuevaFila, nuevaColumna))

        return movimientos

    def coste(self,n_pos, m_pos):
        # Cálculo del coste de moverse entre dos casillas en un mapa cuadrado
        x1, y1 = n_pos
        x2, y2 = m_pos

        # Si es un movimiento en línea recta (horizontal o vertical), el coste es 1
        if x1 == x2 or y1 == y2:
            return 1
        else:
            return 1.5

    def calorias(self,casilla):
        for f in range(self.alto):
            for c in range(self.ancho):
                if self.mapa[f][c] == '.':
                    return 2
                elif self.mapa[f][c] == '~':
                    return 4
                elif self.mapa[f][c] == '*':
                    return 6
                else:
                    return 0


# Funciones
# ---------------------------------------------------------------------
def leer(archivo):
    mapa=[] 
    try:  
        fich=open(archivo, "r")
        fila=-1
        for cadena in fich:
            fila=fila+1            
            mapa.append([])            
            for i in range(len(cadena)):                
                if cadena[i] == ".":
                    mapa[fila].append(0)                    
                if cadena[i] == "#":
                    mapa[fila].append(1)
                if cadena[i] == "~":
                    mapa[fila].append(4)
                if cadena[i] == "*":
                    mapa[fila].append(5)
                    
    except:
        print ("Error de fichero")
        fich.close()
        
    fich.close()
    return mapa
 

# ---------------------------------------------------------------------
if __name__=="__main__":   
    mapa = Mapa('mapa.txt')
    print (mapa)
    
    