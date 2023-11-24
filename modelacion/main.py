import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import dijkstra_path

# Establecer valores por defecto para la ciudad
ciudad_norte = 54
ciudad_sur = 50
ciudad_este = 14
ciudad_oeste = 10

# Establecer valores por defecto para los pesos de los arcos
peso_por_defecto_J = 5
peso_por_defecto_A = 7

# Establecer valores específicos para los arcos
peso_norte_sur_J = 7
peso_norte_sur_A = 9
peso_oeste_este_J = 10
peso_oeste_este_A = 12

# Crear funciones para crear y visualizar los grafos
def crear_grafo(paso_defecto, paso_norte_sur, paso_oeste_este, name):
    G = nx.DiGraph()
    if name == "J":
        print("creando grafo Javier ")
        for i in range(ciudad_sur, ciudad_norte + 1):
            for j in range(ciudad_oeste, ciudad_este + 1):
                G.add_node((i, j), label=str(i) + ',' + str(j))
                if i < ciudad_norte:
                    if j == 14 or j == 13 or j == 12:
                        G.add_edge((i, j), (i + 1, j), weight=peso_norte_sur_J)
                    else:
                        G.add_edge((i, j), (i + 1, j), weight=peso_por_defecto_J)
                if j < ciudad_este:
                    if i == 51:
                        G.add_edge((i, j), (i, j + 1), weight=peso_oeste_este_J)
                    else:
                        G.add_edge((i, j), (i, j + 1), weight=peso_por_defecto_J)
                if i > ciudad_sur:
                    if j == 14 or j == 13 or j == 12:
                        G.add_edge((i, j), (i - 1, j), weight=peso_norte_sur_J)
                    else:
                        G.add_edge((i, j), (i - 1, j), weight=peso_por_defecto_J)
                if j > ciudad_oeste:
                    if i == 51:
                        G.add_edge((i, j), (i, j - 1), weight=peso_oeste_este_J)
                    else:
                        G.add_edge((i, j), (i, j - 1), weight=peso_por_defecto_J)
        return G    
    elif name =="A":
        print("creando grafo Andreina ")
        for i in range(ciudad_sur, ciudad_norte + 1):
            for j in range(ciudad_oeste, ciudad_este + 1):
                G.add_node((i, j), label=str(i) + ',' + str(j))
                if i < ciudad_norte:
                    if j == 14 or j == 13 or j == 12:
                        G.add_edge((i, j), (i + 1, j), weight=peso_norte_sur_A)
                    else:
                        G.add_edge((i, j), (i + 1, j), weight=peso_por_defecto_A)
                if j < ciudad_este:
                    if i == 51:
                        G.add_edge((i, j), (i, j + 1), weight=peso_oeste_este_A)
                    else:
                        G.add_edge((i, j), (i, j + 1), weight=peso_por_defecto_A)
                if i > ciudad_sur:
                    if j == 14 or j == 13 or j == 12:
                        G.add_edge((i, j), (i - 1, j), weight=peso_norte_sur_A)
                    else:
                        G.add_edge((i, j), (i - 1, j), weight=peso_por_defecto_A)
                if j > ciudad_oeste:
                    if i == 51:
                        G.add_edge((i, j), (i, j - 1), weight=peso_oeste_este_A)
                    else:
                        G.add_edge((i, j), (i, j - 1), weight=peso_por_defecto_A)
        return G


def visualizar_grafo(G):
    pos = {k: (k[1], k[0]) for k in G.nodes}
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, node_size=1000, font_size=12, node_color='skyblue', with_labels=True,horizontalalignment='center', verticalalignment='center')
    nx.draw_networkx_edge_labels(G, pos=nx.spring_layout(G), edge_labels=edge_labels, label_pos=0.5, font_size=10,horizontalalignment='center',verticalalignment='center')
    plt.show()


# Funciones para modificar el grafo y calcular el camino más corto
def modificar_grafo(G, inicio, fin, peso):
    for n in G.nodes:
        if n == inicio:
            G[n][fin]['weight'] = peso
            return G

def calcular_camino_mas_corto(G, salida, llegada):
    return dijkstra_path(G, salida, llegada)

def calculate_time(graph, start_node, end_node):
    path = nx.dijkstra_path(graph, start_node, end_node)
    time = sum(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
    print("El tiempo necesario para recorrer el camino es: ", time)
    return time
#Funcion para escoger el local que se va a visitar
def local_llegada():
    opcion = input("""
    Seleccione el local al que irá la pareja en cuestión:
    1. Discoteca Darkness
    2. Bar La Pasión
    3. Cervecería Mi Rolita
    4. Café Sensación
    > 
                   """)
    match opcion: 
        case "1":
            print("Discoteca Darkness")
            local = "50,14"
        case "2":
            print("Bar La Pasión")
            local = "54,11"
        case "3":
            print("Cervecería Mi Rolita")
            local = "50,12"
        case "4":
            print("Café Sensación")
            local = "50,10"
        case _:
            print("Se van a ver en una esquina recóndita ya que no decidiste")
            local = "54,10"
    print(local)
    value = tuple(map(int,local.split(',')))
    return value


# Implementar menú recursivo
def menu(G_J,G_A):
    while(True):
        casaJ = "54,14"
        casaA = "52,13"
        print("1. Mostrar ambos grafos.")
        print("2. Modificar algún arco de ser necesario.")
        print("3. ¿A donde saldrá la linda pareja?")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Grafo J:")
            visualizar_grafo(G_J)
            edge_data = nx.get_edge_attributes(G_J, 'weight')

            # Imprimir el diccionario de pesos de las aristas
            print(edge_data)

            print("Grafo A:")
            visualizar_grafo(G_A)
            edge_data = nx.get_edge_attributes(G_A, 'weight')

            # Imprimir el diccionario de pesos de las aristas
            print(edge_data)

        elif opcion == "2":
            grafo = input("A qué grafo se hará la edición (J o A): ").upper()
            inicio = tuple(map(int, input("Ingrese las coordenadas de inicio (orden: latitud, longitud): ").split(',')))
            fin = tuple(map(int, input("Ingrese las coordenadas de llegada (orden: latitud, longitud): ").split(',')))
            peso = int(input("Ingrese el nuevo peso del arco: "))

            if grafo == 'J':
                G_J = modificar_grafo(G_J, inicio, fin, peso)
            elif grafo == 'A':
                G_A = modificar_grafo(G_A, inicio, fin, peso)

        elif opcion == "3":
            salidaJ = tuple(map(int,(casaJ).split(',')))
            salidaA = tuple(map(int,(casaA).split(',')))
            llegada = local_llegada()
            print("Cambur")
            print(llegada)

            print("Camino más corto en el grafo J:")
            camino_mas_corto_J = calcular_camino_mas_corto(G_J, salidaJ, llegada)
            tiempo_J = calculate_time(G_J, salidaJ, llegada)
            print(camino_mas_corto_J)

            print("Camino más corto en el grafo A:")
            camino_mas_corto_A = calcular_camino_mas_corto(G_A, salidaA, llegada)
            tiempo_A = calculate_time(G_A, salidaA, llegada)
            print(camino_mas_corto_A)
            couple_time = tiempo_J - tiempo_A
            if couple_time < 0:
                print(f"Javier llegaría primero que Andreina, Javier debe esperarse {-1*couple_time} minutos para llegar al mismo tiempo.")
            else:
                print(f"Andreina llegaría primero que Javier, Andreina debe esperarse {couple_time} minutos para llegar al mismo tiempo.")

            
            
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            

# Crear grafos J y A
G_J = crear_grafo(peso_por_defecto_J, peso_norte_sur_J, peso_oeste_este_J,"J")
G_A = crear_grafo(peso_por_defecto_A, peso_norte_sur_A, peso_oeste_este_A,"A")
menu(G_J,G_A)