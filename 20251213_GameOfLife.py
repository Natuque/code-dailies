** start of main.py **

def game_of_life(grid):
    # Copy the grid for reference
    finalGrid = [each[:] for each in grid]

    # Define the range of the grid
    rowLimit = len(grid) - 1
    columnLimit = len(grid[0]) - 1

    for rowIndex, eachRow in enumerate(grid):
        y = rowIndex
        for columnIndex, eachValue in enumerate(eachRow):
            x = columnIndex
            currentLoc = [x, y]
            liveCount = 0

            # Map directions
            directions = [
                [x - 1, y],     # N
                [x - 1, y + 1], # NE
                [x, y + 1],     # E
                [x + 1, y + 1], # SE
                [x + 1, y],     # S
                [x + 1, y - 1], # SW
                [x, y - 1],     # W
                [x - 1, y - 1], # NW
            ]

            for eachDir in directions:
                if eachDir[0] <= columnLimit and eachDir[0] >= 0:
                    if eachDir[1] <= rowLimit and eachDir[1] >= 0:
                        if grid[eachDir[1]][eachDir[0]] == 1:
                            liveCount += 1
            

            # Check state
            state = grid[y][x]

            if state == 1:
                if liveCount < 2 or liveCount > 3:
                    finalGrid[y][x] = 0
            else:
                if liveCount == 3:
                    finalGrid[y][x] = 1

    print(finalGrid)
    return finalGrid

game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]])
game_of_life([[1, 1, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]])
game_of_life([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
game_of_life([[0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 0]])

** end of main.py **

