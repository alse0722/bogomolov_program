import random

def generate_random_graph(n):
    max_edges = min(n * (n - 1), 100)  # Максимальное количество дуг
    avg_edges = max_edges // n  # Среднее количество дуг для каждой вершины
    remaining_edges = max_edges % n  # Оставшееся количество дуг для равномерного распределения

    graph = [['0' for _ in range(n)] for _ in range(n)]
    count = 0

    # Распределяем среднее количество дуг для каждой вершины
    for i in range(n):
        edges = avg_edges
        if remaining_edges > 0:
            edges += 1
            remaining_edges -= 1

        for _ in range(edges):
            j = random.randint(0, n - 1)
            while j == i or graph[i][j] != '0':
                j = random.randint(0, n - 1)

            random_value = random.choice(['+', '-', '0'])
            graph[i][j] = random_value
            count += 1

    print('Было сгенерировано', count, 'дуг')
    return [graph, count]

def save_graph_to_file(graph, filename):
    with open(filename, 'w') as file:
        for row in graph:
            line = ' '.join(row)
            file.write(line + '\n')

# Генерация случайного графа
def gen(filename, n):
    print('Генерация случайного графа')

    random_graph = generate_random_graph(n)

    save_graph_to_file(random_graph[0], filename)

    print(f"Сгенерированный граф с {n} вершинами сохранен в файл '{filename}'")

    return random_graph[1]
