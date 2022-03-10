import queue


grafo = {
    "A": ["B", "C", "D"],
    "B": ["E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"]
}

grafo2 = {
    "A": ["B", "C", "D"],
    "B": ["E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
    "G": [],
    "H": [],
    "I": [],
    "J": []
}

# Recorrido recursivo del grafo empleado DFS (en profundidad)


def bpp_recursivo(grafo, origen, camino=[]):
    if origen not in camino:
        camino.append(origen)

        if origen not in grafo:
            return camino  # No está en el grafo, no hay nada por devolver.

        for vecino in grafo[origen]:
            camino = bpp_recursivo(grafo, vecino, camino)

    return camino

# Llamada a la función


camino = bpp_recursivo(grafo, "A")

print(" ".join(camino))


# Recorrido recursivo del grafo empleado BFS (en amplitud)

queue = []


def bfs_recursivo(grafo, origen, camino=[]):
    if origen not in camino:  # Revisa si el origen no está en el camino y lo añade.
        camino.append(origen)
        queue.append(origen)

        if origen not in grafo:
            return camino  # No está en el grafo, no hay nada por devolver.

        while queue:  # Iterando sobre la queue, se saca un nodo de la lista y, por cada vecino de ese nodo,
            # si no está en la queue, lo añade tanto al camino como a la queue mientras no estén visitados.
            s = queue.pop(0)

            for vecino in grafo[s]:
                if vecino not in camino:
                    camino.append(vecino)
                    queue.append(vecino)

    return camino


camino = bfs_recursivo(grafo2, "A")

print(" ".join(camino))
