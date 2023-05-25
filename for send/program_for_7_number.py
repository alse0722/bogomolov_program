import pygame as pg
import time

# Размер клетки
cell_size = 100

# Размер окна
window_width = 900
window_height = 900

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Инициализация Pygame
pg.init()

# Создание окна
window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Cellular Automaton")

# Определение размеров сетки
grid_width = window_width // cell_size
grid_height = window_height // cell_size

# Создание двумерного массива для хранения состояний клеток
grid = [[0] * grid_height for _ in range(grid_width)]

# Установка начального состояния клетки в центре
start_x = grid_width // 2
start_y = grid_height // 2
grid[start_x][start_y] = 1

# Функция для определения следующего состояния клетки
def get_next_state(x, y):
    neighbors = 0

    # Подсчет количества живых соседей
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx = (x + dx + grid_width) % grid_width
            ny = (y + dy + grid_height) % grid_height
            if grid[nx][ny] == 1:
                neighbors += 1

    # Правило перехода
    if neighbors % 2 == 0:
        return 1
    else:
        return 0

# Основной цикл программы
running = True

while running:
    # Обработка событий
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Рендеринг клеток
    for x in range(grid_width):
        for y in range(grid_height):
            rect = pg.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if grid[x][y] == 1:
                pg.draw.rect(window, BLACK, rect)
            else:
                pg.draw.rect(window, WHITE, rect)

    # Обновление дисплея
    pg.display.flip()

    # Задержка в секундах между кадрами
    time.sleep(1)

    # Обновление состояний клеток
    next_grid = [[get_next_state(x, y) for y in range(grid_height)] for x in range(grid_width)]
    grid = next_grid

# Завершение работы Pygame
pg.quit()
