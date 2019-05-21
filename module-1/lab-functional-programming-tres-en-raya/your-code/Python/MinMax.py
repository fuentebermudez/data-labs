import pdb
pdb.set_trace()

import copy

class Tree(object):
    "Generic tree node."
    def __init__(self, name=[], children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

arbol=Tree()

tableroZero = [["X","X","X"], ["O","X","-"], ["-","-","X"]]
arbol=Tree(tableroZero)


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
    estados=[]
    libres=posicionesLibres(tablero)
    
    for posicion in libres:
        tableroNext=copy.deepcopy(tablero)
        fila=posicion[0]
        columna=posicion[1]
        tableroNext[fila][columna]=jugador
        estados.append(tableroNext)
    return estados

Estados=siguientesJuagadas(tableroZero)
print(Estados)
