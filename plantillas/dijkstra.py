def dijkstra(grafo :dict, origen :str) -> dict|dict:
    """ Algoritmo de Dijkstra """
    distancias, predecesores = {}, {}
    no_visitados = []

    for vertice in grafo:
        distancias[vertice] = float('inf')
        predecesores[vertice] = None
        no_visitados.append(vertice)
    distancias[origen] = 0

    while no_visitados:
        u = min(no_visitados, key=distancias.get)
        no_visitados.remove(u)
        for vecino in grafo[u]:
            if vecino in no_visitados and distancias[vecino] > distancias[u] + grafo[u][vecino]:
                distancias[vecino] = distancias[u] + grafo[u][vecino]
                predecesores[vecino] = u

    return distancias, predecesores

def camino_mas_corto(grafo :dict, origen :str, destino :str) -> list|int:
   """ Encuentra el camino más corto usando dijkstra """
   distancias, predecesores = dijkstra(grafo, origen)

   camino = []
   distancia = distancias[destino]
   actual = destino
   while actual:
       camino.append(actual)
       actual = predecesores[actual]

   camino.reverse()
   return camino, distancia

# Programa
grafo = { # origen: {destino: peso}
    'a': {'b': 4, 'c': 3},
    'b': {'d': 5},
    'c': {'b': 2, 'd': 3, 'e': 6},
    'd': {'f': 5, 'e': 1},
    'e': {'g': 5},
    'g': {'z': 4},
    'f': {'g': 2, 'z': 7},
    'z': {}
}

distancias, predecesores = dijkstra(grafo, 'a')
print(f'Distancias: {distancias}')
print(f'Predecesores: {predecesores}')

camino, distancia = camino_mas_corto(grafo, 'a', 'z')
print(f'Camino: {camino}')
print(f'Distancia: {distancia}')
