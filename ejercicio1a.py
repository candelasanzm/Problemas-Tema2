def mejor_candidato(candidatos :list) -> any:
    """ Devuelve el mejor candidato """
    pareja = [candidatos[0], candidatos[1]]
    candidatos= candidatos[2:]
    return pareja, candidatos

def voraz(candidatos :list) -> list:
    solucion = []
    while len(candidatos) > 0:
        pareja, candidatos = mejor_candidato(candidatos)
        solucion.append(pareja)
    return solucion

lista = [5, 8, 1, 4, 7, 9]
parejas = voraz(lista)
mayor=0
for pareja in parejas:
    mayor=max(mayor, pareja[0]+pareja[1])
print(mayor)