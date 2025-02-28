HORA_INICIO = 0
HORA_FIN = 1

def ordena_reservas(reservas : list[tuple[int, int]]) -> list[tuple[int, int]] :
    """ Ordena las reservas por hora de inicio de menor a mayor """
    inicio = lambda reserva: reserva[0] # defino la funcion lambda para obtener la hora de inicio de cada reserva
    return sorted(reservas, key = inicio)

def num_min_pistas(reservas : list[tuple[int, int]]) -> int:
    """ Busca cuantas pistas necesito, ordenando por hora de inicio las reservas """
    
    # ordeno las reservas por hora de inicio 
    reservas_ordenadas = ordena_reservas(reservas)
    
    # inicializo una lista donde ire agregando las horas de finalizacion
    pistas = []

    for reserva in reservas_ordenadas:
        inicio, fin = reserva # separo los valores de la tupla

        # busco una pista que quede libre antes de que empiece una nueva reserva
        pista_asignada = False

        i = 0

        while i < len(pistas) and pistas[i] > inicio: # bucle para encontrar la primera pista que esté libre antes del inicio de la nueva reserva
            i += 1

        pista_asignada = i < len(pistas) # verificar si se encontró una pista libre
        if pista_asignada :
            pistas[i] = fin # actualizar la hora de finalizacion de la pista que queda libre con la nueva reserva    

        if pista_asignada == False:
            pistas.append(fin) # crear nueva pista

    return len(pistas)


res = [(10, 12), (9, 11), (11, 13)]
print(ordena_reservas(res))
print(num_min_pistas(res))

def test_ordenar_reservas():
    reservas_desordenadas = [(10, 12), (9, 11), (11, 13)]
    reservas_ordenadas = [(9, 11), (10, 12), (11, 13)]
    assert ordena_reservas(reservas_desordenadas) == reservas_ordenadas

def test_num_min_pistas():
    reservas_desordenadas = [(10, 12), (9, 11), (11, 13)]
    reservas_ordenadas = ordena_reservas(reservas_desordenadas)
    res = 2
    assert num_min_pistas(reservas_ordenadas) == res

def test_benchmark_ordena_reservas (benchmark):
    reservas_desordenadas = [(10, 12), (9, 11), (11, 13)]
    reservas_ordenadas = [(9, 11), (10, 12), (11, 13)]
    res = benchmark(ordena_reservas, reservas_desordenadas)
    assert res == reservas_ordenadas

def test_benchmark_num_min_pistas (benchmark):
    reservas_desordenadas = [(10, 12), (9, 11), (11, 13)]
    reservas_ordenadas = ordena_reservas(reservas_desordenadas)
    min_pistas = benchmark(num_min_pistas, reservas_ordenadas)
    res = 2
    assert min_pistas == res