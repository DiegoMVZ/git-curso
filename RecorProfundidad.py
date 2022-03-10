# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 22:49:51 2022

@author: Diego
"""

##RECORRIDO EN PROFUNDIDAD
grafo = {'A':['B','C','D'],
       'B':['E'],
       'C':['F','G'],
       'D':['H'],
       'E':['I'],
       'F':['J']

}

visitado = set()  # Seguimiento a nodos visitados


def bpp_recursivo(visitado, grafo, origen, destino):  
    if origen not in visitado:
        print(origen)

        # Comprobamos si el nodo actual es el que buscamos
        if origen == destino:
            return True

        visitado.add(origen)
        for vecino in grafo[origen]:
            # Si encontramos el nodo, salimos del bucle.
            if bpp_recursivo(visitado, grafo, vecino, destino):
                return True
        # Si no encontramos el nodo que buscábamos, devolvemos False
        return False



if __name__  == "__main__":
    bpp_recursivo(visitado, grafo, 'A', 'I')
    
