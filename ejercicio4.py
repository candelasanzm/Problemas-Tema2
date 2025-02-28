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
    aristas_ordenadas = [('Zaragoza', 'Oviedo', 100),
                         ('Zaragoza', 'Cádiz', 200), 
                         ('Santiago', 'Almeria', 200),
                         ('Valencia', 'Santander', 200),
                         ('Salamanca', 'Zaragoza', 300), 
                         ('Almeria', 'Valencia', 300),
                         ('Almeria', 'Santander', 300),    
                         ('Salamanca', 'Valencia', 400), 
                         ('Santiago', 'Cádiz', 400), 
                         ('Oviedo', 'Santiago', 500), 
                         ('Cádiz', 'Valencia', 700),
                         ('Cádiz', 'Almeria', 900)]
    caso_prueba = []
    assert ordena_aristas(aristas) == aristas_ordenadas
    assert ordena_aristas(aristas_ordenadas) == aristas_ordenadas
    assert ordena_aristas(caso_prueba) == []

def test_find():
    aristas = [('Salamanca', 'Zaragoza', 300),       
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
    arista_buscada = ('Salamanca', 'Zaragoza', 300)
    assert find(aristas, 'Salamanca') == arista_buscada
    assert find(aristas, 'Madrid') == None

def test_union():
    conjuntos = [{'Salamanca'}, {'Zaragoza'}, {'Oviedo'}]
    union (conjuntos, ('Salamanca', 'Zaragoza', 300))
    assert conjuntos == [{'Oviedo'}, {'Salamanca', 'Zaragoza'}]
    union (conjuntos, ('Zaragoza', 'Oviedo', 100))
    assert conjuntos == [{'Salamanca', 'Zaragoza', 'Oviedo'}]
    conjuntos_vacio = []
    union (conjuntos_vacio, ('Salamanca', 'Madrid', 300))
    assert conjuntos_vacio == []

def test_is_bucle():
    conjuntos = [{'Salamanca', 'Zaragoza'}, {'Oviedo'}, {'Santiago'}, {'Cádiz'}, {'Almeria'}, {'Valencia'}, {'Santander'}]
    assert is_bucle(conjuntos, ('Salamanca', 'Oviedo', 400)) == False
    assert is_bucle(conjuntos, ('Salamanca', 'Zaragoza', 300))    # si hay bucle, 'Salamanca' y 'Zaragoza' ya están en el mismo conjunto

    # Unir 'Salamanca' y 'Oviedo'
    union(conjuntos, ('Salamanca', 'Oviedo', 400))
    assert is_bucle(conjuntos, ('Zaragoza', 'Oviedo', 100))  

def test_kruskal():
    aristas = [('Salamanca', 'Zaragoza', 300),       
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
    ciudades = ['Salamanca', 'Zaragoza', 'Oviedo', 'Santiago', 'Cádiz', 'Almeria', 'Valencia', 'Santander']
    conjuntos = [{ciudad} for ciudad in ciudades] 
    solucion = [('Zaragoza', 'Oviedo', 100), ('Zaragoza', 'Cádiz', 200), ('Santiago', 'Almeria', 200), ('Valencia', 'Santander', 200), ('Salamanca', 'Zaragoza', 300), ('Almeria', 'Valencia', 300), ('Salamanca', 'Valencia', 400)]
    assert kruskal(aristas, conjuntos) == solucion