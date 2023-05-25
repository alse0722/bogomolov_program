
import graph_generator
import graph_demo

filename = 'graph.txt'
output_filename = 'cycles.txt'

def find_cycles(graph):
    n = len(graph)
    visited = [False] * n  # список посещенных вершин
    path = []  # список текущего пути
    cycles = []  # список найденных циклов

    def dfs(node):
        visited[node] = True
        path.append(node)

        for neighbor in range(n):
            if graph[node][neighbor] == 1:  # существует дуга из вершины node в соседнюю вершину neighbor
                if neighbor in path:  # найден цикл
                    start_index = path.index(neighbor)
                    cycle = path[start_index:]

                    # Преобразование цикла вершин в цикл дуг
                    cycle_edges = []
                    for i in range(len(cycle) - 1):
                        edge = (cycle[i], cycle[i + 1])
                        cycle_edges.append(edge)
                    edge = (cycle[-1], cycle[0])  # Дуга, соединяющая последнюю вершину с первой
                    cycle_edges.append(edge)

                    cycles.append(cycle_edges)
                elif not visited[neighbor]:
                    dfs(neighbor)

        path.remove(node)
        visited[node] = False

    for i in range(n):
        dfs(i)

    return cycles


def add_binary_form(array):
    result = []

    for row in array:
        transformed_row = []
        for element in row:
            if element == '+':
                transformed_row.append(1)
            elif element == '-':
                transformed_row.append(1)
            elif element == '0':
                transformed_row.append(0)
            else:
                raise ValueError("Invalid element: " + str(element))
        result.append(transformed_row)

    return [array, result]


def check_cycle_type(string):
    if all(char == '+' for char in string):
        return 'positive'
    elif all(char == '-' for char in string):
        return 'negative'
    elif all(string[i] != string[i+1] for i in range(len(string)-1)) and string[0] != string[-1]:
        return 'mixed'
    else:
        return 'invalid'

def save_to_file(array, filename):

    def reverse_array_to_string(arr):
        arr.append(arr[0])
        print(arr)
        fixed_arr = []
        for point in arr:
            fixed_arr.append(point + 1)
        reversed_arr = fixed_arr[::-1]
        reversed_string = ' '.join(map(str, reversed_arr))
        return reversed_string
    
    with open(filename, 'w') as file:
        
        file.write('\npositive:\n')
        for cycle in array:
            if cycle[1] == 'positive':
                file.write(reverse_array_to_string(cycle[0]) + '\n')
        
        file.write('\nnegative:\n')
        for cycle in array:
            if cycle[1] == 'negative':
                file.write(reverse_array_to_string(cycle[0]) + '\n')
        
        file.write('\nmixed:\n')
        for cycle in array:
            if cycle[1] == 'mixed':
                file.write(reverse_array_to_string(cycle[0]) + '\n')


def cycles_process():
    print('Поиск контуров начат')
    with open(filename, 'r') as file:
        adjacency_matrix = [line.strip().split() for line in file]

    extended_matrix = add_binary_form(adjacency_matrix)

    all_cycles = find_cycles(extended_matrix[1])


    fin = []
    for cycle in all_cycles:
        cycle_signs = ''
        path = []
        for element in cycle:
            path.append(element[0])
            cycle_signs += extended_matrix[0][element[0]][element[1]]
        fin.append([path, cycle_signs])

    final_result = []
    added_cycles = []
    for cycle in fin:
        if sorted(cycle[0]) not in added_cycles and check_cycle_type(cycle[1]) != 'invalid':
            final_result.append([cycle[0], check_cycle_type(cycle[1]), cycle[1]])
            added_cycles.append(sorted(cycle[0]))

    save_to_file(final_result, output_filename)
    print(f"Все контуры графа найдены и сохранены в файл '{output_filename}'")

def main():
    # генерация случайного графа
    #graph_generator.gen(filename, 6)

    # поиск контуров
    cycles_process()

    # вывод графика
    graph_demo.demo(filename)

main()