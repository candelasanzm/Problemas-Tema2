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
min, max = voraz(v)
print(f"Mínimo: {min}, Máximo: {max}")

def test_voraz():
    v = [3, 4, 1, 7, 5, 9, 10]
    min=1
    max=10
    assert voraz(v)== (min, max)

def test_benchmark(benchmark):
    v = [3, 4, 1, 7, 5, 9, 10]
    min=1
    max=10
    res = benchmark(voraz, v)
    assert res== (min, max)