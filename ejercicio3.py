def voraz(candidatos: list) -> tuple:
    if not candidatos:
        return None, None
    elif len(candidatos) == 1:
        return candidatos[0], candidatos[0]
    
    min_candidato = float('inf')  #Valor muy grande para comparar
    max_candidato = float('-inf')  #Valor muy pequeño para comparar

    for i in range(0, len(candidatos) - 1, 2):  
        if candidatos[i] < candidatos[i + 1]:  #1 comparacion
            min_candidato = min(min_candidato, candidatos[i])  #1 comparacion
            max_candidato = max(max_candidato, candidatos[i+1]) #1 comparacion
        else:
            min_candidato = min(min_candidato, candidatos[i+1])  #1 comparacion
            max_candidato = max(max_candidato, candidatos[i])  #1 comparacion

    if len(candidatos) % 2 == 1:  # Si hay un elemento extra (impares)
        min_candidato = min(min_candidato, candidatos[-1])
        max_candidato = max(max_candidato, candidatos[-1])

    return min_candidato, max_candidato

v = [3, 4, 1, 7, 5, 9, 10]
minimo, maximo = voraz(v)
print(f"Mínimo: {minimo}, Máximo: {maximo}")

def test_voraz():
    v1 = [3, 4, 1, 7, 5, 9, 10]
    minimo_v1=1
    maximo_v1=10
    assert voraz(v1)== (minimo_v1, maximo_v1)

    v2=[]
    minimo_v2 = None
    maximo_v2= None
    assert voraz(v2)== (minimo_v2, maximo_v2)

    v3 = [2]
    minimo_v3=2
    maximo_v3=2
    assert voraz(v3)== (minimo_v3, maximo_v3)

