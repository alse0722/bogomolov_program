import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(graph):
    n = len(graph)
    G = nx.DiGraph()

    for i in range(n):
        for j in range(n):
            if graph[i][j] == '+':
                G.add_edge(j+1, i+1, sign='+')
            elif graph[i][j] == '-':
                G.add_edge(j+1, i+1, sign='-')

    pos = nx.spring_layout(G, k=0.2)  # Расположение вершин графа с параметром k=0.2

    # Рисование вершин
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=300)

    # Рисование дуг
    positive_edges = [(u, v) for (u, v, d) in G.edges(data=True) if d['sign'] == '+']
    negative_edges = [(u, v) for (u, v, d) in G.edges(data=True) if d['sign'] == '-']

    nx.draw_networkx_edges(G, pos, edgelist=positive_edges, edge_color='green', arrows=True,
                           connectionstyle='arc3,rad=0.2')
    nx.draw_networkx_edges(G, pos, edgelist=negative_edges, edge_color='red', arrows=True,
                           connectionstyle='arc3,rad=0.3')

    # Рисование номеров вершин
    node_labels = {i+1: i+1 for i in range(n)}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12)

    # Добавление подписей для цветов дуг
    plt.text(0.01, 0.9, 'Green: Positive', color='green', transform=plt.gca().transAxes)
    plt.text(0.01, 0.85, 'Red: Negative', color='red', transform=plt.gca().transAxes)

    plt.axis('off')  # Отключение осей координат
    plt.show()


# Пример использования
def read_graph(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        graph = []
        for line in lines:
            row = line.strip().split()
            graph.append(row)
        return graph

def demo(filename):
    graph = read_graph(filename)
    draw_graph(graph)
