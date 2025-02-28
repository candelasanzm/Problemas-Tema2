def mejor_candidato(candidatos :list) -> any:
    """ Devuelve el mejor candidato """
    pass

def es_completable(solucion :list, candidato :any) -> bool:
    """ Comprueba si se puede llegar a la solución usando ese candidato """
    pass

def voraz(candidatos :list) -> list:
    solucion = []
    while len(candidatos) > 0:
        c = mejor_candidato(candidatos)
        candidatos.remove(c)
        if es_completable(solucion, c):
            solucion.append(c)
    return solucion