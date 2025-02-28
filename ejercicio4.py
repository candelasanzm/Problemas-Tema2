U = 0
V = 1
PESO = 2

def ordena_aristas(aristas : list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
    """ Ordena las aristas por peso de menor a mayor """
    peso = lambda arista: arista[PESO]
    return sorted(aristas, key = peso)

def find(conjuntos :list, u :int) -> set:
    """ Devuelve el conjunto al que pertenece un nodo """
    for conjunto in conjuntos:
        if u in conjunto:
            return conjunto
    return None

def union(conjuntos :list, arista :tuple) -> None:
    """ Actualiza los conjuntos """
    set_u = find(conjuntos, arista[U])
    set_v = find(conjuntos, arista[V])
    if set_u != set_v:
        conjuntos.remove(set_u)
        conjuntos.remove(set_v)
        conjuntos.append(set_u.union(set_v))

def is_bucle(conjuntos :list, arista :tuple) -> bool:
    """ Hay un bucle si los nodos pertenecen al mismo conjunto (algoritmo union-find) """
    set_u = find(conjuntos, arista[U])
    set_v = find(conjuntos, arista[V])
    return set_u == set_v

def kruskal(aristas :list, conjuntos :list) -> list:
    """ Algoritmo de Kruskal """
    aristas = ordena_aristas(aristas)
    solucion = []
    for arista in aristas:
        if not is_bucle(conjuntos, arista):
            solucion.append(arista)
            union(conjuntos, arista)
    return solucion

# Programa
ciudades = ['Salamanca', 'Zaragoza', 'Oviedo', 'Santiago', 'Cádiz', 'Almeria', 'Valencia', 'Santander']
fibra = [('Salamanca', 'Zaragoza', 300),       # funcionan como aristas
         ('Salamanca', 'Valencia', 400), 
         ('Zaragoza', 'Cádiz', 200), 
         ('Zaragoza', 'Oviedo', 100), 
         ('Oviedo', 'Santiago', 500), 
         ('Santiago', 'Cádiz', 400), 
         ('Santiago', 'Almeria', 200), 
         ('Cádiz', 'Almeria', 900), 
         ('Cádiz', 'Valencia', 700),
         ('Almeria', 'Valencia', 300),
         ('Almeria', 'Santander', 300),
         ('Valencia', 'Santander', 200)]


conjuntos = [{ciudad} for ciudad in ciudades]   #serían nuestros nodos

# Ejecutar Kruskal
resultado = kruskal(fibra, conjuntos)

# Mostrar el resultado
print("Tramos de fibra óptica seleccionados para minimizar el coste:")
coste_total = 0
for arista in resultado:
    print(f"{arista[U]} - {arista[V]}: {arista[PESO]}€")
    coste_total += arista[PESO]

print(f"\nCoste total mínimo: {coste_total}€")


def test_ordena_aristas():
    aristas = [('Salamanca', 'Zaragoza', 300),       
               ('Salamanca', 'Valencia', 400), 
               ('Zaragoza', 'Oviedo', 100), 
               ('Oviedo', 'Santiago', 500),  
               ('Cádiz', 'Almeria', 900), 
               ('Cádiz', 'Valencia', 700),
               ('Valencia', 'Santander', 200)]
    aristas_ordenadas = [('Zaragoza', 'Oviedo', 100),
                         ('Valencia', 'Santander', 200),
                         ('Salamanca', 'Zaragoza', 300),     
                         ('Salamanca', 'Valencia', 400), 
                         ('Oviedo', 'Santiago', 500), 
                         ('Cádiz', 'Valencia', 700),
                         ('Cádiz', 'Almeria', 900)]
    assert ordena_aristas(aristas) == aristas_ordenadas

test_ordena_aristas()

"""def test_find():

def test_union():

def test_is_bucle():

def test_kruskal():"""
