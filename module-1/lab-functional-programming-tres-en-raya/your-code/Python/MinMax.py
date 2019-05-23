import pdb
#pdb.set_trace()

import copy

class Tree(object):
    "Generic tree node."
    def __init__(self, name="", children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    #def __repr__(self):
    #    return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
        



def posicionesLibres(tablero):
    posicionesLibres=[]
    for fila in range(len(tablero)):
        for columna in range(len(tablero)):
            EstadoposicionTablero=tablero[fila][columna]
            if EstadoposicionTablero=="-":
                
                coordenadaTablero=[fila,columna]
                posicionesLibres.append(coordenadaTablero)
                
    return posicionesLibres
    

def siguientesJuagadas(tablero,jugador="X"):
    Jugadas=[]
    libres=posicionesLibres(tablero)
    
    for posicion in libres:
        tableroNext=copy.deepcopy(tablero)
        fila=posicion[0]
        columna=posicion[1]
        tableroNext[fila][columna]=jugador
        Jugadas.append(tableroNext)
    return Jugadas

def cambiaJugador(jugador):
    if jugador=="X":
        jugador="O"
    else:
        jugador="X"
    return jugador

def rellenaArbol (jugada,jugador,arbol):
    Jugadas=siguientesJuagadas(jugada,jugador)
    print(Jugadas)
    if Jugadas.count>0:
    
        for jugada in Jugadas:
            nodoJugada=Tree(jugada)
            arbol.add_child(nodoJugada)
            jugador=cambiaJugador(jugador)
            rellenaArbol(jugada,jugador,nodoJugada)
            
        
######################################################################
#Main
######################################################################


        
jugada = [["X","O","X"], ["O","X","O"], ["-","-","-"]]

arbol=Tree(jugada)

rellenaArbol(jugada,"X",arbol)

for name in arbol.children:
    print(name.name)

