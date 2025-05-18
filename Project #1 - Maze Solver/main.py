from algorithms import breadthFirstSearch, depthFirstSearch


def printGrid(grid, path=None, visited=None):
    totalRows = len(grid)
    totalColumns = len(grid[0])

    for rowIndex in range(totalRows):
        for columnIndex in range(totalColumns):
            cell = grid[rowIndex][columnIndex]
            position = (rowIndex, columnIndex)

            if cell == 1:
                print("|", end="")               # wall
            elif path and position in path:
                print("x", end="")               # path to end
            elif visited and position in visited:
                print(".", end="")               # dead end path
            else:
                print(" ", end="")
        print()
    print()


def main():
    mazeGrid = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]

    startPosition = (0, 0)
    endPosition = (4, 4)

    print("dfs test:")
    visitedDFS, pathDFS = depthFirstSearch(
        mazeGrid, startPosition, endPosition)
    print(visitedDFS)
    print(pathDFS)
    printGrid(mazeGrid, pathDFS, visitedDFS)

    print("bfs test:")
    visitedBFS, pathBFS = breadthFirstSearch(
        mazeGrid, startPosition, endPosition)
    print(visitedBFS)
    print(pathBFS)
    printGrid(mazeGrid, pathBFS, visitedBFS)


if __name__ == "__main__":
    main()
