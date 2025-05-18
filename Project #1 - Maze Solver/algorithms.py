
def getAdjacent(position, grid):
    rowIndex, columnIndex = position
    adjacent = []
    totalRows = len(grid)
    totalColumns = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for deltaRow, deltaColumn in directions:
        newRow = rowIndex + deltaRow
        newColumn = columnIndex + deltaColumn

        if (0 <= newRow < totalRows and 0 <= newColumn < totalColumns and grid[newRow][newColumn] == 0):
            adjacent.append((newRow, newColumn))

    return adjacent


def depthFirstSearch(grid, startPosition, endPosition):
    stack = [startPosition]
    visitedCells = set()
    parentMap = {}
    visitOrder = []

    while stack:
        currentPosition = stack.pop()

        if currentPosition in visitedCells:
            continue

        visitedCells.add(currentPosition)
        visitOrder.append(currentPosition)

        if currentPosition == endPosition:
            break

        for adjacent in getAdjacent(currentPosition, grid):
            if adjacent not in visitedCells:
                stack.append(adjacent)
                if adjacent not in parentMap:
                    parentMap[adjacent] = currentPosition

    path = reconstructPath(parentMap, startPosition, endPosition)

    return visitOrder, path


def breadthFirstSearch(grid, startPosition, endPosition):
    queue = [startPosition]
    visitedCells = set()
    parentMap = {}
    visitOrder = []

    while queue:
        currentPosition = queue.pop(0)

        if currentPosition in visitedCells:
            continue

        visitedCells.add(currentPosition)
        visitOrder.append(currentPosition)

        if currentPosition == endPosition:
            break

        for adjacent in getAdjacent(currentPosition, grid):
            if adjacent not in visitedCells and adjacent not in queue:
                queue.append(adjacent)
                if adjacent not in parentMap:
                    parentMap[adjacent] = currentPosition

    path = reconstructPath(parentMap, startPosition, endPosition)
    return visitOrder, path


def reconstructPath(parentMap, startPosition, endPosition):
    if endPosition not in parentMap:
        return []

    path = []
    currentPosition = endPosition

    while currentPosition != startPosition:
        path.append(currentPosition)
        currentPosition = parentMap[currentPosition]

    path.append(startPosition)
    path.reverse()
    return path
