"""
Tenemos objetos de distintos valores y volúmenes, y queremos llenar una mochila  maximizando el valor de su contenido.

Mochila:
- Capacidad de 8L.
Objetos:
- Tablet (100€ / 1L)
- Cuaderno (1€ / 1L)
- Termo (10€ / 0.5L)
- Tupper con comida (13€ / 2L)
- Abrigo (50€ / 5L)
- Estuche con material (20€ / 1.5L)
- Cargador del ordenador (20€ / 1L)

"""

##############################
#    FUNCIONES AUXILIARES    #
##############################
def _objeto(nombre :str, valor :float, volumen :float) -> dict:
    """ Diccionario para almacenar los datos de un objeto """
    return {'nombre': nombre, 'valor': valor, 'volumen': volumen}

def sumar(mochila :list[_objeto], campo :str) -> float:
    """ Calcula la suma del valor o del volumen de una lista de objetos """
    assert campo == 'valor' or campo == 'volumen', 'PRE: debe ser un campo válido'
    suma = 0
    for objeto in mochila:
        suma += objeto[campo]
    return suma

##############################
#      ALGORITMO VORAZ       #
##############################
def es_completable(solucion :list, candidato :any) -> bool:
    """ Comprueba si se puede llegar a la solución usando ese candidato """
    return sumar(solucion, 'volumen') + candidato['volumen'] <= CAPACIDAD_MOCHILA

def mejor_candidato(candidatos :list) -> any:
    """ Opción A: Objetos de menor volumen """
    funcion = lambda objeto: objeto['volumen'] 
    candidatos = sorted(candidatos, key=funcion) # ¿Podemos ordenar fuera?
    return candidatos[0] # Buscar tiene un coste menor que ordenar: O(n) vs O(nlog(n))

def voraz(candidatos :list) -> list:
    solucion = []
    while len(candidatos) > 0: # Vamos a devolver la solución cuando no queden candidatos que comprobar: O(n)
        c = mejor_candidato(candidatos)
        candidatos.remove(c)
        if es_completable(solucion, c):
            solucion.append(c)
    return solucion

##############################
#      INICIALIZACIÓN        #
##############################
CAPACIDAD_MOCHILA = 8

if __name__ == '__main__':

    candidatos = [_objeto('Tablet',  100, 1), 
                  _objeto('Cuaderno',  1, 1), 
                  _objeto('Termo',    10, 0.5), 
                  _objeto('Tupper',   13, 2), 
                  _objeto('Abrigo',   50, 5),
                  _objeto('Estuche',  20, 1.5),
                  _objeto('Cargador', 20, 1)]
    
    solucion = voraz(candidatos)
    print('Solución: ')
    for objeto in solucion:
        print(f"{objeto['nombre']:10} | {objeto['volumen']:5.1f}€ | {objeto['valor']:5.1f}L")
    print("----------------------------")
    print(f"Valor total: {sumar(solucion, 'valor')}€")
    print(f"Volumen total: {sumar(solucion, 'volumen')}L")
