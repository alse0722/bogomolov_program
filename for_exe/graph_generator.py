import random

def generate_random_graph(n):
    graph = [['0' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                random_value = random.choice(['+', '-', '0'])
                graph[i][j] = random_value

    return graph

def save_graph_to_file(graph, filename):
    with open(filename, 'w') as file:
        for row in graph:
            line = ' '.join(row)
            file.write(line + '\n')

# Генерация случайного графа
def gen(filename, n):
    print('Генерация случайного графа')

    #n = 4
    random_graph = generate_random_graph(n)

    # Сохранение графа в файл
    #filename = 'graph.txt'
    save_graph_to_file(random_graph, filename)

    print(f"Сгенерированный граф c {n} вершинами сохранен в файл '{filename}'")