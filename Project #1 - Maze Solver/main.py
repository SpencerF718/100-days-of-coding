import pygame
from algorithms import depthFirstSearch, breadthFirstSearch

ROWS, COLS = 20, 20
CELL_SIZE = 30
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")
clock = pygame.time.Clock()

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
start = (0, 0)
end = (ROWS - 1, COLS - 1)


def drawGrid():
    for rowIndex in range(ROWS):
        for colIndex in range(COLS):
            rect = pygame.Rect(colIndex * CELL_SIZE,
                               rowIndex * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            color = WHITE
            if (rowIndex, colIndex) == start:
                color = GREEN
            elif (rowIndex, colIndex) == end:
                color = RED
            elif grid[rowIndex][colIndex] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)


def drawPath(path, visitOrder):
    for cell in visitOrder:
        if cell == start or cell == end:
            continue
        rowIndex, colIndex = cell
        rect = pygame.Rect(colIndex * CELL_SIZE, rowIndex *
                           CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, rect)
        pygame.draw.rect(screen, GRAY, rect, 1)
        pygame.display.update()
        pygame.time.delay(20)

    for cell in path:
        if cell == start or cell == end:
            continue
        rowIndex, colIndex = cell
        rect = pygame.Rect(colIndex * CELL_SIZE, rowIndex *
                           CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, PURPLE, rect)
        pygame.draw.rect(screen, GRAY, rect, 1)
        pygame.display.update()
        pygame.time.delay(30)


def getCellFromMouse(pos):
    x, y = pos
    return y // CELL_SIZE, x // CELL_SIZE


running = True
while running:
    screen.fill(WHITE)
    drawGrid()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif pygame.mouse.get_pressed()[0]:
            rowIndex, colIndex = getCellFromMouse(pygame.mouse.get_pos())
            if (rowIndex, colIndex) != start and (rowIndex, colIndex) != end:
                grid[rowIndex][colIndex] = 1

        elif pygame.mouse.get_pressed()[2]:
            rowIndex, colIndex = getCellFromMouse(pygame.mouse.get_pos())
            if (rowIndex, colIndex) != start and (rowIndex, colIndex) != end:
                grid[rowIndex][colIndex] = 0

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                visitOrder, path = breadthFirstSearch(grid, start, end)
                drawPath(path, visitOrder)
            elif event.key == pygame.K_d:
                visitOrder, path = depthFirstSearch(grid, start, end)
                drawPath(path, visitOrder)

    clock.tick(60)

pygame.quit()
