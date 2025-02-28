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
    v = [3, 4, 1, 7, 5, 9, 10]
    minimo_v=1
    maximo_v=10
    assert voraz(v)== (minimo_v, maximo_v)

