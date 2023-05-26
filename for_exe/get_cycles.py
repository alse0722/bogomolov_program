
import graph_generator
import graph_demo
import tkinter as tk
from tkinter import messagebox
import os

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
    return len(final_result)

def generator():
    top = tk.Toplevel()
    top.title('Генерация случайного графа')
    top.geometry('400x190')

    label = tk.Label(top, text='Введите количество вершин графа')
    label.pack()

    entry = tk.Entry(top)
    entry.pack()

    def generate_graph():
        try:

            os.remove(filename)
            os.remove(output_filename)

            num_vertices = int(entry.get())
            branches = graph_generator.gen(filename,num_vertices)
            #cycles = cycles_process()
            top.destroy()
            message = f'Новый граф сохранен в graph.txt\nОбщее количество вершин: {num_vertices}\nОбщее количество дуг: {branches}'
            messagebox.showinfo('Генерация случайного графа', message)
            #graph_demo.demo(filename)

        except ValueError:
            messagebox.showerror('Ошибка', 'Введите корректное количество вершин!')

    button = tk.Button(top, text='Подтвердить', command=generate_graph)
    button.pack()

def cycler():
    try:
        cycles = cycles_process()
        
        message = f'Количество найденных контуров: {cycles}\nКонтуры сохранены в файле cycles.txt'
        messagebox.showinfo('Исследование заданного графа', message)
        #graph_demo.demo(filename)
        
    except FileNotFoundError:
        messagebox.showerror('Ошибка', 'Файл graph.txt не найден!')

def graph_demonstator():
    try:
        graph_demo.demo(filename)
        
    except FileNotFoundError:
        messagebox.showerror('Ошибка', 'Файл graph.txt не найден!')

def matix_demonstator():

    try:
        with open(filename, "r") as file:
            content = file.read()

        window = tk.Toplevel()
        window.title("Матрица графа")
        window.geometry("400x300")

        text_area = tk.Text(window)
        text_area.insert(tk.END, content)
        text_area.pack(fill=tk.BOTH, expand=True)

        window.mainloop()
        
    except FileNotFoundError:
        messagebox.showerror('Ошибка', f'Файл {filename} не найден!')


def contours_demonstator():

    try:
        with open(output_filename, "r") as file:
            content = file.read()

        window = tk.Toplevel()
        window.title("Контуры графа")
        window.geometry("400x300")

        text_area = tk.Text(window)
        text_area.insert(tk.END, content)
        text_area.pack(fill=tk.BOTH, expand=True)

        window.mainloop()
        
    except FileNotFoundError:
        messagebox.showerror('Ошибка', f'Файл {output_filename} не найден!')


def main():
    root = tk.Tk()
    root.title('Приветствие')
    root.geometry('400x190')

    label = tk.Label(root, text='Вас приветствует программа поиска контуров графа!')
    label.pack()

    show_button = tk.Button(root, text='Показать заданный граф', width=100, command=graph_demonstator)
    show_button.pack()

    generate_button = tk.Button(root, text='Сгенерировать случайный граф', width=100, command=generator)
    generate_button.pack()

    read_button = tk.Button(root, text='Исследовать заданный граф', width=100, command=cycler)
    read_button.pack()

    show_matrix_button = tk.Button(root, text='Показать матрицу графа', width=100, command=matix_demonstator)
    show_matrix_button.pack()

    show_contour_button = tk.Button(root, text='Показать контуры графа', width=100, command=contours_demonstator)
    show_contour_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()