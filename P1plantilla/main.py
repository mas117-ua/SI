import sys, pygame
from casilla import *
from mapa import *
from pygame.locals import *
from estado import *


MARGEN=5
MARGEN_INFERIOR=60
TAM=30
NEGRO=(0,0,0)
HIERBA=(250, 180, 160)
MURO=(30, 70, 140)
AGUA=(173, 216, 230)
ROCA=(110, 75, 48)
AMARILLO=(255, 255, 0)

# ---------------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------------

def imprimir_matriz_estados(matriz):
    for fila in matriz:
        print(" ".join(str(celda) for celda in fila))



def astar(mapa, origen, destino, camino):
    cal_tot = 0
    li = []
    lf = []
    estado_origen = Estado(origen.getFila(), origen.getCol(), 0, 0, padre=None)
    lf.append(estado_origen)

    mapa_estados = [[-1 for j in range(mapa.getAncho())] for i in range(mapa.getAlto())]

    while lf:
        # Obtenemos el nodo con menor f de lf:
        n = lf[0]  # n = estado con menor f
        for est in lf:
            if est.getF() < n.getF():
                n = est

        if n.getPos() == (destino.getFila(), destino.getCol()):
            coste_tot = n.getF()  # Utilizamos n.getF() para el coste total
            # Reconstruir camino
            camino_reconstruido = []
            while n is not None:
                camino_reconstruido.append(n.getPos())
                cal_tot += mapa.calorias(Casilla(n.getPos()[0], n.getPos()[1]))

                n = n.getPadre()
            camino_reconstruido.reverse()  # Invertimos el camino

            # Marcar el camino en la matriz 'camino' para visualizarlo
            for (fila, col) in camino_reconstruido:
                camino[fila][col] = 'X'  # Marcar el camino de solución con 'X' por ejemplo

            print("Camino encontrado:", camino_reconstruido)
            imprimir_matriz_estados(mapa_estados)

            return coste_tot,cal_tot  # Terminar la función, ya que hemos encontrado el destino

        else:
            lf.remove(n)
            li.append(n)

            # Obtener los hijos de n
            hijos_n = []
            casilla_n = Casilla(n.getPos()[0], n.getPos()[1])
            hijos_casilla_n = mapa.movimientosValidos(casilla_n)

            for movimiento in hijos_casilla_n:
                hijos_n.append((movimiento[0], movimiento[1]))

            for m in hijos_n:  # Recorremos cada tupla de n
                # Calcular g y f
                coste_g_m = n.getG() + mapa.coste(n.getPos(), (m[0], m[1]))
                coste_f_m = coste_g_m  # f = g porque h = 0

                # Verificamos si m no está en la lista interior (li)
                if not any(estadoli.getPos() == m for estadoli in li):
                    # Si m no está en la lista frontera (lf)
                    if not any(estadolf.getPos() == m for estadolf in lf):
                        estado_m = Estado(m[0], m[1], coste_g_m, coste_f_m, padre=n)
                        lf.append(estado_m)
                    else:
                        for estadolf in lf:
                            if estadolf.getPos() == m:
                                if coste_g_m < estadolf.getG():
                                    estadolf.setPadre(n)
                                    estadolf.setF(coste_f_m)  # Actualizar f
                                    estadolf.setG(coste_g_m)  # Actualizar g
                                break

                # Para imprimir los costes
                if m[0] == origen.getFila() and m[1] == origen.getCol():
                    mapa_estados[m[0]][m[1]] = 0
                else:
                    mapa_estados[m[0]][m[1]] = int(coste_g_m)

    print("Error: no se encuentra solución con el algoritmo")










# Devuelve si una casilla del mapa se puede seleccionar como destino o como origen
def bueno(mapi, pos):
    res= False

    if mapi.getCelda(pos.getFila(),pos.getCol())==0 or mapi.getCelda(pos.getFila(),pos.getCol())==4 or mapi.getCelda(pos.getFila(),pos.getCol())==5:
       res=True

    return res

# Devuelve si una posición de la ventana corresponde al mapa
def esMapa(mapi, posicion):
    res=False

    if posicion[0] > MARGEN and posicion[0] < mapi.getAncho()*(TAM+MARGEN)+MARGEN and \
    posicion[1] > MARGEN and posicion[1] < mapi.getAlto()*(TAM+MARGEN)+MARGEN:
        res= True

    return res

#Devuelve si se ha pulsado algún botón
def pulsaBoton(mapi, posicion):
    res=-1

    if posicion[0] > (mapi.getAncho()*(TAM+MARGEN)+MARGEN)//2-65 and posicion[0] < (mapi.getAncho()*(TAM+MARGEN)+MARGEN)//2-15 and \
       posicion[1] > mapi.getAlto()*(TAM+MARGEN)+MARGEN+10 and posicion[1] < MARGEN_INFERIOR+mapi.getAlto()*(TAM+MARGEN)+MARGEN:
        res=1
    elif posicion[0] > (mapi.getAncho()*(TAM+MARGEN)+MARGEN)//2+15 and posicion[0] < (mapi.getAncho()*(TAM+MARGEN)+MARGEN)//2+65 and \
       posicion[1] > mapi.getAlto()*(TAM+MARGEN)+MARGEN+10 and posicion[1] < MARGEN_INFERIOR+mapi.getAlto()*(TAM+MARGEN)+MARGEN:
        res=2


    return res

# Construye la matriz para guardar el camino
def inic(mapi):
    cam=[]
    for i in range(mapi.alto):
        cam.append([])
        for j in range(mapi.ancho):
            cam[i].append('.')

    return cam




# función principal
def main():
    pygame.init()

    reloj=pygame.time.Clock()

    if len(sys.argv)==1: #si no se indica un mapa coge mapa.txt por defecto
        file='mapa.txt'
    else:
        file=sys.argv[-1]

    mapi=Mapa(file)
    camino=inic(mapi)

    anchoVentana=mapi.getAncho()*(TAM+MARGEN)+MARGEN
    altoVentana= MARGEN_INFERIOR+mapi.getAlto()*(TAM+MARGEN)+MARGEN
    dimension=[anchoVentana,altoVentana]
    screen=pygame.display.set_mode(dimension)
    pygame.display.set_caption("Practica 1")

    boton1=pygame.image.load("boton1.png").convert()
    boton1=pygame.transform.scale(boton1,[50, 30])

    boton2=pygame.image.load("boton2.png").convert()
    boton2=pygame.transform.scale(boton2,[50, 30])

    personaje=pygame.image.load("rabbit.png").convert()
    personaje=pygame.transform.scale(personaje,[TAM, TAM])

    objetivo=pygame.image.load("carrot.png").convert()
    objetivo=pygame.transform.scale(objetivo,[TAM, TAM])

    coste=-1
    cal=0
    running= True
    origen=Casilla(-1,-1)
    destino=Casilla(-1,-1)

    while running:
        #procesamiento de eventos
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if pulsaBoton(mapi, pos)==1 or pulsaBoton(mapi, pos)==2:
                    if origen.getFila()==-1 or destino.getFila()==-1:
                        print('Error: No hay origen o destino')
                    else:
                        camino=inic(mapi)
                        if pulsaBoton(mapi, pos)==1:
                            ###########################
                            #coste, cal=llamar a A estrella
                            #coste, cal = astar(mapi, origen, destino, camino)
                            coste, cal = astar(mapi,origen,destino,camino)

                            if coste==-1:
                                print('Error: No existe un camino válido entre origen y destino')
                        else:
                            ###########################
                            #coste, cal=llamar a A estrella subepsilon
                            if coste==-1:
                                print('Error: No existe un camino válido entre origen y destino')

                elif esMapa(mapi,pos):
                    if event.button==1: #botón izquierdo
                        colOrigen=pos[0]//(TAM+MARGEN)
                        filOrigen=pos[1]//(TAM+MARGEN)
                        casO=Casilla(filOrigen, colOrigen)
                        if bueno(mapi, casO):

                            #SACAMOS LOS MOVIMIENTOS VALIDOS
                            origen=casO
                            movimientos=mapi.movimientosValidos(origen) # recibe una casilla
                            print("Movimientos válidos desde origen:", movimientos)

                        else: # se ha hecho click en una celda no accesible
                            print('Error: Esa casilla no es válida')
                    elif event.button==3: #botón derecho
                        colDestino=pos[0]//(TAM+MARGEN)
                        filDestino=pos[1]//(TAM+MARGEN)
                        casD=Casilla(filDestino, colDestino)
                        if bueno(mapi, casD):
                            destino=casD
                        else: # se ha hecho click en una celda no accesible
                            print('Error: Esa casilla no es válida')

        #código de dibujo
        #limpiar pantalla
        screen.fill(NEGRO)
        #pinta mapa
        # Pinta el mapa
        for fil in range(mapi.getAlto()):
            for col in range(mapi.getAncho()):
                if camino[fil][col] == 'X':  # Si es parte del camino
                    pygame.draw.rect(screen, AMARILLO,
                                     [(TAM + MARGEN) * col + MARGEN, (TAM + MARGEN) * fil + MARGEN, TAM, TAM], 0)
                elif mapi.getCelda(fil, col) == 0:
                    pygame.draw.rect(screen, HIERBA,
                                     [(TAM + MARGEN) * col + MARGEN, (TAM + MARGEN) * fil + MARGEN, TAM, TAM], 0)
                elif mapi.getCelda(fil, col) == 4:
                    pygame.draw.rect(screen, AGUA,
                                     [(TAM + MARGEN) * col + MARGEN, (TAM + MARGEN) * fil + MARGEN, TAM, TAM], 0)
                elif mapi.getCelda(fil, col) == 5:
                    pygame.draw.rect(screen, ROCA,
                                     [(TAM + MARGEN) * col + MARGEN, (TAM + MARGEN) * fil + MARGEN, TAM, TAM], 0)
                elif mapi.getCelda(fil, col) == 1:
                    pygame.draw.rect(screen, MURO,
                                     [(TAM + MARGEN) * col + MARGEN, (TAM + MARGEN) * fil + MARGEN, TAM, TAM], 0)

        #pinta origen
        screen.blit(personaje, [(TAM+MARGEN)*origen.getCol()+MARGEN, (TAM+MARGEN)*origen.getFila()+MARGEN])
        #pinta destino
        screen.blit(objetivo, [(TAM+MARGEN)*destino.getCol()+MARGEN, (TAM+MARGEN)*destino.getFila()+MARGEN])
        #pinta botón
        screen.blit(boton1, [anchoVentana//2-65, mapi.getAlto()*(TAM+MARGEN)+MARGEN+10])
        screen.blit(boton2, [anchoVentana//2+15, mapi.getAlto()*(TAM+MARGEN)+MARGEN+10])
        #pinta coste y energía
        if coste!=-1:
            fuente= pygame.font.Font(None, 25)
            textoCoste=fuente.render("Coste: "+str(coste), True, AMARILLO)
            screen.blit(textoCoste, [anchoVentana-90, mapi.getAlto()*(TAM+MARGEN)+MARGEN+15])
            textoEnergía=fuente.render("Cal: "+str(cal), True, AMARILLO)
            screen.blit(textoEnergía, [5, mapi.getAlto()*(TAM+MARGEN)+MARGEN+15])



        #actualizar pantalla
        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

#---------------------------------------------------------------------
if __name__=="__main__":
    main()
