import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def calculate_time(cuadras, is_javier):
    base_time = 5
    special_carreras = {12, 13, 14}
    special_calles = {51}

    if cuadras[0] in special_carreras:
        base_time = 7
    elif cuadras[1] in special_calles:
        base_time = 10

    if is_javier:
        return base_time
    else:
        return base_time + 2

def find_optimal_path(destination):
    graph = {
        'Carrera 10': {'Calle 50': 5},
        'Carrera 11': {'Calle 54': 5},
        'Carrera 12': {'Calle 50': 7},
        'Carrera 13': {'Calle 52': 7},
        'Carrera 14': {'Calle 50': 7},
    }

    javier_start = 'Calle 54'
    andreina_start = 'Calle 52'

    javier_times = dijkstra(graph, javier_start)
    andreina_times = dijkstra(graph, andreina_start)

    time_difference = 0
    if javier_times[destination] != andreina_times[destination]:
        if javier_times[destination] < andreina_times[destination]:
            time_difference = andreina_times[destination] - javier_times[destination]
            return f'Javier debe salir {time_difference} minutos antes para llegar simultáneamente.'
        else:
            time_difference = javier_times[destination] - andreina_times[destination]
            return f'Andreína debe salir {time_difference} minutos antes para llegar simultáneamente.'
    else:
        return 'Ambos pueden salir al mismo tiempo y llegarán simultáneamente.'

# Ejemplo de uso
destination = 'Calle 50'
result = find_optimal_path(destination)
print(result)